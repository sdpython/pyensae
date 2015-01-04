
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

* retrieve data for practical lessons
* import a tsv file into a database
* retrieve stock prices from Yahoo Finance
* magic commands to easily use SQLite3 from a notebook
* magic commands to access a Cloudera Cluster and run PIG jobs
* magic commands to access Azure Blob Storage and HDInsight
* magic commands to display content of a folder in DataFrame

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
    

Contributions
-------------

Started in 2013/08.

* First contributor: `Xavier Dupré <http://www.xavierdupre.fr/>`_.
* Others contributors: ENSAE's students.

Versions
--------

* **1.1 - 2014/??/??**
    * **change:** magic command ``%tail_stderr`` nows displays keyword ``ERROR`` in red.
    * **new:** magic command ``%blob_downmerge`` to download the content of a folder from a blob storage
    * **add:** method :meth:`upload_cluster <pyensae.remote.remote_connection.ASSHClient.upload_cluster>`
    * **add:** method :meth:`download_cluster <pyensae.remote.remote_connection.ASSHClient.download_cluster>`
    * **add:** add magic command to test a streaming script for PIG
    * **add:** function :func:`file_head <pyensae.file_helper.content_helper.file_head>`, :func:`file_tail <pyensae.file_helper.content_helper.file_tail>`,
    * **add:** add magic command ``%lsrepo``, ``%compress``
* **1.0 - 2014/11/10**
    * **add:** add magic command ``%tail_stderr`` for :class:`AzureClient <pyensae.remote.azure_connection.AzureClient>`
    * **add:** add magic commands for SQLite3 + a notebook
    * **fix:** the setup does not need the file ``README.rst`` anymore
    * **new:** magic commands ``%lsr`` to retrieve the content of a folder
    * **new:** various function to format the size of a file
* **0.9 - 2014/11/03**
    * **add:** Python version is now checked, ImportError is raised if it used on Python 2
    * **add:** option -local to %jobsubmit    
    * **add:** add magic command and methods to enable a shell from a notebook (a kind of putty) (command ``%open_remove_shell``, ...)
    * **new:** function :func:`parse_code <pyensae.languages.antlr_grammar_use.parse_code>` parses a script in R, PIG, SQLite syntax and checks if there is any mistake, it requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_
    * **new:** new class :class:`AzureClient <pyensae.remote.azure_connection.AzureClient>` to handle some basic needs with Azure
    * **add:** add magic command and methods to handle Azure from a notebook
