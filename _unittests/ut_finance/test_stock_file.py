"""
@brief      test log(time=3s)
"""


import sys
import os
import unittest
import datetime


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


if __name__ == "__main__":
    unittest.main()
