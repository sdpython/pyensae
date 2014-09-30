"""
@file
@brief Various conversion function
"""

import pandas

from ..sql.database_main import Database

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

def dBase2sqllite(db, table, encoding="cp437"):
    """
    Put all rows from a dBase database into sqlite
    
    Add a dbase table to an open sqlite database.
    
    @param      db          cursor on SQLite or file name
    @param      table       DBF object
    @param      encoding    encoding if table is a filename
    
    The table will be removed if it exists.
    """
    
    typemap = {
        'F': 'FLOAT',
        'L': 'BOOLEAN',
        'I': 'INTEGER',
        'C': 'TEXT',
        'N': 'REAL',  # because it can be integer or float
        'M': 'TEXT',
        'D': 'DATE',
        'T': 'DATETIME',
        '0': 'INTEGER',
    }    
    
    if isinstance(db,str):
        cursor = Database(db)
        cursor.connect()
    else :
        cursor = db
        
    if isinstance(table, str):
        import dbfread
        table = dbfread.open(table, load=False, encoding=encoding)
    
    cursor.execute('drop table if exists %s' % table.name)

    field_types = {}
    for f in table.fields:
        field_types[f.name] = typemap.get(f.type, 'TEXT')

    #
    # Create the table
    #
    defs = ', '.join(['%s %s' % (f, field_types[f])
                      for f in table.field_names])
    sql = 'create table %s (%s)' % (table.name, defs)
    cursor.execute(sql)

    # Create data rows
    refs = ', '.join([':' + f for f in table.field_names])
    sql = 'insert into %s values (%s)' % (table.name, refs)

    for i,rec in enumerate(table):
        cursor._connection.execute(sql, list(rec.values())) 
        #if i % 20000 == 0 : print(i)
    
    if isinstance(db, str):
        cursor.commit()
        cursor.close()
        
        