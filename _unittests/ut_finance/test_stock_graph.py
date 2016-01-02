"""
@brief      test log(time=2s)
"""


import sys
import os
import unittest


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

from pyquickhelper import fLOG
from src.pyensae.finance.astock import StockPrices
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, is_travis_or_appveyor


class TestStockGraph (unittest.TestCase):

    def test_graph(self):
        """
        This test is failing with Python 3.4 if many pictures are drawn.
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor() == "appveyor":
            return

        fix_tkinter_issues_virtualenv()

        from matplotlib import pyplot as plt

        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache2")
        stocks = [StockPrices("BNP.PA", folder=cache),
                  StockPrices("CA.PA", folder=cache),
                  StockPrices("SAF.PA", folder=cache),
                  ]

        if True:
            fLOG("A", sys.executable)
            fig, ax = plt.subplots()
            ax = StockPrices.draw(
                stocks, figsize=(
                    16, 8), field=[
                    "Adj Close", "Close"],
                ax=ax)
            img = os.path.abspath(
                os.path.join(
                    os.path.split(__file__)[0],
                    "temp_image.png"))
            if os.path.exists(img):
                os.remove(img)
            fig.savefig(img)
            plt.close('all')
            assert os.path.exists(img)

        if True:
            fLOG("B")
            fig, ax = plt.subplots()
            ax = StockPrices.draw(stocks, begin="2010-01-01", ax=ax)
            img = os.path.abspath(
                os.path.join(
                    os.path.split(__file__)[0],
                    "temp_image2.png"))
            if os.path.exists(img):
                os .remove(img)
            fig.savefig(img)
            plt.close('all')
            assert os.path.exists(img)

        if True:
            fLOG("C")
            fig, ax = plt.subplots()
            ax = StockPrices.draw(stocks[:1], begin="2010-01-01", ax=ax)
            img = os.path.abspath(
                os.path.join(
                    os.path.split(__file__)[0],
                    "temp_image3.png"))
            if os.path.exists(img):
                os .remove(img)
            fig.savefig(img)
            plt.close('all')
            assert os.path.exists(img)

        fLOG("thisend")


if __name__ == "__main__":
    unittest.main()
