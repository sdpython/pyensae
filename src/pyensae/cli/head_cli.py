"""
@file
@brief Wrapper function @see fn file_head into a command line.

.. versionadded:: 1.5
"""
from __future__ import print_function
import os
import sys
from pyquickhelper.cli.cli_helper import call_cli_function


def file_head_cli(fLOG=print, args=None):
    """
    Takes the first lines from a file using function @see fn file_head.

    @param      fLOG        logging function
    @param      args        to overwrite ``sys.args``

    .. cmdref::
        :title: extract the first lines of a file
        :cmd: pyensae.cli.head_cli:file_head_cli

        Extracts the first line of a file.
    """
    try:
        from pyensae.file_helper.content_helper import file_head
    except ImportError:
        folder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(folder)
        from pyensae.file_helper.content_helper import file_head

    call_cli_function(file_head, args=args, fLOG=fLOG,
                      skip_parameters=('fLOG',))


if __name__ == "__main__":
    file_head_cli()
