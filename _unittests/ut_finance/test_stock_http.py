# coding: latin-1
"""
@brief      test log(time=3s)
"""


import sys, os, unittest, datetime


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.pyensae.finance.astock import StockPrices


class TestStockHttp (unittest.TestCase):
    
    def test_download_stock(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache")
        name = os.path.join(cache, "BNP.PA.2000-01-03.2014-01-15.txt")
        if os.path.exists(name) : os.remove(name)
        stock = StockPrices ("BNP.PA", folder = cache, end=datetime.datetime(2014,1,15))
        assert os.path.exists(name)
        df = stock.dataframe
        assert len(df) > 0

    def test_available_dates(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache2")
        stocks = [ StockPrices ("BNP.PA", folder = cache),
                    StockPrices ("CA.PA", folder = cache),
                    StockPrices ("SAN.PA", folder = cache),
                    ]
        av = StockPrices.available_dates(stocks)
        assert len(av)>0
        
        missing = stocks[-1].missing(av)
        assert len(missing)>0
        
    def test_covariance(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        cache = os.path.abspath(os.path.split(__file__)[0])
        cache = os.path.join(cache, "temp_cache2")
        stocks = [ StockPrices ("BNP.PA", folder = cache),
                    StockPrices ("CA.PA", folder = cache),
                    StockPrices ("SAN.PA", folder = cache),
                    ]
                    
        dates = StockPrices.available_dates( stocks )
        ok    = dates[ dates["missing"] == 0 ]
        stocks= [ v.keep_dates(ok) for v in stocks ]
                    
        cov = StockPrices.covariance(stocks)
        assert len(cov) == 3
        
        cor = StockPrices.covariance(stocks, cov = False)
        assert len(cor) == 3
        assert cor.ix["BNP.PA","BNP.PA"]==1
        assert cor.ix[2,2]==1
        
        ret, mat = StockPrices.covariance(stocks, cov = False, ret = True)
        assert len(ret) == 3
        
    def test_no_wifi(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        data = os.path.abspath(os.path.split(__file__)[0])
        data = os.path.join(data,"data")
        file = os.path.join(data, "BNP.PA.2000-01-03.2014-02-24.txt")
        fLOG(os.path.exists(file))
        fLOG(file)
        try:
            stock = StockPrices(file)
        except Exception as e :
            assert "pandas cannot parse the file" in str(e)

if __name__ == "__main__"  :
    unittest.main ()    
