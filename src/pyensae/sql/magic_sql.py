#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to communicate with an Hadoop cluster.
"""
import os

from IPython.core.magic import magics_class, line_magic
from IPython.core.magic import line_cell_magic
from pyquickhelper.ipythonhelper import MagicCommandParser, MagicClassWithHelpers
from .sql_interface import InterfaceSQL, InterfaceSQLException


@magics_class
class MagicSQL(MagicClassWithHelpers):

    """
    Defines SQL commands to play with `sqlite3 <https://docs.python.org/3.4/library/sqlite3.html>`_
    """

    def get_connection(self, name):
        """
        returns the connection stored in the workspace

        @param      name        variable name of the database
        @return                 object
        """
        if isinstance(name, str):
            if self.shell is None:
                raise Exception("No detected workspace.")

            if name not in self.shell.user_ns:
                raise KeyError(
                    "No opened sqlite3 database called: " + str(name))

            return self.shell.user_ns[name]
        else:
            return name

    @staticmethod
    def SQL_connect_parser():
        """
        defines the way to parse the magic command ``%SQL_connect``
        """
        parser = MagicCommandParser(prog="SQL_connect",
                                    description='connect to a SQL database')
        parser.add_argument('filename', type=str,
                            help='database filename', eval_type=str)
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_connect(self, line):
        """
        define ``SQL_connect`` which connects to a SQL database,
        it stores the database object in variable DB by default
        """
        parser = self.get_parser(MagicSQL.SQL_connect_parser, "SQL_connect")
        args = self.get_args(line, parser)

        if args is not None:
            obj = InterfaceSQL.create(args.filename)
            obj.connect()
            self.shell.user_ns[args.variable] = obj
            return obj

    @staticmethod
    def SQL_close_parser():
        """
        defines the way to parse the magic command ``%SQL_close``
        """
        parser = MagicCommandParser(prog="SQL_close",
                                    description='connect to a SQL database')
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object (and to close)')
        return parser

    @line_magic
    def SQL_close(self, line=""):
        """
        define ``SQL_close`` which closes a database
        """
        parser = self.get_parser(MagicSQL.SQL_close_parser, "SQL_close")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            r = db.close()
            return r

    @staticmethod
    def SQL_tables_parser():
        """
        defines the way to parse the magic command ``%SQL_tables``
        """
        parser = MagicCommandParser(prog="SQL_tables",
                                    description='list the tables of a database')
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_tables(self, line=""):
        """
        define ``%SQL_tables`` whichs lists the tables in a database
        """
        parser = self.get_parser(MagicSQL.SQL_tables_parser, "SQL_tables")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            return db.get_table_list()

    @staticmethod
    def SQL_drop_table_parser():
        """
        defines the way to parse the magic command ``%SQL_drop_table``
        """
        parser = MagicCommandParser(prog="SQL_drop_table",
                                    description='drop a table from a database')
        parser.add_argument('table', type=str, help='table', eval_type=str)
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_drop_table(self, line):
        """
        defines ``%SQL_drop_table`` which drops a table from a database
        """
        parser = self.get_parser(
            MagicSQL.SQL_drop_table_parser, "SQL_drop_table")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            return db.drop_table(args.table)

    @staticmethod
    def SQL_refresh_completion_parser():
        """
        defines the way to parse the magic command ``%SQL_refresh_completion``
        """
        parser = MagicCommandParser(prog="SQL_refresh_completion",
                                    description='refresh completion (tables names, ...)')
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_refresh_completion(self, line=""):
        """
        defines ``%SQL_refresh_completion``
        """
        parser = self.get_parser(
            MagicSQL.SQL_refresh_completion_parser, "SQL_refresh_completion")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            db.refresh_completion()

    @staticmethod
    def SQL_schema_parser():
        """
        defines the way to parse the magic command ``%SQL_schema``
        """
        parser = MagicCommandParser(prog="SQL_schema",
                                    description='schema of a table')
        parser.add_argument('table', type=str, help='table', eval_type=str)
        parser.add_argument(
            '--as_list', help='as a dictionary (False) or as a list (True)', action="store_true")
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_schema(self, line=""):
        """
        define ``SQL_schema``
        """
        parser = self.get_parser(MagicSQL.SQL_schema_parser, "SQL_schema")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            return db.get_table_columns(args.table, as_dict=not args.as_list)

    @staticmethod
    def SQL_import_tsv_parser():
        """
        defines the way to parse the magic command ``%SQL_import_tsv``
        """
        parser = MagicCommandParser(prog="SQL_import_tsv",
                                    description='import a tsv file into the database')
        parser.add_argument('filename', type=str,
                            help='tsv file name', eval_type=str)
        parser.add_argument('-t', '--table', type=str,
                            help='table name', default="-", eval_type=str)
        parser.add_argument(
            '--verbose', help='print progress', action="store_true")
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_import_tsv(self, line):
        """
        defines ``%SQL_import_tsv`` whichs import a TSV file into a database
        """
        parser = self.get_parser(
            MagicSQL.SQL_import_tsv_parser, "SQL_import_tsv")
        args = self.get_args(line, parser)

        if args is not None:
            if not os.path.exists(args.filename):
                raise FileNotFoundError(args.filename)
            db = self.get_connection(args.variable)
            table = os.path.splitext(os.path.split(args.filename)[-1])[0] \
                if len(args.table) == 0 or args.table == "-" else args.table
            return db.import_flat_file(args.filename, table)

    @staticmethod
    def SQL_add_function_parser():
        """
        defines the way to parse the magic command ``%SQL_add_function``
        """
        parser = MagicCommandParser(prog="SQL_add_function",
                                    description='add a custom function to the database')
        parser.add_argument('funct', type=str, help='function name')
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_add_function(self, line):
        """
        defines ``%SQL_add_function`` which adds a function to the database
        """
        parser = self.get_parser(
            MagicSQL.SQL_add_function_parser, "SQL_add_function")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)
            if isinstance(args.funct, str):
                if self.shell is not None:
                    if args.funct not in self.shell.user_ns:
                        raise KeyError(
                            "unable to find function %s in your workspace" %
                            args.funct)
                    fu = self.shell.user_ns[args.funct]
                else:
                    raise Exception("unable to find IPython workspace")
            else:
                fu = args.funct
            return db.add_function(fu)

    @staticmethod
    def SQL_import_df_parser():
        """
        defines the way to parse the magic command ``%SQL_import_df``
        """
        parser = MagicCommandParser(prog="SQL_import_df",
                                    description='import a dataframe into the database')
        parser.add_argument('df', type=str, help='dataframe', no_eval=True)
        parser.add_argument('-t', '--table', type=str,
                            help='table name', default="-", eval_type=str)
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_magic
    def SQL_import_df(self, line):
        """
        defines ``%SQL_import_df`` which imports a dataframe into a database
        """
        parser = self.get_parser(
            MagicSQL.SQL_import_df_parser, "SQL_import_df")
        args = self.get_args(line, parser)

        if args is not None:
            db = self.get_connection(args.variable)

            df = args.df
            if self.shell is not None:
                if df not in self.shell.user_ns:
                    raise KeyError(
                        "unable to find dataframe %s in your workspace" %
                        df)
                odf = self.shell.user_ns[df]
            else:
                raise Exception("unable to find IPython workspace")

            table = df if len(
                args.table) == 0 or args.table == "-" else args.table
            return db.import_dataframe(table, odf)

    @staticmethod
    def SQL_parser():
        """
        defines the way to parse the magic command ``%%SQL``
        """
        parser = MagicCommandParser(prog="SQL",
                                    description='query the database')
        parser.add_argument(
            '--df', type=str, help='output dataframe', default="temp_view", no_eval=True)
        parser.add_argument('-n', '--n', type=int,
                            help='number of first lines to display', default=10, eval_type=int)
        parser.add_argument('-q', '--query', type=str,
                            help='when used in a single line (no cell), query is the SQL query, the command returns the full dataframe', default="", eval_type=str)
        parser.add_argument(
            '-v',
            '--variable',
            default="DB",
            help='variable name used to store the database object')
        return parser

    @line_cell_magic
    def SQL(self, line, cell=None):
        """
        defines command ``%%SQL``
        """
        parser = self.get_parser(MagicSQL.SQL_parser, "SQL")
        args = self.get_args(line, parser)

        if args is not None:
            full = False
            db = self.get_connection(args.variable)

            if cell is None or len(cell) == 0:
                cell = args.query
                if cell is None or len(cell) == 0:
                    raise ValueError("no SQL query is defined")
                else:
                    query = cell
                    full = True
            else:
                query = cell

            query = query.strip()
            if len(query) > 0 and query[0] == '"' and query[-1] == '"':
                query = query[1:-1]

            db = self.get_connection(args.variable)
            try:
                df = db.execute(query)
                ok = True
            except InterfaceSQLException as e:
                print(str(e))
                ok = False

            if ok:
                self.shell.user_ns[args.df] = df
                if full:
                    return df
                else:
                    return df.head(n=args.n)


def register_sql_magics(ip=None):
    """
    register magics function, can be called from a notebook

    @param      ip      from ``get_ipython()``
    """
    if ip is None:
        from IPython import get_ipython
        ip = get_ipython()
    ip.register_magics(MagicSQL)
