# -*- coding: utf-8 -*-
"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import requests
import azure.storage

class AzureException(Exception):
    """
    exception raised by @see cl AzureClient
    """
    def __init__(self, message, ret):
        """
        store more information than a regular exception

        @param      message             error message
        @param      ret                 results of the requests
        """
        Exception.__init__(self, message)

        if ret is not None:
            code = ret.status_code
            try:
                js = ret.json()
            except Exception as e :
                js = str(e) + "\n" + str(ret)

            self.ret = (code, js)
        else:
            self.ret = (None,None)

    def __str__(self):
        """
        usual
        """
        s = Exception.__str__(self)
        f = "STATUS: {0}, JSON: {1}\n{2}".format(self.ret[0], self.ret[1], s)
        return f

class AzureClient():
    """

    .. index: Azure

    A simple class to access and communicate with `Azure <http://azure.microsoft.com/>`_.
    It requires modules:

    * `azure <https://github.com/Azure/azure-sdk-for-python>`_
    * `requests <http://docs.python-requests.org/en/latest/>`_

    Main functionalities related to blob:
        * list_containers, create_container, list_blobs, put_blob, put_block_blob_from_bytes
        * put_block_blob_from_text, put_page_blob_from_file, get_blob, get_blob

    .. index: blob

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
                        ]

    def __init__(self,  blob_name,
                        blob_key,
                        hadoop_name = None,
                        hadoop_key  = None,
                        hadoop_user_name = "admin",
                        fLOG = None):
        """
        constructor

        @param      blob_name       blob storage name
        @param      blob_key        account key for the blob storage
        @param      hadoop_name     hadoop server name (can be None if HDInsight is not used)
        @param      hadoop_key      hadoop key (can be None if HDInsight is not used)
        @param      fLOG            logging function
        """
        self.account_name       = blob_name
        self.account_key        = blob_key
        self.hadoop_name        = hadoop_name
        self.hadoop_key         = hadoop_key
        self.hadoop_user_name   = hadoop_user_name
        if fLOG is None:
            def _log_(*l,**p): return
            self.LOG = _log_
        else:
            self.LOG = fLOG

    @staticmethod
    def mask_string(s):
        """
        return empty string or as many ``*`` as the length of the string
        """
        if s is None : return ""
        else: return "*" * len(s)

    def __str__(self):
        """
        usual
        """
        mes = "AzureClient [blob:({0},{1}), hadoop:({2},{3},{4})]".format( AzureClient.mask_string(self.account_name),
                    AzureClient.mask_string(self.account_key), AzureClient.mask_string(self.hadoop_name),
                    AzureClient.mask_string(self.hadoop_key), AzureClient.mask_string(self.hadoop_user_name))
        return mes

    def open_blob_service(self):
        """
        open a blob service
        """
        return azure.storage.BlobService(self.account_name, self.account_key)

    def ls(self, blob_service, container_name = None, path = None):
        """
        return the content of a blob storage

        @param      blob_service        blob service, returned by @see me open_blob_service
        @param      container_name      None for all, its name otherwise
        @param      path                path in the container
        @return                         list of dictionaries
        """
        res = [ ]
        if container_name is None:
            for cn in blob_service.list_containers():
                self.LOG("exploring ", cn.name)
                r = self.ls(blob_service, cn.name, path = path)
                res.extend(r)
            return res
        else :
            res = [ ]
            for b in blob_service.list_blobs(container_name, prefix = path):
                obs = { }
                obs["name"] = b.name
                obs["url"] = b.url
                obs["metadata"] = b.metadata
                for p in AzureClient._blob_properties:
                    obs[p] = b.properties.__dict__[p]
                res.append ( obs )
            return res

    _chunk_size = 4 * 1024 * 1024

    def upload( self,
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

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.
        """
        blob_service.create_container(container_name, None, None, False)
        blob_service.put_blob(container_name, blob_name, None, 'BlockBlob')

        block_ids = []
        index = 0
        with open(file_path, 'rb') as f:
            while True:
                data = f.read(AzureClient._chunk_size)
                if data:
                    length = len(data)
                    block_id = '{0:08d}'.format(index)
                    blob_service.put_block(container_name, blob_name, data, block_id)
                    block_ids.append(block_id)
                    index += 1
                    self.LOG("uploaded", index, " bytes from ",file_path)
                else:
                    break

        blob_service.put_block_list(container_name, blob_name, block_ids)

    def download(   self,
                    blob_service,
                    container_name,
                    blob_name,
                    file_path):
        """
        Downloads data from a blob storage to a file.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        @param      file_path           local file path
        @return                         local file

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.
        """
        props = blob_service.get_blob_properties(container_name, blob_name)
        blob_size = int(props['content-length'])

        index = 0
        with open(file_path, 'wb') as f:
            while index < blob_size:
                chunk_range = 'bytes={}-{}'.format(index, index + AzureClient._chunk_size - 1)
                data = blob_service.get_blob(container_name, blob_name, x_ms_range=chunk_range)
                length = len(data)
                index += length
                self.LOG("downloaded ", index, "bytes from ",file_path)
                if length > 0:
                    f.write(data)
                    if length < AzureClient._chunk_size:
                        break
                else:
                    break
        return file_path

    def download_merge(   self,
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
        raise NotImplementedError()
        
    def delete_blob(self, blob_service, container_name, blob_name):
        """
        delete a blob

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        """
        return blob_service.delete_blob(container_name, blob_name)

    def url_blob(self, blob_service, container, blob_name):
        """
        returns an url for a blob file name

        @param      container       container
        @param      blob_name       blob_name
        @return                     url
        """
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
            raise AttributeError("no hadoop server was given to the constructor")
        webHCatUrl='https://' + self.hadoop_name + '.azurehdinsight.net/templeton/v1/' + cmd
        return webHCatUrl

    def wasb_to_file(self, container_name, blob_file):
        """
        return something like ``wasb://demo@myblobstorage.blob...``

        @param      container_name  name of a container
        @param      blob_file       path to a file
        @return                     return a url to blob file (pig script for example)
        """
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
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("status")

        r = requests.get(  webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key))
        if r.status_code != 200:
            raise AzureException("unable to the status of server: " + webHCatUrl, r)
        return r.json()

    def get_version(self):
        """
        return the status of the WebHCat version

        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("version/hive")

        r = requests.get(  webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key))
        if r.status_code != 200:
            raise AzureException("unable to the version of server: " + webHCatUrl, r)
        return r.json()

    def pig_submit(self, container_name, blob_pig, status_dir = None):
        """
        Submit a PIG job assuming this script
        was uploaded to the blog storage

        The code comes from `How to use HDInsight from Linux <http://blogs.msdn.com/b/benjguin/archive/2014/02/18/how-to-use-hdinsight-from-linux.aspx>`_
        and `start a Pig + Jython job in HDInsight thru WebHCat <http://blogs.msdn.com/b/benjguin/archive/2014/03/21/start-a-pig-jython-job-in-hdinsight-thru-webhcat.aspx>`_.
        The API is described at `Pig Job — POST pig <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Pig>`_.

        @param      container_name  name of a container
        @param      blob_pig        path to the job in the blob storage
        @param      status_dir      folder used by Hadoop to store job's progress, it should contain
                                    your alias if you want to avoid collision with others' jobs
        @return                     json

        @example(Azure___Submit a job PIG)

        The script PIG must include an instruction ``LOAD``.
        This instruction use file name defined with the `wasb syntax <http://azure.microsoft.com/en-us/documentation/articles/hdinsight-use-blob-storage/>`_.

        If you place the string ``__CONTAINER__`` before a stream name,
        it will be replaced by the corresponding wasb syntax associated
        to the container name defined by ``container_name``.
        The function will then load your script,
        modify it and save another one with the by adding
        ``.wasb.pig``.

        @code
        blobstorage = "****"
        blobpassword = "*********************"
        hadoop_name = "*********"
        hadoop_password = "********"
        cl = AzureClient(blobstorage,
                         blobpassword,
                         hadoop_name,
                         hadoop_password)
        script = '''
            myinput = LOAD '__CONTAINER__<input.csv>'
                      using PigStorage(',')
                      AS (index:long, sequence, tag, timestamp:long, dateformat, x:double,y:double, z:double, activity) ;
            filt = FILTER myinput BY activity == 'walking' ;
            STORE filt INTO '__CONTAINER__<output.csv>' USING PigStorage() ;
            '''

        script = script.replace("__CONTAINER__", cl.wasb_prefix(blobstorage))

        with open("script_walking.pig","w") as f :
            f.write(script)

        bs = cl.open_blob_service()
        cl.upload(bs, blobstorage, "testensae/script.pig", "script_walking.pig")

        for f in cl.ls(bs, blobstorage, "testensae"):
            print(f["name"])

        js = cl.pig_submit(blobstorage, "testensae/script.pig", "status/pig/xavierdupre")
        print(js)

        js = cl.job_status('job_1414863995725_0013')
        @endcode
        @endexample
        """
        if self.hadoop_user_name is None:
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        wasb = self.wasb_to_file(container_name, blob_pig)

        params =    {'user.name':self.hadoop_user_name,
                     'file': wasb,
                     'arg':'-v'}

        if status_dir is not None:
            params['statusdir'] = self.wasb_to_file(container_name, status_dir)

        webHCatUrl = self.url_webHCatUrl("pig")

        r = requests.post(  webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key),
                            data=params)

        if r.status_code != 200:
            raise AzureException("unable to submit job: " + blob_pig, r)
        return r.json()

    def job_queue(self, showall = False):
        """
        returns the list of jobs

        It uses the API `Job Information — GET queue/:jobid <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Jobs>`_.

        @param      showall     if True, show all your jobs (not only yours)
        @return                 list of jobs
        """
        if self.hadoop_user_name is None:
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        webHCatUrl = self.url_webHCatUrl("jobs")

        params = { "user.name": self.hadoop_user_name }
        if showall:
            params["showall"]="true"

        r = requests.get(   webHCatUrl,
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
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        params = { "user.name":self.hadoop_user_name}
        webHCatUrl = self.url_webHCatUrl("jobs/" + jobid)

        r = requests.get(  webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key),
                            params=params)
        if r.status_code != 200:
            raise AzureException("unable to the version of server: " + webHCatUrl, r)
        return r.json()

    def job_kill(self, jobid):
        """
        kills a job

        see `Delete Job — DELETE queue/:jobid <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+DeleteJob>`_
        for the outcome

        @param          jobid       jobid
        @return                     json
        """
        if self.hadoop_user_name is None:
            raise AttributeError("no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError("no hadoop password was given to the constructor")

        params = { "user.name":self.hadoop_user_name}
        webHCatUrl = self.url_webHCatUrl("jobs/" + jobid)

        r = requests.delete(  webHCatUrl,
                            auth=(self.hadoop_user_name, self.hadoop_key),
                            params=params)
        if r.status_code != 200:
            raise AzureException("unable to the version of server: " + webHCatUrl, r)
        return r.json()
        
        