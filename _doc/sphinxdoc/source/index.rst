pyensae documentation
=====================

.. contents::
   :depth: 3


Introduction
------------

This module contains various helpers for teachings at the ENSAE.

See :ref:`l-README`.
    
Installation 
------------

From the page `Pieces of codes, libraries <http://www.xavierdupre.fr/site2013/index_code.html>`_:

* Windows installation: 
    * run the setup ``pyensae*.win32.exe``
* Windows installation with source:
    * download the file ``pyensae*.tar.gz`` and unzip it
    * type the following commands::
    
        set PATH=%PATH%;c:\Python33
        python.exe setup.py install    
        
* Linux installation:
    * download the file ``pyensae*.tar.gz``
    * type the following commands::
    
        tar xf pyensae-py3.3.tar.gz
        sudo su
        python3.3 setup.py install
        
* Using pip::

    pip install pyensae


You can check the module is working for basic functions by running::
    
    import pyensae
    pyensae.check()
    
        
Quick overview
--------------

* **retrieve data for practical lessons**
    * download data or modules:  :func:`download_data <resources.http_retrieve.download_data>`

See also :ref:`l-usecase`.

Changes
-------

* :ref:`l-changes`

Contribution
------------

The library is public and available on `github <https://github.com/sdpython/pyensae/>`_. 
Please do not commit without running the unit test and add a unit test for every of your contributions.
See :ref:`l-doctestunit` to see how to run them and to generate the documentation.

About this documentation
------------------------

.. toctree::
    :maxdepth: 2

    generatedoc
    glossary
    confr_pyp

    
Indices and tables
==================

* :ref:`l-modules`
* :ref:`l-functions`
* :ref:`l-classes`
* :ref:`l-methods`
* :ref:`l-staticmethods`
* :ref:`l-properties`
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
   

