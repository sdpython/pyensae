

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
        from pyquickhelper.loghelper import fLOG
        import os
        fLOG(OutputPrint=True)

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
                import_flatfile_into_database(file_db, os.path.join(datapath, f),table_name(f), fLOG=fLOG)
