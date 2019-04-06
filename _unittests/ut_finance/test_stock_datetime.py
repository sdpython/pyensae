"""
@brief      test log(time=3s)
"""
import os
import unittest
import datetime
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyensae.finance.astock import StockPrices


class TestStockFileDatetime(unittest.TestCase):

    tick = 'GOOGL'
    source = 'yahoo_new'

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
        ret = stock2.returns()
        df.loc["2013-04-01":"2013-04-30", "Close"] = 0
        ret.dataframe.loc["2013-04-01":"2013-04-30", "Close"] = 0


if __name__ == "__main__":
    unittest.main()
