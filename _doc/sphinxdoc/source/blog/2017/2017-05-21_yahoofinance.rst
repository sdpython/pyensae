
.. blogpost::
    :title: Yahoo finance needs cookie
    :keywords: yahoo finance, quandl, google finance, cookie
    :date: 2017-05-21
    :categories: finance
    :lid: blog-yahoo-finance-201711

    `Yahoo Finance <https://finance.yahoo.com/quote/BNPQY/history?p=BNPQY>`_
    now requires cookies to download the data and it becomes
    difficult to automate the downloading of historical data.
    I had to change the default provider to
    `Google <https://www.google.com/finance>`_. However, it is not
    possible to get historical prices for European markets.
    For these one,
    `quandl <https://www.quandl.com/data/EURONEXT/BNP-Bnp-Paribas-Act-A-BNP>`_
    seems to be the best alternative as there is a dedicated module
    to get the data
    `quandl <https://www.quandl.com/tools/python>`_. However, historical
    data do not get as far as Google's.
    See :class:`StockPrices <pyensae.finance.astock.StockPrices>`.
