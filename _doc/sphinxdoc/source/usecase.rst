.. _l-usecase:

Use case
========

.. contents::
   :depth: 3
    
    
    
Resources for teachings
-----------------------

Download data for a practical lesson
++++++++++++++++++++++++++++++++++++

::

    from pyensae import download_data
    download_data('voeux.zip', website = 'xd')
    



SQLite
------

Import a flat file into a SQLite database
+++++++++++++++++++++++++++++++++++++++++

::

    from pyensae import import_flatfile_into_database
    dbf = "database.db3"
    file = "textfile.txt"
    import_flatfile_into_database(dbf, file)
    

Export the results of a SQL query into a flat file
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    from pyensae.sql.database_main import Database
    dbfile = "filename.db3"
    filetxt = "fileview.txt"
    sql = "..."
    db = Database(dbfile)
    db.connect()
    db.export_view_into_flat_file (sql, fileview, header = True)
    db.close()
    
