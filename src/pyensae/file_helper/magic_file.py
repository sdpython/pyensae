#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
import sys, os, pandas

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML

from pyquickhelper.filehelper.synchelper import explore_folder_iterfile, explore_folder_iterfile_repo
from pyquickhelper import MagicCommandParser, run_cmd, zip_files, gzip_files, zip7_files, MagicClassWithHelpers
from .format_helper import format_file_size, format_file_mtime
from .content_helper import file_head, file_tail


@magics_class
class MagicFile(MagicClassWithHelpers):
    """
    Defines magic commands to list the content of a folder

    .. versionadded:: 1.1
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
            args = parser.parse_cmd(line, context = self.Context)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            rows = file_head(args.f, args.n, args.encoding)
            return HTML("<pre>\n{0}\n</pre>".format("".join(rows)))

    @staticmethod
    def tail_parser():
        """
        defines the way to parse the magic command ``%tail``
        """
        parser = MagicCommandParser(description='display the last lines of a text file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument('-n', '--n', type=int, default=10, help='number of lines to display')
        parser.add_argument('-e', '--encoding', default="utf8", help='file encoding')
        return parser
    _parser_tail = None

    @line_magic
    def tail(self, line):
        """
        defines ``%tail``
        which displays the last lines of a file
        """
        if MagicFile._parser_tail is None:
            MagicFile._parser_tail = MagicFile.tail_parser()
        parser = MagicFile._parser_tail

        try:
            args = parser.parse_cmd(line, context = self.Context)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            rows = file_tail(args.f, args.n, args.encoding)
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
        define ``%lsr`` which returns the content of a folder,
        the method stops after around 10000 files --> you should precise the filter.
        """
        if MagicFile._parser_lsr is None:
            MagicFile._parser_lsr = MagicFile.lsr_parser()
        parser = MagicFile._parser_lsr

        try:
            args = parser.parse_cmd(line, context = self.Context)
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

    @cell_magic
    def PYTHON(self, line, cell = None):
        """
        defines command ``%%PYTHON``
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%PYTHON <filename>")
            print("")
            print("The command store the content of the cell as a local file.")
        else:
            filename = line.strip()
            with open(filename, "w", encoding="utf8") as f :
                f.write("# -*- coding: utf8 -*-\n")
                f.write(cell.replace("\r",""))

    @cell_magic
    def runpy(self, line, cell = None):
        """
        defines command ``%%runpy``

        run a python script which accepts standards input and produces standard outputs,
        a timeout is set up at 10s

        .. versionadded:: 1.1
        """
        if line in [None, ""] :
            print("Usage:")
            print("     %%runpy <pythonfile.py> <args>")
            print("     first row")
            print("     second row")
            print("     ...")
        else:
            filename = line.strip().split()
            if len(filename) == 0:
                self.runpy("")
            else:
                args = " ".join(filename[1:])
                filename = filename[0]
                cmd = sys.executable.replace("pythonw", "python") + " " + filename + " " + args
                tosend = cell
                out,err = run_cmd(cmd, wait=True, sin=tosend, communicate=True, timeout=10, shell=False)
                if len(err) > 0 :
                    return HTML ('<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML ('<pre>\n%s\n</pre>' % out)

    @staticmethod
    def _lsrepo_parser():
        """
        defines the way to parse the magic command ``%lsrepo``
        """
        parser = MagicCommandParser(description='display the content of a repository (GIT or SVN)')
        parser.add_argument('path', type=str, nargs="?", help='path', default=".")
        return parser
    _parser_lsrepo = None

    @line_magic
    def lsrepo(self, line):
        """
        define ``%lsrepo``, the method returns the files present in a repository (GIT or SVN)

        .. versionadded:: 1.1
        """
        if MagicFile._parser_lsrepo is None:
            MagicFile._parser_lsrepo = MagicFile._lsrepo_parser()
        parser = MagicFile._parser_lsrepo

        try:
            args = parser.parse_cmd(line, context = self.Context)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            if args.path is None or len(args.path) == 0 :
                filename = "."
            else:
                filename = args.path

            iter = explore_folder_iterfile_repo(filename)
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

    @staticmethod
    def _compress_parser():
        """
        defines the way to parse the magic command ``%compress``

        .. versionadded:: 1.1
        """
        parser = MagicCommandParser(description='display the content of a repository (GIT or SVN)')
        parser.add_argument('dest', type=str, help='destination, the extension defines the compression format, zip, gzip 7z')
        parser.add_argument('files', type=str, nargs="?", help='files to compress or a python list')
        return parser
    _parser_compress = None

    @line_magic
    def compress(self, line):
        """
        define ``%compress``, it compress a list of files,
        it returns the number of compressed files

        .. versionadded:: 1.1
        """
        if MagicFile._parser_compress is None:
            MagicFile._parser_compress = MagicFile._compress_parser()
        parser = MagicFile._parser_compress

        try:
            args = parser.parse_cmd(line, context = self.Context)
        except SystemExit:
            print( parser.print_help() )
            args = None

        if args is not None:
            dest   = args.dest
            files  = args.files
            format = os.path.splitext(dest)[-1].strip(".").lower()

            if format == "zip":
                return zip_files(dest, files)
            elif format == "gzip":
                return gzip_files(dest, files)
            elif format == "7z":
                return zip7_files(dest, files)
            else:
                raise ValueError("unexpected format: " + format)

def register_file_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicFile)