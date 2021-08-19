pyensae documentation
=====================

.. image:: https://travis-ci.com/sdpython/pyensae.svg?branch=master
    :target: https://travis-ci.com/sdpython/pyensae
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/jioxwx1igwbqwa28?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyensae
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pyensae/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pyensae/tree/master

.. image:: https://badge.fury.io/py/pyensae.svg
    :target: https://pypi.org/project/pyensae/

.. image:: http://img.shields.io/github/issues/sdpython/pyensae.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyensae/issues

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/pyensae/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyensae?branch=master

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/pyensae/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

.. image:: https://pepy.tech/badge/pyensae/month
    :target: https://pepy.tech/project/pyensae/month
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/pyensae.svg
    :target: https://github.com/sdpython/pyensae/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/pyensae.svg
    :target: https://github.com/sdpython/pyensae/
    :alt: Stars

**Links:** `pypi <https://pypi.python.org/pypi/pyensae/>`_,
`github <https://github.com/sdpython/pyensae/>`_,
`documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#pyensae>`_,
`travis <https://travis-ci.com/sdpython/pyensae>`_,
:ref:`l-README`,
:ref:`blog <ap-main-0>`,
:ref:`l-issues-todolist`

What is it?
-----------

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_
for teaching purposes but not only.
It requires `github/pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_.

Data used for teachings at the
`ENSAE <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_
are available through function::

    download_data("td8_velib.zip", website = "xd")

The data comes from `xavierdupre.fr <http://www.xavierdupre.fr/>`_.
The module also implements magic commands
to run SQL queries on `SQLite <https://sqlite.org/>`_,
parsing financial data from `Google Finance <https://finance.google.com/finance>`_.

Galleries and examples
----------------------

.. toctree::
    :maxdepth: 1

    api/index
    i_ex
    i_nb
    i_cmd
    i_faq
    gyexamples/index
    all_notebooks
    blog/blogindex
    HISTORY

Functionalities
---------------

* retrieve data for practical lessons (see :func:`download_data <pyensae.datasource.http_retrieve.download_data>`)
* import a tsv file into a database (see :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`)
* retrieve stock prices from Yahoo Finance (see :class:`StockPrices <pyensae.finance.astock.StockPrices>`)

The magic commands will be automatically enabled if the module is imported from a notebook.
It also proposes others magic commands such as ``%head``, ``%tail``, ``%textdiff``,
``%hhelp``, ``%runpy``, ``%lsr``, ``%compress``. Type ``<magic_command> -h``
to get their usage.

Navigation
----------

.. toctree::
    :maxdepth: 1

    indexmenu

+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`l-modules`       |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods`   | :ref:`l-staticmethods` | :ref:`l-properties`                            |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`modindex`        |  :ref:`l-EX2`       | :ref:`search`       | :ref:`l-license`   | :ref:`l-changes`       | :ref:`l-README`                                |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
| :ref:`API <genindex>`  |  :ref:`l-FAQ2`      | :ref:`l-notebooks`  | :ref:`l-NB2`       | :ref:`l-statcode`      | `Unit Test Coverage <coverage/index.html>`_    |
+------------------------+---------------------+---------------------+--------------------+------------------------+------------------------------------------------+
