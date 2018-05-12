"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import datetime
import decimal
import pandas
import numpy
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

from src.pyensae.sql.database_main import Database
from src.pyensae.sql.database_core import DatabaseCore
from src.pyensae.sql.database_exception import DBException
from src.pyensae.sql.type_helpers import get_default_value_type, guess_type_value_type, guess_type_value


class TestDatabaseMissing(ExtTestCase):

    def test_makedirs(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_missing_makedirs")
        dbf = os.path.join(temp, 'tr', 'td.db3')

        values = [{"name": "A", "age": 10, "score": 34.5},
                  {"name": "B", "age": 20, "score": -34.5}, ]
        df = pandas.DataFrame(values)
        db = Database.fill_sql_table(df, dbf, "newtable")
        db.execute_view("SELECT * FROM newtable")
        db.close()

    def test_makedirs_badengine(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_missing_makedirs2")
        dbf = os.path.join(temp, 'tr', 'td.db3')

        values = [{"name": "A", "age": 10, "score": 34.5},
                  {"name": "B", "age": 20, "score": -34.5}, ]
        df = pandas.DataFrame(values)
        try:
            Database.fill_sql_table(df, dbf, "newtable", engine='rty')
            raise AssertionError('engine is recognized but should not')
        except DBException:
            pass

    def test_makedirs_badengine2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        res = DatabaseCore.idaytodate(1, 2018, 3, 1)
        self.assertEqual(res, '2018-03-02')
        res = DatabaseCore.isectoday(1)
        self.assertEqual(res, '00:00:01')
        res = DatabaseCore.itimestamp(1, 2018, 3, 1)
        self.assertEqual(res, '2018-03-01 00:00:01')

    def test_db_index(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_missing_makedirs")
        dbf = os.path.join(temp, 'tr', 'td.db3')

        values = [{"name": "A", "age": 10, "score": 34.5},
                  {"name": "B", "age": 20, "score": -34.5}, ]
        df = pandas.DataFrame(values)
        db = Database.fill_sql_table(df, dbf, "newtable")
        has = db.has_index('ind')
        self.assertFalse(has)
        resi = db.get_index_on_table('newtable', full=True)
        self.assertEqual(resi, [])
        resi = db.get_index_on_table('newtable', full=False)
        self.assertEqual(resi, [])
        resi = db.get_column_type('newtable', 'name')
        self.assertEqual(resi, str)
        self.assertRaise(lambda: db.get_column_type(
            'newtable', 'name2'), DBException)
        resi = db.get_table_nfirst_lines('newtable', 2)
        self.assertEqual(resi, [(10, 'A', 34.5, 1), (20, 'B', -34.5, 2)])
        cur = db.execute_script('SELECT name FROM newtable')
        self.assertEqual(cur, None)
        cur = db.execute_script('SELECT name FROM newtable', close=False)
        self.assertFalse(cur is None)

        db.create_table("nextable2", columns={-1: ("key", int, "PRIMARYKEY", "AUTOINCREMENT"),
                                              0: ("name", str), 1: ("number", float),
                                              2: ('tint', int),
                                              3: ('tint64', numpy.int64),
                                              4: ('tfloat64', numpy.float64),
                                              5: ('tdt', datetime.datetime),
                                              6: ('tdec', decimal.Decimal)})
        cur.close()
        db.close()

    def test_guess(self):
        self.assertEqual(guess_type_value(5), int)
        self.assertEqual(guess_type_value('5'), int)
        self.assertEqual(guess_type_value(5.5), float)
        self.assertEqual(guess_type_value('5.5'), float)
        self.assertEqual(guess_type_value(None), None)
        self.assertEqual(guess_type_value(None, None), None)
        self.assertEqual(guess_type_value_type(), [None, str, int, float])
        self.assertEqual(get_default_value_type(int), 0)
        self.assertEqual(get_default_value_type(float), 0.)
        self.assertEqual(get_default_value_type(str), '')
        self.assertEqual(get_default_value_type(None), None)
        self.assertEqual(get_default_value_type(
            decimal.Decimal), decimal.Decimal(0))


if __name__ == "__main__":
    unittest.main()
