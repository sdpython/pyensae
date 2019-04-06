"""
@brief      test log(time=2s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, ExtTestCase
from pyensae.finance.astock import StockPrices


class TestStockGraphOHLC(ExtTestCase):

    tick = 'MSFT'
    source = 'yahoo_new'

    def test_graph_ohlc(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        fix_tkinter_issues_virtualenv()

        from matplotlib import pyplot as plt

        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache_ohlc")
        stock = StockPrices(TestStockGraphOHLC.tick,
                            folder=cache, url=TestStockGraphOHLC.source)

        fig, ax = plt.subplots(figsize=(16, 8))
        ax = stock.plot(ax=ax, field="ohlc")
        img = os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "temp_image_ohlc.png"))
        if os.path.exists(img):
            os.remove(img)
        fig.savefig(img)
        plt.close('all')
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
