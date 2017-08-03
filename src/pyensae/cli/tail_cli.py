"""
@file
@brief Wrapper function @see fn file_tail into a command line.

.. versionadded:: 1.5
"""
from __future__ import print_function
import os
import sys
from pyquickhelper.cli.cli_helper import call_cli_function


def file_tail_cli(fLOG=print, args=None):
    """
    Takes the last lines from a file using function @see fn file_tail.

    @param      fLOG        logging function
    @param      args        to overwrite ``sys.args``

    .. cmdref::
        :title: extract the last lines of a file
        :cmd: pyensae.cli.tail_cli:file_tail_cli

        Extracts the first line of a file.
    """
    try:
        from pyensae.file_helper.content_helper import file_tail
    except ImportError:
        folder = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", ".."))
        sys.path.append(folder)
        from pyensae.file_helper.content_helper import file_tail

    call_cli_function(file_tail, args=args, fLOG=fLOG,
                      skip_parameters=('fLOG',))


if __name__ == "__main__":
    file_tail_cli()
