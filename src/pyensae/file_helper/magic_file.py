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
from pyquickhelper import MagicCommandParser
from .format_helper import format_file_size, format_file_mtime


@magics_class
class MagicFile(Magics):
    """
    Defines magic commands to list the content of a folder

    ..versionadded:: 1.1
    """

    @staticmethod
    def head_parser():
        """
        defines the way to parse the magic command ``%head``
        """
        parser = MagicCommandParser(description='display the first lines of a text file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument('-n', '--n', type=int, default=10, help='number of lines to display')
        parser.add_argument('-e', '--encoding', default="utf8", help='file encoding')
        return parser
    _parser_head = None

    @line_magic
    def head(self, line):
        """
        defines ``%head``
        which displays the first lines of a file
        """
        if MagicFile._parser_head is None:
            MagicFile._parser_head = MagicFile.head_parser()
        parser = MagicFile._parser_head

        try:
            args = parser.parse_cmd(line)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            if not os.path.exists(args.f) :
                raise FileNotFoundError(args.f)
            if not os.path.isfile(args.f):
                raise FileNotFoundError("{0} is not a file".format(args.f))
            rows = [ ]
            with open(args.f, "r", encoding=args.encoding) as f :
                for line in f :
                    rows.append(line)
                    if len(rows) >= args.n :
                        break

            return HTML("<pre>\n{0}\n</pre>".format("".join(rows)))

    @staticmethod
    def lsr_parser():
        """
        defines the way to parse the magic command ``%lsr``
        """
        parser = MagicCommandParser(description='display the content of a folder as a dataframe')
        parser.add_argument('path', type=str, nargs="?", help='path', default=".")
        parser.add_argument('-f', '--filter', type=str, default=".*", help='filter, same syntax as a regular expression')
        return parser
    _parser_lsr = None

    @line_magic
    def lsr(self, line):
        """
        define ``%lsr``, the method stops after around 10000 files --> you should precise the filter.
        """
        if MagicFile._parser_lsr is None:
            MagicFile._parser_lsr = MagicFile.lsr_parser()
        parser = MagicFile._parser_lsr

        try:
            args = parser.parse_cmd(line)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            if args.path is None or len(args.path) == 0 :
                filename = "."
            else:
                filename = args.path
            pattern = args.filter

            if "*" in filename:
                pattern = filename
                filename = "."

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