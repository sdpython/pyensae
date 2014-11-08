#-*- coding: utf-8 -*-
"""
@file
@brief Abstract class to connect to a SQL server using various way.
It will be used to implement magic functions
"""

import re

class AutoCompletionSQLObject:
    """
    a simple class which allows auto completion
    for tables, columns...
    """
    def __init__ (self, name):
        """
        creates an instance with a given name
        """
        self._true_name = name
        self._filt_name = AutoCompletionSQLObject._filter_name(name)

    @staticmethod
    def _filter_name(name):
        """
        removes unavailable characters
        """
        return name.replace(".","_").replace(" ","_")

    @property
    def _(self):
        """
        returns the true name of the object
        """
        return self._true_name

    @property
    def _f(self):
        """
        returns the filtered name
        """
        return self._filt_name

    def _add(self, name):
        """
        add a subname to the class

        @param      name        string
        @return                 an AutoCompletionSQLObject

        the filtered name (``_f``) of the new object will
        be added to ``self.__dict__``, if an object
        already exists with the same name, it will raise an exception
        """
        au = AutoCompletionSQLObject(name)
        af = au._f
        if af in self.__dict__:
            raise KeyError("the object %s was already added to %s" % (af, self._f))
        self.__dict__[af] = au
        return au


class InterfaceSQL:
    """
    Abstract class to connect to a SQL server using various way.
    It will be used to implement magic functions
    """

    @staticmethod
    def create(obj):
        """

        @param      obj     a filename, a connection string, ...

        ``obj`` can be a:
            * file -->  the class :class:`Database <pyensae.sql.database_main.Database>` will be used, we assume this file
                        is sqlite database, the file does not have to exist, in that case, it will created
        """
        if isinstance(obj, str):
            from .sql_interface_database import InterfaceSQLDatabase
            return InterfaceSQLDatabase(obj)
        else:
            raise NotImplementedError("nothing is implemented for type: %s" % str(type(obj)))

    def populate_completion(self):
        """
        the method create an object which contains a class
        the user could use to speed the typing SQL queries,
        functions in a notebook

        This object will added with the name ``CC``,
        it is returned by the function.

        @return         @see cl AutoCompletionSQLObject

        The method should called when the method @see me connect
        is called.
        """
        self.CC = AutoCompletionSQLObject("TBL")
        tbls = self.get_table_list()
        for tb in tbls:
            compl = self.CC._add(tb)
            cols = self.get_table_columns(tb)
            for k,v in cols.items():
                compl._add(v[0])
        return self.CC

    def __init__(self, obj):
        """
        initialize the object

        @param      obj         anything, see below

        ``obj`` can be a:
            * file -->  the class :class:`Database <pyensae.sql.database_main.Database>` will be used, we assume this file
                        is sqlite database, the file does not have to exist, in that case, it will created
        """
        raise NotImplementedError()

    def connect(self):
        """
        connection to the database
        """
        raise NotImplementedError()

    def close(self):
        """
        close the connection to the database
        """
        raise NotImplementedError()

    def get_table_list(self):
        """
        returns the list of tables in the database

        @return     list of strings
        """
        raise NotImplementedError()

    def get_table_columns(self, table_name):
        """
        returns the list of columns in a table

        @param      table_name      table name
        @return                     dictionary { "column": (position, type) }
        """
        raise NotImplementedError()

    def execute(self, sql_query):
        """
        execute a SQL query

        @param      sql_query       query to execute
        @return                     pandas DataFrame

        The function takes care of the unexpected syntax introduction
        by the autocompletion object: it just replaces
        ``DB.CC.<name>`` by the ``true_name``.
        """
        sql_query = self.process_query(sql_query)
        return self.execute_clean_query(sql_query)

    def execute_clean_query(self, sql_query):
        """
        The function does the same thing as @see me execute
        but it does not replace autocompletion object.
        It is this function which should be overloaded by
        classes inheriting from this one.

        @param      sql_query       query to execute
        @return                     pandas DataFrame
        """
        raise NotImplementedError()

    _exp = re.compile("(DB[.]CC[.][a-zA-Z0-9_]+([.][a-zA-Z0-9_]+)*)")

    def process_query(self, sql_query):
        """
        replaces autocompletion object by their real names

        @param      sql_query       SQL query
        @return                     clean sql_query
        """
        # i don't remember the syntax but it should be replaced using regular expression, not
        # string replace
        fi = InterfaceSQL._exp.findall(sql_query)
        if len(fi) > 0:
            only = [ _[0] for _ in fi ]
            only.sort(reverse=True)
            for o in only :
                co = "self." + o[3:]
                ev = eval(co)
                sql_query = sql_query.replace(o, ev._)
        return sql_query

    def import_flat_file(self, filename, table_name):
        """
        import a flat file as a table, we assume the columns
        separator is ``\\t`` and the file name contains a header

        @param      filename        filename
        @param      table           table name
        """
        raise NotImplementedError()