"""
@brief      test log(time=3s)
"""


import sys
import os
import unittest
import datetime
import warnings


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
from pyquickhelper.pycode import get_temp_folder
from src.pyensae.finance.astock import StockPrices, StockPricesHTTPException


class TestStockUrl(unittest.TestCase):

    def test_download_stock_default(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_url_default")
        try:
            stock = StockPrices("NASDAQ:MSFT", folder=cache,
                                begin=datetime.datetime(2014, 1, 15))
        except StockPricesHTTPException as e:
            warnings.warn(str(e))
            return
        df = stock.dataframe
        dmin = df.Date.min()
        self.assertIn("2014", str(dmin))
        self.assertTrue(stock.url_.startswith(
            "https://finance.google.com/finance/historical?q=NASDAQ:MSFT&startdate=Jan+15%2C+2014"))


if __name__ == "__main__":
    unittest.main()
