"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv
from pyensae.graphhelper.magic_graph import MagicGraph


class TestGraph (unittest.TestCase):

    def test_graph_style(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        mg = MagicGraph()
        cmd = "ggplot"
        mg.mpl_style(cmd)


if __name__ == "__main__":
    unittest.main()
