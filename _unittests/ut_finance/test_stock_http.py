"""
@brief      test log(time=3s)
"""


import sys
import os
import unittest
import datetime


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
from src.pyensae.finance.astock import StockPrices, StockPricesException


class TestStockHttp (unittest.TestCase):

    def test_download_stock(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_cache_download_http")
        stock = StockPrices(
            "NASDAQ:MSFT",
            folder=cache,
            end=datetime.datetime(
                2014,
                1,
                15))
        name = os.path.join(cache, "NASDAQ_MSFT.2000-01-03.2014-01-15.txt")
        self.assertTrue(os.path.exists(name))
        df = stock.dataframe
        self.assertTrue(len(df) > 0)

    def test_available_dates(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_cache_dates")
        stocks = [StockPrices("NASDAQ:GOOGL", folder=cache),
                  StockPrices("NASDAQ:MSFT", folder=cache),
                  StockPrices("NASDAQ:AAPL", folder=cache),
                  ]
        av = StockPrices.available_dates(stocks)
        self.assertTrue(len(av) > 0)

        missing = stocks[-1].missing(av)
        self.assertTrue(missing is None or len(missing) > 0)

    def test_covariance(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_cache_cov")
        stocks = [StockPrices("NASDAQ:GOOGL", folder=cache),
                  StockPrices("NASDAQ:MSFT", folder=cache),
                  StockPrices("NASDAQ:AAPL", folder=cache),
                  ]

        dates = StockPrices.available_dates(stocks)
        ok = dates[dates["missing"] == 0]
        stocks = [v.keep_dates(ok) for v in stocks]

        cov = StockPrices.covariance(stocks)
        self.assertEqual(len(cov), 3)

        cor = StockPrices.covariance(stocks, cov=False)
        self.assertEqual(len(cor), 3)
        self.assertTrue(
            abs(cor.loc["NASDAQ:GOOGL", "NASDAQ:GOOGL"] - 1) < 1e-5)
        self.assertTrue(abs(cor.iloc[2, 2] - 1) < 1e-5)

        ret, mat = StockPrices.covariance(stocks, cov=False, ret=True)
        self.assertEqual(len(ret), 3)

    def test_no_wifi(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        data = os.path.abspath(os.path.split(__file__)[0])
        data = os.path.join(data, "data")
        file = os.path.join(data, "BNP.PA.2000-01-03.2014-02-24.txt")
        fLOG(os.path.exists(file))
        fLOG(file)
        try:
            StockPrices(file)
        except StockPricesException as e:
            if "schema: " not in str(e):
                raise Exception("unexpected error (1)") from e
        except Exception as e:
            if "pandas cannot parse the file" not in str(e):
                raise Exception("unexpected error (2)") from e
            if "Error tokenizing data" in str(e):
                raise Exception("unexpected error (3)") from e

    def test_index(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = get_temp_folder(__file__, "temp_cache_index")
        stock = StockPrices(
            "NASDAQ:GOOGL",
            folder=cache,
            end=datetime.datetime(
                2014,
                1,
                15))
        some = stock["2001-01-01":"2002-02-02"]
        self.assertTrue(isinstance(some, StockPrices))
        self.assertTrue(len(some) < 1000)


if __name__ == "__main__":
    unittest.main()
