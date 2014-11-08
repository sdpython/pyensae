"""
@brief      test log(time=28s)
"""


import sys, os, unittest, datetime, pandas


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
from src.pyensae.datasource.convert import dBase2df, dBase2sqllite


class TestConvert(unittest.TestCase):

    def test_dbf2df(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__", LogFile = "temp_hal_log2.txt")
        fold = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(fold, "data", "varmod_naissances.dbf")
        df = dBase2df(file)
        assert df is not None
        #fLOG(df)

    def test_dbf2sqlite(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__", LogFile = "temp_hal_log2.txt")
        fold = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(fold, "data", "varmod_naissances.dbf")

        outf = os.path.join(fold, "out_dbfsqlite")
        if not os.path.exists(outf) : os.mkdir(outf)

        dbfile = os.path.join(outf, "naissance.db3")
        if os.path.exists(dbfile) : os.remove(dbfile)

        df = dBase2df(file)
        dBase2sqllite(dbfile, file)
        assert df is not None
        assert os.path.exists(dbfile)

if __name__ == "__main__"  :
    unittest.main ()