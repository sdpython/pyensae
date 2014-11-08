"""
@file

@brief @see cl Database
"""

import re,copy

class DatabaseJoinGroup :
    
    """
    This class is not neant to be working alone. 
    It contains functions for a database able to build 
    SQL requests for frequent needs such as join SQL requests.
    @see cl Database
    """
    
    class JoinTreeNode :
        """define a node meant to be included in a graph to define a big join
        """
        def __init__ (self, table, 
                            parent_key      = None,   
                            key             = None,
                            where           = None,
                            prefix          = None,
                            avoid_prefix    = False) :
            """constructor
            this node defines a join on two tables (parent_table, table)
            on two keys (parent_key, key). The keys can be tuple or string.
            @param      table           
            @param      parent_key      None if it is the root
            @param      key             None if it is the root
            @param      where           clause where
                                                where is a where clause defined as a dictionary: example:
                                                
                                                @code
                                                {   "field": ("==", value),
                                                    ("table","field"): (">=", value) }
                                                @endcode
                                                
                                                You may add field not connected to a table,
                                                they will not taken into account.
            @param      prefix          add a prefix, avoid different fields collide
            @param      avoid_prefix    avoid using a prefix to build SQL queries (use syntax ( ... ) AS ...
            """
            self.table          = table
            self.parent_key     = parent_key
            self.key            = key
            self.where          = { }
            self.predecessor    = None
            self.successor      = [ ]
            self.prefix         = None
            self._count_as      = 0
            self._avoid_prefix  = avoid_prefix
            if self.parent_key is None and self.key != None :
                raise Exception ("parent_key is missing")
                
            if where is not None :
                if not isinstance (where, dict) :
                    raise Exception ("parameter where: only dict or None expected (not %s)" % str (type (where)))
                for k,v in where.items() :
                    if not isinstance (k, tuple) : k = tuple (k.split ("."))
                    if   len (k) == 1 :             self.where [k[0] ] = v
                    elif len (k) == 2 :
                        if k [-2] == self.table :   self.where [k[-1]] = v
                    else :
                        raise Exception ("not able to deal with than clause %s:%s" % (str (k), str (v)))
            
        def __str__ (self) :
            """usual
            """
            mes = ["*nb succ: %d" % len (self.successor)]
            for k,v in sorted(self.__dict__.items()) :
                if k not in ["table", "parent_key", "where", "key"] : continue
                s  = k + " " * (12 - len (k))
                s += str (v)
                mes.append (s)
            i = 0
            for n in self.successor :
                r = str (n)
                l = r.split ("\n")
                l = [ "    " + s for s in l ]
                r = "\n".join (l)
                mes.append ("node %d" % i)
                mes.append (r)
                i += 1
            return "\n".join (mes) + "\n"
            
        def append (self, n) :
            """add a successor
            @param      n       new successor
            """
            if n.predecessor != None :
                raise Exception ("This node was already added in another part of the tree. You must duplicate it.")
            self.successor.append (n)
            n.predecessor = self
            
        def get_nb_successor (self) :
            """
            @return the number of successors
            """
            return len (self.successor)
            
        def check_prefix (self, nb = -1) :
            """
            @param      nb      index of this node is the predecessor list of successor
            check the prefixes, all one if there is none
            """
            if self._avoid_prefix :
                self.PREFIX = ""
                return 
            if "PREFIX" in self.__dict__ : return
            if self.prefix == None : 
                if nb == -1 :   self.prefix = ""
                else :          self.prefix = chr (97+nb)
            for i,n in enumerate (self.successor) : 
                n.check_prefix (i)
            self.PREFIX = "" if self.prefix is None else self.prefix
            self.PREFIX = self._build_predecessor_prefix () + self.PREFIX
                
        def _build_predecessor_prefix (self) :
            """
            private method
            """
            if self._avoid_prefix : return ""
            r = ""
            n = self.predecessor
            while n is not None :
                r += n.prefix
                n = n.predecessor
            return r
            
        def clean (self) :
            """
            remove all sql,fields members
            """
            if "SELECT" in self.__dict__ : 
                del self.__dict__ ["SELECT"]
                del self.__dict__ ["FIELDS"]
                del self.__dict__ ["PREFIX"]
            for n in self.successor :
                n.clean ()
                
        def _in_select (self, db) :
            """return the SQL select on the table
            @param      db  database
            @return         list of tuple (fieldas, table, field, which), where
            """
            fields  = db.get_table_columns_list (self.table)
            where   = { }
            for f,t in fields :
                if f in self.where :                   
                    where ["%s.%s" % (self.table,f)] = self.where [f]
                elif (self.table,f) in self.where : 
                    where ["%s.%s" % (self.table,f)] = self.where
                elif "." in f :
                    table,z = f.split(".")[-2:]
                    if table == self.table and z in self.where :
                        where ["%s.%s" % (table,z)] = self.where [z]
            
            prefix  = self.PREFIX
            fas     = []
            for f,t in fields :
                fas.append ( (prefix + f, self.table, f, True) )
            return fas, where
            
        def _build_select (self, db, fas, where, tfrom = None) :
            """build a select SQL request
            @param      db      database
            @param      fas     list of tuple table,f,fas
            @param      where   where clause
            @param      tfrom   from clause, if None, --> self.table
            @return             string
            """
            lines = []
            lines.append ("SELECT")
            alkey = True
            if len (fas) > 0 : 
                mx = max ( [ len (s[0]) for s in fas ] ) + 1
                name_changed = 0
                for well in fas :
                    fn,t,fo = well [:3]
                    if fn == self.key :
                        if alkey :
                            alkey = False
                            doit = True
                        else :
                            doit = False
                    else :
                        doit = True
                        
                    if doit :
                        s = " " * (mx - len (fn))
                        if len (well) == 4 and well [3] :  
                            s = "    %s%s AS %s," % (fo,s,fn) 
                            name_changed += 1
                        else :  
                            s = "    %s," % fn
                        lines.append (s)
                
                lines [-1] = lines [-1][:-1]  # kill the last comma
            else :
                raise Exception ("fas should not be empty")
                
            if tfrom is None : tfrom = self.table
                
            if "\n" in tfrom :  
                lines.append ("FROM (\n%s) AS temp_tbl%d" % (tfrom, self._count_as) )
                self._count_as += 1
            else :              
                lines.append ("FROM %s" % tfrom)
            
            if len (where) > 0 :
                wh = db._build_where_condition (where)
                lines.append (wh)
                
            return "\n".join (lines)
            
        def _find_in_fas (self, fas, a,b) :
            """find a,b in fas (column 1 and 2)
            @param      fas     list [ (new_name, table, name)]
            @param      a       table name
            @param      b       name
            """
            for name, tbl, field in fas :
                if a == tbl and b == field :
                    return name
            raise Exception ("unable to find field %s.%s in (%s)" % (a,b, str (fas)))
            
        def _build_join (self, db, fas, select, n) :
            """
            see :meth:`build_sql <pyensae.sql.database_join_group.build_sql>`
            
            @param      db              database
            @param      fas             list [(new_name, table, name)]
            @param      select          condition
            @param      n               node
            """
            
            other_select = n.SELECT
            parent_key   = n.parent_key
            key          = n.key
            
            other_select = other_select.split ("\n")
            other_select = ["    " + s for s in other_select ]
            other_select = "\n".join (other_select)
            select       = select.split ("\n")
            select       = ["    " + s for s in select ]
            select       = "\n".join (select)
            
            res  = self._build_select (db, fas, { }, select)
            res += "\nINNER JOIN (\n"
            res += other_select + ")"
            res += "\nON  "
            
            ppref = n.predecessor.PREFIX
            pref  = n.PREFIX
            
            if isinstance (parent_key, str) or isinstance (parent_key, str) :
                
                if parent_key.startswith ("<PREFIX>") :
                    a,b         = parent_key [8:].split (".")
                    parent_key  = (self._find_in_fas (fas, a,b),)
                else :
                    parent_key  = (ppref + parent_key,)
                    
                if key.startswith ("<PREFIX>") :
                    a,b         = key [8:].split (".")
                    key         = (self._find_in_fas (fas, a,b),)
                else :
                    key         = (pref + key,)
                
            else :
                pk = []
                k  = []
                for m,n in zip (parent_key, key) :
                    if m.startswith ("<PREFIX>") :
                        a,b     = m [8:].split (".")
                        pk.append (self._find_in_fas (fas, a,b))
                    else : 
                        pk.append (ppref + m)
                        
                    if n.startswith ("<PREFIX>") :
                        a,b     = n.split (".")
                        k.append (self._find_in_fas (fas, a,b))
                    else : 
                        k.append (pref + n)
                    
                parent_key = tuple ( pk )
                key        = tuple ( k )
                
            oni = [ ]
            for k,l in zip (parent_key, key) :
                oni.append ( "%s == %s" % (k,l) )
            oni = " AND \n    ".join (oni)
            res += oni
            return res
            
        def build_sql (self, db) :
            """
            build the sql request
            
            @param      db      database
            
            The function adds two attributes:
                - SELECT:   sql request for a node
                - FIELDS:   list of [ (final_name, table, original_name)
            """
            self.check_prefix ()
            
            for n in self.successor :
                n.build_sql (db)
                
            fas,where   = self._in_select (db)
            fields      = [ f [:3] for f in fas ]
            select      = self._build_select (db, fas, where)
            
            if self.get_nb_successor () == 0 :
                pass
            else :
                for n in self.successor :
                    fields.extend (n.FIELDS)
                    select = self._build_join (db, fields, select, n)
                
            self.SELECT     = select
            self.FIELDS     = fields
            
    def __init__ (self) :
        """
        constructor
        """
        self._count_as = 0

    ##################################################
    # the class itself: multiple joins using this tree
    ##################################################
    
    def inner_joins (self,  root,
                            execute             = False, 
                            create_index        = False,
                            created_table       = None,
                            duplicate_column    = True,
                            order               = [],
                            unique              = False,
                            distinct            = False,
                            fields              = None,
                            nolog               = True) :
                            
        """create several SQL inner join requests (included into each others)
        @param      root                JoinTreeNode (the root)
        @param      execute             if True, execute the query
        @param      create_index        if True, creates an index on the second table if it does not exist: it accelerates the inner join
        @param      created_table       if execute is True, you must specify a table name to be created
        @param      duplicate_column    do not include columns from the second table if their name is already in the first one
        @param      order               order clause, list of 2-tuple (column, way)  way is None or DESC
        @param      unique              unique or not
        @param      distinct            add the keyword DISTINCT
        @param      fields              restriction to fields given by fields or no restriction if None
        @param      nolog               if True, do not log the query
        @return                         SQL request, list of fields ("source", "new name")
        
        @warning Some options are not available yet:
                    - create_index      True
                    - duplicate_column  False
                    - order             != []
                    - unique            True
                    
        @todo   Three tasks (however, this won't probably happen)
                    - Finish The function inner_joins (parameters create_index, duplicate_column, order, unique).
                    - Improve the handling of keyword DISTINCT
                    - Handle keyword fields
        """
        if create_index :           raise Exception ("create_index = True: this option is not available")
        if not duplicate_column :   raise Exception ("duplicate_column = False: this option is not available")
        if len (order) > 0 :        raise Exception ("order != []: this option is not available")
        if unique :                 raise Exception ("unique = True: this option is not available")
        if fields is not None :     raise Exception ("fields != None: this option is not possible yet %s." % (str (fields)))
        
        root.build_sql (self)
        select = root.SELECT
        fields = root.FIELDS
        
        if distinct :
            if not select.startswith ("SELECT") :
                raise Exception ("algorithm problem")
            select = "SELECT DISTINCT" + select [len("SELECT"):]
            
        
        if execute :
            if created_table == None : 
                raise Exception ("unable to execute the SQL query: not specified name for the table to create")
            if created_table in self.get_table_list () :
                raise Exception ("table %s already exists" % created_table)
                
            select = "CREATE TABLE %s AS \n" % created_table + select
            self.execute (select, nolog = nolog)
        
        return select, fields
            
    ##################################################
    # the other methods
    ##################################################
    
    def _build_where_condition (self, where, add_keyword_where = True) :
        """builds a where condition (including the WHERE keyword)
        @param      where               condition where to interpret
                                            @code
                                            { "field": ("==", value) }
                                            @endcode
        @param      add_keyword_where   add the keyword where ?
        @return                         sql syntax
        
        @todo This function should deal with a tree to express AND and OR logical links. 
              (However, this probably won't happen.)
        """
        sql = ""
        if where is not None and len (where) > 0 :
            if add_keyword_where : sql += " WHERE "
            if isinstance (where, str) : 
                sql += where
            elif isinstance (where, dict) :
                a = []
                for k,v in where.items() :
                    if v [1] not in ['==', '<=', '>=', '>', '<', '!='] :
                        v = (v[1], v [0])
                    if v [1] not in ['==', '<=', '>=', '>', '<', '!='] :
                        raise Exception ("unable to understand where %s,%s " % (k,str (v)))
                    if v [1] == '==' and self.isMSSQL () : v = (v[0], '=')
                    v = ( v [0], " %s " % v [1] )
                    if isinstance (v [0], str) :
                        if "'" in v [0] :  s = k + v [1] + "'" + v [0].replace ("'", "''") + "'"
                        else :              s = k + v [1] + "'" + v [0] + "'"
                    else :                  s = k + v [1] + str (v [0])
                    a.append ( s )
                sql += " AND ".join (a)
            else :
                raise Exception ("unable to interpret this where condition %s" % (str (where)))
        return sql
    
    def histogram  (self,   table,
                            columns,
                            col_sums            = [],
                            values              = None,
                            sql_add             = None,
                            execute             = False, 
                            created_table       = None,
                            new_column          = "histogram",
                            nolog               = False) :
        """
        create a SQL request to compute an histogram
        
        @param      table               table
        @param      columns             column or columns (in a tuple) to be histogrammized
        @param      col_sums            candidate columns for a sum
        @param      values              specific values, several cases:
                                            - if None: does a GROUP BY
                                            - if dictionary of tuple:  ``{'cat1':('val1', 'val2', ...) }``
                                                then groups together several values into one category
                                            - if list of float: does an histogram on a real variable
        @param      new_column          name of the new column
        @param      sql_add             string to be added at the end of the SQL request
        @param      execute             if True, execute the request
        @param      created_table       the histogram can be stored into a table whose name is given by this parameter
        @param      nolog               if True, do not log the query
        @return                         SQL request
        
        """
        
        if isinstance (columns, str) :
            columns = (columns,)
        
        cols = self.get_table_columns_list (table)
        for column in columns :
            if column not in [x [0] for x in cols ] :
                raise Exception ("%s is not a column of table %s\n- columns:\n%s" % (column, table, "\n".join ([str (x) for x in cols])))
            
        if sql_add is None or len (sql_add) == 0 :  sql_add = ""
        else :                                      sql_add = ",\n       " + sql_add
            
        sum_column = []
        for c in col_sums :
            s = "SUM(%s) AS sum_%s" % (c,c)
            sum_column.append (s)
        str_sum = ", ".join (sum_column)
        if len (str_sum) > 0 : str_sum = ", " + str_sum
        
        if values is None :
            sql     = "SELECT %s AS %s, COUNT(%s) AS %s_nb%s%s\nFROM %s\nGROUP BY %s" % \
                             (", ".join (columns),
                              new_column,
                              "*",
                              new_column,
                              str_sum,
                              sql_add,
                              table,
                              ", ".join (columns))
            select  = sql
            
        elif isinstance (values, dict) :
            values_rev = { }
            for k,vv in values.items() :
                for v in vv :
                    if v not in values_rev : values_rev [v] = []
                    values_rev [v].append (k)
            for k,v in values_rev.items() :
                if len (v) > 1 : 
                    raise Exception ("a category is shared by several values %s and %s" % (k, ", ".join (v)) )
            for k in values_rev : values_rev [k] = values_rev [k][0]
            
            def filterfunctionhistogramdict1 (v)            : return values_rev.get (v, "none")
            def filterfunctionhistogramdict2 (a,b)          : return values_rev.get ((a,b), "none")
            def filterfunctionhistogramdict3 (a,b,c)        : return values_rev.get ((a,b,c), "none")
            def filterfunctionhistogramdict4 (a,b,c,d)      : return values_rev.get ((a,b,c,d), "none")
            def filterfunctionhistogramdict5 (a,b,c,d,e)    : return values_rev.get ((a,b,c,d,e), "none")
            
            self.add_function ("filterfunctionhistogramdict1",1,filterfunctionhistogramdict1)
            self.add_function ("filterfunctionhistogramdict2",2,filterfunctionhistogramdict2)
            self.add_function ("filterfunctionhistogramdict3",3,filterfunctionhistogramdict3)
            self.add_function ("filterfunctionhistogramdict4",4,filterfunctionhistogramdict4)
            self.add_function ("filterfunctionhistogramdict5",5,filterfunctionhistogramdict5)
            
            st   = ",".join (["a", "b", "c", "d", "e"][:len(cols)])
            sql  = "\n    -- def filterfunctionhistogramdict%d (%s) : return %s.get (%s, 'none')\n\n" % (len (columns), st, str (values_rev), st)
            sql += "\n    SELECT " + ",\n           ".join ( [x [0] for x in cols ] )
            sql += ",\n           filterfunctionhistogramdict%d (%s) AS histo_temp_col" % (len (columns), ", ".join (columns),)
            sql += "\n    FROM %s" % table
            sql  = "(" + sql + ") AS temp_tbl%d" % self._count_as
            self._count_as += 1
            
            select = "SELECT histo_temp_col AS %s,COUNT(histo_temp_col) AS %s_nb\n  %s\n  %s\nFROM %s\nGROUP BY histo_temp_col" % \
                             (new_column, new_column, str_sum, sql_add, sql)
            
        elif isinstance (values, list) :
            values = copy.copy (values)
            values.sort ()
            values2 = values [1:] + [max (1e10, max (values)+1),]
            names   = [ x for x in values ]
            couple = list(zip (range (0, len (values)), values, values2, names))
            
            def filterfunctionhistogramlist (v) : 
                for i,x,x_,n in couple :
                    if v < x_ : return n
                raise Exception ("unable to process, " + str (v) + " is a value higher than 1e10")
            self.add_function ("filterfunctionhistogramlist",1,filterfunctionhistogramlist)
                
            sql  = ""
            sql += "\n    SELECT " + ",\n    ".join ([x [0] for x in cols ])
            sql += ",\n    filterfunctionhistogramlist (%s) AS histo_temp_col" % (", ".join (columns),)
            sql += "\n    FROM %s" % table
            sql  = "(" + sql + ")"
            
            select = "SELECT histo_temp_col AS %s,COUNT(histo_temp_col) AS %s_nb\n  %s\n  %s\nFROM %s\nGROUP BY histo_temp_col" % \
                         (new_column, new_column, str_sum, sql_add, sql)
            
        else :
            raise Exception ("values has not a type (%s) not in [None, dict, list]" % ( str (type(values)) ) )
    
        if execute :
            if created_table is None :
                raise Exception ("unable to execute the SQL query: not specified name for the table to create")
            if created_table in self.get_table_list () :
                raise Exception ("table %s already exists" % created_table)
                
            select = "CREATE TABLE %s AS \n" % created_table + select
            self.execute (select, nolog = nolog)
        
        return select
        
    def inner_join (self,   table1, table2, 
                            field1, field2      = None, 
                            where               = None, 
                            execute             = False, 
                            create_index        = True,
                            created_table       = None,
                            prefix              = "",
                            duplicate_column    = True,
                            prefix_all          = "",
                            order               = [],
                            unique              = True,
                            params              = { },
                            nolog               = True) :
        """create a SQL inner join request
        @param      table1              first table
        @param      table2              second table
        @param      field1              inner join on field1 from table1
        @param      field2              inner join on field2 from table2 (if None --> field2 = field1
        @param      where               where clause (if None, do not add it), dictionary or string
        @param      execute             if True, execute the query
        @param      create_index        if True, creates an index on the second table if it does not exist: it accelerates the inner join
        @param      created_table       if execute is True, you must specify a table name to be created
        @param      prefix              prefix for fields from the second table
        @param      duplicate_column    do not include columns from the second table if their name is already in the first one
        @param      prefix_all          prefix for all fields 
        @param      order               order clause, list of 2-tuple (column, way)  way is None or DESC
        @param      unique              unique or not
        @param      params              special parameters for inner_joins method
        @param      nolog               if True, do not log the query, otherwise, skip that part
        @return                         SQL request, list of fields ("source", "new name")
        """
        
        if field2 is None :
            field2 = field1
        
        cols1 = self.get_table_columns_list (table1)
        cols1 = [f[0] for f in cols1]
        if len (cols1) == 0 : raise Exception ("table %s has no field" % table1)
        
        joinsm = table2 == '________________'
        if joinsm :
            cols2 = [ f[1] for f in params ["fields"] ]
            if len (cols2) == 0 : raise Exception ("imported table has no field")
            table2 = params ["sql"].split ("\n")
            table2 = ["     " + s for s in table2 ]
            table2 = "\n".join (table2)
            table2 = "(%s)"% (table2.strip ("\n\r "),)
        else :
            cols2 = self.get_table_columns_list (table2)
            cols2 = [f[0] for f in cols2]
            if len (cols2) == 0 : raise Exception ("table %s has no field" % table2)
        
        if isinstance (field1, tuple) :
            for k in field1 : 
                if k not in cols1 : raise Exception ("unable to find field %s in table %s" % (k, table1))
            for k in field2 : 
                if k not in cols2 : raise Exception ("unable to find field %s in table %s" % (k, table2))
        else :
            if field1 not in cols1 : raise Exception ("unable to find field %s in table %s" % (field1, table1))
            if field2 not in cols2 : raise Exception ("unable to find field %s in table %s" % (field2, table2))
            field1 = (field1,)
            field2 = (field2,)
            
        if create_index and joinsm:
            li  = self.get_index_list ()
            ind = False
            for name, tbl_name, sql in li :
                if tbl_name != table2 : continue
                fields = re.compile ("[(](\w*)[)]").search (sql).groups ()
                if len (fields) == 0 : continue
                field = fields [0]
                if field not in field2 : continue
                ind = True
            
            if not ind :
                self.LOG("creating an index on table %s, field %s" % (table2, ", ".join (field2)))
                self.create_index ("index_" + table2.replace (".", "_") + "_" + "_".join (field2), 
                                    table2, field2, unique = unique) 
            
        keyfields = { }
        for k in field1 :
            if k in cols2 :   
                if k not in field2 :    keyfield = ("%s.%s" % (table1,k),  table1 + "_" + k)
                else :                  keyfield = ("%s.%s" % (table1,k),                 k)
            else :                      keyfield = (k,                     k)
            keyfields [k] = keyfield
            
        if "." in table1 :  ptable1 = table1.split (".") [1]
        else :              ptable1 = table1
        if "." in table2 :  ptable2 = table2.split (".") [1]
        else :              ptable2 = table2
            
        fields = []
        for c in cols1 :
            if   ":" in c : continue
            elif c in keyfields : fields.append (keyfields [c])
            elif c in cols2 :    
                if duplicate_column :   fields.append ( ("%s.%s" % (ptable1, c), "%s_%s" % (ptable1, c) ) )
                else :                  fields.append ( ("%s.%s" % (ptable1, c), c)                       )
            else :                      fields.append ( (c,                      c)                       )
                
        for c in cols2 :
            if ":" in c : continue
            if c in field2 : continue
            if c in cols1 : 
                if duplicate_column :   fields.append ( ("%s.%s" % (ptable2, c), prefix + "%s_%s" % (ptable2, c) ) )
            else :                      fields.append ( (c,                      prefix + c)                       )
                
        mx      = max ( [ len (f [0]) for f in fields ] ) + 1                
        rem     = params.get ("as_remove", None)
        
        if rem is None :
            fields  = [ (f[0] + " " * (mx - len (f [0])), prefix_all + f [1]) for f in fields ]
        else :
            cfields = fields
            fields  = []
            for f in cfields :
                a = f[0] + " " * (mx - len (f [0]))
                b = (prefix_all + f [1]).replace (rem, "")
                if b in cols1 :
                    b = (prefix_all + f [1]).replace (rem, "_")
                fields.append ( (a,b) )
                
        all     = [ " AS ".join (f) for f in fields ]
        select  = ",\n       ".join (all)
        select  = "SELECT " + select + "\nFROM %s\n" % table1
        
        if unique :                 select += "INNER JOIN %s\n" % table2
        else :                      select += "JOIN %s\n" % table2

        nb = 0
        for k1,k2 in zip (field1, field2) :
            if nb > 0 :                         select += "   AND "
            else :                              select += "ON     "
                
            if k1 in cols2 :                    select += "%s.%s " % (table1,k1)
            else :                              select += "%s " % k1
            
            if k2 in cols1 and not joinsm :     select += "== %s.%s\n" % (table2,k2)
            else :                              select += "== %s\n" % k2
                
            nb += 1
            
        if where is not None and len (where) > 0 :
            select += "WHERE " + where + "\n"
            
        if order is not None and len (order) > 0 :
            te = []
            for o in order :
                if isinstance (o, tuple) : 
                    if o [0] in cols1 and o [0] in cols2 :  te.append (ptable1 + "." + o [0] + " " + o [1])
                    else :                                  te.append ( o [0] + " " + o [1])
                else : 
                    if o in cols1 and o in cols2 :  te.append (ptable1 + "." + o)
                    else :                          te.append ( o )
            select += "ORDER BY " + ", ".join (te) + "\n"
            
        #select += ";"
    
        if execute :
            if created_table is None :
                raise Exception ("unable to execute the SQL query: not specified name for the table to create")
            if created_table in self.get_table_list () :
                raise Exception ("table %s already exists" % created_table)
                
            select = "CREATE TABLE %s AS \n" % created_table + select
            self.execute (select, nolog = nolog)
        
        fields = [ (a.strip (), b) for a,b in fields ]
        return select, fields
        
        