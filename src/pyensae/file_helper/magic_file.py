#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
import sys, os, pandas

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML

from pyquickhelper.sync.synchelper import explore_folder_iterfile
from .format_helper import format_file_size, format_file_mtime


@magics_class
class MagicFile(Magics):
    """
    Defines magic commands to list the content of a folder

    ..versionadded:: 1.1
    """

    @line_magic
    def lsr(self, line):
        """
        define ``%lsr``, the method stops after around 10000 files --> you should precise the filter.
        """
        filename = line.strip()
        if filename == "-h":
            print("Usage:")
            print("  %lsl [path] [filter]")
            print("if path is not filled, it is replaced by '.'")
            print("filter is optional and is a regular expression")
            print("the function is recursive but stops after around 10000 files")
            print("path do not allow spaces")
        else:
            if filename is None or len(filename) == 0 :
                filename = "."
            spl = filename.split()
            if len(spl) == 2 :
                filename,pattern = spl
            elif len(spl) == 1:
                if "*" in filename or "+" in filename:
                    pattern = filename
                    filename = "."
                else:
                    pattern = None
            else:
                raise Exception("unexpected parameters (try %lsr -h): " + filename)

            iter = explore_folder_iterfile(filename, pattern)
            rows = [ ]
            for r in iter :
                d = os.path.isfile(r)
                if d :
                    st = os.stat(r)
                    r = {   "name":r,
                            "size":format_file_size(st.st_size),
                            "last_modified":format_file_mtime(st.st_mtime),
                            "directory":False }
                else:
                    r = { "name":r, "directory":True }
                rows.append(r)
            return pandas.DataFrame(rows)

def register_file_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicFile)