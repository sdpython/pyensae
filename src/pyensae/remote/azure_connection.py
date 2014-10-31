# -*- coding: utf-8 -*-
"""
@file
@brief A class to help connect with a remote machine and send command line.
"""

import time, socket
import azure.storage


class AzureClient():
    """
    
    .. index: Azure
    
    A simple class to access to communite with `Azure <http://azure.microsoft.com/>`_.
    It requires modules 
    `azure <https://github.com/Azure/azure-sdk-for-python>`_.
    
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
                                   "another_local_filaname.txt")
    
    @endcode
    @endexample
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

    def __init__(self, account_name, account_key, fLOG = None):
        """
        constructor
        
        @param      account_name    account name
        @param      account_key     account key
        @param      fLOG            logging function
        """
        self.account_name = account_name
        self.account_key  = account_key
        if fLOG is None:
            def _log_(*l,**p): return
            self.LOG = _log_
        else:
            self.LOG = fLOG
        
    def __str__(self):
        """
        usual
        """
        return "AzureClient"

    def open_blob_service(self):
        """
        open a blob service
        """
        return azure.storage.BlobService(self.account_name, self.account_key)
        
    def ls(self, blob_service, container_name = None):
        """
        return the content of a blob storage
        
        @param      blob_service        blob service, returned by @see me open_blob_service
        @param      container_name      None for all, its name otherwise
        @return                         list of dictionaries
        """
        res = [ ]
        if container_name is None:
            for cn in bs.list_containers():
                self.LOG("exploring ", cn.name)
                r = self.ls(blob_service, cn.name)
                res.extend(r)
            return res
        else :
            res = [ ]
            for b in bs.list_blobs(container_name):
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
        Downloads data from a file to a blob storage.
        No more than 64Mb can be downloaded  at the same, it needs to be split into
        pieces.
        
        @param      blob_service        returns by @see me open_blob_service
        @param      container_name      container name
        @param      blob_name           blob name (remote file name)
        @param      file_path           local file path
        
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
        
if __name__ == "__main__":
    pass
