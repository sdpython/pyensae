"""
@file
@brief Common API to upload, download data from Azure

.. versionadded:: 1.1
"""
from .cloud_transfer import CloudTransfer
from .azure_connection import AzureClient


class AzureDrive(CloudTransfer):
    """
    defines a common API for a remote storage

    .. versionadded:: 1.1
    """

    def __init__(self, blob, key, fLOG=None, container="backup"):
        """
        constructor

        @param      blob        blob storage
        @param      key         key
        @param      container   container name
        @param      fLOG        logging function
        """
        CloudTransfer.__init__(self, blob, key, fLOG)
        self._client = AzureClient(blob, key)
        self._container = container

    def connect(self):
        """
        connect
        """
        self._service = self._client.open_blob_service()

    def close(self):
        """
        close the connection
        """
        pass

    def upload_data(self, remote_path, data):
        """
        upload binary data

        @param      remote_path     path on the remote drive
        @param      data            bytes
        @return                     boolean
        """
        self._client.upload_data(
            self._service, self._container, remote_path, data)

    def download_data(self, remote_path):
        """
        download binary data

        @param      remote_path     path on the remote drive
        @return                     data (bytes)
        """
        return self._client.download_data(self._service, self._container, remote_path)
