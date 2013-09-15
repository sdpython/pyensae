"""
@file
@brief Main file
"""

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
