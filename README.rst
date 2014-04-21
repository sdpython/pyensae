
.. _l-README:

README
======

   
**Links:**
    * `pypi/pyensae <https://pypi.python.org/pypi/pyensae/>`_
    * `GitHub/pyensae <https://github.com/sdpython/pyensae/>`_
    * `documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pyensae>`_


Description        
-----------

This project contain helpers used at the `ENSAE <http://www.ensae.fr/>`_ for teaching purposes.
The project is hosted `here <http://www.xavierdupre.fr/site2013/index_code.html>`_ 
on github: `github/pyensae <https://github.com/sdpython/pyensae/>`_,
on pypi: `pypi/pyensae <https://pypi.python.org/pypi/pyensae/>`_.
It requires `github/pyquickhelper <https://github.com/sdpython/puquickhelper/>`_.

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
                StockPrices ("SAN.PA", folder = cache), ]
    fig, ax, plt = StockPrices.draw(stocks)
    fig.savefig("image.png")
    
    # or 
    
    fig, ax, plt = StockPrices.draw(stocks, begin="2010-01-01")
    plt.show()  

    
Dependencies
------------

* `numpy <http://www.numpy.org/>`_
* `pandas <http://pandas.pydata.org/>`_
* `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper>`_

For the class :class:`StockPrices <finance.astock.StockPrices>`:
    * `dateutil <https://pypi.python.org/pypi/python-dateutil>`_
    * `six <https://pypi.python.org/pypi/six>`_

On Windows, most of the interesting modules can installed from `here <http://www.lfd.uci.edu/~gohlke/pythonlibs/>`_.


Contributions
-------------

Started in 2013/08.

* First contributor: `Xavier Dupré <http://www.xavierdupre.fr/>`_.
* Others contributors: ENSAE's students.

Versions
--------


* **v0.6 - 2014/??/??**
    * **new:** convert a DataFrame into a SQLite3 database and the other way, see :meth:`to_df <sql.database_main.Database.to_df>`
* **v0.5 - 2014/04/20**
    * **new:** add notebooks to the documentation
    * **new:** add function :meth:`to_excel <finance.astock.StockPrices.to_excel>` to StockPrices
    * **new:** add method :meth:`plot <finance.astock.StockPrices.plot>` which calls method :meth:`plot <finance.astock.StockPrices.draw>` but is not static
    * **change:** method :meth:`draw <finance.astock.StockPrices.draw>` can now draw another series on a second axis
* **v0.4 - 2014/04/05**
    * **change:** the method :meth:`finance.astock.StockPrices.draw` works now with others fields than ``Close``, it also works with two fields in a list, see `pyensae et notebook <http://www.xavierdupre.fr/blog/notebooks/example%20pyensae.html>`_
    * **change:** the method :meth:`finance.astock.StockPrices.draw` does better with dates
    * **new:** the class :class:`finance.astock.StockPrices` overloads operator ``__getitem__``, see `pyensae et notebook <http://www.xavierdupre.fr/blog/notebooks/example%20pyensae.html>`_
    
    

