"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase
from pyensae.sql.database_helper import import_flatfile_into_database
from pyensae.sql.database_main import Database


class TestDatabase(ExtTestCase):

    def test_import_flatflit(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        file = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data",
            "ACA.PA.txt")
        dbf = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_database.db3")
        if os.path.exists(dbf):
            os.remove(dbf)
        import_flatfile_into_database(dbf, file, fLOG=fLOG)
        self.assertExists(dbf)
        db = Database(dbf, LOG=fLOG)
        db.connect()
        view = db.execute_view("SELECT * FROM ACAPA")
        self.assertGreater(len(view), 0)
        self.assertEqual(len(view[0]), 7)


if __name__ == "__main__":
    unittest.main()
