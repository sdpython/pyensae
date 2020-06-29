"""
@brief      test tree node (time=6s)
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.cli import file_head_cli


class TestHeadCli(unittest.TestCase):

    def test_head_cli(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        rows = []

        def flog(*la):
            rows.append(la)

        file_head_cli(args=['-h'], fLOG=flog)

        r = rows[0][0]
        if not r.startswith("usage: file_head [-h] [-f FILENAME] [-n NBLINE] [-e ENCODING] [-er ERRORS]"):
            raise Exception(r)


if __name__ == "__main__":
    unittest.main()
