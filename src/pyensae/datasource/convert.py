"""
@file
@brief Various conversion function
"""

import pandas

def dBase2df(file, encoding="cp437"):
    """
    converts a dBase file into a list of dataframe (one per table)
    
    @param      file        file name
    @param      encoding    table encoding
    @return                 list of dataframes (pandas)
    
    The module relies on `dbfread <https://pypi.python.org/pypi/dbfread/>`_.
    """
    
    import dbfread
    table = dbfread.open(file, load=True, encoding=encoding)
    res = [ _ for _ in table ]
    return pandas.DataFrame(table.records)

    