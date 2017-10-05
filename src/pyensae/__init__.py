#-*- coding: utf-8 -*-
"""
@file
@brief Module *pyense*.
Recurrent needs for teachings
turned into functions.
"""
import sys
from .datasource.http_retrieve import download_data


if sys.version_info[0] < 3:
    raise ImportError("pyensae only works with Python 3")

__version__ = "1.1"
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
    if add_print:
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


def load_ipython_extension(ip):
    """
    to allow the call ``%load_ext pyensae``

    @param      ip      from ``get_ipython()``
    """
    from .remote.magic_remote_ssh import register_magics_ssh
    try:
        from .remote.magic_azure import register_azure_magics
        az = True
    except ImportError as e:
        if "azure" in str(e):
            az = False
        else:
            raise e

    from .sql.magic_sql import register_sql_magics
    from .file_helper.magic_file import register_file_magics
    from .graph_helper.magic_graph import register_graph_magics
    from .notebook_helper.magic_notebook import register_notebook_magics

    register_magics_ssh(ip)
    if az:
        register_azure_magics(ip)
    register_sql_magics(ip)
    register_file_magics(ip)
    register_graph_magics(ip)
    register_notebook_magics(ip)
