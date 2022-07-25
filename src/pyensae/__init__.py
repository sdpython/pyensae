# -*- coding: utf-8 -*-
"""
@file
@brief Module *pyensae*.
Recurrent needs for teachings
turned into functions.
"""
__version__ = "1.3.964"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pyensae"
__url__ = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html"
__license__ = "MIT License"


def _setup_hook(add_print=False, unit_test=False):
    """
    if this function is added to the module,
    the help automation and unit tests call it first before
    anything goes on as an initialization step.
    It should be run in a separate process.

    @param      add_print       print *Success: _setup_hook*
    @param      unit_test       used only for unit testing purpose
    """
    # we can check many things, needed module
    # any others things before unit tests are started
    if add_print:  # pragma: no cover
        print("Success: _setup_hook")


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception

    .. faqref::
        :title: Installation issue

        If the installation fails because of a *SyntaxError*

        ::

            Collecting pyensae
            Using cached pyensae-1.1.302.tar.gz
            Complete output from command python setup.py egg_info:
            Traceback (most recent call last):
            File "<string>", line 20, in <module>
            File "/private/var/folders/qv/something/T/pip-build-xxxx/pyensae/setup.py", line 98
                raise ImportError(message) from e
                                            ^
            SyntaxError: invalid syntax

        It probably means you are trying to install *pyensae* on Python 2.7
        instead of using Python 3.
    """
    return True


def load_ipython_extension(ip):  # pragma: no cover
    """
    to allow the call ``%load_ext pyensae``

    @param      ip      from ``get_ipython()``
    """
    from .sql.magic_sql import register_sql_magics
    from .filehelper.magic_file import register_file_magics
    from .graphhelper.magic_graph import register_graph_magics
    from .notebookhelper.magic_notebook import register_notebook_magics

    register_sql_magics(ip)
    register_file_magics(ip)
    register_graph_magics(ip)
    register_notebook_magics(ip)
