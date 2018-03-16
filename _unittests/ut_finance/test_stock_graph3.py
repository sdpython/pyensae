"""
@brief      test log(time=2s)
"""


import sys
import os
import unittest


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

from pyquickhelper.loghelper import fLOG
from src.pyensae.finance.astock import StockPrices
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, ExtTestCase


class TestStockGraph3(ExtTestCase):

    tick = ['MSFT', 'GOOGL']
    source = 'yahoo'

    def test_graph3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()

        from matplotlib import pyplot as plt

        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache3")
        stock = StockPrices(
            TestStockGraph3.tick[0], folder=cache, url=TestStockGraph3.source)
        stock2 = StockPrices(
            TestStockGraph3.tick[1], folder=cache, url=TestStockGraph3.source)

        fig, ax = plt.subplots(figsize=(16, 8))
        ax = stock.plot(ax=ax)
        ax = stock2.plot(ax=ax, axis=2)
        img = os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "temp_image3.png"))
        if os.path.exists(img):
            os.remove(img)
        fig.savefig(img)
        plt.close('all')
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
