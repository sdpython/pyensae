"""
@file
@brief Download stock prices (from Yahoo website) and other prices
"""
import os
import urllib.request
import urllib.error
import datetime
import pandas
import numpy
from pyquickhelper.filehelper import is_file_string


class StockPricesException(Exception):
    """
    raised by StockPrices classes
    """
    pass


class StockPrices:

    """
    defines a class containing stock prices, provides basic functions,
    the class uses `pandas <http://pandas.pydata.org/>`_ to load the data.

    .. exref::
        :title: retrieve stock prices from the Yahoo source

        ::

            prices = StockPrices(tick = "NASDAQ:MSFT")
            print (prices.dataframe.head())
    """

    def __init__(self, tick, url="google", folder="cache",
                 begin=None, end=None, sep=",",
                 intern=False):
        """
        Loads a stock price from either a url or a folder where the data was cached.
        If a filename ``<folder>/<tick>.<day1>.<day2>.txt`` already exists, it takes it from here.
        Otherwise, it downloads it.

        If url is yahoo, the data will be download using ``http://finance.yahoo.com/q/cp?s=^FCHI+Components``.
        The CAC40 composition is described `here <http://fr.wikipedia.org/wiki/CAC_40>`_.
        However Yahoo introduced the use of cookies in May 2017 and it is not so easy to automate.
        The default provider will be *google*.
        Tick names depends on the data prodiver. More details:
        `European Markets Information <https://www.stockmarketeye.com/users-guide/ticker-symbols-and-data-providers/euro-stocks.html>`_.
        You can also go to `quandl <https://www.quandl.com/data/EURONEXT/BNP-Bnp-Paribas-Act-A-BNP>`_
        and get the tick for the module `quandl <https://www.quandl.com/tools/python>`_.

        @param      tick        tick name, ex ``NASDAQ:MSFT``
        @param      url         if yahoo, downloads the data from there if it was not done before
        @param      folder      cache folder (created if it does not exists
        @param      begin       first day (datetime), see below
        @param      end         last day (datetime), see below
        @param      sep         column separator
        @param      intern      do not use unless you know what to do (see :meth:`__getitem__ <pyensae.finance.astock.StockPrices.__getitem__>`)

        If begin is None, the date will 2000/01/03 (it seems Yahoo Finance does not provide
        prices for a date before this one).
        If end is None, the date will the date of yesterday.

        .. exref::
            :title: Compute the average returns and correlation matrix

            ::

                import pyensae, pandas
                from pyensae.finance.astock import StockPrices

                # download the CAC 40 composition from my website (for Yahoo)
                pyensae.download_data('cac40_2013_11_11.txt', website='xd')

                # download all the prices (if not already done) and store them into files
                actions = pandas.read_csv("cac40_2013_11_11.txt", sep="\t")

                # we remove stocks with not enough historical data
                stocks = { k:StockPrices(tick = k) for k,v in actions.values }
                dates = StockPrices.available_dates(stocks.values())
                stocks = {k:v for k,v in stocks.items() if len(v.missing(dates)) <= 10}
                print("nb left", len(stocks))

                # we remove dates with missing prices
                dates = StockPrices.available_dates(stocks.values())
                ok    = dates[dates["missing"] == 0]
                print("all dates before", len(dates), " after:" , len(ok))
                for k in stocks:
                    stocks[k] = stocks[k].keep_dates(ok)

                # we compute correlation matrix and returns
                ret, cor = StockPrices.covariance(stocks.values(), cov = False, ret = True)

        You should also look at `pyensae et notebook <http://www.xavierdupre.fr/blog/notebooks/example%20pyensae.html>`_.
        If you use Google Finance as a provider, the tick name is usually
        prefixed by the market places (NASDAQ for example). The export
        does not work for all markets places.

        """
        if isinstance(url, pandas.DataFrame):
            self.datadf = url
            self.tickname = tick
            if "Date" not in url.columns:
                raise Exception(
                    "the dataframe does not contain any column 'Date': {0}".format(
                        ",".join(
                            _ for _ in url.columns)))
        elif isinstance(tick, str) and is_file_string(tick) and os.path.exists(tick):
            with open(tick, "r") as f:
                for line in f.readlines():
                    if line.startswith('<!DOCTYPE html PUBLIC'):
                        raise Exception(
                            "pandas cannot parse the file, check your have access to internet: " + str(tick))
                    break
            try:
                self.datadf = pandas.read_csv(tick, sep=sep)
            except Exception as e:
                with open(tick, "r") as t:
                    content = t.read()
                if "Firewall Authentication" in content:
                    raise Exception(
                        "pandas cannot parse the file, check your have access to internet: " + str(tick)) from e
                else:
                    raise e
        else:
            if not os.path.exists(folder):
                try:
                    os.mkdir(folder)
                except PermissionError as e:
                    raise Exception(
                        "PermissionError, unable to create directory " +
                        folder +
                        ", check you execute the program in a folder you have permission to modify (" +
                        os.getcwd() +
                        ")") from e
            self.tickname = tick

            if begin is None:
                begin = datetime.datetime(2000, 1, 3)
            if end is None:
                now = datetime.datetime.now()
                end = now - datetime.timedelta(1)

            sbeg = begin.strftime("%Y-%m-%d")
            send = end.strftime("%Y-%m-%d")
            name = os.path.join(
                folder,
                tick.replace(":", "_").replace("/", "_").replace("\\", "_") +
                ".{0}.{1}.txt".format(
                    sbeg,
                    send))

            date_format = None
            if not os.path.exists(name):
                if url == "google":
                    use_url = True
                    url_string = "http://www.google.com/finance/historical?q={0}".format(
                        self.tickname)
                    url_string += "&startdate={0}&enddate={1}&output=csv".format(
                        begin.strftime('%b %d, %Y'), end.strftime('%b %d, %Y'))
                    url = url_string.replace(" ", "%20")
                    date_format = "%b-%d-%Y"
                elif url == "quandl":
                    import quandl
                    df = quandl.get(
                        "EURONEXT/BNP", start_date=begin.strftime('%Y-%m-%d'), end_date=end.strftime('%Y-%m-%d'))
                    df.reset_index(drop=False).to_csv(
                        name, sep=sep, index=False)
                    use_url = False
                elif url in("yahoo", "google", "fred", "famafrench"):
                    import pandas_datareader.data as web
                    df = web.DataReader(self.tickname, url,
                                        begin, end).reset_index(drop=False)
                    df.to_csv(name, sep=sep, index=False)
                    use_url = False
                else:
                    raise Exception(
                        "unable to download data from the following website" + str(tick) + " - " +
                        url)

                if use_url:
                    try:
                        u = urllib.request.urlopen(url)
                        text = u.read()
                        u.close()
                    except urllib.error.HTTPError as e:
                        raise Exception(
                            "HTTPError, unable to load tick " + tick + "\nURL: " + url) from e

                    if len(text) < 10:
                        raise Exception("nothing to download for " + tick +
                                        " less than 10 downloaded bytes")

                    try:
                        f = open(name, "wb")
                        f.write(text)
                        f.close()
                    except PermissionError as e:
                        raise Exception(
                            "PermissionError, unable to create directory " +
                            folder +
                            ", check you execute the program in a folder you have permission to modify (" +
                            os.getcwd() +
                            ")") from e

            try:
                self.datadf = pandas.read_csv(name, sep=sep)
            except Exception as e:
                with open(tick, "r") as t:
                    content = t.read()
                if "Firewall Authentication" in content:
                    raise Exception(
                        "pandas cannot parse the file, check your have access to internet" + str(tick)) from e
                else:
                    raise e

            if date_format is not None:
                self.datadf["Date"] = pandas.to_datetime(self.datadf["Date"])
                self.datadf["Date"] = self.datadf["Date"].apply(
                    lambda x: x.strftime('%Y-%m-%d'))
                self.datadf.to_csv(name, sep=sep, index=False)

        if not intern:
            try:
                self.datadf = self.datadf.sort_values("Date")
            except AttributeError:
                self.datadf = self.datadf.sort("Date")
            except KeyError as e:
                raise StockPricesException("schema: {}".format(
                    ",".join(self.datadf.columns))) from e
            self.datadf.reset_index(drop=True, inplace=True)
            self.datadf.set_index("Date", drop=False, inplace=True)

    def __getitem__(self, key):
        """
        overloads the ``getitem`` operator to get a StockPrice object

        @param      key     key
        @return             StockPrice
        """
        return StockPrices(
            self.tick, self.datadf.__getitem__(key), intern=True)

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

    def df(self):
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
        da2 = {v: 1 for v in da}

        if isinstance(trading_dates, dict):
            se = trading_dates
        else:
            se = trading_dates[
                "Date"] if "Date" in trading_dates.columns else trading_dates.index

        tbl = [{"Date": v} for v in se if v not in da2]
        if len(tbl) > 0:
            df = pandas.DataFrame(tbl)
            try:
                return df.sort_values("Date")
            except AttributeError:
                return df.sort("Date")
        else:
            return None

    @staticmethod
    def available_dates(listStockPrices, missing=True, field="Close"):
        """
        Returns the list of values (Open or High or Low or Close or Volume) from each stock
        for all the available_dates for a list of stock prices.

        A missing date is a date for which there is at least one stock price and one missing stock price.

        if ``missing`` is true a column is added which gives the number of missing stock prices for this dates

        @param      listStockPrices     list of StockPrices
        @param      missing             True or False
        @param      field               which field to use to fill the matrix
        @return                         matrix with the available dates for each stock
        """
        if field == "ohlc":
            field = ["Open", "High", "Low", "Close"]
        dates = []
        if isinstance(field, str):
            for st in listStockPrices:
                lifi = list(st.dataframe.columns)
                index = lifi.index(field)
                for row in st.dataframe.values:
                    date = row[0]
                    dates.append(
                        {"Date": date, "tick": st.tick, field: row[index]})
        elif isinstance(field, tuple) or isinstance(field, list):
            for st in listStockPrices:
                lifi = list(st.dataframe.columns)
                indexes = [lifi.index(f) for f in field]
                for row in st.dataframe.values:
                    date = row[0]
                    r = {"Date": date, "tick": st.tick, }
                    for i, f in zip(indexes, field):
                        r[f] = row[i]
                    dates.append(r)
        else:
            raise TypeError("field must be a string, a tuple or a list")

        df = pandas.DataFrame(dates)
        if isinstance(field, str):
            piv = df.pivot("Date", "tick", field)
        elif isinstance(field, tuple) or isinstance(field, list):
            pivs = [df.pivot("Date", "tick", f) for f in field]
            for fi, piv in zip(field, pivs):
                col = [c + "," + fi for c in piv.columns]
                piv.columns = col
            if len(pivs) == 1:
                piv = pivs[0]
            else:
                piv = pivs[0].merge(pivs[1], how="outer",
                                    left_index=True, right_index=True)
                for p in pivs[2:]:
                    piv = piv.merge(
                        p, how="outer", left_index=True, right_index=True)
        else:
            raise TypeError("field must be a string, a tuple or a list")

        if missing:
            def count_nan(row):
                n = 0
                for k, v in row.items():
                    if k == "Date":
                        continue
                    if numpy.isnan(v):
                        n += 1
                return n
            piv["missing"] = piv.apply(lambda row: count_nan(row), axis=1)

        try:
            piv = piv.sort_index()
        except AttributeError:
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
        da2 = {v: 1 for v in da}

        if isinstance(trading_dates, dict):
            se = trading_dates
        else:
            se = trading_dates[
                "Date"] if "Date" in trading_dates.columns else trading_dates.index

        tbl = {v: 1 for v in se if v in da2}
        if len(tbl) > 0:
            ave = self.dataframe.apply(lambda row: row["Date"] in tbl, axis=1)
            return StockPrices(self.tickname, self.dataframe.loc[ave, :])
        else:
            raise Exception("no trading dates left")

    def returns(self):
        """
        builds the returns series

        @param      col     column to use to compute the returns
        @return             StockPrices
        """
        df = self.dataframe
        fd = self.FirstDate()
        ld = self.LastDate()

        plus = df["Date"] > fd    # dates from FirstDate+1 to LastDate
        moins = df["Date"] < ld    # dates from FirstDate to LastDate-1

        res = df.loc[plus, ["Date", "Volume"]]

        for k in df.columns:
            if k in ["Date", "Volume"]:
                continue
            m = numpy.array(df.loc[moins, k])
            p = numpy.array(df.loc[plus, k])
            res[k] = (p - m) / m

        return StockPrices(self.tickname, res)

    @staticmethod
    def covariance(
            listStockPrices, missing=True, field="Close", cov=True, ret=False):
        """
        computes the covariances matrix (of returns)

        @param      listStockPrices     list of StockPrices
        @param      field               which field to use to fill the matrix
        @param      cov                 if True, returns the covariance, otherwise, the correlations
        @param      ret                 if True, also add the returns
        @return                         square dataframe or 2 dataframe (returns, correlation)
        """
        listStockPrices = [v.returns() for v in listStockPrices]
        mat = StockPrices.available_dates(listStockPrices, False, field)

        npmat = numpy.matrix(mat)
        cov = numpy.cov(
            npmat.transpose()) if cov else numpy.corrcoef(
            npmat.transpose())
        names = [v.tick for v in listStockPrices]
        ret_mat = pandas.DataFrame(cov, columns=names, index=names)

        if ret:
            rows = [{"tick": v.tick, "return": v.dataframe[field].mean()}
                    for v in listStockPrices]
            ret = pandas.DataFrame(rows)
            ret.set_index("tick", drop=True, inplace=True)
            return ret, ret_mat
        else:
            return ret_mat

    def plot(self, begin=None, end=None,
             field="Close", date_format=None,
             existing=None, axis=1, ax=None,
             **args):
        """
        see :meth:`draw <pyensae.finance.astock.StockPrices.draw>`
        """
        return StockPrices.draw(self, begin=begin, end=end,
                                field=field, date_format=date_format,
                                existing=existing, axis=axis, ax=ax, **args)

    @staticmethod
    def draw(listStockPrices, begin=None, end=None,
             field="Close", date_format=None,
             existing=None, axis=1, ax=None,
             **args):
        """
        Draw a graph showing one or several time series.
        The example was taken `here <http://matplotlib.org/examples/api/date_demo.html>`_.

        @param      listStockPrices     list of @see cl StockPrices (or one @see cl StockPrices if it is the only one)
        @param      begin               first date (datetime) or None to take the first one
        @param      end                 last included date (datetime) or None to take the last one
        @param      field               Open, High, Low, Close, Adj Close, Volume
        @param      date_format         ``%Y`` or ``%Y-%m`` or ``%Y-%m-%d`` or None if you prefer the function to choose
        @param      args                other arguments to send to ``plt.subplots``
        @param      axis                1 or 2, it only works if existing != None. If axis is 2, the function draws the curves on the second axis.
        @param      args                other parameters to give method ``plt.subplots``
        @param      ax                  use existing `axes <http://matplotlib.org/api/axes_api.html>`_
        @return     fig, ax, plt        `axes <http://matplotlib.org/api/axes_api.html>`_

        The parameter ``figsize`` of the method `subplots <http://matplotlib.org/api/pyplot_api.html?highlight=subplots#matplotlib.pyplot.subplots>`_
        can change the graph size (see the example below).

        .. exref::
            :title: graph of a financial series

            ::

                stocks = [ StockPrices ("NASDAQ:MSFT", folder = cache),
                           StockPrices ("NASDAQ:GOOGL", folder = cache),
                           StockPrices ("NASDAQ:AAPL", folder = cache)]
                fig, ax, plt = StockPrices.draw(stocks)
                fig.savefig("image.png")
                fig, ax, plt = StockPrices.draw(stocks, begin="2010-01-01", figsize=(16,8))
                plt.show()

            You can also chain the graphs and add a series on a second graph:

            ::

                stock = StockPrices ("NASDAQ:MSFT", folder = cache)
                stock2 = StockPrices ("NASDAQ:GOOGL", folder = cache)
                fig, ax, plt = stock.plot(figsize=(16,8))
                fig, ax, plt = stock2.plot(existing=(fig,ax), axis=2)
                plt.show()

        .. versionchanged:: 1.1
            Parameter *existing* was removed and parameter *ax* was added.
            If the date overlaps, the method
            `autofmt_xdate <http://matplotlib.org/api/figure_api.html#matplotlib.figure.Figure.autofmt_xdate>`_
            should be called.
        """
        if isinstance(listStockPrices, StockPrices):
            listStockPrices = [listStockPrices]

        data = StockPrices.available_dates(
            listStockPrices, missing=False, field=field)
        if begin is None:
            if end is not None:
                data = data[data.index <= end]
        else:
            if end is not None:
                data = data[(data.index >= begin) & (data.index <= end)]
            else:
                data = data[data.index >= begin]

        dates = [datetime.datetime.strptime(_, '%Y-%m-%d') for _ in data.index]
        begin = dates[0]
        end = dates[-1]

        def price(x):
            return '%1.2f' % x

        import matplotlib.pyplot as plt
        import matplotlib.dates as mdates

        if ax is not None:
            ex_h, ex_l = ax.get_legend_handles_labels()
            ex_l = tuple(ex_l)
            ex_h = tuple(ex_h)
            if axis == 2:
                ax = ax.twinx()
            fig = None
        else:
            fig, ax = plt.subplots(**args)
            ex_h, ex_l = tuple(), tuple()

        curve = []
        if field == "ohlc":
            from matplotlib.finance import candlestick_ohlc
            ohlc = list(list(data.iloc[i, :4])
                        for i in range(0, data.shape[0]))
            ohlc = [[mdates.date2num(t)] + v for t, v in zip(dates, ohlc)]
            candlestick_ohlc(ax, ohlc, colorup="g")
        else:
            for stock in data.columns:
                if axis == 2:
                    curve.append(
                        ax.plot(dates, data[stock], "r", linestyle='solid', label=str(stock)))
                else:
                    curve.append(
                        ax.plot(dates, data[stock], linestyle='solid', label=str(stock)))

        if existing is None:
            ax.format_xdata = mdates.DateFormatter('%Y-%m-%d')
            if len(dates) < 30:
                days = mdates.DayLocator()
                ax.xaxis.set_major_locator(days)
                ax.xaxis.set_minor_locator(days)
                if date_format is not None:
                    fmt = mdates.DateFormatter(date_format)
                    ax.xaxis.set_major_formatter(fmt)
                else:
                    ax.xaxis.set_major_formatter(
                        mdates.DateFormatter("%Y-%m-%d"))
            elif len(dates) < 500:
                months = mdates.MonthLocator()
                days = mdates.DayLocator()
                ax.xaxis.set_major_locator(months)
                ax.xaxis.set_minor_locator(days)
                ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
                if date_format is not None:
                    fmt = mdates.DateFormatter(date_format)
                    ax.xaxis.set_major_formatter(fmt)
                else:
                    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
            else:
                years = mdates.YearLocator()
                months = mdates.MonthLocator()
                ax.xaxis.set_major_locator(years)
                ax.xaxis.set_minor_locator(months)
                if date_format is not None:
                    fmt = mdates.DateFormatter(date_format)
                    ax.xaxis.set_major_formatter(fmt)
                else:
                    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))

        ax.set_xlim(begin, end)
        ax.format_ydata = price
        if fig is not None:
            fig.autofmt_xdate()

        if axis == 2:
            if isinstance(curve, list):
                curve = [_[0] for _ in curve]
            ax.legend(ex_h + tuple(curve), ex_l + tuple(data.columns))
        else:
            ax.grid(True)
            ax.legend(ex_l + tuple(data.columns))

        return fig, ax, plt

    def to_csv(self, filename, sep="\t", index=False, **params):
        """
        saves the file in text format
        see `to_csv <http://pandas.pydata.org/pandas-docs/version/0.13.1/generated/pandas.DataFrame.to_csv.html>`_

        @param      filename        filename
        @param      sep             separator
        @param      index           to keep or drop the index
        @param      params          other parameters
        """
        self.dataframe.to_csv(filename, sep=sep, index=index, **params)

    def to_excel(self, excel_writer, **params):
        """
        saves the file in Excel format,
        see `to_excel <http://pandas.pydata.org/pandas-docs/version/0.13.1/generated/pandas.DataFrame.to_excel.html>`_
        """
        self.dataframe.to_excel(excel_writer, **params)
