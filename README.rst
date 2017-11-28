
.. _l-README:

README
======

.. image:: https://travis-ci.org/sdpython/pyensae.svg?branch=master
    :target: https://travis-ci.org/sdpython/pyensae
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/jioxwx1igwbqwa28?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyensae
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pyensae/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pyensae/tree/master

.. image:: https://badge.fury.io/py/pyensae.svg
    :target: http://badge.fury.io/py/pyensae

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://requires.io/github/sdpython/pyensae/requirements.svg?branch=master
     :target: https://requires.io/github/sdpython/pyensae/requirements/?branch=master
     :alt: Requirements Status

.. image:: https://codecov.io/github/sdpython/pyensae/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyensae?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/pyensae.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyensae/issues

.. image:: https://badge.waffle.io/sdpython/pyensae.png?label=ready&title=Ready
    :alt: Waffle
    :target: https://waffle.io/sdpython/pyensae

.. image:: http://www.xavierdupre.fr/app/pyensae/helpsphinx/_images/nbcov.png
    :target: http://www.xavierdupre.fr/app/pyensae/helpsphinx/all_notebooks_coverage.html
    :alt: Notebook Coverage

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
