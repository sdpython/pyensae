# coding: latin-1
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
from src.pyensae.sql.database_main import Database


class TestDatabase (unittest.TestCase):
    
    def test_import_flatflit(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        file = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "data", "ACA.PA.txt")
        dbf  = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "temp_database.db3")
        if os.path.exists(dbf) : os.remove(dbf)
        import_flatfile_into_database(dbf, file, fLOG = fLOG)
        assert os.path.exists(dbf)
        db = Database(dbf, LOG = fLOG)
        db.connect()
        view = db.execute_view("SELECT * FROM ACAPA")
        assert len(view) > 0
        assert len(view[0]) == 7

if __name__ == "__main__"  :
    unittest.main ()    
