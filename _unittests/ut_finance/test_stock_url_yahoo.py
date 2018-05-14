"""
@brief      test log(time=3s)
"""


import sys
import os
import unittest
import datetime
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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


class TestStockUrlYahoo(unittest.TestCase):

    source = 'yahoo_new'

    def test_download_stock_yahoo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_url_yahoo")
        exc = []
        for n in range(0, 4):
            stock = StockPrices("^FCHI", folder=cache, url=TestStockUrlYahoo.source,
                                begin=datetime.datetime(2014, 1, 15))
            df = stock.dataframe
            dmin, dmax = df.Date.min(), df.Date.max()
            try:
                self.assertIn("2014", str(dmin))
                self.assertNotEqual(dmin, dmax)
                if "^FCHI.2014-01-15" not in stock.url_:
                    raise AssertionError(stock.url_)
                return
            except AssertionError as e:
                exc.append(e)
        if len(exc) > 0:
            e = exc[0]
            raise AssertionError('nb tries={0}'.format(len(exc))) from e


if __name__ == "__main__":
    unittest.main()
