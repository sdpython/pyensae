pyensae documentation
=====================

   
   
**Links:**
    * `pypi/pyensae <https://pypi.python.org/pypi/pyensae/>`_
    * `GitHub/pyensae <https://github.com/sdpython/pyensae/>`_
    * `documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
    * `Windows Setup <http://www.xavierdupre.fr/site2013/index_code.html#pyensae>`_


Description        
-----------

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_ 
for teaching purposes but not only.
It requires `github/pyquickhelper <https://github.com/sdpython/pyquickhelper/>`_.

Data used for teachings at the
`ENSAE <http://www.xavierdupre.fr/site2013/enseignements/index.html>`_
are available through function::

    download_data("td8_velib.zip", website = "xd")
    
The data comes from `xavierdupre.fr <http://www.xavierdupre.fr/>`_.
    
Functionalities
---------------

* retrieve data for practical lessons (see :func:`download_data <pyensae.resources.http_retrieve.download_data>`)
* import a tsv file into a database (see :func:`import_flatfile_into_database <pyensae.sql.database_helper.import_flatfile_into_database>`)
* retrieve stock prices from Yahoo Finance (see :class:`StockPrices <pyensae.finance.astock.StockPrices>`)
* magic commands to easily use SQLite3 from a notebook (see :class:`MagicSQL <pyensae.sql.magic_sql.MagicSQL>`)
* magic commands to access a Cloudera Cluster and run PIG jobs (see :class:`MagicRemote <pyensae.remote.magic_remote.MagicRemote>`)
* magic commands to access Azure Blob Storage and HDInsight (see :class:`MagicAzure <pyensae.remote.magic_azure.MagicAzure>`)
* magic commands to display content of a folder in DataFrame (see :class:`MagicFile <pyensae.file_helper.magic_file.MagicFile>`)

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

The :class:`AzureClient <pyensae.remote.azure_connection.AzureClient>` requires:
    * `azure <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_

The function :func:`register_magics <pyensae.remote.magic_remote.register_magics>` defines magic commands
to send commands to a remote commands through a SSH connection:
    * ``%remote_open``, ``%remote_close``
    * ``%remote_cmd``, ``%remote_up``, ``%remote_down``
    
The magic commands will be automatically enabled if the module is imported from a notebook.


Indices and tables
==================

+------------------+---------------------+---------------------+------------------+------------------------+----------------------------------------------------+
| :ref:`l-modules` |  :ref:`l-functions` | :ref:`l-classes`    | :ref:`l-methods` | :ref:`l-staticmethods` | :ref:`l-properties`                                |
+------------------+---------------------+---------------------+------------------+------------------------+----------------------------------------------------+
| :ref:`genindex`  |  :ref:`modindex`    | :ref:`search`       | :ref:`l-license` | :ref:`l-changes`       | :ref:`l-README`                                    |
+------------------+---------------------+---------------------+------------------+------------------------+----------------------------------------------------+
| :ref:`l-example` |  :ref:`l-FAQ`       | :ref:`l-notebooks`  |                  | :ref:`l-exampleAzure`  | `Unit Test Coverage <coverage/index.html>`_        |
+------------------+---------------------+---------------------+------------------+------------------------+----------------------------------------------------+

Navigation
==========

.. toctree::
    :maxdepth: 1

    doctestunit
    generatedoc
    generatesetup
    installation
    all_example
    all_example_Azure
    all_FAQ
    all_notebooks
    glossary
    index_module
    license
    filechanges
    README
    all_indexes

    
