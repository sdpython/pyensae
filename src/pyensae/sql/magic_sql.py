#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to communicate with an Hadoop cluster.
"""
import sys, os, pandas

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML

from .sql_interface import InterfaceSQL, InterfaceSQLException

@magics_class
class MagicSQL(Magics):
    """
    Defines SQL commands to play with `sqlite3 <https://docs.python.org/3.4/library/sqlite3.html>`_
    """

    def get_connection(self):
        """
        returns the connection stored in the workspace
        """
        if self.shell is None:
            raise Exception("No detected workspace.")

        if "DB" not in self.shell.user_ns:
            raise KeyError("No opened sqlite3 database.")

        return self.shell.user_ns["DB"]

    @line_magic
    def SQL_connect(self, line):
        """
        define ``SQL_connect``
        """
        filename = line.strip()
        if len(filename) == 0:
            print("Usage:")
            print("  %SQL_connect <filename>")
        else:
            obj = InterfaceSQL.create(filename)
            obj.connect()
            self.shell.user_ns["DB"] = obj
            return obj

    @line_magic
    def SQL_close(self, line):
        """
        define ``SQL_close``
        """
        db = self.get_connection()
        db.close()
        del self.shell.user_ns["DB"]

    @line_magic
    def SQL_tables(self, line):
        """
        define ``%SQL_tables``
        """
        db = self.get_connection()
        return db.get_table_list()
        
    @line_magic
    def SQL_drop_table(self,line):
        """
        define ``%SQL_drop_table``
        """
        line = line.strip()
        if len(line) == 0 :
            print("Usage:")
            print("    SQL_drop_table <table_name>")
        else:
            db = self.get_connection()
            db.drop_table(line)
            
    @line_magic
    def SQL_refresh_completion(self):
        """
        define SQL_refresh_completion
        """
        db = self.get_connection()
        db.refresh_completion()

    @line_magic
    def SQL_schema(self, line):
        """
        define ``SQL_schema``
        """
        if len(line) == 0:
            print("Usage:")
            print("  %SQL_schema <table_name>")
        else:
            db = self.get_connection()
            return db.get_table_columns(line)

    @line_cell_magic
    def SQL(self, line, cell = None):
        """
        defines command ``%%SQL``
        """
        def usage():
            print("Usage:")
            print("  %SQL <SQL query or a string containing the query>")
            print("or")
            print("  %%SQL  <variable dataframe>")
            print("  <query>")

        cont = True
        addv = None
        if cell is None:
            if len(line) == 0:
                usage()
                cont = False
            else:
                query = line.strip()

                if self.shell is not None and query in self.shell.user_ns:
                    query = self.shell.user_ns[query]

        elif len(cell) == 0 :
            usage()
            cont = False
        else:
            query = cell
            addv = line.strip()
            if len(addv) == 0 : addv = None

        if cont:
            db = self.get_connection()
            try:
                df = db.execute(query)
                ok = True
            except InterfaceSQLException as e :
                print (str(e))
                ok = False

            if ok:
                if addv is not None and self.shell is not None:
                    self.shell.user_ns[addv] = df
                    return df.shape
                else:
                    return df
            
    @line_magic
    def SQL_import_tsv(self,line):
        """
        define ``%SQL_import_tsv``
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   SQL_import_tsv tablename filename")
        else:
            if not os.path.exists(spl[1]):
                raise FileNotFoundError(spl[1])
            db = self.get_connection()
            db.import_flat_file(spl[1], spl[0])
        
    @line_magic
    def SQL_add_function(self, line):
        """
        define ``%SQL_add_function``
        """
        line.strip()
        if len(line)==0:
            print("Usage:")
            print("   SQL_add_function function_name")
        else:
            if self.shell is not None:
                if line not in self.shell.user_ns:
                    raise KeyError("unable to find function %s in your workspace" % line)
                fu = self.shell.user_ns[line]
            else:
                raise Exception("unable to find IPython workspace")
            db = self.get_connection()
            db.add_function(fu)

    @line_magic
    def SQL_import_df(self, line):
        """
        define ``%SQL_import_dataframe``
        """
        spl = line.strip().split()
        if len(spl) != 2 :
            print("Usage:")
            print("   SQL_import_df tablename dataframe")
        else:
            db = self.get_connection()
            
            df = spl[1]
            if self.shell is not None:
                if df not in self.shell.user_ns:
                    raise KeyError("unable to find dataframe %s in your workspace" % df)
                odf = self.shell.user_ns[df]
            else:
                raise Exception("unable to find IPython workspace")
            
            db.import_dataframe(spl[0], odf)
        

def register_sql_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicSQL)
    