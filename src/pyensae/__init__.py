#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

__version__ = "0.7"
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
from .file.file_helper import replace_comma_by_point
from .finance.astock import StockPrices
from .sql.database_main import Database
from .datasource.data_velib import DataVelibCollect
from .datasource.convert import dBase2df