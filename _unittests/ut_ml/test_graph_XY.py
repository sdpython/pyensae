"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from datetime import datetime
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
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

from src.pyensae.mlhelper import TableFormula


class TestTableFormulaGraph (unittest.TestCase):

    def test_graph_XY(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_graph_XY")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        from matplotlib import pyplot as plt

        df = TableFormula(dict(xx=[0.1, 0.2, 0.3], yy=[1.1, 1.2, 1.3]))

        subplot_kw = dict(aspect='equal', facecolor='white')
        fig, ax = plt.subplots(1, 1, subplot_kw=subplot_kw)
        df.graph_XY([[lambda row: row["xx"], lambda row: row["yy"], "xyl"]],
                    ax=ax, title="a title")

        img = os.path.join(temp, "graph_XY.png")
        fig.savefig(img)
        # if __name__ == "__main__":
        #     plt.show()
        plt.close('all')
        self.assertTrue(os.path.exists(img))

    def test_graph_XY_date(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_graph_XY")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        from matplotlib import pyplot as plt

        df = TableFormula(dict(xx=[datetime(2015, 1, 1), datetime(2016, 1, 1), datetime(2017, 1, 1)],
                               yy=[1.1, 1.2, 13]))

        subplot_kw = dict(aspect='equal', facecolor='white')
        fig, ax = plt.subplots(1, 1, subplot_kw=subplot_kw)
        df.graph_XY([[lambda row: row["xx"], lambda row: row["yy"], "xyl"]],
                    ax=ax, title="a title")

        img = os.path.join(temp, "graph_XY.png")
        fig.savefig(img)
        # if __name__ == "__main__":
        #     plt.show()
        plt.close('all')
        self.assertTrue(os.path.exists(img))


if __name__ == "__main__":
    unittest.main()
