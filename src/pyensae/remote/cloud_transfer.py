"""
@file
@brief Common API for many remote drives

.. versionadded:: 1.3
"""
from pyquickhelper.loghelper import noLOG


class CloudTransfer:
    """
    defines a common API for a remote storage
    """

    def __init__(self, user, pwd, fLOG=None):
        """
        constructor

        @param      user        user name
        @param      pwd         password
        @param      fLOG        logging function
        """
        self._user = user
        self._pwd = pwd
        self.fLOG = noLOG if fLOG is None else fLOG

    def connect(self):
        """
        connect
        """
        raise NotImplementedError()

    def close(self):
        """
        close the connection
        """
        raise NotImplementedError()

    def upload_data(self, remote_path, data):
        """
        upload binary data

        @param      remote_path     path on the remote drive
        @param      data            bytes
        @return                     boolean
        """
        raise NotImplementedError()

    def download_data(self, remote_path):
        """
        download binary data

        @param      remote_path     path on the remote drive
        @return                     data (bytes)
        """
        raise NotImplementedError()
