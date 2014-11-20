"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest
import pandas


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
from src.pyensae import ASSHClient


class TestOutConnected (unittest.TestCase):
    
    def test_parsels(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        out = """Found 6 items
                                    drwx------   - xavierdupre xavierdupre          0 2014-11-18 01:00 .Trash
                                    drwx------   - xavierdupre xavierdupre          0 2014-11-16 02:38 .staging
                                    -rw-r--r--   3 xavierdupre xavierdupre    129.6 K 2014-11-16 02:37 ConfLongDemo_JSI.small.example.txt
                                    drwxr-xr-x   - xavierdupre xavierdupre          0 2014-11-16 02:38 ConfLongDemo_JSI.small.example2.walking.txt
                                    -rw-r--r--   3 xavierdupre xavierdupre    450.6 K 2014-11-20 01:33 paris.2014-11-11_22-00-18.331391.txt
                                    drwxr-xr-x   - xavierdupre xavierdupre          0 2014-11-20 01:53 velib_1hjs""".replace("                                    ","")
        fLOG(out)
        parse = ASSHClient.parse_lsout(out)
        fLOG(parse.columns)
        assert list(parse.columns) == ['attributes', 'code', 'alias', 'folder', 'size', 'unit', 'name', 'isdir']
        assert len(parse) > 0
        


if __name__ == "__main__"  :
    unittest.main ()