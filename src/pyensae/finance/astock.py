"""
@file
@brief Download stock prices (from Yahoo website) and other prices
"""
import os, urllib.request, urllib.error, datetime
import pandas, numpy
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


class StockPrices:
    """
    defines a class containing stock prices, provides basic functions,
    the class uses `pandas <http://pandas.pydata.org/>`_ to load the data.
    
    @example(retrieve stock prices from the Yahoo source)
    @code
    prices = StockPrices(tick = "BNP.PA")
    print (prices.dataframe.head())
    @endcode
    @endexample
    """
    
    def __init__(self, tick, url="yahoo", folder="cache",
                begin = None, end = None, sep = ",", 
                intern=False): 
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
        @param      sep         column separator
        @param      intern      do not use unless you know what to do (@see me __getitem__)
        
        If begin is None, the date will 2000/01/03 (it seems Yahoo Finance does not provide
        prices for a date before this one).
        If end is None, the date will the date of yesterday.
        
        @example(Compute the average returns and correlation matrix)
        @code
        import pyensae, pandas
        from pyensae import StockPrices

        # download the CAC 40 composition from my website
        pyensae.download_data('cac40_2013_11_11.txt', website = 'xd')

        # download all the prices (if not already done) and store them into files
        actions = pandas.read_csv("cac40_2013_11_11.txt", sep = "\t")

        # we remove stocks with not enough historical data
        stocks = { k:StockPrices(tick = k) for k,v in actions.values  if k != "SOLB.PA"}
        dates = StockPrices.available_dates( stocks.values() )
        stocks = { k:v for k,v in stocks.items() if len(v.missing(dates)) <= 10 }
        print ("nb left", len(stocks))

        # we remove dates with missing prices
        dates = StockPrices.available_dates( stocks.values() )
        ok    = dates[ dates["missing"] == 0 ]
        print ("all dates before", len(dates), " after:" , len(ok))
        for k in stocks : stocks[k] = stocks[k].keep_dates(ok)

        # we compute correlation matrix and returns
        ret, cor = StockPrices.covariance(stocks.values(), cov = False, ret = True)
        @endcode
        @endexample
        
        You should also look at `pyensae et notebook <http://www.xavierdupre.fr/blog/notebooks/example%20pyensae.html>`_.
    
        """
        if isinstance(url, pandas.DataFrame) :
            self.datadf = url
            self.tickname = tick
        elif isinstance(tick, str) and os.path.exists(tick):
            try:
                self.datadf = pandas.read_csv(tick, sep=sep)
            except Exception as e :
                with open(tick,"r") as t : content = t.read()
                if "Firewall Authentication" in content :
                    raise Exception("pandas cannot parse the file, check your have access to internet") from e
                else :
                    raise e
        else :
            if not os.path.exists(folder) :
                try:
                    os.mkdir(folder)
                except PermissionError as e :
                    raise Exception("unable to create directory " + folder + ", check you execute the program in a folder you have permission to modify (" + os.getcwd() + ")")
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
                       
                try:
                    f = open (name, "wb")
                    f.write(text)
                    f.close ()
                except PermissionError as e :
                    raise Exception("unable to create directory " + folder + ", check you execute the program in a folder you have permission to modify (" + os.getcwd() + ")")
                
            try:
                self.datadf = pandas.read_csv(name, sep=sep)
            except Exception as e :
                with open(tick,"r") as t : content = t.read()
                if "Firewall Authentication" in content :
                    raise Exception("pandas cannot parse the file, check your have access to internet") from e
                else :
                    raise e
            
        if not intern:
            self.datadf = self.datadf.sort("Date")
            self.datadf.reset_index(drop = True, inplace=True)
            self.datadf.set_index("Date", drop=False, inplace=True)
        
    def __getitem__(self, key):
        """
        overloads the ``getitem`` operator to get a StockPrice object
        
        @param      key     key
        @return             StockPrice
        """
        return StockPrices(self.tick, self.datadf.__getitem__(key), intern=True)
        
    def __len__(self):
        """
        @return     number of observations
        """
        return len(self.datadf)
        
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
        if isinstance(field,str):
            for st in listStockPrices :
                lifi = list(st.dataframe.columns)
                index = lifi.index(field)
                for row in st.dataframe.values :
                    date = row[0]
                    dates.append ( { "Date":date, "tick": st.tick, field:row[index] } )
        elif isinstance(field, tuple) or isinstance(field, list):
            for st in listStockPrices :
                lifi = list(st.dataframe.columns)
                indexes = [ lifi.index(f) for f in field ]
                for row in st.dataframe.values :
                    date = row[0]
                    r = { "Date":date, "tick": st.tick, } 
                    for i,f in zip(indexes,field) : r[f] = row[i]
                    dates.append(r)
        else :
            raise TypeError("field must be a string, a tuple or a list")

        df = pandas.DataFrame(dates)
        if isinstance(field,str):
            piv = df.pivot("Date", "tick", field)
        elif isinstance(field, tuple) or isinstance(field, list):
            pivs = [ df.pivot("Date", "tick", f) for f in field ]
            for fi,piv in zip(field,pivs):
                col = [ c + "," + fi for c in piv.columns ]
                piv.columns = col
            if len(pivs)==1: piv = pivs[0]
            else :
                piv = pivs[0].merge(pivs[1],how="outer", left_index=True, right_index=True)
                for p in pivs[2:]:
                    piv = piv.merge(p,how="outer", left_index=True, right_index=True)
        else :
            raise TypeError("field must be a string, a tuple or a list")
        
        if missing :
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
    def draw(listStockPrices, begin = None, end = None, 
                field="Close", date_format = None,
                **args) :
        """
        Draw a graph showing one or several time series.
        The example was taken `here <http://matplotlib.org/examples/api/date_demo.html>`_.
        
        @param      listStockPrices     list of @see cl StockPrice (or one @see cl StockPrice if it is the only one)
        @param      begin               first date (datetime) or None to take the first one
        @param      end                 last included date (datetime) or None to take the last one
        @param      field               Open, High, Low, Close, Adj Close, Volumne
        @param      date_format         ``%Y`` or ``%Y-%m`` or ``%Y-%m-%d`` or None if you prefer the function to choose
        @param      args                others arugments to send to ``plt.subplots``
        @return                         fig, ax, plt, (fig,ax) comes plt.subplot, plt is matplotlib.pyplot
        
        The parameter ``figsize`` of the method `subplots <http://matplotlib.org/api/pyplot_api.html?highlight=subplots#matplotlib.pyplot.subplots>`_
        can change the graph size (see the example below).
        
        @example(graph of a financial series)
        @code
        stocks = [ StockPrices ("BNP.PA", folder = cache),
                    StockPrices ("CA.PA", folder = cache),
                    StockPrices ("SAN.PA", folder = cache),
                    ]
        fig, ax, plt = StockPrices.draw(stocks)
        fig.savefig("image.png")
        fig, ax, plt = StockPrices.draw(stocks, begin="2010-01-01", figsize=(16,8))
        plt.show()  
        @endcode
        @endexample
        """
        if isinstance(listStockPrices, StockPrices):
            listStockPrices = [ listStockPrices ]
        
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
        
        def price(x): return '%1.2f'%x
        fig, ax = plt.subplots(**args)
        
        curve = [ ]
        for stock in data.columns :
            curve.append ( ax.plot(dates, data[stock], linestyle='solid') )
            
        ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
        if len(dates) < 30:
            days     = mdates.DayLocator()
            ax.xaxis.set_major_locator(days)
            ax.xaxis.set_minor_locator(days)
            if date_format != None :
                fmt = mdates.DateFormatter(date_format)
                ax.xaxis.set_major_formatter(fmt)
            else :
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d"))
        elif len(dates) < 500:
            months   = mdates.MonthLocator() 
            days     = mdates.DayLocator()
            ax.xaxis.set_major_locator(months)
            ax.xaxis.set_minor_locator(days)
            ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
            if date_format != None :
                fmt = mdates.DateFormatter(date_format)
                ax.xaxis.set_major_formatter(fmt)
            else :
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
        else :
            years    = mdates.YearLocator() 
            months   = mdates.MonthLocator()
            ax.xaxis.set_major_locator(years)
            ax.xaxis.set_minor_locator(months)
            if date_format != None :
                fmt = mdates.DateFormatter(date_format)
                ax.xaxis.set_major_formatter(fmt)
            else :
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
            
        ax.set_xlim(begin, end)
        ax.format_ydata = price
        ax.grid(True)
        fig.autofmt_xdate()
        ax.legend( tuple(data.columns))
        return fig, ax, plt

