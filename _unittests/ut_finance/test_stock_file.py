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
from pyquickhelper.pycode import is_travis_or_appveyor
from src.pyensae.finance.astock import StockPrices


class TestStockFile (unittest.TestCase):

    def test_save_stock(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache_file")
        name = os.path.join(cache, "BNP.PA.2000-01-03.2014-01-15.txt")
        if os.path.exists(name):
            os.remove(name)

        stock = StockPrices(
            "BNP.PA",
            folder=cache,
            end=datetime.datetime(
                2014,
                1,
                15))

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        assert os.path.exists(file)

        stock2 = StockPrices(file, sep="\t")
        assert stock.dataframe.shape == stock2.dataframe.shape
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        assert os.path.exists(file)

    def test_save_stock_google(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache_file_google")
        name = os.path.join(cache, "NASDAQ_GOOG.2000-01-03.2014-01-15.txt")
        if os.path.exists(name):
            os.remove(name)

        try:
            stock = StockPrices(
                "NASDAQ:GOOG",
                url="google",
                folder=cache,
                end=datetime.datetime(
                    2014,
                    1,
                    15))
        except ImportError as e:
            # There is an issue with pandas_datareader on travis.
            # Not up to date with the latest pandas.
            if is_travis_or_appveyor():
                warnings.warn(
                    "Probably an issue with pandas_datareader.\n" + str(e))
                return

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        assert os.path.exists(file)

        stock2 = StockPrices(file, sep="\t")
        assert stock.dataframe.shape == stock2.dataframe.shape
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        assert os.path.exists(file)


if __name__ == "__main__":
    unittest.main()
