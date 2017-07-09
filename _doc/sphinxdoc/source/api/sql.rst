
SQL
===

.. contents::
    :local:

magic commands
++++++++++++++

The magic command implements an easy way to access a
`SQLite3 <https://docs.python.org/3.6/library/sqlite3.html>`_ database.

.. autosignature:: pyensae.sql.magic_sql.MagicSQL
    :members:

database
++++++++

These classes implements manipulation with databases.
You should prefer *pandas* or *sqlite3* instead.

.. autosignature:: pyensae.sql.database_main.Database
    :members:

.. autosignature:: pyensae.sql.sql_interface_database.InterfaceSQLDatabase

import file
+++++++++++

These methods do not handle sparse files but they guess types and handles missing
values when converting a file into a database or a dataframe.
You should prefer *pandas* or *sqlite3* instead. They become sometimes useful
if *pandas* fails.

.. autosignature:: pyensae.sql.pandas_sql_helper.import_flatfile_into_database_pandas

.. autosignature:: pyensae.sql.database_helper.import_flatfile_into_database

These class reads csv files. You should use them if regulars ways fail.

.. autosignature:: pyensae.sql.file_text_binary.TextFile
    :members:

.. autosignature:: pyensae.sql.file_text_binary_columns.TextFileColumns
    :members:
