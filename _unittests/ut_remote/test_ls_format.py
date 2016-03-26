"""
@brief      test log(time=140s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.pyensae.remote import ASSHClient

thisfold = os.path.abspath(os.path.split(__file__)[0])
thiscomm = os.path.join(thisfold, "..")
sys.path.append(thiscomm)


class TestLsFormat(unittest.TestCase):

    def test_ls(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        line = "-rw-rw-r-- 1 xavierdupre xavierdupre 21546346 Sep 27 11:18 ConfLongDemo_JSI.txt"
        out = ASSHClient.parse_lsout(line, False)
        self.assertEqual(out.shape, (1, 9))
        fLOG(out)
        fLOG(out.columns)


if __name__ == "__main__":
    unittest.main()
