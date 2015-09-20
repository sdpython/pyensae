"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas
import string
import numpy


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

from pyquickhelper import fLOG, get_temp_folder
from src.pyensae.graph_helper import Corrplot
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv


class TestGraph (unittest.TestCase):

    def test_graph_corrplot(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            # it requires scipy which is not included in the requirements.txt
            return

        fix_tkinter_issues_virtualenv()
        from matplotlib import pyplot as plt
        plt.style.use('ggplot')

        temp = get_temp_folder(__file__, "temp_corrplot")
        letters = "ABCDEFGHIJKLMNOP"[0:10]
        df = pandas.DataFrame(
            dict(((k, numpy.random.random(10) + ord(k) - 65) for k in letters)))
        df = df.corr()

        fig = plt.figure(num=None, facecolor='white')
        ax = plt.subplot(1, 1, 1, aspect='equal', axisbg='white')

        c = Corrplot(df)
        ax = c.plot(fig=fig, ax=ax)

        fLOG("save")
        img = os.path.join(temp, "corrplot.png")
        fig.savefig(img)
        fLOG("close")
        plt.close('all')
        fLOG("end")
        assert os.path.exists(img)

if __name__ == "__main__":
    unittest.main()
