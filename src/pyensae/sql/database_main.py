"""
@file
@brief      generic class to access a SQL database
"""
from pyquickhelper.loghelper import fLOG
from .database_core import DatabaseCore
from .database_import_export import DatabaseImportExport
from .database_object import DatabaseObject
from .database_join_group import DatabaseJoinGroup


class Database(DatabaseCore, DatabaseImportExport, DatabaseObject, DatabaseJoinGroup):
    """
    This class allows the user to load table from text files and store them into a
    SQL file which can be empty or not,
    it is using :epkg:`SQLite3` module.
    Under Windows, you can use
    `SQLiteSpy <http://www.yunqa.de/delphi/doku.php/products/sqlitespy/index>`_
    to have a graphical overview of the database.
    Parameter *dbfile* can be of type
    `sqlite3.Connection <https://docs.python.org/3/library/sqlite3.html#sqlite3.Connection>`_.
    """

    def __init__(self, dbfile, engine="SQLite", user=None, password=None,
                 host="localhost", LOG=fLOG, attach=None):
        """

        @param      dbfile          database file (use ``:memory:`` to avoid creating a file and using only memory)
                                    it can also contain several files separated by ;
                                    ``name_file ; nickname,second_file ; ...``
        @param      engine          SQLite or MySQL (if it is installed)
        @param      user            user if needed
        @param      password        password if needed
        @param      host            to connect to a MSSQL database
        @param      LOG             LOG function
        @param      attach          dictionary: { nickname: filename }, list of database to attach

        @warning If the folder does not exist, it will be created
        """
        DatabaseJoinGroup.__init__(self)
        DatabaseCore.__init__(self, sql_file=dbfile, engine=engine, user=user, password=password,
                              host=host, LOG=LOG, attach=attach)

    @staticmethod
    def schema_database(df, add_id=True):
        """
        Returns the schema for a database which would contains this database.

        @param      df          pandas DataFrame
        @param      add_id      if True, adds an index "PRIMARYKEY"
        @return                 dictionary { index_column: (name, type) }
        """
        schema = {i: (l, str) for i, l in enumerate(df.columns)}
        if add_id is not None:
            if isinstance(add_id, bool):
                if add_id:
                    add_id = "PRIMARYKEY"
                    schema[-1] = (add_id, int, "PRIMARYKEY", "AUTOINCREMENT")
            else:
                schema[-1] = (add_id, int, "PRIMARYKEY", "AUTOINCREMENT")

        if len(df) > 0:
            # we use the first row to determine type
            for i, v in enumerate(df.values[0]):
                if not isinstance(v, str):
                    schema[i] = (schema[i][0], type(v))
        return schema

    @staticmethod
    def fill_sql_table(df, filename_or_database, tablename, add_id="idr", **kwargs):
        """
        Returns a Database object, creates the database if it does not exists,
        same for the table.

        @param      df                      pandas DataFrame
        @param      filename_or_database    filename or Database object,
                                                in that second case, we assume method connect was called before
        @param      tablename               table name
        @param      add_id                  if != None then the function adds an id, it first takes the
                                            ``max(id)`` and goes on incrementing it
        @param      kwargs                  sent to @see cl Database
        @return                             ``Database`` object (new or the one from the parameters),
                                            in both case, the database is not disconnected

        .. exref::
            :title: import a DataFrame into a SQL table
            :tag: SQL

            ::

                values = [  {"name":"A", "age":10, "score":34.5 },
                            {"name":"B", "age":20, "score":-34.5 }, ]
                df  = pandas.DataFrame(values)
                dbf = "something.db3"
                db  = Database.fill_sql_table(df, dbf, "mytable")

            This example could be replaced by:

            ::

                values = [  {"name":"A", "age":10, "score":34.5 },
                            {"name":"B", "age":20, "score":-34.5 }, ]
                df  = pandas.DataFrame(values)
                dbf = "something.db3"
                db  = Database(dbf)
                db.connect()
                db.import_dataframe(df, "mytable)
                db.close()
        """

        schema = Database.schema_database(df, add_id)

        if isinstance(filename_or_database, str):
            db = Database(filename_or_database, **kwargs)
            db.connect()

            if tablename not in db.get_table_list():
                cursor = db.create_table(tablename, schema)
                db.append_values(df.values, tablename, schema, cursor=cursor)
            else:
                db.append_values(df.values, tablename, schema)
        else:
            db = filename_or_database
            if tablename not in db.get_table_list():
                cursor = db.create_table(tablename, schema)
                db.append_values(df.values, tablename, schema, cursor=cursor)
            else:
                db.append_values(df.values, tablename, schema)

        return db

    def import_dataframe(self, df, tablename, add_id="idr"):
        """
        Imports a DataFrame into a table.

        @param      df              pandas DataFrame
        @param      tablename       table name
        @param      add_id          an index, maybe to be added
        @return                     self
        """
        return Database.fill_sql_table(df, self, tablename, add_id)

    def to_df(self, request):
        """
        Converts a SQL request into a :epkg:`pandas:Dataframe`.

        @param      request     SQL request
        @return                 DataFrame
        """
        import pandas  # pylint: disable=C0415
        cols = self.get_sql_columns(request)
        iter = self.execute_view(request, nolog=True)
        return pandas.DataFrame(iter, columns=cols)

    def copy_to(self, db, subset=None):
        """
        Copies all tables into db, we assume both database are not connected.

        @param      db      another database (possibly empty)
        @param      subset  list of tables to copy or None for all
        """
        self.connect()
        db.connect()
        for tbl in self.get_table_list():
            if subset is None or tbl in subset:
                self.LOG("copy_to: create table " + tbl)
                sch = self.get_table_columns_list(tbl, True)
                curins = db.create_table(tbl, sch)
                cursor = self.execute("SELECT * FROM %s" % tbl)
                buffer = []
                for row in cursor:
                    buffer.append(row)
                    if len(buffer) >= 1000:
                        db.insert(tbl, buffer, cursor=curins)
                        buffer = []
                if len(buffer) > 0:
                    db.insert(tbl, buffer)
                db.commit()
                cursor.close()
        self.close()
        db.close()
