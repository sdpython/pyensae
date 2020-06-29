"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.sql import TextFileColumns


class TestFileColumns (unittest.TestCase):

    def test_read_csv_file(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        file = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data",
            "ACA.PA.txt")

        f = TextFileColumns(file, fLOG=fLOG)
        f.open()
        rows = list(f)
        f.close()
        for li in rows[:5]:
            fLOG(li)
            assert isinstance(li, dict)
            assert isinstance(li["Adj_Close"], float)


if __name__ == "__main__":
    unittest.main()
