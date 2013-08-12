# coding: latin-1
"""
@file

@brief defines logged exceptions for SQL requests
"""

import sys, os, sqlite3 as SQLite


class ExceptionSQL (Exception) :
    """
    exception related to SQL instructions and only them
    """
    def __init__ (self, description, ex, sql, log = True) :
        """constructor
        @param      description     message
        @param      ex              sqlite exception
        @param      sql             SQL instruction
        @param      log             log the exception
        """
        HalException.__init__ (self, description, log = False)
        self.ex  = ex
        self.sql = sql
        if log :
            self._log ()
        
    def __str__ (self) :
        mes  = HalException.__str__ (self)
        mes += "\n" + str (self.ex)
        mes += "\n" + "\n".join ( repr (self.sql).split ("\\n") )
        if len (mes) > 10000 :
            mes = mes [10000:] + "\n..."
        return mes
