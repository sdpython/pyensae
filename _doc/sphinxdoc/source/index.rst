pyensae documentation
=====================

.. image:: https://travis-ci.org/sdpython/pyensae.svg?branch=master
    :target: https://travis-ci.org/sdpython/pyensae
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/jioxwx1igwbqwa28?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyensae
    :alt: Build Status Windows

.. image:: https://badge.fury.io/py/pyensae.svg
    :target: http://badge.fury.io/py/pyensae

.. image:: http://img.shields.io/github/issues/sdpython/pyensae.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyensae/issues

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://landscape.io/github/sdpython/pyensae/master/landscape.svg?style=flat
   :target: https://landscape.io/github/sdpython/pyensae/master
   :alt: Code Health

.. image:: https://requires.io/github/sdpython/pyensae/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pyensae/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/pyensae/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyensae?branch=master

.. image:: https://badge.waffle.io/sdpython/pyensae.png?label=ready&title=Ready
    :alt: Waffle
    :target: https://waffle.io/sdpython/pyensae

.. image:: nbcov.png
    :target: http://www.xavierdupre.fr/app/pyensae/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

**Links:** `pypi <https://pypi.python.org/pypi/pyensae/>`_,
`github <https://github.com/sdpython/pyensae/>`_,
`documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_,
`wheel <http://www.xavierdupre.fr/site2013/index_code.html#pyensae>`_,
`travis <https://travis-ci.org/sdpython/pyensae>`_,
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
The module also implements magic commands to access an Hadoop cluster
(Azure, Cloudera), to run SQL queries on `SQLite <https://sqlite.org/>`_,
parsing financial data from `Yahoo Finance <https://fr.finance.yahoo.com/>`_.

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
    HISTORY

Functionalities
---------------

* retrieve data for practical lessons (see :func:`download_data <pyensae.datasource.http_retrieve.download_data>`)
* import a tsv file into a database (see :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`)
* retrieve stock prices from Yahoo Finance (see :class:`StockPrices <pyensae.finance.astock.StockPrices>`)
* magic commands to easily use SQLite3 from a notebook (see :class:`MagicSQL <pyensae.sql.magic_sql.MagicSQL>`)
* magic commands to access a Cloudera Cluster and run PIG jobs (see :class:`MagicRemoteSSH <pyensae.remote.magic_remote_ssh.MagicRemoteSSH>`)
* magic commands to access Azure Blob Storage and HDInsight (see :class:`MagicAzure <pyensae.remote.magic_azure.MagicAzure>`)
* magic commands to display content of a folder in DataFrame (see :class:`MagicFile <pyensae.file_helper.magic_file.MagicFile>`)
* magic commands to display an autamated menu in a notebook (see :class:`MagicFile <pyensae.notebook_helper.magic_notebook.MagicNotebook>`)

Dependencies
------------

* `numpy <http://www.numpy.org/>`_
* `pandas <http://pandas.pydata.org/>`_
* `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper>`_

For the class :class:`StockPrices <pyensae.finance.astock.StockPrices>`:
    * `dateutil <https://pypi.python.org/pypi/python-dateutil>`_
    * `six <https://pypi.python.org/pypi/six>`_

The :class:`ASSHClient <pyensae.remote.ssh_remote_connection.ASSClient>` requires:
    * `paramiko <http://www.paramiko.org/>`_
    * `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_
    * `ecdsa <https://pypi.python.org/pypi/ecdsa>`_

The :class:`AzureClient <pyensae.remote.azure_connection.AzureClient>` requires:
    * `azure <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_

The function :func:`register_magics_ssh <pyensae.remote.magic_remote_ssh.register_magics_ssh>` defines magic commands
to send commands to a remote commands through a SSH connection:
    * ``%remote_open``, ``%remote_close``
    * ``%remote_cmd``, ``%remote_up``, ``%remote_down``

The magic commands will be automatically enabled if the module is imported from a notebook.
It also proposes others magic commands such as ``%head``, ``%tail``, ``%textdiff``,
``%hhelp``, ``%runpy``, ``%lsr``, ``%compress``. Type ``<magic_command> -h``
to get their usage.

Installation
------------

``pip install pyquickhelper`` or to avoid installing the dependencies ``pip install pyquickhelper --no-deps``.

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
