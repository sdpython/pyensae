#-*- coding: utf-8 -*-
"""
@file
@brief Main file
"""

import sys
if sys.version_info[0] < 3:
    raise ImportError("pyensae only works with Python 3")

__version__ = "1.1"
__author__ = "Xavier Dupré"
__github__ = "https://github.com/sdpython/pyensae"
__url__ = "http://www.xavierdupre.fr/app/pyensae/helpsphinx/index.html"
__downloadUrl__ = "http://www.xavierdupre.fr/site2013/index_code.html#pyensae"
__license__ = "MIT License"


def check(log=False):
    """
    Checks the library is working.
    It raises an exception.

    @param      log     if True, display information, otherwise
    @return             0 or exception

    @FAQ(Installation issue)

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

    @endFAQ
    """
    return True

from .resources.http_retrieve import download_data


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


try:
    from IPython import get_ipython
    ip = get_ipython()
    if ip is not None:
        load_ipython_extension(ip)

except ImportError as e:
    # IPython is not installed
    pass
