#-*- coding: utf-8 -*-
"""
@file
@brief Various functions about graphviz.

.. versionadded:: 1.1
"""

import os
from pyquickhelper.helpgen.conf_path_tools import get_graphviz_dot
from pyquickhelper.loghelper import run_cmd


def dot_exe():
    """
    retrieve graphivz executable

    @return     filename

    .. versionadded:: 1.1
    """
    r = get_graphviz_dot()
    if r is None:
        raise FileNotFoundError("unable to find graphviz")
    return r


def run_dot(dot_file, outimg):
    """
    calls graphivz on a dot file and produces an image

    @param      dot_file        file, format `DOT <http://www.graphviz.org/doc/info/lang.html>`_
    @param      outimg          output image
    @return                     out, err (stdout, stderr from graphviz)

    .. versionadded:: 1.1
    """
    ext = os.path.splitext(outimg)[-1].strip(".")
    exe = dot_exe()
    cmd = "\"{0}\" -T{1} -o{2} {3}".format(exe, ext, outimg, dot_file)
    out, err = run_cmd(cmd, wait=True)
    if len(err) > 0:
        raise Exception("unable to run graphviz on {0}.\nCMD:\n{1}\nOUT:\n{2}\nERR:\n{3}".format(
            dot_file, cmd, out, err))
    return out, err
