"""
@brief      test log(time=3s)
"""


import sys
import os
import unittest
import datetime
import warnings
from quandl.errors.quandl_error import LimitExceededError


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
from src.pyensae.finance.astock import StockPrices


class TestStockFile (unittest.TestCase):

    def _test_save_stock_google(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_cache_file_google")
        cache = temp

        stock = StockPrices(
            "NASDAQ:MSFT",
            folder=cache,
            end=datetime.datetime(
                2014,
                1,
                15))

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        self.assertTrue(os.path.exists(file))

        stock2 = StockPrices(file, sep="\t")
        self.assertEqual(stock.dataframe.shape, stock2.dataframe.shape)
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        self.assertTrue(os.path.exists(file))

    def _test_save_stock_quandl(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_cache_file_quandl")
        cache = temp

        try:
            stock = StockPrices("EURONEXT/BNP", url="quandl", folder=cache,
                                end=datetime.datetime(2017, 1, 15))
        except LimitExceededError:
            warnings.warn(
                "[test_save_stock_quandl] reached quandl free quota. Stop test.")
            return

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        self.assertTrue(os.path.exists(file))

        stock2 = StockPrices(file, sep="\t")
        self.assertEqual(stock.dataframe.shape, stock2.dataframe.shape)
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        self.assertTrue(os.path.exists(file))

    def test_save_stock_yahoo_new(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_cache_file_yahoo")
        cache = temp

        stock = StockPrices(
            "AAPL",
            folder=cache,
            url="yahoo_new",
            end=datetime.datetime(
                2014,
                1,
                15))

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        self.assertTrue(os.path.exists(file))

        stock2 = StockPrices(file, sep="\t")
        self.assertEqual(stock.dataframe.shape, stock2.dataframe.shape)
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        self.assertTrue(os.path.exists(file))


if __name__ == "__main__":
    unittest.main()
