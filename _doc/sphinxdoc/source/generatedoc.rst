Generate this documentation
===========================

Tips to generate the documentation
++++++++++++++++++++++++++++++++++

.. generatedoc:

You need to install sphinx (pip install sphinx). If you do not have any projet, you need to run sphinx-quicl-install
from the folder you want to use to generate the documentation. Look at the configuration:

Run::

   make clean
   make html
    
However, some steps are missing:
    * automatically create a list of files to document
    * convert javadoc syntax into rst syntax
    * create a copy of the file to document

Tips:
    * 3 spaces before any included files

Pointers:
    * `Sphinx short syntax <http://matplotlib.org/sampledoc/cheatsheet.html>`_
    * `Sphinx long syntax <http://sphinx-doc.org/contents.html>`_
    * `Documenting Your Project Using Sphinx <http://pythonhosted.org/an_example_pypi_project/sphinx.html>`_
    * `Sphinx extensions for embedded plots, math and more <http://matplotlib.org/sampledoc/extensions.html>`_
    * `A page with many examples <http://docutils.sourceforge.net/docs/user/rst/demo.txt>`_
    * `FAQ <http://sphinx.readthedocs.org/en/latest/faq.html>`_
    * `Welcome to The Hitchhiker's Guide to Packaging <http://guide.python-distribute.org/>`_

configuration:
    *   confr_pyp
 
Extensions to install
+++++++++++++++++++++

* `fancybox <http://spinus.github.io/sphinxcontrib-fancybox/>`_: the module is not bullet proof for Python 3.x, unicode type must be replaced by str.
