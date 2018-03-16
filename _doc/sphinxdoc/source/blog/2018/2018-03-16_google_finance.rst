
.. blogpost::
    :title: Google Finance stopped delivering historical data
    :keywords: module, pyenbc
    :date: 2018-03-16
    :categories: module

    After :epkg:`Yahoo Finance <https://finance.yahoo.com/>`_
    made it more difficult to access historical data,
    `Google Finance <https://finance.google.com/finance/historical>`_
    stopped giving historical data. So you should see the
    following error message:

    .. runpython::
        :showcode:

        try:
            from src.pyensae.finance.astock import StockPrices
            stock = StockPrices("NASDAQ:MSFT", folder=cache,
                                begin=datetime.datetime(2018, 3, 10))
            print(stock)
        except Exception as e:
            print(e)
