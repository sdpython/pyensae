"""
@file

@brief @see cl Database
"""
import os
import sys
import math
import re
import time
import decimal
import sqlite3 as SQLite
import datetime
import numpy
from .database_exception import ExceptionSQL, DBException
from .database_core2 import DatabaseCore2

module_odbc = None


class DatabaseCore (DatabaseCore2):

    """
    core methods, @see cl Database
    """

    """
    @var    _engine     engine type (SQLite is the only available)
    @var    _sql_file   database file, if it does not exist, it will be created.
    """

    _sql_keywords = ["order", "by", "select", "from", "group", "where", "as", "like", "upper", "collapse", "join", "union",
                     "inner", "default", "id", "double", "text", "varchar", "float", "long", "Decimal"]

    _SQL_conversion_types = {"": float,
                             "TEXT": str,
                             "text": str,
                             "INTEGER": int,
                             "FLOAT": float,
                             "REAL": float,
                             "float": float,
                             "numeric": float,
                             "LONG": int,
                             "int": int,
                             "varchar": str,
                             "VARCHAR": str,
                             "Decimal": decimal.Decimal,
                             "DATETIME": datetime.datetime,
                             "smallint": int,
                             "bigint": float, }

    _engines = ["SQLite", "MySQL", "ODBCMSSQL"]
    _field_option = ["PRIMARYKEY", "AUTOINCREMENT", "AUTOFILL"]

    def __init__(self, sql_file,
                 engine="SQLite",
                 user=None,
                 password=None,
                 host="localhost",
                 LOG=None,
                 attach=None):
        """constructor
        @param      sql_file        database file database file (use ``:memory:`` to avoid creating a file and using only memory)
                                    it can also contain several files separated by ;
                                        @code
                                        name_file ; nickname,second_file ; ...
                                        @endcode
        @param      engine          SQLite or MySQL (if it is installed), ODBCMSSQL
        @param      user            user if needed
        @param      host            to connect to a MSSQL database
        @param      password        password if needed
        @param      LOG             LOG function, if None, choose ``print``
        @param      attach          dictionary ``{ nickname: filename }``, list of database to attach
        @warning If the folder does not exist, it will be created
        """

        # attach cases
        if attach is None:
            attach = {}
        else:
            attach = attach.copy()

        if isinstance(sql_file, str):

            for e in DatabaseCore._engines:
                if sql_file.startswith(e + ":::"):
                    engine = e
                    sql_file = sql_file[len(e) + 3:]
                    if "###" in sql_file:
                        host, sql_file = sql_file.split("###")
                    break

            if ";" in sql_file:
                li = [s.strip() for s in sql_file.split(";")]
                sql_file = li[0]
                rest = li[1:]
                for s in rest:
                    ok = s.split(",")
                    if len(ok) != 2:
                        raise DBException("unable to find an alias in %s" % s)
                    nick = ok[0].strip()
                    file = ",".join(ok[1:])
                    attach[nick] = file.strip()
            elif sql_file.startswith(":"):
                if sql_file != ":memory:":
                    raise FileNotFoundError(
                        "unable to interpret file: " +
                        sql_file)

        # some initialization
        self._password = password
        self._user = user
        self._host = host

        # the rest
        if LOG is None:
            def blind(*l, **p):
                pass
            LOG = blind
        self.LOG = LOG

        if isinstance(LOG, dict):
            raise TypeError("fLOG should be a function, not a dictionary")
        if isinstance(self.LOG, dict):
            raise TypeError("LOG should be a function, not a dictionary")

        if engine == "SQLite":
            self._sql_file = sql_file
            self._engine = engine

        elif engine == "ODBCMSSQL":
            raise DBException("unable to connect to a SQL server")

        else:
            raise DBException(
                "unfounded engine %s in %s" %
                (engine, ", ".join(
                    DatabaseCore._engines)))

        # write a file able to build a database summary
        if not self.isMemory():
            folder = os.path.split(sql_file)[0]
            if len(folder) > 0 and not os.path.exists(folder):
                os.makedirs(folder)
            summary = os.path.join(folder, "temp_quick_look_up.py")
            if not os.path.exists(summary):
                #cwd = os.path.join (os.path.abspath (os.path.split (__file__) [0]), "..", "..")
                #fi  = os.path.split (sql_file) [1]

                if "SCRIPT_LOOKUP" in DatabaseCore.__dict__:
                    script = DatabaseCore.SCRIPT_LOOKUP
                    lines = script.split("\n")
                    lines = [l if "__CWD__ =" not in l else
                             l.replace(
                                 "(__file__)",
                                 "(r'%s')" %
                                 os.path.realpath(__file__))
                             for l in lines]
                    script = "\n".join(lines)
                    script = script.replace(
                        "python quick_look_up.py",
                        "%s quick_look_up.py" %
                        sys.executable)
                    self.LOG("creating script ", summary)
                    try:
                        f = open(summary, "w")
                        f.write(script)
                        f.close()
                    except IOError:
                        self.LOG("unable to write ", summary)
                        pass

        self._attach = attach
        self._buffer_insert = []
        self._buffer_insert_s = 0

        if self.isMemory():
            self._connection = SQLite.connect(self._sql_file)

    def isMSSQL(self):
        """says if the syntax is MS SQL Server
        """
        if self._engine == "ODBCMSSQL":
            return True
        return False

    def isMemory(self):
        """
        tells if the Database takes place in memory (``:memory:``)
        """
        return self._sql_file == ":memory:"

    ##########################################################################
    # connection
    ##########################################################################

    def SetBufferInsert(self, n):
        """
        This function offers the possibility to postpone the insertion,
        they will be processed all at the time during when method commit is called.
        @param      n           number of insertion to postpone
        """
        self._buffer_insert_s = n

    def is_connected(self):
        """says if the database is connected
        @return         "_connection" in self.__dict__
        """
        return "_connection" in self.__dict__

    @staticmethod
    def regex_match(exp, st):
        return 0 if re.compile(exp).search(st) is None else 1

    @staticmethod
    def idaytodate(dayint, year, month, day):
        try:
            d = datetime.datetime(year, month, day)
            day = datetime.datetime(year, month, day + 1) - d
            cur = d + day * dayint
            return str(cur).split()[0]
        except Exception as e:
            return str(e)

    @staticmethod
    def isectoday(sec):
        if sec < 0:
            return "negative time"
        elif sec >= 86400:
            return "out of day"
        else:
            s = int(sec)
            h = s / 3600
            m = (s % 3600) / 60
            s %= 60
            return "%02d:%02d:%02d" % (h, m, s)

    @staticmethod
    def itimestamp(t, year, month, day):
        d = DatabaseCore.idaytodate(int(t / 86400), year, month, day)
        s = DatabaseCore.isectoday(int(t - 86400. * int(t / 86400)))
        return d + " " + s

    @staticmethod
    def string_to_date(s):
        d = int(s[:2])
        m = int(s[3:5])
        y = int(s[6:])
        return datetime.datetime(y, m, d)

    @staticmethod
    def _special_function_init_():
        _list_special_function = [
            ("log", math.log, 1, "log(s) --> float", "log"),
            ("exp", math.exp, 1, "exp(s) --> float", "exp"),
            ("len", len, 1, "len(s) --> int", "string length"),
            ("lower",
             lambda s:s.lower(),
             1,
             "lower(s) --> string",
             "lower case"),
            ("upper",
             lambda s:s.upper(),
             1,
             "upper(s) --> string",
             "upper case"),
            ("isubstring", lambda sub, s: 1 if sub in s else 0,
             2, "isubstring(sub,str) --> {0,1}", "return 1 if str includes sub, 0 otherwise"),
            ("match", DatabaseCore.regex_match,
             2, "match(regex,str) --> {0,1}", "return 1 if str matches the regular expression exp, 0 otherwise"),
            ("idaytodate", DatabaseCore.idaytodate,
             4, "idaytodate (day, 1970, 1, 1) --> str", "date if day is the number of days since 01/01/1970"),
            ("itimestamp", DatabaseCore.itimestamp,
             4, "itimestamp (t, 1970, 1, 1) --> str", "date,time if t is the number of seconds since 01/01/1970"),
            ("isectoday", DatabaseCore.isectoday,
             1, "isectoday (isec) --> str", "time if isec is the number of seconds since midnight"),
        ]
        return _list_special_function

    def connect(self, odbc_string=None):
        """open a connection to the database
        @param      odbc_string     use a different odbc string
        """
        if self.isMemory():
            if "_connection" not in self.__dict__:
                raise DBException(
                    "It is a database in memory, the database should already be connected.")
        else:
            if "_connection" in self.__dict__:
                raise Exception("a previous connection was not closed")

            if self._engine == "SQLite":
                self._connection = SQLite.connect(self._sql_file)
            # elif self._engine == "MySQL" :  self._connection =
            # MySQLdb.connect (self._host, self._user, self._password,
            # self._sql_file)
            elif self._engine == "ODBCMSSQL":

                if odbc_string is None:
                    temp = ["DRIVER={SQL Server Native Client 10.0}",  # {SQL Server}",
                            "SERVER=%s" % self._host,
                            "DATABASE=%s" % self._sql_file,
                            "Trusted_Connection=yes",
                            "MARS_Connection=yes",
                            #"MultipleActiveResultSets=True",
                            #"Integrated Security=SSPI",
                            ]
                    #temp = ["DSN=%s" % self._sql_file ]
                    if self._user is not None:
                        temp.append("UID=%s" % self._user)
                    if self._password is not None:
                        temp.append("PASSWORD=%s" % self._password)
                    st = ";".join(temp)
                    self.LOG("connection string ", st)
                    self._connection = module_odbc.connect(st)
                else:
                    st = odbc_string
                    self.LOG("connection string ", st)
                    self._connection = module_odbc.connect(st)

            else:
                raise DBException(
                    "This engine does not exists (%s)" %
                    self._engine)

            for func in DatabaseCore._special_function_init_():
                self.add_function(func[0], func[2], func[1])

            for k, v in self._attach.items():
                self.attach_database(v, k)

    def close(self):
        """close the database
        """
        if self.isMemory():
            # we should not close, otherwise, we lose the data
            pass
        else:
            self._check_connection()
            self._connection.close()
            del self._connection

    def commit(self):
        """call this function after any insert request
        """
        self._check_connection()

        for s in self._buffer_insert:
            self._connection.execute(s)
        del self._buffer_insert[:]

        self._connection.commit()

    ##########################################################################
    # access part
    ##########################################################################

    def get_file(self, attached_db=False):
        """
        @param      attached_db     if True, add the list of attached databases
        @return                     the database file
        """
        if attached_db:
            files = [self._sql_file]
            att = self.get_attached_database_list(True)
            for alias, file in att:
                files.append("%s,%s" % (alias, file))
            temp = ";".join(files)
            if self._engine != "SQLite":
                if self._host is None:
                    temp = "%s:::%s" % (self._engine, temp)
                else:
                    temp = "%s:::%s###%s" % (self._engine, self._host, temp)
            return temp
        else:
            return self._sql_file

    def has_table(self, table):
        """say if the table belongs to the database
        @param      table       table name
        @return                 boolean
        """
        return table in self.get_table_list("." in table)

    def has_index(self, index):
        """say if the index belongs to the database
        @param      index       index name
        @return                 boolean"""
        return index in [s[0] for s in self.get_index_list()]

    def get_index_on_table(self, table, full=False):
        """
        return the list of indexes on a specific table
        @param      table       table
        @param      full        if True returns all fields, otherwise, returns only the index names
        @return                 list of the index on this table
        """
        indexes = self.get_index_list()
        if full:
            return [l for l in indexes if l[1] == table]
        else:
            return [l[0] for l in indexes if l[1] == table]

    def get_column_type(self, table, column):
        """return the column type of a table
        @param      table       table name
        @param      column      column name
        @return                 type (python class)
        """
        self._check_connection()
        cols = self.get_table_columns_list(table)
        for c in cols:
            if c[0] == column:
                return c[1]
        raise DBException(
            "column %s were not found in table %s" %
            (column, table))

    def get_index_list(self, attached="main"):
        """return the list of indexes
        @param        attached      if main, returns the index for the main database, otherwise, for an attached database
        @return                     list of tuple (index_name, table, sql_request, fields)
        """
        self._check_connection()
        if attached == "main":
            request = """   SELECT name,tbl_name,sql
                            FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) AS temptbl
                            WHERE type='index' ORDER BY name;"""
        else:
            request = """   SELECT name,tbl_name,sql
                            FROM (SELECT * FROM %s.sqlite_master) AS temptbl
                            WHERE type='index' ORDER BY name;""" % attached
        select = self._connection.execute(request)

        exp = re.compile("[(]([a-zA-Z0-9_,]+)[)]")
        res = []
        for a, b, c in select:
            fi = exp.findall(c)
            if len(fi) != 1:
                raise DBException("unable to extract index fields from %s" % c)
            fi = tuple([s.strip() for s in fi[0].split(",")])
            res.append((a, b, c, fi))
        select.close()
        #self.LOG ("number of indices ", len (res))
        select = res

        res = []
        if attached == "main":
            res = select
        else:
            for el in select:
                res.append((el[0], attached + "." + el[1], el[2], el[3]))
        #self.LOG ("number of indices ", len (res))

        if attached == "main":
            attach = self.get_attached_database_list()
            for a in attach:
                if a == "main" or a == "temp":
                    continue
                r = self.get_index_list(a)
                res.extend(r)

        return res

    def get_attached_database_list(self, file=False):
        """return all the attached database (avoid the temporary ones and the main one)
        @param      file        ask for file also
        @return                 a list of tuple (alias, file)
        """
        if self.isMSSQL():
            return []
        else:
            cur = self._connection.cursor()
            cur.execute("PRAGMA database_list;")
            res = cur.fetchall()
            cur.close()
            res = [r for r in res if r[1] != "temp" and r[1] != "main"]
            if file:
                return [(r[1], r[2]) for r in res]
            else:
                return [r[1] for r in res]

    def get_table_list(self, add_attached=False):
        """
        return the list of table

        @param      add_attached        if True, add the list of tables included in the attached databases
        @return                         the table list
        """
        self._check_connection()
        if self.isMSSQL():
            request = """   SELECT TABLE_NAME FROM (
                                SELECT TABLE_NAME, OBJECTPROPERTY(object_id(TABLE_NAME), N'IsUserTable') AS type
                                FROM INFORMATION_SCHEMA.TABLES) AS temp_tbl
                            WHERE type = 1 ORDER BY TABLE_NAME"""
        else:
            request = """   SELECT name
                            FROM (SELECT * FROM sqlite_master UNION ALL SELECT * FROM sqlite_temp_master) AS temptbl
                            WHERE type in('table','temp') AND name != 'sqlite_sequence' ORDER BY name;"""

        select = self._connection.execute(request)
        res = []
        for el in select:
            res.append(el[0])

        if add_attached:
            att = self.get_attached_database_list()
            for at in att:
                if at == "temp":
                    continue
                sql = "SELECT name FROM %s.sqlite_master" % at
                vie = self._connection.execute(sql)
                vie = ["%s.%s" % (at, v[0]) for v in vie]
                res.extend(vie)
        return res

    def get_table_columns(self, table, dictionary=False):
        """
        @see me get_table_columns_list
        example: (dictionary == False)
        @code
        [('fid', <type 'int'>), ('fidp', <type 'int'>), ('field', <type 'str'>)]
        @endcode

        or (dictionary = True)
        @code
        {0: ('fid', <type 'int'>), 1: ('fidp', <type 'int'>), 2: ('field', <type 'str'>)}
        @endcode
        """
        return self.get_table_columns_list(table, dictionary)

    def get_table_columns_list(self, table, dictionary=False):
        """return all the columns for a table
        @param      table       table name
        @param      dictionary  returns the list as a dictionary
        @return                 a list of tuple (column name, Python type)

        example: (dictionary == False)
        @code
        [('fid', <type 'int'>), ('fidp', <type 'int'>), ('field', <type 'str'>)]
        @endcode

        or (dictionary = True)
        @code
        {0: ('fid', <type 'int'>), 1: ('fidp', <type 'int'>), 2: ('field', <type 'str'>)}
        @endcode
        """
        if "." in table:
            prefix = table.split(".")[0] + "."
            table = table.split(".")[1]
        else:
            table = table
            prefix = ""
        cur = self._connection.cursor()

        if self.isMSSQL():
            prf = "" if len(prefix) == 0 else prefix + "."
            sql = """SELECT * FROM (SELECT OBJECT_NAME(c.OBJECT_ID) TableName,c.name AS ColumnName,t.name AS TypeName
                            FROM sys.columns AS c
                            JOIN sys.types AS t ON c.user_type_id=t.user_type_id
                            ) AS ttt
                            WHERE ttt.TableName = '%s%s'""" % (prf, table)
            cur.execute(sql)
        else:
            cur.execute("PRAGMA %stable_info(%s)" % (prefix, table) + ";")

        res = cur.fetchall()
        cur.close()
        res = [(r[1], DatabaseCore._SQL_conversion_types[r[2]]) for r in res]
        if dictionary:
            dic = {}
            for i in range(0, len(res)):
                dic[i] = res[i]
            return dic
        else:
            return res

    def get_table_nb_lines(self, table):
        """return the number of lines in a table (or number of observations)
        @param      table       table name
        @return                 integer
        """
        sql = "SELECT COUNT(*) FROM " + table + ";"
        cur = self._connection.cursor()
        cur.execute(sql)
        res = cur.fetchall()
        cur.close()
        return res[0][0]

    def len(self, table):
        """
        returns the number of lines of table ``table``
        @param  table       table
        @return             int
        """
        return self.get_table_nb_lines(table)

    def get_table_nfirst_lines(self, table, n=1):
        """returns the n first lines
        @param      table       table name
        @param      n           number of asked lines
        @return                 integer
        """
        sql = "SELECT * FROM %s ;" % table
        cur = self._connection.cursor()
        cur.execute(sql)
        if n <= 1:
            res = [cur.fetchone()]
        else:
            res = []
            for line in cur:
                n -= 1
                if n <= -1:
                    break
                res.append(line)
        cur.close()
        return res

    def get_sql_columns(self, request):
        """
        return the columns name for a SQL request
        @param      request             SQL request
        @return                         list of columns name
        """
        cur = self.execute(request)
        col_name_list = [tuple[0] for tuple in cur.description]
        cur.close()
        return col_name_list

    ##########################################################################
    # execution
    ##########################################################################

    class _cross_product_iter:

        """
        iterator for CROSS
        """

        def __init__(self, db, request):
            com = re.compile("^(.*)(--.*)$")
            lines = request.split("\n")
            clean = []
            for l in lines:
                r = com.match(l)
                if r is not None:
                    l = l[:r.span(1)[1]]
                clean.append(l.strip())
            req = " ".join(clean)
            cross = re.compile(" *CROSS +([ a-zA-Z_0-9,]+?) +"
                               "PLACE +([,a-zA-Z_0-9()]+?) +"
                               "FROM +([a-zA-Z_0-9]+?)( +AS +[_a-z0-9])? +ORDER +BY "
                               "+([ a-zA-Z_0-9,]+?)( +WHERE(.*?))?( +LIMIT +([0-9]+)?)?$", re.IGNORECASE)
            db.LOG("cross product", req)
            find = cross.search(req)
            self.request = request
            self.find = find
            self.db = db

            if self.find is None:
                return

            gr = self.find.groups()
            key, value, table, count_as, order, where, _, __, limit = gr
            if limit is not None:
                limit = int(limit)
            db.LOG("parameters ", [key, value, table, order, where, limit])
            fkey = key.split(",")
            fval = value.split(",")
            if where is None:
                where = ""

            nkey = len(fkey)
            #nval = len (fval)
            sql = "SELECT %s,%s FROM %s %s ORDER BY %s" % (
                key, value, table, where, order)
            cur = self.db.execute(sql)
            data = {}
            #tot  = nkey + nval
            for sample in cur:
                key = sample[:nkey]
                val = sample[nkey:]
                if key not in data:
                    data[key] = []
                data[key].append(val)
            cur.close()

            keys = sorted(data.keys())

            if nkey == 1:
                temp = [[str(k[0]) + ';' + s for s in fval] for k in keys]
            else:
                temp = [
                    [",".join([str(_s) for _s in k]) + ';' + s for s in fval] for k in keys]
            self.description = []
            for t in temp:
                self.description.extend(t)
            self.description = [(k, None) for k in self.description]

            matrix = []
            pos = 0
            while True:
                stil = 0
                line = []
                for k in keys:
                    v = data[k]
                    if pos < len(v):
                        stil += 1
                        line.extend(list(v[pos]))
                    else:
                        line.extend([None for f in fval])
                if stil > 0:
                    matrix.append(line)
                    pos += 1
                    if limit is not None and pos >= limit:
                        break
                else:
                    break
            self.matrix = matrix
            self.pos = 0

        def is_working(self):
            return self.find is not None

        def __iter__(self):
            """
            iterator
            """
            return self

        def __next__(self):
            """
            iterator
            """
            if "matrix" not in self.__dict__:
                raise StopIteration
            if self.pos < len(self.matrix):
                n = self.pos
                self.pos += 1
                return self.matrix[n]
            else:
                raise StopIteration

        def close(self):
            pass

    def _analyse(self, request, header=False):
        """analyse the request  does it contains cross product
        @param      request     request
        @param      header      add a header in the first line
        @return                 None or an iterator

        example:
        @code
        CROSS f1,f2,f3
        PLACE a,b,c
        FROM table
        ORDER BY f8
        WHERE f9 == ' '  -- optional
        @endcode
        """
        if "CROSS" not in request.upper():
            return None
        iter = DatabaseCore._cross_product_iter(self, request)
        if not iter.is_working():
            return None
        else:
            return iter

    def execute(self, request, nolog=False):
        """open a cursor with a query and return it to the user
        @param      request         SQL request
        @param      nolog           if True, do not log anything
        @return                     cursor

        .. exref::
            :title: run a select command on a table
            :tag: SQL

            ::

                t   = Database (file)
                cur = t.execute ("SELECT * FROM table1 ;")
                for f in cur :
                    print(f)
                cur.close ()

        There is another case outside SQL syntax to build cross product. Syntax:

        ::

            CROSS f1,f2,f3
            FROM table
            PLACE a,b,c
            ORDER BY f8
            WHERE f9 == ' '  -- optional

        The request must begin by CROSS
        """
        res = self._analyse(request)
        if res is not None:
            return res
        else:
            # classic ways
            self._check_connection()
            cur = self._connection.cursor()
            dat = time.clock()
            try:
                # if 1 :
                if not nolog:
                    self.LOG("SQL ",
                             "\n".join([repr(x) for x in request.split("\n")]))
                cur.execute(request)
                dat2 = time.clock()
                if dat2 - dat > 10:
                    self.LOG("SQL end")
            except Exception as e:
                # else :
                raise ExceptionSQL(
                    "unable to execute a SQL request (1)(file %s)" %
                    self.get_file(),
                    e,
                    request) from e
            return cur

    def execute_view(self, request, add_column_name=False, nolog=False):
        """open a cursor with a query and returns the result into a list
        @param      request             SQL request
        @param      add_column_name     add the column name before the first line
        @param      nolog               if True, do not log anything
        @return                         cursor

        example
        @code
        t    = Database (file)
        view = t.execute_view ("SELECT * FROM table1 ;")
        @endcode
        """
        cur = self.execute(request, nolog=nolog)
        if add_column_name:
            col_name_list = [tuple[0] for tuple in cur.description]
            res = [col_name_list] + [x for x in cur]
        else:
            res = [x for x in cur]
        cur.close()
        if not nolog and (len(res) == 0 or len(res) > 1e4):
            self.LOG("execute_view ", len(res), "results")
        return res

    def execute_script(self, script, nolog=False):
        """open a cursor and run a script
        @param      script              SQL script
        @param      nolog               if True, do not log anything
        @return                         cursor
        """
        self._check_connection()
        if not nolog:
            self.LOG("SQL start + ",
                     "\n".join([repr(x) for x in script.split("\n")]))
        cur = self._connection.cursor()
        cur.executescript(script)
        cur.close()
        if not nolog:
            self.LOG("SQL end")

    ##########################################################################
    # extra functions
    ##########################################################################

    def attach_database(self, db, alias):
        """attach another database
        @param      db          database to attach
        @param      alias       database alias
        """
        if isinstance(db, str):
            self.LOG("ATTACH DATABASE '%s' TO '%s' ALIAS %s" % (db, db, alias))
            self.execute("ATTACH DATABASE '%s' AS %s;" % (db, alias))
        else:
            self.LOG(
                "ATTACH DATABASE '%s' TO '%s' ALIAS %s" %
                (db._sql_file, self._sql_file, alias))
            self.execute(
                "ATTACH DATABASE '%s' AS %s;" %
                (db.get_file(), alias))

    def add_function(self, name, nbparam, function):
        """add a function which can be used as any other SQL function (strim, ...)
        @param      name            function name (it does not allow _)
        @param      nbparam         number of parameters
        @param      function        function to add
        """
        if "_" in name:
            raise Exception("SQLite does not allow function name with _")
        self._check_connection()
        if self._engine == "SQLite":
            self._connection.create_function(name, nbparam, function)

    ##########################################################################
    # creation function
    ##########################################################################

    def create_index(self, indexname, table, columns, unique=False):
        """creates an index on a table using some columns
        @param      indexname   index name
        @param      table       table name
        @param      columns     list of columns
        @param      unique      any value in the columns is unique?
        """
        if not isinstance(columns, list) and not isinstance(columns, tuple):
            columns = [columns]

        if "." in table:
            prefix = table.split(".")[0] + "."
            table = table.split(".")[1]
        else:
            prefix = ""
            table = table

        self.LOG("index create ", indexname, table, columns, unique)
        if unique:
            sql = "CREATE UNIQUE INDEX %s%s ON %s (%s);" % (
                prefix, indexname, table, ",".join(columns))
        else:
            sql = "CREATE INDEX %s%s ON %s (%s);" % (
                prefix, indexname, table, ",".join(columns))
        self.execute(sql)

    def create_table(self, table, columns, temporary=False, nolog=False):
        """creates a table
        @param      table           table name
        @param      columns         columns definition, dictionary { key:(column_name,python_type) }
                                    if PRIMARYKEY is added, the key is considered as the primary key.
                                    Example:
                                    @code
                                    columns = { -1:("key", int, "PRIMARYKEY", "AUTOINCREMENT"),
                                                            0:("name",str), 1:("number", float) }
                                    @endcode
        @param      temporary       if True the table is temporary
        @param      nolog           @see me execute
        @return                     cursor
        """
        if self._engine == "SQLite" and table == "sqlite_sequence":
            raise DBException("unable to create a table named sql_sequence")

        tables = self.get_table_list()
        if table in tables:
            raise DBException(
                "table " +
                table +
                " is already present, it cannot be added")

        if temporary:
            sql = "CREATE TEMPORARY TABLE " + table + "("
        else:
            sql = "CREATE TABLE " + table + "("
        col = []
        for c, val in columns.items():
            if self.isMSSQL():
                if isinstance(val[1], tuple):
                    v, l = val[1]
                else:
                    v, l = val[1], 2048

                if l > 8000:
                    col.append(val[0] + " TEXT")
                elif v is str:
                    col.append(val[0] + " VARCHAR(%d)" % l)
                elif v is int:
                    col.append(val[0] + " INTEGER")
                elif v is float:
                    col.append(val[0] + " FLOAT")
                elif v is numpy.int64:
                    col.append(val[0] + " INTEGER")
                elif v is numpy.float64:
                    col.append(val[0] + " FLOAT")
                elif v is decimal.Decimal:
                    col.append(val[0] + " Decimal")
                elif v is datetime.datetime:
                    col.append(val[0] + " DATETIME")
                else:
                    raise DBException(
                        "unable to add column " +
                        str(c) +
                        " ... " +
                        str(val) +
                        " v= " +
                        str(v))
            else:
                if isinstance(val[1], tuple):
                    v, l = val[1]
                else:
                    v, l = val[1], 2048

                if v is str:
                    col.append(val[0] + " TEXT")
                elif v is int:
                    col.append(val[0] + " INTEGER")
                elif v is float:
                    col.append(val[0] + " FLOAT")
                elif v is numpy.int64:
                    col.append(val[0] + " INTEGER")
                elif v is numpy.float64:
                    col.append(val[0] + " FLOAT")
                elif v is decimal.Decimal:
                    col.append(val[0] + " Decimal")
                elif v is datetime.datetime:
                    col.append(val[0] + " DATETIME")
                else:
                    raise DBException(
                        "unable to add column " +
                        str(c) +
                        " ... " +
                        str(val) +
                        " v= " +
                        str(v))

            fval = val[2:]
            for v in fval:
                if v not in DatabaseCore._field_option:
                    raise DBException(
                        "an option is unexpected %s should be in %s" %
                        (v, str(
                            DatabaseCore._field_option)))

            if "PRIMARYKEY" in val:
                if val[1] != int:
                    raise DBException(
                        "unable to create a primary key on something differont from an integer (%s)" %
                        str(val))
                col[-1] += " PRIMARY KEY"
                if "AUTOINCREMENT" in val:
                    if self.isMSSQL():
                        col[-1] += " IDENTITY(0,1)"
                    else:
                        col[-1] += " AUTOINCREMENT"

        sql += ",\n       ".join(col)
        sql += ");"
        return self.execute(sql, nolog=nolog)

    ##########################################################################
    # deletion
    ##########################################################################

    def remove_table(self, table):
        """remove a table
        @param      table       table name
        @return                 return a cursor
        """
        self.execute("DROP TABLE %s" % table)

    ##########################################################################
    # modification
    ##########################################################################

    def _insert_sql(self, table, insert_values):
        """build the sql for an insert request
        @param      table               table name
        @param      insert_values       dictionary or a list
        @return                         string
        """
        if isinstance(insert_values, dict):
            keys = []
            values = []
            for k, v in insert_values.items():
                keys.append(k)
                if v is None:
                    values.append('')
                elif isinstance(v, str):
                    v = "'" + str(v).replace("'", "''") + "'"
                    values.append(v)
                elif isinstance(v, datetime.datetime):
                    v = "'" + str(v) + "'"
                    values.append(v)
                else:
                    values.append(str(v))
            keys = ",".join(keys)
            values = ",".join(values)
            sql = "INSERT INTO %s (%s) VALUES (%s)" % (table, keys, values)
            return sql
        elif isinstance(insert_values, tuple) or isinstance(insert_values, list):
            values = []
            for v in insert_values:
                if v is None:
                    values.append('')
                elif isinstance(v, str):
                    v = "'" + str(v).replace("'", "''") + "'"
                    values.append(v)
                elif isinstance(v, datetime.datetime):
                    v = "'" + str(v) + "'"
                    values.append(v)
                else:
                    values.append(str(v))
            values = ",".join(values)
            sql = "INSERT INTO %s VALUES (%s)" % (table, values)
            return sql
        else:
            raise TypeError("unexpected type: " + str(type(insert_values)))

    def insert(self, table, insert_values, cursor=None, nolog=True):
        """insert into a table
        @param      table           table name
        @param      insert_values   values to insert (a list of dictionary or a single dictionary)
        @param      cursor          if cursor != None, use it, otherwise creates a new one
        @param      nolog           if True, do not log anything
        @return                     sql request or None if several insertion were sent (result is too long)

        @warning The commit is not done and must be done to stored these modifications.
        """
        if isinstance(insert_values, list):
            # we expect several insertion
            if self._engine != "SQLite":
                for d in insert_values:
                    self.insert(table, d, cursor)
            else:
                if isinstance(insert_values[0], dict):
                    ins = {}
                    for k in insert_values[0]:
                        ins[k] = ":" + k
                    sql = self._insert_sql(table, ins)
                else:
                    q = tuple('?' for _ in insert_values[0])
                    sql = self._insert_sql(table, q).replace("'", "")

                sql = sql.replace("'", "")
                try:
                    if not nolog:
                        self.LOG("SQLs", sql)
                    self._connection.executemany(sql, insert_values)
                    return ""
                except Exception as e:
                    raise ExceptionSQL(
                        "unable to execute a SQL request (3) (cursor %s) (file %s)" %
                        (str(cursor), self.get_file()), e, sql)

        elif isinstance(insert_values, dict):
            sql = self._insert_sql(table, insert_values)

            try:
                if not nolog:
                    self.LOG("SQL", sql)
                if cursor is not None:
                    cursor.execute(sql)
                else:
                    if self._buffer_insert_s > 0:
                        self._buffer_insert.append(sql)

                        if len(self._buffer_insert) >= self._buffer_insert_s:
                            for s in self._buffer_insert:
                                self._connection.execute(s)
                            del self._buffer_insert[:]
                    else:
                        self._connection.execute(sql)

                return sql
            except Exception as e:
                raise ExceptionSQL(
                    "unable to execute a SQL request (2) (cursor %s) (file %s)" %
                    (str(cursor), self.get_file()), e, sql)

        else:
            raise DBException(
                "insert: expected type (list of dict or dict) instead of %s" %
                (str(
                    type(insert_values))))

    def update(self, table, key, value, values):
        """update some values  WHERE key=value
        @param      table       table to update
        @param      key         key
        @param      value       WHERE key = value
        @param      values      values to be updated

        @warning The commit is not done and must be done to stored these modifications.
        """

        self._check_values(values)
        self._check_connection()
        alls = []
        for k, v in values.items():
            if k != key:
                if isinstance(v, str) or isinstance(v, datetime.datetime):
                    alls += ["%s='%s'" % (k, str(v))]
                else:
                    alls += ["%s=%s" % (k, str(v))]
        if isinstance(value, str):
            sql = "UPDATE %s SET %s WHERE %s='%s'" % (
                table, ",".join(alls), key, value.replace("'", "''"))
        elif isinstance(value, datetime.datetime):
            sql = "UPDATE %s SET %s WHERE %s='%s'" % (
                table, ",".join(alls), key, str(value))
        else:
            sql = "UPDATE %s SET %s WHERE %s=%s" % (
                table, ",".join(alls), key, value)

        try:
            self._connection.execute(sql)
            return sql
        except Exception as e:
            raise ExceptionSQL(
                "unable to execute a SQL request (4) (file %s)" %
                self.get_file(), e, sql)
