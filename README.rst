
.. image:: https://github.com/sdpython/pyensae/blob/master/_doc/sphinxdoc/source/_static/project_ico.png?raw=true
    :target: https://github.com/sdpython/pyensae/

.. _l-README:

pyensae: hide complexity for teachings
======================================

.. image:: https://travis-ci.com/sdpython/pyensae.svg?branch=master
    :target: https://app.travis-ci.com/github/sdpython/pyensae
    :alt: Build status

.. image:: https://ci.appveyor.com/api/projects/status/jioxwx1igwbqwa28?svg=true
    :target: https://ci.appveyor.com/project/sdpython/pyensae
    :alt: Build Status Windows

.. image:: https://circleci.com/gh/sdpython/pyensae/tree/master.svg?style=svg
    :target: https://circleci.com/gh/sdpython/pyensae/tree/master

.. image:: https://badge.fury.io/py/pyensae.svg
    :target: https://pypi.org/project/pyensae/

.. image:: https://img.shields.io/badge/license-MIT-blue.svg
    :alt: MIT License
    :target: http://opensource.org/licenses/MIT

.. image:: https://codecov.io/github/sdpython/pyensae/coverage.svg?branch=master
    :target: https://codecov.io/github/sdpython/pyensae?branch=master

.. image:: http://img.shields.io/github/issues/sdpython/pyensae.png
    :alt: GitHub Issues
    :target: https://github.com/sdpython/pyensae/issues

.. image:: http://www.xavierdupre.fr/app/pyensae/helpsphinx/_images/nbcov.png
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

.. image:: https://pepy.tech/badge/pyensae/month
    :target: https://pepy.tech/project/pyensae/month
    :alt: Downloads

.. image:: https://img.shields.io/github/forks/sdpython/pyensae.svg
    :target: https://github.com/sdpython/pyensae/
    :alt: Forks

.. image:: https://img.shields.io/github/stars/sdpython/pyensae.svg
    :target: https://github.com/sdpython/pyensae/
    :alt: Stars

This project contains helpers used at the `ENSAE <http://www.ensae.fr/>`_
for teachings available at
`ENSAE - Programmation - Xavier Dupré <http://www.xavierdupre.fr/app/ensae_teaching_cs/helpsphinx/index.html>`_.
It was the first module created for that usage.
It does not have a clear purpose except hiding
some annoying logic and shorten notebooks.
It can:

* retrieve data for practical lessons
* import a tsv file into a database
* retrieve stock prices from Yahoo Finance

It implements a couple of magic commands to play with
*SQLite3* in a notebook and easily show the head or tail
of a text file. It can fill missing values in timeseries
with *add_missing_indices* or download data from a website,
a helper to change the size of *folium* maps or some grammar
to parse language such as *R* or *SQL*. It also implements a basic
way to convert a *R* script into nasty *Python*.

**Links:**

* `GitHub/pyensae <https://github.com/sdpython/pyensae/>`_
* `documentation <http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html>`_
* `Blog <http://www.xavierdupre.fr/app/pyensae/helpsphinx/blog/main_0000.html#ap-main-0>`_
