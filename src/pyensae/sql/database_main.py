# coding: latin-1
"""
@file
@brief      generic class to access a SQL database
"""

import os, sys


from .file_text_binary          import TextFile
from .database_exception        import ExceptionSQL
from .database_core2            import DatabaseCore2
from .database_core             import DatabaseCore
from .database_import_export    import DatabaseImportExport
from .database_object           import DatabaseObject

class Database (DatabaseCore, DatabaseImportExport, DatabaseObject) :
    
    """
    This class allows the user to load table from text files and store them into a 
    SQL file which can be empty or not,
    it is using SQLite3 module.
    
    Under Windows, you can use SQLiteSpy to have a graphical overview of the database. 
    http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index    
    """
    
    def __init__ (self, dbfile, 
                        engine      = "SQLite", 
                        user        = None, 
                        password    = None, 
                        host        = "localhost",
                        LOG         = print,
                        attach      = None) :
        """
        constructor
        
        @param      dbfile          database file (use :memory:) to avoid creating a file and using only memory
                                    it can also contain several files separated by ;
                                        @code
                                        name_file ; nickname,second_file ; ...
                                        @endcode
        @param      engine          SQLite or MySQL (if it is installed)
        @param      user            user if needed
        @param      password        password if needed
        @param      host            to connect to a MSSQL database
        @param      LOG             LOG function
        @param      attach          dictionary: { nickname: filename }, list of database to attach
        @warning If the folder does not exist, it will be created
        """
        DatabaseCore.__init__ (self,    sql_file    = dbfile, 
                                        engine      = engine, 
                                        user        = user, 
                                        password    = password, 
                                        host        = host,
                                        LOG         = LOG, 
                                        attach      = attach)
        
