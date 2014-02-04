"""
@file
@brief Download stock prices (from Yahoo website) and other prices
"""
import os, sys, re, urllib.request, urllib.error, datetime

class StockPrices:
    """
    defines a class containing stock prices, provides basic functions,
    the class uses `pandas <http://pandas.pydata.org/>`_ to load the data.
    
    Example:
    @code
    prices = StockPrices(tick = "BNP.PA")
    print (prices.dataframe.head())
    @endcode
    """
    
    def __init__(self, tick, url="yahoo", folder="cache",
                    begin = None, end = None): 
        """
        Loads a stock price from either a url or a folder where the data was cached.
        If a filename ``<folder>/<tick>.<day1>.<day2>.txt`` already exists, it takes it from here.
        Otherwise, it downloads it.
        
        If url is yahoo, the data will be download using ``http://finance.yahoo.com/q/cp?s=^FCHI+Components``.
        The CAC40 composition is described `here <http://fr.wikipedia.org/wiki/CAC_40>`_.
        
        @param      tick        tick name, ex: ``BNP.PA``
        @param      url         if yahoo, downloads the data from there if it was not done before
        @param      folder      cache folder (created if it does not exists
        @param      begin       first day (datetime), see below
        @param      end         last day (datetime), see below
        
        If begin is None, the date will 2000/01/03 (it seems Yahoo Finance does not provide
        prices for a date before this one).
        If end is None, the date will the date of yesterday.
        """
        import pandas

        if isinstance(url, pandas.DataFrame) :
            self.datadf = url
            self.tickname = tick
        else :

            if not os.path.exists(folder) :
                os.mkdir(folder)
            self.tickname = tick
            
            if begin == None : 
                begin = datetime.datetime(2000,1,3)
            if end == None :
                now = datetime.datetime.now()
                end = now - datetime.timedelta(1)
            
            sbeg = begin.strftime("%Y-%m-%d")
            send = end.strftime("%Y-%m-%d")
            name = os.path.join(folder, tick + ".{0}.{1}.txt".format(sbeg, send))
            
            if not os.path.exists (name) :
                if url == "yahoo" :
                    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d={0}&e={1}&f={2}&g=d&a={3}&b={4}&c={5}&ignore=.csv".format(
                                    end.month-1, end.day, end.year,
                                    begin.month-1,begin.day, begin.year)
                    url = url % tick
                else :
                    raise Exception("unable to download data from the following webiste " + url)
                
                try :
                    u = urllib.request.urlopen (url)
                    text = u.read ()
                    u.close ()
                except urllib.error.HTTPError as e :
                    raise Exception ("unable to load tick " + tick) from e
                
                if len(text) < 10 :
                    raise Exception("nothing to download for " + tick)
                        
                f = open (name, "wb")
                f.write(text)
                f.close ()
                
            self.datadf = pandas.read_csv(name, sep=",")
            
        self.datadf = self.datadf.sort("Date")
        self.datadf.reset_index(drop = True, inplace=True)
        self.datadf.set_index("Date", drop=False, inplace=True)
        
    @property
    def tick(self):
        """
        returns the tick name
        """
        return self.tickname
    
    @property
    def dataframe(self):
        """
        returns the dataframe
        """
        return self.datadf
        
    def FirstDate(self):
        """
        returns the first date
        """
        return self.datadf["Date"].min()

    def LastDate(self):
        """
        returns the first date
        """
        return self.datadf["Date"].max()
        
    def missing(self, trading_dates):
        """
        return the list of missing dates from an overset of trading dates
        
        @param      trading_dates       trading_dates (DataFrame having the column ``Date`` or in the index)
        @return                         missing dates (or None if issues)
        """
        import pandas
        
        da = self.dataframe["Date"]
        da2 = { v:1 for v in da }
        
        if isinstance(trading_dates, dict) :
            se = trading_dates
        else :
            se = trading_dates["Date"] if "Date" in trading_dates.columns else trading_dates.index
            
        tbl = [ { "Date":v } for v in se if v not in da2 ]
        if len(tbl) > 0 :
            df = pandas.DataFrame(tbl)
            return df.sort("Date")
        else :
            return None
        
    @staticmethod
    def available_dates ( listStockPrices, missing = True, field="Close") :
        """
        Returns the list of values (Open or High or Low or Close or Volumne) from each stock 
        for all the available_dates for a list of stock prices.
        
        A missing date is a date for which there is at least one stock price and one missing stock price.
        
        if ``missing`` is true a column is added which gives the number of missing stock prices for this dates
        
        @param      listStockPrices     list of StockPrices
        @param      missing             True or False
        @param      field               which field to use to fill the matrix
        @return                         matrix with the available dates for each stock
        """
        
        dates = []
        for st in listStockPrices :
            for row in st.dataframe.values :
                date = row[0]
                dates.append ( { "Date":date, "tick": st.tick, field:row[4] } )
        import pandas
        df = pandas.DataFrame(dates)
        piv = df.pivot("Date", "tick", field)
        
        if missing :
            import numpy
            def count_nan(row) :
                n = 0
                for k,v in row.items():
                    if k == "Date": continue
                    if numpy.isnan(v) : n+= 1
                return n
            piv ["missing"] = piv.apply( lambda row : count_nan(row), axis=1 )
        
        piv = piv.sort()
        return piv
        
    def head(self):
        """
        usual
        """
        return self.dataframe.head()
        
    def tail(self):
        """
        usual
        """
        return self.dataframe.tail()
        
    def keep_dates(self, trading_dates):
        """
        removes undesired dates
        
        @param      trading_dates   dates
        @return                     new series
        """
        import pandas
        
        da = self.dataframe["Date"]
        da2 = { v:1 for v in da }
        
        if isinstance(trading_dates, dict) :
            se = trading_dates
        else :
            se = trading_dates["Date"] if "Date" in trading_dates.columns else trading_dates.index
            
        tbl = { v:1 for v in se if v in da2 }
        if len(tbl) > 0 :
            ave = self.dataframe.apply(lambda row : row["Date"] in tbl, axis=1)
            return StockPrices( self.tickname, self.dataframe.ix[ ave ,: ] )
        else :
            raise Exception("no trading dates left")

    def returns(self):
        """
        builds the returns series
        
        @return     StockPrices
        """
        import numpy
        df    = self.dataframe
        fd    = self.FirstDate()
        ld    = self.LastDate()
        
        moins = df ["Date"] > fd
        plus  = df ["Date"] < ld
        
        res   = df.ix[plus , ["Date", "Volume"]]
        
        for k in ["Open", "High", "Low", "Close"] :
            m = numpy.array(df.ix[moins,"Close"])
            p = numpy.array(df.ix[plus,k])
            res[k] = (p - m) / m
            
        return StockPrices(self.tickname, res)
    
    @staticmethod
    def covariance(listStockPrices, missing = True, field="Close", cov = True, ret = False) :
        """
        computes the covariances matrix (of returns)
        
        @param      listStockPrices     list of StockPrices
        @param      field               which field to use to fill the matrix
        @param      cov                 if True, returns the covariance, otherwise, the correlations
        @param      ret                 if True, also add the returns
        @return                         square dataframe or 2 dataframe (returns, correlation)
        """
        
        listStockPrices = [ v.returns() for v in listStockPrices ]
        mat = StockPrices.available_dates (listStockPrices, False, field)
        import numpy, pandas
        npmat = numpy.matrix(mat)
        cov = numpy.cov (npmat.transpose()) if cov else numpy.corrcoef (npmat.transpose())
        names = [ v.tick for v in listStockPrices ]
        ret_mat = pandas.DataFrame (cov, columns = names, index = names)
        
        if ret :
            rows = [ {"tick":v.tick, "return": v.dataframe[field].mean() } for v in listStockPrices ]
            ret = pandas.DataFrame(rows)
            ret.set_index("tick", drop=True, inplace=True)
            return ret, ret_mat
        else :
            return ret_mat
            
    @staticmethod
    def draw(listStockPrices, begin = None, end = None, field="Close", date_format = '%Y') :
        """
        Draw a graph showing one or several time series.
        The example was taken `here <http://matplotlib.org/examples/api/date_demo.html>`_.
        
        @param      listStockPrices     list of @see cl StockPrice
        @param      begin               first date (datetime) or None to take the first one
        @param      end                 last included date (datetime) or None to take the last one
        @param      field               Open, High, Low, Close
        @param      date_format         ``%Y`` or ``%Y-%m`` or ``%Y-%m-%d``
        @return                         fig, ax, plt, (fig,ax) comes plt.subplot, plt is matplotlib.pyplot
        
        
        Example:
        @code
        stocks = [ StockPrices ("BNP.PA", folder = cache),
                    StockPrices ("CA.PA", folder = cache),
                    StockPrices ("SAN.PA", folder = cache),
                    ]
        fig, ax, plt = StockPrices.draw(stocks)
        fig.savefig("image.png")
        fig, ax, plt = StockPrices.draw(stocks, begin="2010-01-01")
        plt.show()  
        @endcode
        """
        data = StockPrices.available_dates(listStockPrices, missing = False, field = field)
        if begin == None :
            if end != None :
                data = data [ data.index <= end ]
        else :
            if end != None :
                data = data [ (data.index >= begin) &  (data.index <= end)]
            else :
                data = data [ data.index >= begin ]
                
        dates = [ datetime.datetime.strptime(_, '%Y-%m-%d') for _ in data.index ]
        begin = dates[0]
        end   = dates[-1]
        
        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates
        import matplotlib.cbook as cbook

        years    = mdates.YearLocator()   # every year
        months   = mdates.MonthLocator()  # every month
        yearsFmt = mdates.DateFormatter(date_format)
        def price(x): return '%1.2f'%x
        fig, ax = plt.subplots()
        
        curve = [ ]
        for stock in data.columns :
            curve.append ( ax.plot(dates, data[stock]) )

        ax.xaxis.set_major_locator(years)
        ax.xaxis.set_major_formatter(yearsFmt)
        ax.xaxis.set_minor_locator(months)
        ax.set_xlim(begin, end)
        ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        ax.format_ydata = price
        ax.grid(True)
        fig.autofmt_xdate()
        ax.legend( tuple(data.columns))
        return fig, ax, plt

