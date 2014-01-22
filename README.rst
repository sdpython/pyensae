.. _l-README:

README
======

.. contents::
   :depth: 3


Introduction
------------

This project contain helpers used at the `ENSAE <http://www.ensae.fr/>`_ for teaching purposes.
The project is hosted `here <http://www.xavierdupre.fr/site2013/index_code.html>`_ 
on github: `github/pyensae <https://github.com/sdpython/pyensae/>`_,
on pypi: `pypi/pyensae <https://pypi.python.org/pypi/pyensae/>`_.
It requires `github/pyquickhelper <https://github.com/sdpython/puquickhelper/>`_.

The main function is used to download data used for my teachings at the 
`ENSAE <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_
from the website `http://www.xavierdupre.fr/`_::

    download_data("td8_velib.zip", website = "xd")
    
The second functionality is the ability to import a text file into a SQLite database::

    import_flatfile_into_database("sqlitedb.db3", "flat_file.txt")
    
The last function is about getting stock prives from `Yahoo Finance <http://fr.finance.yahoo.com/>`_ ::

    stock = StockPrices( "BNP.PA", folder = "temp" )
    
    
Contributions
-------------

Started in 2013/08.

* First contributor: `Xavier Dupré <http://www.xavierdupre.fr/>`_.
* Others contributors: ENSAE's students.

