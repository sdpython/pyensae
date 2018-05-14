"""
@brief      test log(time=2s)
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, ExtTestCase


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


from src.pyensae.finance.astock import StockPrices


class TestStockGraph4 (ExtTestCase):

    tick = 'GOOGL'
    source = 'yahoo_new'

    def test_graph4(self):
        """
        This test is failing with Python 3.4 if many pictures are drawn.
        """
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()

        from matplotlib import pyplot as plt

        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache4")
        stock = StockPrices(TestStockGraph4.tick,
                            folder=cache, url=TestStockGraph4.source)
        ret = stock.returns()["2012-04-01":"2014-04-15"]

        fig, ax = plt.subplots(figsize=(16, 8))
        ax = stock.plot(ax=ax)
        ax = ret.plot(ax=ax, axis=2)
        img = os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "temp_image4.png"))
        if os.path.exists(img):
            os.remove(img)
        fig.savefig(img)
        plt.close('all')
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
