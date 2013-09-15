# coding: latin-1
"""
@file

@brief @see cl Database
"""

import re, copy, sys, os, random, sqlite3 as SQLite, datetime



from .file_text_binary      import TextFile
from .database_exception    import ExceptionSQL


class DatabaseCore2 :
    
    """
    complementary methods for class Database
    """
    
    _split_expr           = re.compile ("\\r?\\t")
    
    def _check_connection (self) :
        """check the SQL connection"""
        if "_connection" not in self.__dict__ : 
            message = "use connect method before doing operation on this database"
            raise Exception (message)
            
    def _check_values (self, values) :
        """when values are inserted or updated, this method doubles "'"
        it does not allow str values, only str
        @param      values      dictionary
        @return                 dictionary
        """
        mod = []
        for k,v in values.items() :
            if isinstance (v, str) and "'" in v :
                mod.append (k)
        if len (mod) == 0 :
            return values
        else :
            values = copy.copy (values)
            for k in mod :
                values [k] = values [k].replace ("'", "''")
            return values
            
    def summary (self, light = False) :
        """return the list of tables, their columns, and their length
        @param      light   light version, no count, no first lines
        @return             a dictionary where the keys are (t,i), t is a table name, i is in ["columns", "size", "first_lines"],
                            a str message
                              
        """
        tables  = self.get_table_list ()
        indexes = self.get_index_list ()
        res     = { }
        lines   = [ ]
        
        for t in tables : 
            col     = self.get_table_columns_list (t)
            if not light : 
                size    = self.get_table_nb_lines (t)
                first   = self.get_table_nfirst_lines (t)
            else :
                size    = -1
                first   = []
                
            res [t,"columns"]       = col
            res [t,"size"]          = size
            res [t,"first_lines"]   = first
            
            lines.append ( t  + "\t" + str (size) + " records") 
            lines.append ( "    columns" )
            for c in col :
                lines.append ("        " + str (c))
                
            if len (first) > 0 :
                lines.append ( "    first_lines" )
                for l in first :
                    fo = []
                    if l == None : lines.append ("        None")
                    else :
                        for x in l :
                            if not isinstance (x, str) : fo.append (str (x))
                            else : fo.append (x)
                        lines.append ( "        " + "\t".join ( fo) )
            
        if len (indexes) > 0 :
            lines.append ("\n")
            lines.append ("indexes")
            for tu in indexes :
                if isinstance (tu, tuple) or isintance (tu, list) :
                        lines.append ("    " + "\t".join ( [ str(x) for x in tu ] ))
                else :  lines.append ("    " + tu)
                    
        attached = self.get_attached_database_list ()
        if len (attached) > 0 :
            lines.append ("\n")
            lines.append ("attached databases")
            for a in attached :
                if a == "main" : continue
                lines.append ("    " + "\t" + a)
                continue
                rrr = self.execute ("SELECT name FROM %s.sqlite_master ORDER BY name;" %(a,))
                for b in rrr :
                    lines.append ("       " + "\t" + b [0])


        return res, "\n".join (lines)
            
    def _guess_columns (self, file, format, columns_name = None, filter_case = None) :
        """guess the columns types from a file (the method assumes there is a header)
        @param      file            file name
        @param      format          format (only tsv)
        @param      columns_name    if None, the first line contains the columns, otherwise it is the columns name
        @param      filter_case     process every case information (used to replace space for example)
        @return                     columns"""
        f = TextFile (file, utf8 = True, fLOG = self.LOG)
        f.open ()
        lines  = []
        for line in f :
            if len (lines) > 1000 : break
            if len (lines) > 900 and random.randint (0,10) > 0 : continue
            lines.append (DatabaseCore2._split_expr.split (line.strip (" \r\n").strip ('\ufeff')))
        f.close ()
        
        if len (lines) <= 1 : 
            raise HalException ("file %s is empty" % file)
            
        exp     = re.compile ("\\W+")
        columns = { }
        done    = { }
        count   = { }
        for i in range (0, len (lines [0])) :
            if lines [0][i] in ['\ufeffID', '\ufeffid', '\ufeffqid', '\ufeffQID'] : 
                lines [0][i] = "qid"

            if columns_name == None :   name = lines [0][i].replace (":", "_")
            else :                      name = columns_name [i].replace (":", "_")
            name = name.replace ("-", "_").replace (" ", "_")
            spl  = exp.split (name)
            if len (spl) > 1 : name = "".join (spl)
            if name [0] in "0123456789" : name = "_" + name
                
            if name in count : 
                count [name] += 1
                name         += str (count [name])
            else :  
                count [name]  = 1
                
            #lines [0][i] = name
            columns  [i] = (name, int)
            done     [i] = False
            
        length = {}
        nbline = 0
        for line_ in lines [1:] :
            if filter_case == None :    line = line_
            else :                      line = [ filter_case (s) for s in line_ ]
            nbline += 1
            if line == [] or line == [''] : continue

            for i in range (0, len (line)) :
                
                vl = length.get (i, 0)
                if len (line [i]) > vl :
                    length [i] = len (line [i])
                
                try :
                    if done [i] : continue
                except KeyError as e :
                    str_columns = ""
                    for k,v in columns.items() :
                        str_columns += "       " + str (k) + "\t" + str (v) + "\n"
                    mes = "KeyError:" + str (e) + "\n" + str (done) + "\n" + str_columns + "\nnb line " + str (nbline) + " columns: " + str (len(line)) + "\n" + str (line)
                    raise HalException ("problem\n" + mes)
                    
                try :
                    if columns [i][1] == float : raise ValueError ("")
                    x           = int (line [i])
                    if abs (x) >= 2147483647 : raise ValueError ("too big int")
                    columns [i] = (columns [i][0], int)
                except ValueError :
                    try :
                        x           = float (line [i])
                        if columns [i][1] != float :
                            columns [i] = (columns [i][0], float)
                            self.LOG ("   switch to float ", columns [i], " value ", line [i])
                    except ValueError :
                        columns [i]  = (columns [i][0], (str, len (line [i])*2) )
                        done [i]     = True
                        self.LOG ("   swith to str ", columns [i], " value ", line [i])

        # if not done, choose str by default
        for c in columns :
            v = columns [c]
            if v [1] == str :
                columns [c] = (v [0], (str, length.get (c, 4)*2))
                        
        for c,v in columns.items() :
            t = v [1]
            if isinstance (t, tuple) and t [0] == str and t [1] == 0 :
                raise HalException ("the length is null for column %s - %s" % (c, str (v)))
                        
        self.LOG ("   guess", columns)
        return columns
            
    def _process_text_line (self, line, columns, format, lower_case, num_line, 
                                fill_missing = 0, filter_case = None,
                                strict_separator = False) :
        """process a text line
        @param      line                text line to process (or a list if it already splitted)
        @param      columns             columns definition @see me _append_table
        @param      format              only tsv for the moment
        @param      lower_case          put every str object in lower_case
        @param      num_line            line number
        @param      fill_missing        fill the missing values by a default value, at least not more than fill_missing values
        @param      filter_case         process every case information (used to replace space for example)
        @param      strict_separator    strict number of columns, it assumes there is no separator in the content of every column
        @return                         a dictionary
        """
        if not isinstance (line, list) and not isinstance (line, tuple):
            if format != "tsv" : raise HalException ("unable to process format " + format)
            line = line.strip ("\r\n ").replace ("\n", " ")
            line = DatabaseCore2._split_expr.split (line)
        if filter_case != None :
            line = [ filter_case (s) for s in line ]
        
        #try :
        if 1 :
            
            if fill_missing > 0 :
                m    = max (columns.keys ())
                if m >= len (line) :
                    line = copy.copy (line)
                    add  = 0
                    while m >= len (line) and add < fill_missing :
                        a,b = columns [len (line)]
                        if      b is int    : line.append ("0")
                        elif    b is float  : line.append ("0.0")
                        elif    b is decimal.Decimal : line.append ("0")
                        elif    b is str    : line.append ("")
                        else                : line.append ("")
                        add += 1
                        
            res = { }
            for c,v in columns.items() :
                if "AUTOFILL" in v : 
                    res [ v [0] ] = "NULL"
                elif "AUTOINCREMENT" in v :
                    continue
                else :
                    if c >= len (line) :
                        self.LOG("(a)line number ", num_line, "*unable to process a line columns ",c, "#", line, " columns ", columns)
                        return None
                        
                    val = line [c]
                    if len (v) > 2 and v [2].lower () not in ["primarykey", "autofill"] : 
                        val = v [2] (val)
                        
                    try :
                        if   isinstance (v [1], tuple) :  val = v [1][0] (val)
                        elif v[1] is datetime.datetime :
                            if isinstance (val, datetime.datetime) : val = val
                            elif isinstance (val, str) : val = datetime.datetime.parse(val)
                            else : raise TypeError("unable to convert %s into datetime" % str(type(val)))
                        else :                          val = v [1] (val)
                    except ValueError as e :
                        self.LOG("(b)line number ", num_line, "**unable to process a line columns ",c, "#", v [0], " type ", v [1], " value ", repr (line [c]))
                        return None
                        
                    if isinstance (val, str) :
                        val = val.replace ("'", "''")
                        if lower_case : val = val.lower ()
                    res [ v [0] ] = val
                    
            return res
        #except Exception, e
        else :
            self.LOG("(c)line number ", num_line, "***unable to process a line columns ",c, line)
            return None
                    
    def _get_insert_request (   self, dico, 
                                table, 
                                exe = False, 
                                primarykey = None, 
                                cursor = None,
                                skip_exception = False) :
        """build an INSERT SQL request from a dictionary
        @param      dico            dictionary
        @param      table           table name
        @param      exe             if True, execute the request, if False, do nothing except returning the request
        @param      primarykey      primary key column, if it exist
        @param      cursor          if None, creates a new one, otherwise use it
        @param      skip_exception  if True, log exception instead of raising one
        @return                     str """
        keys   = []
        values = []
        for k,v in dico.items() :
            keys.append (k)
            if k != primarykey and isinstance (v, str) : 
                v = "'" + str (v) + "'"
                values.append (v)
            elif isinstance (v, datetime.datetime) :
                values.append ("'" + str (v) + "'")
            else : values.append (str (v))
        keys    = ",".join (keys)
        values  = ",".join (values)
        sql     = "INSERT INTO %s (%s) VALUES (%s);" % (table, keys, values)
        if exe :
            try :
                if cursor != None : cursor.execute (sql)
                else : self._connection.execute (sql)
            except SQLite.OperationalError as e :
                if skip_exception : self.LOG("OperationalError: unable to execute a query", e, sql)
                else : raise ExceptionSQL ("OperationalError: unable to execute a query", e, sql)
            except SQLite.IntegrityError as e :
                if skip_exception : self.LOG("IntegrityError: unable to execute a query", e, sql)
                else : raise ExceptionSQL ("IntegrityError: unable to execute a query", e, sql)
        return sql
        
    def get_python_code (self, varname = "db") :
        """return the python code associated to this database
        @param      varname     name of the variable
        @return                 2-uple: simp, scode (import part, code part)
        """
        
        path  = os.path.realpath (os.path.split (__file__) [0] )
        pos   = path.find ("pyhome3")
        if pos == -1 :
            raise HalException ("the installation of module pyhome3 went wrong: %s dot not contain pyhome3" % path)
        path  = path [:pos-1]
        if not os.path.exists (path) :
            raise HalException ("unable to find path " + path )
        simp  =      [ "import sys"]
        simp +=      [ "sys.path.append (r'%s')" % path ]
        simp +=      [ "from pyhome3 import Database"]
        
        code  =      [ "tblname = r'%s'" % self.get_file () ]
        
        more  = []
        if self._engine   != "SQLite" : code.append ("engine = '%s'"    % self._engine)
        if self._user     != None :     code.append ("user = '%s'"      % self._user)
        if self._password != None :     code.append ("password = '%s'"  % self._password)
        if self._host     != None :     code.append ("host = '%s'"      % self._host)
        more = ", ".join (more)
        
        code.append ( "%s      = Database (dbfile = tblname%s)" % (varname, more) )
        code.append ( "%s.connect ()" % varname)
        att   = self.get_attached_database_list (file = True)
        for alias, file in att :
            if len (file) == 0 : continue
            code.append ("%s.attach_database ('%s','%s')" % (varname,file, alias) )
        
        return "\n".join (simp) + "\n", "\n".join (code) + "\n"
                
        