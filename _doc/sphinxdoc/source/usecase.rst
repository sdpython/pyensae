.. _l-usecase:

Use case
========

.. contents::
   :depth: 3
    
    
    
Resources for teachings
-----------------------

Download data for a practical lesson
++++++++++++++++++++++++++++++++++++

::

    from pyensae import download_data
    download_data('voeux.zip', website = 'xd')
    
see :py:func:`download_data <resources.http_retrieve.download_data>`


SQLite
------

Import a flat file into a SQLite database
+++++++++++++++++++++++++++++++++++++++++

::

    from pyensae import import_flatfile_into_database
    dbf = "database.db3"
    file = "textfile.txt"
    import_flatfile_into_database(dbf, file)

see :py:func:`import_flatfile_into_database <sql.database_helper.import_flatfile_into_database>`


Export the results of a SQL query into a flat file
++++++++++++++++++++++++++++++++++++++++++++++++++

::

    from pyensae.sql.database_main import Database
    dbfile = "filename.db3"
    filetxt = "fileview.txt"
    sql = "..."
    db = Database(dbfile)
    db.connect()
    db.export_view_into_flat_file (sql, fileview, header = True)
    db.close()
    
see :py:func:`Database <sql.database_main.Database>`

Finance
-------

Compute the average returns and correlation matrix
++++++++++++++++++++++++++++++++++++++++++++++++++

::

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

see :py:class:`StockPrices <finance.astock.StockPrices>`.

