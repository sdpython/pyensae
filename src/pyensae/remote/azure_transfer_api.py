"""
@file
@brief API to move files

.. versionadded:: 1.1
"""
import azure
from pyquickhelper.filehelper import TransferAPI
import pyquickhelper.loghelper as pyqlog
from .azure_drive import AzureDrive


class AzureTransferAPI(TransferAPI):
    """
    defines an API to transfer files over a remote location

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
        self.fLOG = fLOG if fLOG else pyqlog.noLOG
        self._azure = AzureDrive(
            blob, key, fLOG=self.fLOG, container=container)
        self._azure.connect()

    def transfer(self, path, data):
        """
        we assume a data holds in memory,
        tansfer data to path

        @param      data        bytes
        @param      path        path to remove location
        @return                 boolean
        """
        self._azure.upload_data(path, data)
        return True

    def retrieve(self, path, exc=True):
        """
        retrieve data from path

        @param      path        remove location
        @param      exc         keep exception
        @return                 data
        """
        if exc:
            return self._azure.download_data(path)
        else:
            try:
                return self._azure.download_data(path)
            except azure.common.AzureMissingResourceHttpError:
                return None
