"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.pyensae.sql.database_helper import import_flatfile_into_database
from src.pyensae import Database, InterfaceSQL


class TestInterfaceSQL (unittest.TestCase):

    def test_interface_sql(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        file = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "data", "ACA.PA.txt")
        dbf  = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "temp_database_int.db3")
        if not os.path.exists(dbf) :
            import_flatfile_into_database(dbf, file, fLOG = fLOG)
        assert os.path.exists(dbf)

        face = InterfaceSQL.create(dbf)
        face.connect()

        tbls = face.get_table_list()
        fLOG(tbls)
        assert tbls == ['ACAPA']

        cols  = face.get_table_columns('ACAPA')
        fLOG(cols )
        assert cols == {0: ('Date', str),
                        1: ('Open', float),
                        2: ('High', float),
                        3: ('Low', float),
                        4: ('Close', float),
                        5: ('Volume', int),
                        6: ('Adj_Close', float)}

        assert face.CC.ACAPA._ == "ACAPA"
        assert face.CC.ACAPA.Date._ == "Date"

        sql = "SELECT COUNT(*) FROM ACAPA"
        df = face.execute(sql)
        fLOG(df)
        assert df.columns== ["COUNT(*)"]
        assert len(df) == 1
        assert df.values[0][0] == 2333

        sql = "SELECT COUNT(*) FROM DB.CC.ACAPA"
        df2 = face.execute(sql)
        fLOG(df)
        assert df.columns== ["COUNT(*)"]
        assert len(df) == 1
        assert df.values[0][0] == 2333

        face.close()

    def test_import_sql(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        file = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "data", "ACA.PA.txt")
        dbf  = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "temp_database_inti.db3")
        if os.path.exists(dbf) : os.remove(dbf)
        assert not os.path.exists(dbf)

        face = InterfaceSQL.create(dbf)
        face.connect()

        face.import_flat_file(file, "ACAPA2")
        assert face.CC.ACAPA2._ == "ACAPA2"

        face.close()


if __name__ == "__main__"  :
    unittest.main ()