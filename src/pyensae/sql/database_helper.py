"""
@file
@brief Contains functions to import a text file into a database (SQLite).
"""

import os
from .database_main import Database


def import_flatfile_into_database(
        filedb,
        filetext,
        table=None,
        header=True,
        columns=None,
        engine='SQLite',
        host='localhost',
        add_key=None,
        encoding="utf-8",
        fLOG=print):
    """

    Function which imports a file into a database.
    It the table exists, it removes it first. There is no addition.

    @param  filedb      something.db3
    @param  filetext    something.txt or .tsv
    @param  table       table name (in the database), if None, the database name will be the filename without extension
    @param  columns     if header is False, this must be specified. It should be a list of column names.
    @param  header      boolean (does it have a header or not)
    @param  engine      engine to use when using a SQL server (SQLite or ODBCMSSQL)
    @param  host        host (server)
    @param  fLOG        logging function (will display information through the command line)
    @param  add_key     name of a key to add (or None if nothing to add)
    @param  encoding    encoding

    @example(Import a flat file into a SQLite database)
    @code
    from pyensae import import_flatfile_into_database
    dbf = "database.db3"
    file = "textfile.txt"
    import_flatfile_into_database(dbf, file)
    @endcode

    On Windows, `SQLiteSpy <http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index>`_ is a free tool
    very useful to run SQL queries against a sqlite3 database.
    @endexample
    """
    # connection
    db = Database(filedb, engine=engine, host=host, LOG=fLOG)
    db.connect()

    if table is None:
        table = os.path.splitext(
            os.path.split(filetext)[-1])[0].replace(".", "").replace(",", "")

    if db.has_table(table):
        fLOG("remove ", table)
        db.remove_table(table)

    if header:
        columns = None

    db.import_table_from_flat_file(filetext, table, columns=columns,
                                   header=header, add_key=add_key,
                                   encoding=encoding)

    db.close()
