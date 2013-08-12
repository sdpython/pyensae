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
    download_data('SQLiteSpy.zip', website = 'xd')
    



SQLite
------

Import a flat file into a SQLite database
+++++++++++++++++++++++++++++++++++++++++

::

    from pyensae import import_flatfile_into_database
    dbf = "database.db3"
    file = "textfile.txt"
    import_flatfile_into_database(dbf, file)
    
