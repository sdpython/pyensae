# -*- coding: utf-8 -*-
"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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

from src.pyensae.sql import TextFileColumns


class TestSeveralFiles(unittest.TestCase):

    def test_sort(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        data = os.path.join(os.path.abspath(
            os.path.split(__file__)[0]), "data")
        file1 = os.path.join(data, "tour2_2007_ext0.txt")
        file2 = os.path.join(data, "tour2_2007_ext1.txt")
        temp = get_temp_folder(__file__, "temp_sort")
        out = os.path.join(temp, "output.txt")

        # fusion
        fLOG("fusion")
        TextFileColumns.fusion("nomdudepartement", [file1, file2], output=out,
                               force_header=True, fLOG=fLOG)
        with open(out, "r", encoding="utf-8") as f:
            lines = f.readlines()
        found = 0
        for i, line in enumerate(lines):
            if "INCONNU" in line:
                found = i
        self.assertEqual(found, 37)

        # sort
        fLOG("sort")
        text_file = TextFileColumns(out, force_header=True)
        outs = os.path.join(temp, "output_sort.txt")
        text_file.sort(outs, "nomdudepartement", maxmemory=2 ** 10, fLOG=fLOG,
                       folder=temp)
        assert os.path.exists(outs)

        with open(outs, "r", encoding="utf-8") as f:
            lines = f.readlines()
        found = 0
        for i, line in enumerate(lines):
            if "INCONNU" in line:
                found = i
        self.assertEqual(found, 51)


if __name__ == "__main__":
    unittest.main()
