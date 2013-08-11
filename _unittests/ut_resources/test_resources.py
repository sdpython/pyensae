# coding: latin-1
"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    import src

from src.pyensae.resources import check_dependency
check_dependency("pyhome3")
    
from pyhome3 import fLOG
from src.pyensae.resources.http_retrieve import download_data


class TestResources (unittest.TestCase):
    
    def test_pyhome3(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        check_dependency("pyhome3")
    
    def test_import_one(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fold = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "temp_http")
        if not os.path.exists(fold): os.mkdir(fold)
        exp = ["SQLiteSpy.exe", "SQLiteSpy.zip"]
        for f in exp :
            g = os.path.join(fold, f)
            if os.path.exists(g): os.remove(g)
        one = "SQLiteSpy.zip"
        res = download_data(one, website = "xd", whereTo = fold, fileprint = fLOG)
        fLOG(res)
        assert len(res) == 1
        assert "SQLiteSpy.exe" in res[0]
        for f in exp :
            g = os.path.join(fold, f)
            assert os.path.exists(g)
        
    def test_import_all(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        all = [" " ]
        if __name__ == "__main__" :
            # we only test all the resources if this file is the main file
            # otherwise it takes too much time
            for a in all :
                pass
        

if __name__ == "__main__"  :
    unittest.main ()    
