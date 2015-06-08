# -*- coding: utf-8 -*-
"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import requests
import os
import time
from .azure_exception import AzureException
from pyquickhelper import noLOG


class AzureClient():

    """

    A simple class to access and communicate with `Azure <http://azure.microsoft.com/>`_.
    It requires modules:

    * `azure <https://github.com/Azure/azure-sdk-for-python>`_
    * `requests <http://docs.python-requests.org/en/latest/>`_

    .. index: blob, Azure

    Main functionalities related to blob:
        * list_containers, create_container, list_blobs, put_blob, put_block_blob_from_bytes
        * put_block_blob_from_text, put_page_blob_from_file, get_blob, get_blob

    See `How to use Blob storage from Python <https://azure.microsoft.com/en-us/documentation/articles/storage-python-how-to-use-blob-storage/>`_.

    @example(Azure___Get the list of containers and files from a blob storage?)

    The functionalities of a ``BlobService`` are described in
    `blobservice.py <https://github.com/Azure/azure-sdk-for-python/blob/master/azure/storage/blobservice.py>`_.

    @code
    from pyensae.remote.azure_connection import AzureClient
    cl = AzureClient("<blob_storage_service>",
                     "<primary_key>")
    bs = cl.open_blob_service()
    res = cl.ls(bs)
    for r in res:
        print(r["name"])
    @endcode
    @endexample

    @example(Azure___Upload, download, to a blob storage)
    The following example uploads and downloads a file on a Blob Storage.

    @code
    from pyensae.remote.azure_connection import AzureClient
    cl = AzureClient("<blob_storage_service>",
                     "<primary_key>")
    bs = cl.open_blob_service()
    cl.upload(bs, "<container>", "myremotefolder/remotename.txt",
                                 "local_filename.txt")

    res = cl.ls(bs,"<container>")
    for r in res:
        if "local_filename" in r["name"]:
            print(r)

    cl.download(bs, "<container>", "myremotefolder/remotename.txt",
                                   "another_local_filename.txt")

    @endcode

    @endexample

    Many function uses WebHCat API.
    The error code can be found here:
    `Error Codes and Responses <https://cwiki.apache.org/confluence/display/Hive/WebHCat+UsingWebHCat#WebHCatUsingWebHCat-ErrorCodesandResponses>`_.

    .. versionchanged::
        PSEUDO, CONTAINER, SCRIPT will be passed to the script as parameters

    """

    _blob_properties = [
        "copy_completion_time",
        "content_encoding",
        "content_language",
        "blob_type",
        "copy_status_description",
        "copy_id",
        "content_md5",
        "lease_duration",
        "copy_source",
        "content_type",
        "content_length",
        "lease_state",
        "copy_progress",
        "copy_status",
        "xms_blob_sequence_number",
        "lease_status",
        "etag",
        "last_modified",
    ]

    def __init__(self, blob_name,
                 blob_key,
                 hadoop_name=None,
                 hadoop_key=None,
                 hadoop_user_name="admin",
                 pseudo="any",
                 fLOG=None):
        """
        constructor

        @param      blob_name       blob storage name
        @param      blob_key        account key for the blob storage
        @param      hadoop_name     hadoop server name (can be None if HDInsight is not used)
        @param      hadoop_key      hadoop key (can be None if HDInsight is not used)
        @param      pseudo          sometimes, the same identification is used to connect to HDInsight,
                                    the pseudo is meant to avoid collisions
        @param      fLOG            logging function

        """
        self.account_name = blob_name
        self.account_key = blob_key
        self.hadoop_name = hadoop_name
        self.hadoop_key = hadoop_key
        self.hadoop_user_name = hadoop_user_name
        self.pseudo = pseudo
        if fLOG is None:
            def _log_(*l, **p):
                return
            self.LOG = _log_
        else:
            self.LOG = fLOG

        if pseudo is None:
            raise ValueError("pseudo cannot be None")

        self.default_parameters = dict(
            SCRIPTPIG=self.pseudo + "/scripts/pig",
            PSEUDO=self.pseudo,
            CONTAINER="")

    def _interpret_path(self, blob_path):
        """
        replace variavble such as ``$PSEUDO``, ``$USERNAME``

        @param      blob_path       path
        @return                     modified path

        .. versionadded:: 1.1
        """
        if blob_path is None:
            return None
        if "$" in blob_path:
            for k, v in self.default_parameters.items():
                blob_path = blob_path.replace("$" + k, v)
        return blob_path

    @staticmethod
    def mask_string(s):
        """
        return empty string or as many ``*`` as the length of the string
        """
        if s is None:
            return ""
        else:
            return "*" * len(s)

    def __str__(self):
        """
        usual
        """
        mes = "AzureClient [blob:({0},{1}), hadoop:({2},{3},{4})]".format(AzureClient.mask_string(self.account_name),
                                                                          AzureClient.mask_string(
            self.account_key), AzureClient.mask_string(
            self.hadoop_name),
            AzureClient.mask_string(self.hadoop_key), AzureClient.mask_string(self.hadoop_user_name))
        return mes

    def open_blob_service(self):
        """
        open a blob service
        """
        import azure.storage
        return azure.storage.BlobService(self.account_name, self.account_key)

    def exists(self, blob_service, container_name, path):
        """
        test the existence of a path on the blob storage

        @param      blob_service        blob service, returned by @see me open_blob_service
        @param      container_name      None for all, its name otherwise
        @param      path                path in the container
        @return                         boolean

        .. versionadded:: 1.1
        """
        path = self._interpret_path(path)
        df = self.ls(blob_service, container_name, path, as_df=False)
        return len(df) > 0

    def ls(self, blob_service, container_name=None,
           path=None, add_metadata=False, as_df=True):
        """
        return the content of a blob storage

        @param      blob_service        blob service, returned by @see me open_blob_service
        @param      container_name      None for all, its name otherwise
        @param      path                path in the container
        @param      add_metadata        add the metadata to the blob
        @param      as_df               if True, returns a DataFrame
        @return                         list of dictionaries

        .. versionchanged:: 1.1
            Parameter *add_metadata* was added and the function now returns the
            property *last_modified*, parameter *as_df*

        """
        res = []
        if container_name is None:
            for cn in blob_service.list_containers():
                self.LOG("exploring ", cn.name)
                r = self.ls(
                    blob_service,
                    cn.name,
                    path=path,
                    add_metadata=add_metadata,
                    as_df=False)
                res.extend(r)
            if as_df:
                import pandas
                return pandas.DataFrame(res)
            else:
                return res
        else:
            path = self._interpret_path(path)
            res = []
            for b in blob_service.list_blobs(container_name, prefix=path,
                                             include="metadata" if add_metadata else None):
                obs = {}
                obs["name"] = b.name
                obs["url"] = b.url
                for p in AzureClient._blob_properties:
                    obs[p] = b.properties.__dict__[p]

                if b.metadata is not None:
                    for k, v in b.metadata.items():
                        obs["meta_%s" % k] = v

                res.append(obs)
            if as_df:
                import pandas
                if len(res) > 0:
                    return pandas.DataFrame(res)
                else:
                    return pandas.DataFrame(columns=["name", "url"])
            else:
                return res

    _chunk_size = 4 * 1024 * 1024

    def upload(self,
               blob_service,
               container_name,
               blob_name,
               file_path):
        """
        Uploads data from a file to a blob storage.
        No more than 64Mb can be uploaded at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        @param      file_path           local file path
        @return                         list of uploaded blob names

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.
        """
        if isinstance(file_path, list):
            res = []
            for filename in file_path:
                only = os.path.split(filename)[-1]
                bn = blob_name.rstrip("/") + "/" + only
                r = self.upload(blob_service, container_name, bn, filename)
                res.append(r)
            return res
        else:
            blob_name = self._interpret_path(blob_name)
            blob_service.create_container(container_name, None, None, False)
            blob_service.put_blob(container_name, blob_name, None, 'BlockBlob')

            block_ids = []
            index = 0
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(AzureClient._chunk_size)
                    if data:
                        block_id = '{0:08d}'.format(index)
                        blob_service.put_block(
                            container_name,
                            blob_name,
                            data,
                            block_id)
                        block_ids.append(block_id)
                        index += 1
                        self.LOG("uploaded", index, " bytes from ", file_path)
                    else:
                        break

            blob_service.put_block_list(container_name, blob_name, block_ids)
            return blob_name

    def download(self,
                 blob_service,
                 container_name,
                 blob_name,
                 file_path,
                 append=False):
        """
        Downloads data from a blob storage to a file.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (or list of blob names) (remote file name)
        @param      file_path           local file path
        @param      append              if True, append the content to an existing file
        @return                         local file

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.

        .. versionchanged:: 1.1
            Parameter *append* was added.
        """
        if not isinstance(blob_name, str):
            res = []
            for blob in blob_name:
                dest = os.path.join(file_path, os.path.split(blob)[-1])
                r = self.download(
                    blob_service,
                    container_name,
                    blob,
                    dest,
                    append)
                res.append(r)
            return res
        else:
            blob_name = self._interpret_path(blob_name)
            props = blob_service.get_blob_properties(container_name, blob_name)
            blob_size = int(props['content-length'])

            index = 0

            mode = 'ab' if append else 'wb'
            with open(file_path, mode) as f:
                while index < blob_size:
                    chunk_range = 'bytes={}-{}'.format(index,
                                                       index + AzureClient._chunk_size - 1)
                    data = blob_service.get_blob(
                        container_name,
                        blob_name,
                        x_ms_range=chunk_range)
                    length = len(data)
                    index += length
                    self.LOG("downloaded ", index, "bytes from ", file_path)
                    if length > 0:
                        f.write(data)
                        if length < AzureClient._chunk_size:
                            break
                    else:
                        break
            return file_path

    def download_merge(self,
                       blob_service,
                       container_name,
                       blob_folder,
                       file_path):
        """
        Downloads all files from a folder in a blob storage to a single local file.
        Files will be merged.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_folder         blob folder(remote file name)
        @param      file_path           local file path
        @return                         local file

        .. versionadded:: 1.1
        """
        blob_folder = self._interpret_path(blob_folder)
        content = self.ls(
            blob_service,
            container_name,
            blob_folder,
            as_df=False)
        first = True
        for cont in content:
            if cont["content_length"] > 0:
                if first:
                    self.download(
                        blob_service,
                        container_name,
                        cont["name"],
                        file_path,
                        append=False)
                    first = False
                else:
                    self.download(
                        blob_service,
                        container_name,
                        cont["name"],
                        file_path,
                        append=True)
        return file_path

    def delete_blob(self, blob_service, container_name, blob_name):
        """
        delete a blob

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        """
        blob_name = self._interpret_path(blob_name)
        blob_service.delete_blob(container_name, blob_name)
        return blob_name

    def delete_folder(self, blob_service, container_name, blob_folder):
        """
        delete a folder and its content

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_folder         blob folder (remote folder name)

        .. versionadded:: 1.1
        """
        blob_folder = self._interpret_path(blob_folder)
        df = self.ls(blob_service, container_name, blob_folder)
        rem = []
        for name in df["name"]:
            r = self.delete_blob(blob_service, container_name, name)
            rem.append(r)
        return rem

    def url_blob(self, blob_service, container, blob_name):
        """
        returns an url for a blob file name

        @param      container       container
        @param      blob_name       blob_name
        @return                     url
        """
        blob_name = self._interpret_path(blob_name)
        src = blob_service.make_blob_url(container, blob_name)
        return src

    def copy_blob(self, blob_service, container, blob_name, source):
        """
        copy a blob

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           destination
        @param      source              source
        """
        blob_name = self._interpret_path(blob_name)
        url = self.url_blob(blob_service, container, source)
        res = blob_service.copy_blob(container, blob_name, url)
        return res

    def url_webHCatUrl(self, cmd):
        """
        returns an url to the cluster

        @param      cmd     something like ``pig``, ``status``
        @return             url
        """
        if self.hadoop_name is None:
            raise AttributeError(
                "no hadoop server was given to the constructor")
        webHCatUrl = 'https://' + self.hadoop_name + \
            '.azurehdinsight.net/templeton/v1/' + cmd
        return webHCatUrl

    def wasb_to_file(self, container_name, blob_file):
        """
        return something like ``wasb://demo@myblobstorage.blob...``

        @param      container_name  name of a container
        @param      blob_file       path to a file
        @return                     return a url to blob file (pig script for example)
        """
        blob_file = self._interpret_path(blob_file)
        return 'wasb://{1}@{0}.blob.core.windows.net/{2}'.format(container_name,
                                                                 self.account_name, blob_file)

    def wasb_prefix(self, container_name):
        """
        when using an instruction ``LOAD`` in a PIG script,
        file blob name must be reference using a wasb syntax.
        This method returns the prefix to add.

        @return     wasb prefix
        """
        return self.wasb_to_file(container_name, "")

    def get_status(self):
        """
        return the status of the webHCatUrl server

        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("status")

        r = requests.get(webHCatUrl,
                         auth=(self.hadoop_user_name, self.hadoop_key))
        if r.status_code != 200:
            raise AzureException(
                "unable to the status of server: " +
                webHCatUrl,
                r)
        return r.json()

    def get_version(self):
        """
        return the status of the WebHCat version

        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("version/hive")

        r = requests.get(webHCatUrl,
                         auth=(self.hadoop_user_name, self.hadoop_key))
        if r.status_code != 200:
            raise AzureException(
                "unable to the version of server: " +
                webHCatUrl,
                r)
        return r.json()

    def pig_submit(self,
                   blob_service,
                   container_name,
                   pig_file,
                   dependencies=None,
                   status_dir=None,
                   stop_on_failure=True,
                   params=None):
        """
        Submit a PIG job, the function uploads it to the cluster
        as well as the dependencies.

        The code comes from `How to use HDInsight from Linux <http://blogs.msdn.com/b/benjguin/archive/2014/02/18/how-to-use-hdinsight-from-linux.aspx>`_
        and `start a Pig + Jython job in HDInsight thru WebHCat <http://blogs.msdn.com/b/benjguin/archive/2014/03/21/start-a-pig-jython-job-in-hdinsight-thru-webhcat.aspx>`_.
        The API is described at `Pig Job — POST pig <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Pig>`_.

        @param      blob_service    returns by @see me open_blob_service
        @param      container_name  name of a container
        @param      pig_file        path to the job in the blob storage
        @param      dependencies    dependencies
        @param      status_dir      folder used by Hadoop to store job's progress, it should contain
                                    your alias if you want to avoid collision with others' jobs
        @param      stop_on_failure stop on failure, do not wait as long as possible
        @param      params          to
        @return                     json

        @example(Azure___Submit a job PIG)

        The script PIG must include an instruction ``LOAD``.
        This instruction use file name defined with the `wasb syntax <http://azure.microsoft.com/en-us/documentation/articles/hdinsight-use-blob-storage/>`_.

        If you place the string ``$CONTAINER`` before a stream name,
        it should be replaced by the corresponding wasb syntax associated
        to the container name defined by ``container_name``.
        The function will then load your script,
        modify it and save another one with the by adding
        ``.wasb.pig``.

        Others constants you could use:
            * ``$PSEUDO``
            * ``$CONTAINER``
            * ``$SCRIPTSPIG``

        However, this replacement is not done by this class, but your code could
        be such as:

        @code
        blobstorage = "****"
        blobpassword = "*********************"
        hadoop_name = "*********"
        hadoop_password = "********"
        username = "********"
        cl = AzureClient(blobstorage,
                         blobpassword,
                         hadoop_name,
                         hadoop_password,
                         username)
        script = '''
            myinput = LOAD '$CONTAINER/<input.csv>'
                      using PigStorage(',')
                      AS (index:long, sequence, tag, timestamp:long, dateformat, x:double,y:double, z:double, activity) ;
            filt = FILTER myinput BY activity == 'walking' ;
            STORE filt INTO '$PSEUDO/<output.csv>' USING PigStorage() ;
            '''

        with open("script_walking.pig","w") as f :
            f.write(script)

        bs = cl.open_blob_service()
        js = cl.pig_submit(bs, blobstorage, "testensae/script_walking.pig")
        print(js)

        js = cl.job_status('job_1414863995725_0013')
        @endcode
        @endexample

        .. versionadded:: 1.1
            parameter *stop_on_failure*
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        # upload
        scripts = self.default_parameters["SCRIPTPIG"]
        toup = [pig_file]
        if dependencies is not None:
            toup.extend(dependencies)
        res = self.upload(blob_service, container_name, scripts, toup)

        # path modification
        wasb = self.wasb_to_file(container_name, res[0])
        if dependencies is not None:
            wasbdep = ",".join(
                self.wasb_to_file(
                    container_name,
                    _) for _ in res[
                    1:])
        else:
            wasbdep = None

        # parameter
        args = ['-v']
        for k, v in sorted(self.default_parameters.items()):
            if k == "CONTAINER":
                args.extend(["-param", '%s=%s' %
                             (k, self.wasb_to_file(container_name, v))])
            else:
                args.extend(["-param", '%s=%s' % (k, v.replace('"', '\\"'))])
        if params is not None:
            for k, v in sorted(params.items()):
                args.extend(["-param", '%s=%s' % (k, v.replace('"', '\\"'))])

        if stop_on_failure:
            args.append("-stop_on_failure")

        # params
        params = {'user.name': self.hadoop_user_name,
                  'file': wasb,
                  'arg': args}

        if wasbdep is not None:
            params["files"] = wasbdep

        if status_dir is not None:
            status_dir = self._interpret_path(status_dir)
            params['statusdir'] = self.wasb_to_file(
                container_name, status_dir + "/" + os.path.split(pig_file)[-1] + ".log")
        else:
            status_dir = self.default_parameters["SCRIPTPIG"]
            params['statusdir'] = self.wasb_to_file(container_name, self.default_parameters[
                                                    "SCRIPTPIG"] + "/" + os.path.split(pig_file)[-1] + ".log")

        webHCatUrl = self.url_webHCatUrl("pig")

        # submit the job
        r = requests.post(webHCatUrl,
                          auth=(self.hadoop_user_name, self.hadoop_key),
                          data=params)

        if r.status_code != 200:
            raise AzureException("unable to submit job: " + pig_file, r)
        return r.json()

    def job_queue(self, showall=False):
        """
        returns the list of jobs

        It uses the API `Job Information — GET queue/:jobid <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Jobs>`_.

        @param      showall     if True, show all your jobs (not only yours)
        @return                 list of jobs
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("jobs")

        params = {"user.name": self.hadoop_user_name}
        if showall:
            params["showall"] = "true"

        r = requests.get(webHCatUrl,
                         auth=(self.hadoop_user_name, self.hadoop_key),
                         params=params)

        if r.status_code != 200:
            raise AzureException("unable to get job queue", r)
        return r.json()

    def job_status(self, jobid):
        """
        return the status of a job

        see `List Versions — GET version <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Job>`_
        for the outcome

        @param          jobid       jobid
        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        params = {"user.name": self.hadoop_user_name}
        webHCatUrl = self.url_webHCatUrl("jobs/" + jobid)

        r = requests.get(webHCatUrl,
                         auth=(self.hadoop_user_name, self.hadoop_key),
                         params=params)
        if r.status_code != 200:
            raise AzureException(
                "unable to the version of server: " +
                webHCatUrl,
                r)
        return r.json()

    def wait_job(self, job_id, delay=5, fLOG=noLOG):
        """
        wait until a job has run or failed

        @param      job_id      job_id
        @param      delay       check every N seconds
        @return                 status

        .. versionadded:: 1.1

        """
        status = self.job_status(job_id)
        while status["status"]["state"] in ["PREP", "RUNNING"]:
            fLOG("job_id", job_id, ":", status["status"]["state"])
            time.sleep(delay)
            status = self.job_status(job_id)
        return status

    def standard_outputs(self, job_id, blob_service, container, folder):
        """
        returns the standard output and error for a specific job id

        @param      job_id          job_id or status
        @param      blob_service    returns by @see me open_blob_service
        @param      container_name  name of a container
        @parm       folder          folder where to download them
        @return                     out, err
        """
        if isinstance(job_id, str):
            status = self.job_status(job_id)
        else:
            status = job_id

        status_dir = status["userargs"]["statusdir"]
        spl = status_dir.split("core.windows.net/")  # to change
        path = spl[-1]
        self.download(
            blob_service, container, [path + "/" + _ for _ in ["stderr", "stdout"]], folder)

        with open(os.path.join(folder, "stdout"), "r", encoding="utf8") as f:
            out = f.read()
        with open(os.path.join(folder, "stderr"), "r", encoding="utf8") as f:
            err = f.read()
        return out, err

    def job_kill(self, jobid):
        """
        kills a job

        see `Delete Job — DELETE queue/:jobid <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+DeleteJob>`_
        for the outcome

        @param          jobid       jobid
        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        params = {"user.name": self.hadoop_user_name}
        webHCatUrl = self.url_webHCatUrl("jobs/" + jobid)

        r = requests.delete(webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key),
                            params=params)
        if r.status_code != 200:
            raise AzureException(
                "unable to the version of server: " +
                webHCatUrl,
                r)
        return r.json()
