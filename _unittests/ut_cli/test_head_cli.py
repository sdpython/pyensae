"""
@brief      test tree node (time=6s)
"""


import sys
import os
import unittest

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
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
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from src.pyensae.cli import file_head_cli


class TestHeadCli(unittest.TestCase):

    def test_head_cli(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        rows = []

        def flog(*l):
            rows.append(l)

        file_head_cli(args=['-h'], fLOG=flog)

        r = rows[0][0]
        if not r.startswith("usage: file_head [-h] [-f FILENAME] [-n NBLINE] [-e ENCODING] [-er ERRORS]"):
            raise Exception(r)


if __name__ == "__main__":
    unittest.main()
