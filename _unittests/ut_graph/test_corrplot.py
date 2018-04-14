"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas
import numpy


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

from pyquickhelper.loghelper import fLOG, CustomLog
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from src.pyensae.graph_helper import Corrplot
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv


class TestGraph(ExtTestCase):

    def test_graph_corrplot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # it requires scipy which is not included in the requirements.txt
            return

        temp = get_temp_folder(__file__, "temp_corrplot")
        clog = CustomLog(temp)
        clog("fix")
        fix_tkinter_issues_virtualenv(fLOG=fLOG)
        clog("import")
        from matplotlib import pyplot as plt

        letters = "ABCDEFGHIJKLMNOP"[0:10]
        df = pandas.DataFrame(
            dict(((k, numpy.random.random(10) + ord(k) - 65) for k in letters)))
        df = df.corr()

        clog("figure")
        subplot_kw = dict(aspect='equal', facecolor='white')
        fig, ax = plt.subplots(1, 1, subplot_kw=subplot_kw)

        clog("corrplot")
        c = Corrplot(df)
        clog("plot")
        for up in ['lower', 'upper', 'method', 'both']:
            ax = c.plot(fig=fig, ax=ax)

        clog("save")
        fLOG("save")
        img = os.path.join(temp, "corrplot.png")
        fig.savefig(img)
        fLOG("close")
        clog("close")
        if __name__ == "__main__":
            plt.show()
        plt.close('all')
        clog("end")
        fLOG("end")
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
