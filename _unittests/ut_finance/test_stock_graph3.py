"""
@brief      test log(time=2s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import fix_tkinter_issues_virtualenv, ExtTestCase
from pyensae.finance.astock import StockPrices


class TestStockGraph3(ExtTestCase):

    tick = ['MSFT', 'GOOGL']
    source = 'yahoo_new'

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
