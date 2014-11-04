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

The :class:`ASSHClient <pyensae.remote.remote_connection.ASSClient>` requires:
    * `paramiko <http://www.paramiko.org/>`_
    * `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_
    * `ecdsa <https://pypi.python.org/pypi/ecdsa>`_
    

Contributions
-------------

Started in 2013/08.

* First contributor: `Xavier Dupré <http://www.xavierdupre.fr/>`_.
* Others contributors: ENSAE's students.

Versions
--------

* **0.9.1 - 2014/??/??**
    * **add:** add magic command ``%tail_stderr`` for azure
* **0.9 - 2014/11/03**
    * **add:** Python version is now checked, ImportError is raised if it used on Python 2
    * **add:** option -local to %jobsubmit    
    * **add:** add magic command and methods to enable a shell from a notebook (a kind of putty) (command ``%open_remove_shell``, ...)
    * **new:** function :func:`parse_code <pyensae.languages.antlr_grammar_use.parse_code>` parses a script in R, PIG, SQLite syntax and checks if there is any mistake, it requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_
    * **new:** new class :class:`AzureClient <pyensae.remote.azure_connection.AzureClient>` to handle some basic needs with Azure
    * **add:** add magic command and methods to handle Azure from a notebook
* **0.8 - 2014/10/24**
    * **add:** add method :meth:`copy_to <pyensae.sql.database_main.Database.copy_to>` to copy every table from a database to another one
    * **fix:** class :class:`Database <pyensae.sql.database_main.Database>` can now handle in memory database
    * **add:** functions to decompress files, see :mod:`decompress_helper <pyensae.decompress_helper>`
    * **change:** function `download_data <pyensae.resources.http_retrieve.download_data>` now works with files .zip, .gz, .tar.gz
    * **new:** add class :class:`ASSHClient <pyensae.remote.remote_connection.ASSClient>` to communicate with a remote SSH connection 
      (it uses `paramiko <http://www.paramiko.org/>`_)
    * **new:** add magic command to use :class:`ASSHClient <pyensae.remote.remote_connection.ASSClient>` in a notebook (``%remote_open``, ...)
* **0.7 - 2014/08/24**
    * **fix:** fix an unexpected zero length column in :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`
    * **add:** add parameter ``add_key`` to function :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>` to add a primary key
    * **fix:** improve behavior of :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`, it is more robust to not so clean flat files
