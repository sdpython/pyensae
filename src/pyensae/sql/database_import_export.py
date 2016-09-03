"""
@file

@brief @see cl Database
"""

import os
import collections


from .file_text_binary import TextFile
from .file_text_binary_columns import TextFileColumns
from .database_exception import DBException


class DatabaseImportExport:

    """
    This class is not neant to be working alone.
    It contains import, export function for a database, in various formats.
    """

    ##########################################################################
    # exporting functions
    ##########################################################################

    def export_table_into_flat_file(self, table,
                                    filename,
                                    header=False,
                                    columns=None,
                                    post_process=None,
                                    encoding="utf8"):
        """
        export a table into a flat file

        @param      table           table name
        @param      filename        filename
        @param      header          add a header on the first line
        @param      columns         export only columns in this list (if None, export all)
        @param      post_process    post_process a line:
                                        - input:  list, dictionary (for your own use, same one all the time)
                                        - output: list
        @param      encoding        encoding

        .. exref::
            :title: Export the results of a SQL query into a flat file
            :tag: SQL

            ::

                from pyensae.sql.database_main import Database
                dbfile = "filename.db3"
                filetxt = "fileview.txt"
                sql = "..."
                db = Database(dbfile)
                db.connect()
                db.export_view_into_flat_file (sql, fileview, header = True)
                db.close()
        """
        if columns is None:
            sql = "SELECT * FROM " + table + ";"
        else:
            sql = "SELECT %s FROM %s ;" % (",".join(columns), table)

        self.export_view_into_flat_file(
            sql, filename, header, post_process, encoding=encoding)

    def _clean_string(self, s):
        """
        @param      s       string
        @return             remove \\r\\t\\n
        """
        rep = {"\t": "\\t",
               "\n": "\\n",
               "\r": "\\r", }
        for k, v in rep.items():
            s = s.replace(k, v)
        return s

    def export_view_into_flat_file(self, view_sql,
                                   filename,
                                   header=False,
                                   post_process=None,
                                   encoding="utf8"):
        """export a table into a flat file
        @param      view_sql        SQL request
        @param      filename        filename
        @param      header          if != None, add a header on the first line (header is a list of string)
        @param      post_process    if != None, use this function to post-process a text line extracted from the file
        @param      encoding        if != None, use this as a parameter to convert any value into str
        """
        sepline = "\n"

        self._check_connection()

        if header:
            if isinstance(header, list) or isinstance(header, tuple):
                header_line = "\t".join(header) + sepline
            elif isinstance(header, bool):
                col = self.get_sql_columns(view_sql)
                header_line = "\t".join(col) + sepline
            else:
                header_line = header + sepline
        else:
            header_line = ""

        sql = view_sql
        cur = self.execute(sql)
        nbline = 0

        f = open(filename, "w", encoding=encoding)
        f.write(header_line)
        memo = {}

        for line_ in cur:

            if post_process is not None:
                line = post_process(line_, memo)
            else:
                line = line_

            pr = "\t".join([self._clean_string(str(x)) for x in line])

            f.write(pr + sepline)
            nbline += 1
            if nbline % 100000 == 0:
                self.LOG("     exporting from view, line ", nbline)

        f.close()
        cur.close()

    ##########################################################################
    # importing functions
    ##########################################################################

    def append_values(
            self, values, tablename, schema, cursor=None, skip_exception=False, encoding="utf-8"):
        """
        use @see me _append_table to fill a table will the values contained in values (as list)

        @param      values          list of list (each cell is a value)
        @param      tablename       name of the table to fill
        @param      schema          schema of the database, it must be present in case on the columns
                                    includes the tag "PRIMARYKEY", in that case, the value for this field
                                    will be automatically set up.
        @param      cursor          if None, create a new one
        @param      skip_exception  skip exception while inserting an element
        @param      encoding        encoding

        """
        self._append_table(
            values,
            tablename,
            schema,
            cursor=cursor,
            skip_exception=skip_exception,
            encoding=encoding)

    def _append_table(self, file,
                      table,
                      columns,
                      format="tsv",
                      header=False,
                      stop=-1,
                      lower_case=False,
                      cursor=None,
                      fill_missing=0,
                      unique=None,
                      filter_case=None,
                      strict_separator=False,
                      skip_exception=False,
                      changes=None,
                      encoding="utf-8",
                      **params):
        """
        append element to a database

        @param      file                file name or a matrix (this matrix can be an iterator)
        @param      table               table name
        @param      columns             columns definition (see below)
        @param      format              tsv, the only one accepted for the time being, it can be a function (line, **params)
        @param      header              the file has a header of not, if True, skip the first line
        @param      stop                if -1, insert every line, otherwise stop when the number of inserted lines is stop
        @param      lower_case          put every str string in lower_case before inserting it
        @param      cursor              if None, create a new one
        @param      fill_missing        fill the missing values by a default value, at least not more than fill_missing values
        @param      unique              if unique is a column number,
                                        the function will not take into account another containing a value already seen on this column
        @param      filter_case         process every case information (used to replace space for example)
        @param      strict_separator    strict number of columns, it assumes there is no separator in the content of every column
        @param      params              see format
        @param      skip_exception      skip exception while inserting an element
        @param      changes             to rewrite column names
        @param      encoding            encoding
        @return                         number of inserted elements

        The columns definition must follow the schema:
            - dictionary ``{ key:(column_name,python_type) }``
            - or ``{ key:(column_name,python_type,preprocessing_function) }``

        ``preprocessing_function`` is a function whose prototype is for example:

        @code
        def preprocessing_score (s) :
            return s.replace (",",".")
        @endcode

        And:
            - if ``PRIMARYKEY`` is added, the key is considered as the primary key
            - if ``AUTOINCREMENT`` is added, the key will automatically filled (like an id)

        """
        if changes is None:
            changes = {}
        if stop != -1:
            self.LOG("SQL append table stop is ", stop)
        self._check_connection()
        nbinsert = 0
        unique_key = {}
        if isinstance(file, list) or (
                isinstance(file, collections.Iterable) and not isinstance(file, str)):
            primarykey = None
            for c, v in columns.items():
                if "PRIMARYKEY" in v:
                    primarykey = v[0]

            if table not in self.get_table_list():
                raise DBException("unable to find table " + table)

            all = 0
            num_line = 0
            for line in file:
                if stop != -1 and all >= stop:
                    break
                dic = self._process_text_line(line,
                                              columns,
                                              format=format,
                                              lower_case=lower_case,
                                              num_line=num_line,
                                              filter_case=filter_case,
                                              strict_separator=strict_separator)

                if unique is not None:
                    if dic[unique] in unique_key:
                        continue
                    else:
                        unique_key[dic[unique]] = 0

                num_line += 1
                if dic is not None:
                    self._get_insert_request(dic,
                                             table,
                                             True,
                                             primarykey,
                                             cursor=cursor,
                                             skip_exception=skip_exception)
                    nbinsert += 1
                    #self._connection.execute (s)
                    all += 1
                    if all % 100000 == 0:
                        self.LOG(
                            "adding %d lines into table %s" %
                            (all, table))
        else:
            primarykey = None
            for c, v in columns.items():
                if "PRIMARYKEY" in v:
                    primarykey = v[0]

            if table not in self.get_table_list():
                table_list = self.get_table_list()
                message = "unable to find table " + table + \
                    " in [" + ",".join(table_list) + "]"
                raise DBException(message)

            column_has_space = len(
                [v[0] for k, v in columns.items() if ' ' in v[0]]) > 0
            self.LOG(
                "   column_has_space", column_has_space, [
                    v[0] for k, v in columns.items()])

            if strict_separator or column_has_space:
                file = TextFile(
                    file,
                    errors='ignore',
                    fLOG=self.LOG,
                    encoding=encoding)
                skip = False
            else:
                self.LOG("   changes", changes)
                file = TextFileColumns(file, errors='ignore', fLOG=self.LOG,
                                       regex=columns, changes=changes, encoding=encoding)
                skip = True

            file.open()
            all = 0
            num_line = 0
            every = 100000
            tsv = format == "tsv"

            for line in file:
                if stop != -1 and all >= stop:
                    break
                num_line += 1
                if skip:
                    dic = line
                else:
                    if header and num_line == 1:
                        continue
                    if len(line.strip("\r\n")) == 0:
                        continue
                    if tsv:
                        dic = self._process_text_line(line,
                                                      columns,
                                                      format,
                                                      lower_case=lower_case,
                                                      num_line=num_line - 1,
                                                      fill_missing=fill_missing,
                                                      filter_case=filter_case,
                                                      strict_separator=strict_separator)
                    else:
                        dic = format(line, **params)
                        if dic is None:
                            continue

                if unique is not None:
                    if dic[unique] in unique_key:
                        continue
                    else:
                        unique_key[dic[unique]] = 0

                if dic is not None:
                    self._get_insert_request(
                        dic,
                        table,
                        True,
                        primarykey,
                        cursor=cursor)
                    nbinsert += 1
                    all += 1
                    if all % every == 0:
                        self.LOG(
                            "adding %d lines into table %s" %
                            (all, table))
            file.close()

        if cursor is not None:
            cursor.close()
        self.commit()
        return nbinsert

    def import_table_from_flat_file(self,
                                    file,
                                    table,
                                    columns,
                                    format="tsv",
                                    header=False,
                                    display=False,
                                    lower_case=False,
                                    table_exists=False,
                                    temporary=False,
                                    fill_missing=False,
                                    indexes=[],
                                    filter_case=None,
                                    change_to_text=[],
                                    strict_separator=False,
                                    add_key=None,
                                    encoding="utf-8",
                                    **params):
        """
        add a table to database from a file

        @param      file                file name or matrix
        @param      table               table name
        @param      columns             columns definition (see below)
                                        if None: columns are guessed
        @param      format              tsv, the only one accepted for the time being, it can be a function whose parameter are a line and **params
        @param      header              the file has a header of not, if True, skip the first line
        @param      lower_case          put every string in lower case before inserting it
        @param      table_exists        if True, do not create the table
        @param      temporary           adding a temporary table
        @param      fill_missing        fill the missing values
        @param      indexes             add indexes before appending all the available observations
        @param      filter_case         process every case information (used to replace space for example)
        @param      encoding            encoding
        @param      params              see format
        @param      change_to_text      changes the format from any to TEXT
        @param      display             if True, print more information on stdout
        @param      strict_separator    strict number of columns, it assumes there is no separator in the content of every column
        @param      add_key             name of a key to add (or None if nothing to add)
        @return                         the number of added rows

        The columns definition must follow the schema:
            - dictionary ``{ key:(column_name,python_type) }``
            - or ``{ key:(column_name,python_type,preprocessing_function) }``


        ``preprocessing_function`` is a function whose prototype is for example:

        @code
        def preprocessing_score (s) :
            return s.replace (",",".")
        @endcode

        And:
            - if ``PRIMARYKEY`` is added, the key is considered as the primary key
            - if ``AUTOINCREMENT`` is added, the key will automatically filled (like an id)

        @warning The function does not react well when a column name includes a space.
        """
        if display:
            if isinstance(file, list):
                self.LOG("processing file ", file[:min(len(file), 10)])
            else:
                self.LOG("processing file ", file)

        self._check_connection()
        if columns is None:
            # here, some spaces might have been replaced by "_", we need to get
            # them back
            columns, changes = self._guess_columns(
                file, format, columns, filter_case=filter_case, header=header, encoding=encoding)
        elif isinstance(columns, list):
            columns_, changes = self._guess_columns(
                file, format, columns, filter_case=filter_case, header=header, encoding=encoding)
            if len(columns_) != len(columns):
                raise DBException(
                    "different number of columns:\ncolumns={0}\nguessed={1}".format(
                        str(columns),
                        str(columns_)))
            columns = columns_

        if add_key is not None:
            columns[
                len(columns)] = (
                add_key,
                int,
                "PRIMARYKEY",
                "AUTOINCREMENT")

        for i in columns:
            v = columns[i]
            if v[0] in change_to_text:
                if len(v) <= 2:
                    v = (v[0], (str, 1000000))
                else:
                    v = (v[0], (str, 1000000)) + v[2:]
            columns[i] = v

        if display:
            self.LOG("   columns ", columns)

        if not isinstance(file, list) and not os.path.exists(file):
            raise DBException("unable to find file " + file)

        if not table_exists:
            cursor = self.create_table(table, columns, temporary=temporary)
        elif table not in self.get_table_list():
            raise DBException("unable to find table " + table + " (1)")
        else:
            cursor = None

        if table not in self.get_table_list():
            raise DBException("unable to find table " + table + " (2)")
        nb = self._append_table(file,
                                table,
                                columns,
                                format=format,
                                header=header,
                                lower_case=lower_case,
                                cursor=cursor,
                                fill_missing=fill_missing,
                                filter_case=filter_case,
                                strict_separator=strict_separator,
                                changes=changes,
                                encoding=encoding,
                                **params)

        self.LOG(nb, " lines imported")

        for ind in indexes:
            if isinstance(ind, str):
                indexname = table + "_" + ind
            else:
                indexname = table + "_" + "_".join(ind)
            if not self.has_index(indexname):
                self.create_index(indexname, table, ind)

        return nb
