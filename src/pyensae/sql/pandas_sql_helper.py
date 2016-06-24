"""
@file
@brief Pandas and SQL
"""
import os
import pandas
from .database_main import Database


def import_flatfile_into_database_pandas(filedb, filetext, table=None,
                                         engine='SQLite', host='localhost', add_key=None,
                                         fLOG=print, **options):
    """
    Function which imports a file into a database using pandas.
    It the table exists, it removes it first. There is no addition.

    @param  filedb      something.db3
    @param  filetext    something.txt or .tsv
    @param  table       table name (in the database), if None, the database name will be the filename without extension
    @param  engine      engine to use when using a SQL server (SQLite or ODBCMSSQL)
    @param  host        host (server)
    @param  fLOG        logging function (will display information through the command line)
    @param  add_key     name of a key to add (or None if nothing to add)
    @param  encoding    encoding
    @param  options     options passed to `pandas.read_csv <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html>`_
    @return             table name
    """
    db = Database(filedb, engine=engine, host=host, LOG=fLOG)
    db.connect()

    if table is None:
        table = os.path.splitext(
            os.path.split(filetext)[-1])[0].replace(".", "").replace(",", "")

    if db.has_table(table):
        fLOG("remove ", table)
        db.remove_table(table)

    params = options.copy()
    params['filepath_or_buffer'] = filetext
    params['iterator'] = True
    params["chunksize"] = options.get('chunksize', 1000000)

    nb = 0
    for part in pandas.read_csv(**params):
        nb += part.shape[0]
        fLOG("number of added lines", nb)
        part.to_sql(con=db._connection, name=table,
                    if_exists="append", index=add_key)

    db.close()
    return table
