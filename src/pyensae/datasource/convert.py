"""
@file
@brief Various conversion functions.
"""
import pandas
from pyquickhelper.loghelper import noLOG
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
    table = dbfread.DBF(file, load=False, encoding=encoding)
    res = [_ for _ in table]
    return pandas.DataFrame(res)


def dBase2sqllite(
        db, table, encoding="cp437", overwrite_table=None, fLOG=noLOG):
    """
    Put all rows from a dBase database into sqlite

    Add a dbase table to an open sqlite database.

    @param      db                  cursor on SQLite or file name
    @param      table               DBF object or filename
    @param      encoding            encoding if table is a filename
    @param      overwrite_table     overwrite the table name
    @param      fLOG                logging function, to see the progress

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

    if isinstance(db, str):
        cursor = Database(db, LOG=fLOG)
        cursor.connect()
    else:
        cursor = db

    if isinstance(table, str):
        import dbfread
        table = dbfread.DBF(table, load=False, encoding=encoding)

    cursor.execute('drop table if exists %s' % table.name)

    field_types = {}
    for f in table.fields:
        field_types[f.name] = typemap.get(f.type, 'TEXT')

    table_name = overwrite_table if overwrite_table is not None else table.name

    # Create the table
    #
    defs = ', '.join(['%s %s' % (f, field_types[f])
                      for f in table.field_names])
    sql = 'create table %s (%s)' % (table_name, defs)
    cursor.execute(sql)

    # Create data rows
    refs = ', '.join([':' + f for f in table.field_names])
    sql = 'insert into %s values (%s)' % (table_name, refs)

    for i, rec in enumerate(table):
        cursor._connection.execute(sql, list(rec.values()))
        if i % 20000 == 0:
            fLOG("moving line ", i, " to table", table_name)

    if isinstance(db, str):
        cursor.commit()
        cursor.close()
