# -*- coding: utf-8 -*-
"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import requests
import os
import time
import io
import warnings

from .azure_exception import AzureException
from pyquickhelper.loghelper import noLOG


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

    .. exref::
        :title: Get the list of containers and files from a blob storage?
        :tag: Azure

        The functionalities of a ``BlobService`` are described in
        `blockblobservice.py <https://github.com/Azure/azure-storage-python/blob/master/azure/storage/blob/blockblobservice.py>`_.

        ::

            from pyensae.remote.azure_connection import AzureClient
            cl = AzureClient("<blob_storage_service>",
                            "<primary_key>")
            bs = cl.open_blob_service()
            res = cl.ls(bs)
            for r in res:
                print(r["name"])

    .. exref::
        :title: Upload, download, to a blob storage
        :tag: Azure

        The following example uploads and downloads a file on a Blob Storage.

        ::

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
            SCRIPTHIVE=self.pseudo + "/scripts/hive",
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
        try:
            from azure.storage.blob import BlobService
        except ImportError:
            from azure.storage.blob import BlockBlobService as BlobService
        return BlobService(self.account_name, self.account_key)

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
                if hasattr(b, "url"):
                    obs["url"] = b.url
                else:
                    obs["url"] = blob_service.make_blob_url(
                        container_name, b.name)
                for p in AzureClient._blob_properties:
                    if hasattr(b.properties, p):
                        obs[p] = getattr(b.properties, p)
                    else:
                        obs[p] = None

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
            if hasattr(blob_service, "put_blob"):
                # this code should disappear as it relies on an old version of
                # the module azure
                blob_service.create_container(
                    container_name, None, None, False)
                blob_service.put_blob(
                    container_name, blob_name, None, 'BlockBlob')

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
                            self.LOG("uploaded", index,
                                     " bytes from ", file_path)
                        else:
                            break

                blob_service.put_block_list(
                    container_name, blob_name, block_ids)
            else:
                blob_service.create_blob_from_path(
                    container_name, blob_name, file_path)

            return blob_name

    def upload_data(self,
                    blob_service,
                    container_name,
                    blob_name,
                    data):
        """
        Uploads data (bytes) to a blob storage.
        No more than 64Mb can be uploaded at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        @param      data                bytes
        @return                         list of uploaded blob names

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.

        .. versionadded:: 1.1
        """
        blob_name = self._interpret_path(blob_name)
        blob_service.create_container(container_name, None, None, False)
        if hasattr(blob_service, "put_blob"):
            # this code should disappear as it relies on an old version of the
            # module azure
            blob_service.put_blob(container_name, blob_name, None, 'BlockBlob')

            block_ids = []
            index = 0
            while True:
                if len(data) > AzureClient._chunk_size:
                    da = data[:AzureClient._chunk_size]
                    data = data[AzureClient._chunk_size:]
                else:
                    da = data
                    data = None
                block_id = '{0:08d}'.format(index)
                blob_service.put_block(
                    container_name,
                    blob_name,
                    da,
                    block_id)
                block_ids.append(block_id)
                index += 1
                if not data:
                    break

            blob_service.put_block_list(container_name, blob_name, block_ids)
        else:
            blob_service.create_blob_from_bytes(
                container_name, blob_name, data)
        return blob_name

    def download(self,
                 blob_service,
                 container_name,
                 blob_name,
                 file_path=None,
                 append=False,
                 chunk_size=None,
                 stop_at=None):
        """
        Downloads data from a blob storage to a file.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (or list of blob names) (remote file name)
        @param      file_path           local file path
        @param      append              if True, append the content to an existing file
        @param      chunk_size          download by chunk
        @param      stop_at             stop at a given size (None to avoid stopping)
        @return                         local file or bytes if *file_path* is None

        The code comes from `Utilisation du service de stockage d'objets blob à partir de Python <http://azure.microsoft.com/fr-fr/documentation/articles/storage-python-how-to-use-blob-storage/>`_.

        .. versionchanged:: 1.1
            Parameters *append*, *chunk_size* were added.
            If *file_path* is None (default value now), the function
            returns bytes.
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
                    append=append,
                    chunk_size=chunk_size,
                    stop_at=stop_at)
                res.append(r)
                if stop_at is not None:
                    if file_path is None:
                        stop_at -= len(r)
                    else:
                        stop_at -= os.stat(r).st_size
                        if stop_at <= 0:
                            break
            if file_path is None:
                st = io.BytesIO()
                for r in res:
                    st.write(r)
                return st.getvalue()
            else:
                return res
        else:
            blob_name = self._interpret_path(blob_name)

            if hasattr(blob_service, "get_blob"):
                # this code should disappear as it relies on an old version of
                # the module azure
                props = blob_service.get_blob_properties(
                    container_name, blob_name)
                if hasattr(props, "properties"):
                    blob_size = props.properties.content_length
                else:
                    blob_size = int(props['content-length'])
                if chunk_size is None:
                    chunk_size = AzureClient._chunk_size
                if stop_at is not None and stop_at < chunk_size:
                    chunk_size = max(stop_at, 0)

                def iterations(f, chunk_size,
                               container_name, blob_name, file_path, stop_at):
                    index = 0

                    while index < blob_size:
                        chunk_range = 'bytes={}-{}'.format(index,
                                                           index + chunk_size - 1)
                        data = blob_service.get_blob(
                            container_name,
                            blob_name,
                            x_ms_range=chunk_range)
                        length = len(data)
                        index += length
                        self.LOG("downloaded ", index,
                                 "bytes from ", file_path)
                        if length > 0:
                            f.write(data)
                            if length < chunk_size:
                                return False
                        else:
                            return False
                        if stop_at is not None and stop_at <= index:
                            return False
                    return True

                if file_path is None:
                    f = io.BytesIO()
                    iterations(f, chunk_size,
                               container_name, blob_name, file_path, stop_at)
                    return f.getvalue()
                else:
                    mode = 'ab' if append else 'wb'
                    with open(file_path, mode) as f:
                        iterations(f, chunk_size,
                                   container_name, blob_name, file_path, stop_at)
                    return file_path
            else:
                bl = blob_service.get_blob_to_bytes(container_name, blob_name)
                if file_path is None:
                    return bl.content
                else:
                    with open(file_path, "wb") as f:
                        f.write(bl.content)
                    return file_path

    def download_data(self,
                      blob_service,
                      container_name,
                      blob_name,
                      chunk_size=None,
                      stop_at=None):
        """
        Downloads data from a blob storage and return bytes.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (or list of blob names) (remote file name)
        @param      chunk_size          download by chunk
        @param      stop_at             stop at a given size (None to avoid stopping)
        @return                         local file or bytes if *file_path* is None

        .. versionadded:: 1.1
        """
        return self.download(blob_service=blob_service, container_name=container_name,
                             blob_name=blob_name, chunk_size=chunk_size, stop_at=stop_at)

    def df_head(self,
                blob_service,
                container_name,
                blob_name,
                stop_at=2 ** 20,
                encoding="utf-8",
                as_df=True,
                merge=False,
                **options):
        """
        Download the beginning of a stream and displays as a DataFrame

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (or list of blob names) (remote file name)
        @param      stop_at             stop at a given size (None to avoid stopping)
        @param      encoding            encoding
        @param      as_df               result as a dataframe or a string
        @param      merge               if True, *blob_name* is a folder, method @see me download_merge is called
        @param      options             see  `read_csv <http://pandas.pydata.org/pandas-docs/version/0.17.0/generated/pandas.read_csv.html?highlight=read_csv#pandas.read_csv>`_
        @return                         local file or bytes if *file_path* is None

        .. versionadded:: 1.1
        """
        if merge:
            do = self.download_merge(blob_service=blob_service,
                                     container_name=container_name,
                                     blob_folder=blob_name,
                                     stop_at=stop_at)
        else:
            do = self.download(blob_service=blob_service,
                               container_name=container_name,
                               blob_name=blob_name,
                               stop_at=stop_at)
        text = do.decode(encoding)
        if as_df:
            pos = text.rfind("\n")
            if pos > 0:
                st = io.StringIO(text[:pos])
            else:
                st = io.StringIO(text)
            import pandas
            return pandas.read_csv(st, **options)
        else:
            return text

    def download_merge(self,
                       blob_service,
                       container_name,
                       blob_folder,
                       file_path=None,
                       chunk_size=None,
                       stop_at=None):
        """
        Downloads all files from a folder in a blob storage to a single local file.
        Files will be merged.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.

        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_folder         blob folder(remote file name)
        @param      file_path           local file path
        @param      chunk_size          download by chunk
        @param      stop_at             stop at a given size (None to avoid stopping)
        @return                         local file

        .. versionchanged:: 1.1
            Parameters *append*, *chunk_size* were added.
            If *file_path* is None (default value now), the function
            returns bytes.
        """
        blob_folder = self._interpret_path(blob_folder)
        content = self.ls(
            blob_service,
            container_name,
            blob_folder,
            as_df=False)
        first = True
        store = io.BytesIO()
        for cont in content:
            if cont["content_length"] > 0:
                by = self.download(
                    blob_service,
                    container_name,
                    cont["name"],
                    file_path=file_path,
                    chunk_size=chunk_size,
                    stop_at=stop_at,
                    append=not first)
                if first:
                    first = False
                if file_path is None:
                    store.write(by)
                    if stop_at is not None:
                        stop_at -= len(by)
                else:
                    if stop_at is not None:
                        stop_at -= os.stat(file_path).st_size
            if stop_at is not None and stop_at <= 0:
                break

        if file_path is None:
            return store.getvalue()
        else:
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
                "no hadoop server was given to the constructor for cmd: {0}".format(cmd))
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

        .. exref::
            :title: Submit a job PIG
            :tag: Azure

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

            ::

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
                    myinput = LOAD '$CONTAINER/input.csv'
                            using PigStorage(',')
                            AS (index:long, sequence, tag, timestamp:long, dateformat, x:double,y:double, z:double, activity) ;
                    filt = FILTER myinput BY activity == 'walking' ;
                    STORE filt INTO '$PSEUDO/output.csv' USING PigStorage() ;
                    '''

                with open("script_walking.pig","w") as f :
                    f.write(script)

                bs = cl.open_blob_service()
                js = cl.pig_submit(bs, blobstorage, "testensae/script_walking.pig")
                print(js)

                js = cl.job_status('job_1414863995725_0013')

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
            raise AzureException(
                "unable to submit job: {0}\n---\nWITH PARAMS\n---\n{1}".format(pig_file, params), r)
        return r.json()

    def hive_submit(self, blob_service, container_name, hive_file, dependencies=None,
                    status_dir=None, stop_on_failure=True, params=None):
        """
        Submit a HIVE job, the function uploads it to the cluster
        as well as the dependencies.

        The code comes from `How to use HDInsight from Linux <http://blogs.msdn.com/b/benjguin/archive/2014/02/18/how-to-use-hdinsight-from-linux.aspx>`_
        and `start a Pig + Jython job in HDInsight thru WebHCat <http://blogs.msdn.com/b/benjguin/archive/2014/03/21/start-a-pig-jython-job-in-hdinsight-thru-webhcat.aspx>`_.
        The API is described at `Pig Job — POST pig <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Pig>`_.

        @param      blob_service    returns by @see me open_blob_service
        @param      container_name  name of a container
        @param      hive_file       path to the job in the blob storage
        @param      dependencies    dependencies
        @param      status_dir      folder used by Hadoop to store job's progress, it should contain
                                    your alias if you want to avoid collision with others' jobs
        @param      stop_on_failure stop on failure, do not wait as long as possible
        @param      params          to
        @return                     json

        .. versionadded:: 1.1
        """
        if self.hadoop_user_name is None:
            raise AttributeError(
                "no hadoop user name was given to the constructor")
        if self.hadoop_key is None:
            raise AttributeError(
                "no hadoop password was given to the constructor")

        # upload
        scripts = self.default_parameters["SCRIPTHIVE"]
        toup = [hive_file]
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
                container_name, status_dir + "/" + os.path.split(hive_file)[-1] + ".log")
        else:
            status_dir = self.default_parameters["SCRIPTHIVE"]
            params['statusdir'] = self.wasb_to_file(container_name, self.default_parameters[
                                                    "SCRIPTHIVE"] + "/" + os.path.split(hive_file)[-1] + ".log")

        webHCatUrl = self.url_webHCatUrl("hive")

        warnings.warn("Hive submission is not tested. It will probably fail.")

        # submit the job
        r = requests.post(webHCatUrl,
                          auth=(self.hadoop_user_name, self.hadoop_key),
                          data=params)

        if r.status_code != 200:
            raise AzureException(
                "unable to submit job: {0}\n---\nWITH PARAMS\n---\n{1}".format(hive_file, params), r)
        return r.json()

    def job_queue(self, showall=False, fields=None):
        """
        returns the list of jobs

        It uses the API `Job Information — GET queue/:jobid <https://cwiki.apache.org/confluence/display/Hive/WebHCat+Reference+Jobs>`_.

        @param      showall     if True, show all your jobs (not only yours)
        @param      fields      to add fields in the requests
        @return                 list of jobs

        .. exref::
            :title: List job queue
            :tag: Azure

            Most of the time, a job remains stuck in the job queue because
            it is full. Here is a code to check that is the case on
            a Azure cluster. It should be executed from a notebook.

            Connection ::

                blobstorage = "..."
                blobpassword = "..."
                hadoop_server = "..."
                hadoop_password = "..."
                username = "..."

                import pyensae
                client, bs = %hd_open

            Job queue ::

                res = client.job_queue()
                res.reverse()   # last submitted jobs first

            Displays the first 20 jobs::

                for i, r in enumerate(res[:20]):
                    st = client.job_status(r["id"])
                    print(i, r, st["status"]["state"],datetime.fromtimestamp(float(st["status"]["startTime"])/1000), st["status"]["jobName"])
                    print(st["userargs"].get("file", None), st["profile"].get("jobName", None))

            It gives::

                0 {'detail': None, 'id': 'job_1451961118663_3126'} PREP 2016-01-26 21:57:28.756000 TempletonControllerJob
                wasb://..../scripts/pig/titi.pig TempletonControllerJob
                1 {'detail': None, 'id': 'job_1451961118663_3125'} PREP 2016-01-26 21:57:28.517999 TempletonControllerJob
                wasb://..../scripts/pig/pre_processing.pig TempletonControllerJob
                2 {'detail': None, 'id': 'job_1451961118663_3124'} PREP 2016-01-26 21:50:32.742000 TempletonControllerJob
                wasb://..../scripts/pig/titi.pig TempletonControllerJob
                3 {'detail': None, 'id': 'job_1451961118663_3123'} RUNNING 2016-01-26 21:46:57.219000 TempletonControllerJob
                wasb://..../scripts/pig/alg1.pig TempletonControllerJob
                4 {'detail': None, 'id': 'job_1451961118663_3122'} SUCCEEDED 2016-01-26 21:40:34.687999 PigLatin:pre_processing.pig
                None PigLatin:pre_processing.pig
                5 {'detail': None, 'id': 'job_1451961118663_3121'} RUNNING 2016-01-26 21:41:29.657000 TempletonControllerJob
                wasb://..../scripts/pig/Algo_LDA2.pig TempletonControllerJob
                6 {'detail': None, 'id': 'job_1451961118663_3120'} SUCCEEDED 2016-01-26 21:40:06.859999 TempletonControllerJob
                wasb://..../scripts/pig/alg1.pig TempletonControllerJob

            To kill a job::

                client.job_kill("id")
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
        if fields:
            if fields != "*":
                raise ValueError("fields can only be *")
            params["fields"] = fields

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

        You can extract the *startTime* by doing::

            from datetime import datetime
            st = client.job_status(<job_id>)
            datetime.fromtimestamp(float(st["status"]["startTime"])/1000)
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
