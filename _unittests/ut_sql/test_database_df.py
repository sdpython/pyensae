"""
@brief      test log(time=10s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas
from pyquickhelper.loghelper import fLOG


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


class TestDatabaseDF (unittest.TestCase):

    def test_import_df(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        dbf = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_database_df.db3")
        if os.path.exists(dbf):
            os.remove(dbf)

        values = [{"name": "A", "age": 10, "score": 34.5},
                  {"name": "B", "age": 20, "score": -34.5}, ]
        df = pandas.DataFrame(values)
        db = Database.fill_sql_table(df, dbf, "newtable")
        db.execute_view("SELECT * FROM newtable")
        df2 = db.to_df("SELECT * FROM newtable")
        df3 = df2[["age", "name", "score"]]
        self.assertGreater(len(df), 0)
        self.assertEqual(len(df3), len(df))
        for a, b in zip(df.values, df3.values):
            self.assertGreater(len(a), 0)
            self.assertEqual(len(a), len(b))
            for c, d in zip(a, b):
                self.assertEqual(c, d)
        db.close()


if __name__ == "__main__":
    unittest.main()
