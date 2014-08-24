pyensae documentation
=====================

   
   
**Links:**
    * `pypi/pyensae <https://pypi.python.org/pypi/pyensae/>`_
    * `GitHub/pyensae <https://github.com/sdpython/pyensae/>`_
    * `documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pyensae>`_


Description        
-----------

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_ for teaching purposes.
It requires `github/pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_.

The main function is used to download data used for my teachings at the 
`ENSAE <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_
from the website `xavierdupre.fr <http://www.xavierdupre.fr/>`_::

    download_data("td8_velib.zip", website = "xd")
    
The second functionality is the ability to import a text file into a SQLite database::

    import_flatfile_into_database("sqlitedb.db3", "flat_file.txt")
    
The last function is about getting stock prives from `Yahoo Finance <http://fr.finance.yahoo.com/>`_ ::

    stock = StockPrices( "BNP.PA", folder = "temp" )
    
To draw a graph with multiple stock prices::

    stocks = [ StockPrices ("BNP.PA", folder = cache),
                StockPrices ("CA.PA", folder = cache),
                StockPrices ("SAN.PA", folder = cache),
                ]
    fig, ax, plt = StockPrices.draw(stocks)
    fig.savefig("image.png")
    
    # or 
    
    fig, ax, plt = StockPrices.draw(stocks, begin="2010-01-01")
    plt.show()  
    
    
Functionalities
---------------

* retrieve data for practical lessons
* import a text file into a database
* retrieve stock prices from Yahoo Finance

Dependencies
------------

* `numpy <http://www.numpy.org/>`_
* `pandas <http://pandas.pydata.org/>`_
* `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper>`_

For the class :class:`StockPrices <finance.astock.StockPrices>`:
    * `dateutil <https://pypi.python.org/pypi/python-dateutil>`_
    * `six <https://pypi.python.org/pypi/six>`_

On Windows, most of the intersting modules can installed from `here <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.


Indices and tables
==================

+------------------+---------------------+---------------------+------------------+------------------------+---------------------+
| :ref:`l-modules` |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods` | :ref:`l-staticmethods` | :ref:`l-properties` |
+------------------+---------------------+---------------------+------------------+------------------------+---------------------+
| :ref:`genindex`  |  :ref:`modindex`    | :ref:`search`       | :ref:`l-license` | :ref:`l-changes`       | :ref:`l-README`     |
+------------------+---------------------+---------------------+------------------+------------------------+---------------------+
| :ref:`l-example` |  :ref:`l-FAQ`       | :ref:`l-notebooks`  |                  |                        |                     |
+------------------+---------------------+---------------------+------------------+------------------------+---------------------+

Navigation
==========

.. toctree::
    :maxdepth: 1

    doctestunit
    generatedoc
    generatesetup
    installation
    all_example
    all_FAQ
    all_notebooks
    glossary
    index_module
    license
    filechanges
    README
    all_indexes

    
