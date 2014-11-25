#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

import sys
if sys.version_info[0] < 3 :
    raise ImportError("pyensae only works with Python 3")

__version__ = "1.1"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pyensae"
__url__ = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#pyensae"
__license__ = "BSD License"

def check( log = False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception
    """
    return True

from .resources.http_retrieve import download_data
from .sql.database_helper import import_flatfile_into_database
from .file_helper.content_helper import replace_comma_by_point
from .finance.astock import StockPrices
from .sql.database_main import Database
from .datasource.data_velib import DataVelibCollect
from .datasource.convert import dBase2df, dBase2sqllite
from .file_helper.decompress_helper import decompress_zip, decompress_targz, decompress_gz
from .remote.ssh_remote_connection import ASSHClient
from .sql.sql_interface import InterfaceSQL, InterfaceSQLException
from .remote.azure_connection import AzureClient

try:
    from IPython import get_ipython
    from .remote.magic_remote_ssh import register_magics_ssh
    try:
        from .remote.magic_azure import register_azure_magics
        az = True
    except ImportError as e :
        if "azure" in str(e):
            az= False
        else:
            raise e
    from .sql.magic_sql import register_sql_magics
    from .file_helper.magic_file import register_file_magics
    ip = get_ipython()
    if ip is not None:
        # the program is not run from a notebook
        register_magics_ssh()
        if az: register_azure_magics()
        register_sql_magics()
        register_file_magics()
except ImportError:
    # IPython is not installed
    pass