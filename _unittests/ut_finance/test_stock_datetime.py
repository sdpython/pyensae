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
from src.pyensae.finance.astock import StockPrices


class TestStockFileDatetime(unittest.TestCase):

    tick = 'GOOGL'
    source = 'yahoo'

    def test_save_stock_datetime(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_save_stock_datetime")
        cache = temp

        stock = StockPrices(TestStockFileDatetime.tick, use_dtime=True, folder=cache,
                            end=datetime.datetime(2014, 1, 15), url=TestStockFileDatetime.source)

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        self.assertTrue(os.path.exists(file))

        stock2 = StockPrices(file, sep="\t", use_dtime=True)
        self.assertEqual(stock.dataframe.shape, stock2.dataframe.shape)
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        self.assertTrue(os.path.exists(file))


if __name__ == "__main__":
    unittest.main()
