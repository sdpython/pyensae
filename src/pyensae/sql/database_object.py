# coding: latin-1
"""
@file

@brief @see cl Database
"""

module_odbc = None


from pyquickhelper.loghelper.flog import fLOG


class DatabaseObject :
    
    """
    methods for database related to object, @see cl Database
    """
    
    def fill_table_with_objects(self, tablename, iterator_on, check_existence = False, skip_exception = False) :
        """
        Fill a table of a database with object (from ``iterator_on``) following the interface:
            - a property ``schema_database`` which gives the schema
            - a property ``asrow`` which puts all values in a row
            - a property ``index`` which precises the index to unless it returns None
            - a property ``indexes`` which precises other indexes to create (optional)
        
        The property ``asrow`` must not include other objects, only their ids.
        If the table does not exists, it creates it.
        
        @param      tablename           name of a table (created if it does not exists)
        @param      iterator_on         iterator_on on StreamRSS object
        @param      check_existence     avoid adding an element if it already exists (based on the index columns)
        @param      skip_exception      skip exception while inserting an element
        
        The function do not check duplicate among elements sent in ``iterator_on``,
        it only checks duplicate between the new and the old ones (meaning in the database).
        """
        schema = None
        index  = None
        indexes = None
        for _ in iterator_on :
            schema = _.schema_database
            index  = _.index
            try : indexes = _.indexes
            except : pass
            break
            
        if schema == None :
            # nothing to do, it is empty
            return
        
        if tablename not in self.get_table_list () : 
            fLOG("create table ", tablename)
            cursor = self.create_table (tablename, schema)
            if index != None :
                self.create_index( 
                            index + "_" + tablename + "_index", 
                            tablename, 
                            [ index ] , 
                            unique = True) 
                if indexes != None :
                    for ind in indexes :
                        if isinstance (ind, str) :
                            self.create_index( 
                                        ind + "_" + tablename + "_index", 
                                        tablename, 
                                        [ ind ] , 
                                        unique = False) 
                        else :
                            self.create_index( 
                                        "_".join(ind) + "_" + tablename + "_index", 
                                        tablename, 
                                        ind, 
                                        unique = False) 
            ite = map(lambda m : m.asrow, iterator_on)
            self.append_values ( ite, tablename, schema, cursor = cursor, skip_exception = skip_exception)
            
        else :
            if check_existence :
                if index == None :
                    raise ValueError("unable to check existence because index property is not set up")
                    
                def enumerate_nodup(iterator):
                    for it in iterator :
                        val  = it.__dict__[index]
                        view = self.execute_view ("SELECT * FROM %s WHERE %s=\"%s\";" % (tablename, index, val))
                        if len(view) == 0 :
                            yield it
                    
                ite = map(lambda m : m.asrow, enumerate_nodup ( iterator_on ) )
                self.append_values ( ite, tablename, schema, cursor = None, skip_exception = skip_exception)
            else :
                ite = map(lambda m : m.asrow, iterator_on)
                self.append_values ( ite, tablename, schema, cursor = None, skip_exception = skip_exception)

        self.commit()
        
    def enumerate_objects(self, table, classObject) :
        """
        iterator on objects assuming each row of a table is a object (classOject type).
        The classObject must have the following properties:
            - a staticmethod ``schema_database_read`` which gives the schema
            - the constructor must accept a constructor where parameter have the same name as the column names
        
        @param      table           table name
        @param      classObject     class object
        @return                     iterator on object
        
        Example:
        @code
        for blog in db.enumerate_objects ("blogs", StreamRSS):
            #...
        @endcode
        """
        schema = classObject.schema_database_read()
        for row in self.execute ("SELECT * FROM %s" % table) :
            di = { schema[i][0]:v for i,v in enumerate(row) }
            yield classObject(**di)
