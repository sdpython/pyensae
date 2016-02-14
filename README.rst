

.. _l-README:

README / Changes
================

.. image:: https://travis-ci.org/sdpython/pyensae.svg?branch=master
    :target: https://travis-ci.org/sdpython/pyensae
    :alt: Build status
   
.. image:: https://ci.appveyor.com/api/projects/status/hw3ixda4622h34qb?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyensae
    :alt: Build Status Windows
    
.. image:: https://badge.fury.io/py/pyensae.svg
    :target: http://badge.fury.io/py/pyensae
      
.. image:: http://img.shields.io/pypi/dm/pyensae.png
    :alt: PYPI Package
    :target: https://pypi.python.org/pypi/pyensae    

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

   
**Links:**

* `GitHub/pyensae <https://github.com/sdpython/pyensae/>`_
* `documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/pyensae/helpsphinx/blog/main_0000.html#ap-main-0>`_


Description        
-----------

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_
for teachings available at
`ENSAE - Programmation - Xavier Dupré <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx3/index.html>`_.

    
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
* `pyquickhelper <https://pypi.python.org/pypi/pyquickhelper/>`_

Class *StockPrices* requires:

* `dateutil <https://pypi.python.org/pypi/python-dateutil>`_
* `six <https://pypi.python.org/pypi/six>`_
    
Class *ASSHClient* requires:

* `paramiko <http://www.paramiko.org/>`_
* `pycrypto <https://pypi.python.org/pypi/pycrypto/>`_
* `ecdsa <https://pypi.python.org/pypi/ecdsa>`_

Class *AzureClient* requires:

* `azure <http://www.xavierdupre.fr/app/azure-sdk-for-python/helpsphinx/index.html>`_

The function *register_magics* defines magic commands
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

* **1.1 - 2016/??/??**
    * **change:** magic command ``%tail_stderr`` nows displays keyword ``ERROR`` in red.
    * **new:** magic command ``%blob_downmerge`` to download the content of a folder from a blob storage
    * **add:** method *pyensae.remote.remote_connection_ssh.ASSHClient.upload_cluster*
    * **add:** method *pyensae.remote.remote_connection_ssh.ASSHClient.download_cluster*
    * **add:** add magic command to test a streaming script for PIG
    * **add:** function *pyensae.file_helper.content_helper.file_head*, 
      *pyensae.file_helper.content_helper.file_tail*, *pyensae.file_helper.content_helper.enumerate_grep*
    * **add:** add magic command ``%lsrepo``, ``%compress``, ``%mpl_style``
    * **del:** delete class *TransferFTP*, moves it to module pyquickhelper
    * **add:** add magic command ``%hhelp`` to display the help for an object in HTML format
    * **new:** function pyensae.graph_helper.graphviz_helper.run_dot
    * **change:** update to antlr 4.5, add CSharp grammar
    * **new:** new magic command ``textdiff``
    * **new:** new magic command ``nb_menu`` to display a menu from all available section in the notebook
    * **new:** function Corrplot copied from module biokit (works in python 3)
    * **new:** magic command ``%jsdf`` which runs module qgrid on a DataFrame
    * **new:** function ``decompress_bz2``
    * **add:** add method ``df_head`` to class ``AzureClient``, the function download can return the content instead of a file
    
* **1.0 - 2014/11/10**
    * **add:** add magic command ``%tail_stderr`` for class AzureClient
    * **add:** add magic commands for SQLite3 + a notebook
    * **fix:** the setup does not need the file ``README.rst`` anymore
    * **new:** magic commands ``%lsr`` to retrieve the content of a folder
    * **new:** various function to format the size of a file
    
