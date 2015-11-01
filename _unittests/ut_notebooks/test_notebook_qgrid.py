"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas

try:
    import src
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG, get_temp_folder, docstring2html
from src.pyensae.notebook_helper.magic_notebook import MagicNotebook


class TestNotebookQGrid(unittest.TestCase):

    def test_qgrid(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        df = pandas.DataFrame([{"x": 2, "y": 3}, {"x": 4, "y": 5}])
        fp = os.path.abspath(__file__)
        mg = MagicNotebook()
        mg.add_context({"df": df})
        res = mg.jsdf("df")
        fLOG(res)
        res = mg.jsdf("df")
        fLOG(res)
        assert res is not None

if __name__ == "__main__":
    unittest.main()
