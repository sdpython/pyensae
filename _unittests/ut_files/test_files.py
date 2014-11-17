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
from src.pyensae.file_helper.magic_file import MagicFile


class TestFiles (unittest.TestCase):

    def test_files(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        path = os.path.dirname(__file__)
        mg = MagicFile()
        cmd = path + " -f .*[.]py"
        fLOG("**",cmd)
        res = mg.lsr(cmd)
        fLOG(res)
        assert len(res) > 0
        res = mg.lsr("")
        fLOG(res)
        assert len(res) > 0

    def test_head(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        path = os.path.dirname(__file__)
        mg = MagicFile()
        res = mg.head("{0} -n 3".format(__file__))
        fLOG(res)
        assert "test log" in res
        res = mg.head("{0} --n 3 -e ascii".format(__file__))
        res = mg.head("{0} --n 3 -e utf8".format(__file__))

if __name__ == "__main__"  :
    unittest.main ()