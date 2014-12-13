"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest, shlex


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
from src.pyensae import file_tail


class TestFiles (unittest.TestCase):

    def test_shlex(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        this = r"c:\rep1\rep2\frep\_urep.py rrr c:\rr\i.py"
        r = shlex.split(this, posix=False)
        fLOG(r)
        assert r[0] == r"c:\rep1\rep2\frep\_urep.py"

    def test_files(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        path = os.path.abspath(os.path.dirname(__file__))
        mg = MagicFile()
        cmd = path + " -f .*[.]py"
        fLOG("**",cmd)
        res = mg.lsr(cmd)
        fLOG(res)
        if len(res) == 0:
            raise FileNotFoundError("cmd: " + cmd)
        res = mg.lsr("")
        fLOG(res)
        assert len(res) > 0

    def test_head(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fp = os.path.abspath(__file__)
        mg = MagicFile()
        fLOG("--",fp)
        res = mg.head("{0} -n 3".format(fp))
        fLOG("*****",res)
        assert "test log" in res.data
        res = mg.head("{0} --n 3 -e ascii".format(fp))
        res = mg.head("{0} --n 3 -e utf8".format(fp))

    def test_tail(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        fp = os.path.abspath(__file__)
        mg = MagicFile()
        fLOG("--",fp)
        res = mg.tail("{0} -n 3".format(fp))
        fLOG("*****",res)
        assert "unittest.main" in res.data
        res = mg.tail("{0} --n 3 -e ascii".format(fp))
        res = mg.tail("{0} --n 3 -e utf8".format(fp))
        res = file_tail ( fp, threshold = 300, nbline = 3 )
        fLOG("#####",res)
        assert "unittest.main" in res[-1]


if __name__ == "__main__"  :
    unittest.main ()