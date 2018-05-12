"""
@brief      test tree node (time=6s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG

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


from src.pyensae.cli import file_tail_cli


class TestTailCli(unittest.TestCase):

    def test_tail_cli(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        rows = []

        def flog(*l):
            rows.append(l)

        file_tail_cli(args=['-h'], fLOG=flog)

        r = rows[0][0]
        if not r.startswith("usage: file_tail [-h] [-f FILENAME] [-n NBLINE] [-e ENCODING] [-t THRESHOLD]"):
            raise Exception(r)


if __name__ == "__main__":
    unittest.main()
