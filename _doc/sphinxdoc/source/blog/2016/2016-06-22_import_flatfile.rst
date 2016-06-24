

.. blogpost::
    :title: Import many flat files into Sqlite3 database
    :keywords: SQL, flat file, import, dataframe
    :date: 2016-06-22
    :categories: SQL
    
    This is a simple script to import big files into a sqlite3 database,
    too big to fit in memory. It relies on
    function :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`.

    ::
    
        # path to your data
        datapath = "<somewhere>"
        
        from pyensae.sql import import_flatfile_into_database, Database
        import os

        # get the list of files
        csv = [_ for _ in os.listdir(datapath) if ".csv" in _]
        
        # name of the database
        file_db = os.path.join(datapath, "datanase.db3")

        # retrieve the list of tables in the database
        db = Database(file_db)
        db.connect()
        tables = db.get_table_list()
        db.close()

        # correct table name
        def table_name(s):
            return os.path.split(s)[-1].split(".")[0].replace("-", "_")
            
        # loop on csv files and import each of them if the 
        # corresponding table is not already here
        # current speed: around 15min/Gb
        for f in csv:
            print("import", f)
            name = table_name(f)
            if name not in tables:
                import_flatfile_into_database(file_db, os.path.join(datapath, f),table_name(f))

    The other option is to use `pandas.to_sql <http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.to_sql.html>`_.
    It is implemented in function
    :func:`import_flatfile_into_database_pandas <pyensae.sql.pandas_sql_helper.import_flatfile_into_database_pandas>`.
    It would look like this:
    
    ::
    
        import os
        import sqlite3
        import pandas
        from pyensae.sql import Database

        datapath = "<somepath>"
        csv = [_ for _ in os.listdir(datapath) if ".csv" in _]
        
        file_db = os.path.join(datapath, "database.db3")

        db = Database(file_db)
        db.connect()
        tables = db.get_table_list()
        db.close()

        def table_name(s):
            return os.path.split(s)[-1].split(".")[0].replace("-", "_")

        with sqlite3.connect(file_db) as con:

            for f in csv:
                print("import", f)
                name = table_name(f)
                if name not in tables:
                    
                    params = {'filepath_or_buffer': os.path.join(datapath, f), 
                              'encoding': "utf-8", 'sep':"," , 
                              'iterator': True, 'chunksize':1000000}
                    nb = 0
                    for part in pandas.read_csv(**params):
                        nb += part.shape[0]
                        print("number of added lines", nb)
                        part.to_sql(con=con, name=name, if_exists="append", index=False)
                                    
                    con.commit()    
