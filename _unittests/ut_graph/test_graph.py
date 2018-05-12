"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv


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

from src.pyensae.graph_helper.magic_graph import MagicGraph


class TestGraph (unittest.TestCase):

    def test_graph_style(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        mg = MagicGraph()
        cmd = "ggplot"
        res = mg.mpl_style(cmd)
        fLOG(res)


if __name__ == "__main__":
    unittest.main()
