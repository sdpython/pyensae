"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.sql.database_helper import import_flatfile_into_database
from pyensae.sql.database_main import Database


class TestDatabaseCopy (unittest.TestCase):

    def test_import_flatflitand_copy(self):
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
            "temp_database_copy.db3")
        if os.path.exists(dbf):
            os.remove(dbf)

        dbf2 = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "out_copy.db3")
        if os.path.exists(dbf2):
            os.remove(dbf2)

        import_flatfile_into_database(dbf, file, fLOG=fLOG)
        assert os.path.exists(dbf)

        db = Database(dbf, LOG=fLOG)
        dbm = Database(dbf2, LOG=fLOG)
        db.copy_to(dbm)

        db.connect()
        dbm.connect()
        tbls = dbm.get_table_list()
        if len(tbls) != 1:
            raise Exception("expects one table not %d" % len(tbls))
        view = db.execute_view("SELECT * FROM ACAPA")
        viewm = dbm.execute_view("SELECT * FROM ACAPA")
        db.close()
        dbm.close()
        assert len(view) == len(viewm)

        dbm2 = Database(":memory:", LOG=fLOG)
        db.copy_to(dbm2)
        dbm2.connect()
        tbls = dbm2.get_table_list()
        if len(tbls) != 1:
            raise Exception("expects one table not %d" % len(tbls))
        viewm2 = dbm2.execute_view("SELECT * FROM ACAPA")
        dbm2.close()
        assert len(view) == len(viewm2)


if __name__ == "__main__":
    unittest.main()
