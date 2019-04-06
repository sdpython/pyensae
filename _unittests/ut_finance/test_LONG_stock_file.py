"""
@brief      test log(time=200s)
"""
import os
import unittest
import datetime
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor, ExtTestCase
from pyensae.finance.astock import StockPrices


class TestLONGStockFile (ExtTestCase):

    tick = 'GOOGL'
    source = 'yahoo_new'

    def test_save_stock_google(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache_file_google")
        name = os.path.join(cache, TestLONGStockFile.tick.replace(
            ":", "_") + ".2000-01-03.2014-01-15.txt")
        if os.path.exists(name):
            os.remove(name)

        try:
            stock = StockPrices(TestLONGStockFile.tick, url=TestLONGStockFile.source,
                                folder=cache, end=datetime.datetime(2014, 1, 15))
        except ImportError as e:
            # There is an issue with pandas_datareader on travis.
            # Not up to date with the latest pandas.
            if is_travis_or_appveyor():
                warnings.warn(
                    "Probably an issue with pandas_datareader.\n" + str(e))
                return
            else:
                raise e

        file = os.path.join(cache, "save.txt")
        if os.path.exists(file):
            os.remove(file)
        stock.to_csv(file)
        self.assertExists(file)

        stock2 = StockPrices(file, sep="\t")
        self.assertEqual(stock.dataframe.shape, stock2.dataframe.shape)
        df = stock2.dataframe
        file = os.path.join(cache, "out_excel.xlsx")
        if os.path.exists(file):
            os.remove(file)
        df.to_excel(file)
        self.assertExists(file)


if __name__ == "__main__":
    unittest.main()
