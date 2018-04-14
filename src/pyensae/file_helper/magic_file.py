# -*- coding: utf-8 -*-
"""
@file
@brief Magic command to handle files
"""
import sys
import os
import pandas

from IPython.core.magic import magics_class, line_magic, cell_magic
from IPython.core.display import HTML

from pyquickhelper.filehelper.synchelper import explore_folder_iterfile, explore_folder_iterfile_repo
from pyquickhelper.loghelper import run_cmd
from pyquickhelper.ipythonhelper import MagicCommandParser, MagicClassWithHelpers
from pyquickhelper.helpgen import docstring2html
from .format_helper import format_file_size, format_file_mtime
from .content_helper import file_head, file_tail, enumerate_grep, file_encoding


@magics_class
class MagicFile(MagicClassWithHelpers):

    """
    Defines magic commands to help with files

    .. faqref::
        :title: Magic command not found

        Magic commands are automatically added when importing the module ::

            import pyensae

        This instruction does not raise any exception.
        To understand what went wrong, the following instruction must be run::

            %load_ext pyensae

        Usually, one necessary module is missing.

    .. versionadded:: 1.1
    """

    @staticmethod
    def head_parser():
        """
        defines the way to parse the magic command ``%head``
        """
        parser = MagicCommandParser(prog="head",
                                    description='display the first lines of a text file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument(
            '-n',
            '--n',
            type=int,
            default=10,
            help='number of lines to display')
        parser.add_argument(
            '-r',
            '--raw',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            '-e',
            '--encoding',
            default="utf8",
            help='file encoding')
        parser.add_argument(
            '-s',
            '--errors',
            default="",
            help='What about errors: "", strict, replace, surrogateescape, '
                 'xmlcharrefreplace, backslashreplace, namereplace')
        return parser

    @line_magic
    def head(self, line):
        """
        defines ``%head``
        which displays the first lines of a file

        .. nbref::
            :tag: file
            :title: head

            The magic command ``%head`` is equivalent to::

                from pyensae.file_helper import file_head
                file_head(<filename>, <n>, <encoding>)
        """
        parser = self.get_parser(MagicFile.head_parser, "head")
        args = self.get_args(line, parser)

        if args is not None:
            errors = args.errors
            if errors is not None and len(errors) < 2:
                errors = None
            encoding = args.encoding
            if encoding is not None and len(encoding) < 2:
                encoding = None
            rows = file_head(args.f, args.n, encoding, errors=errors)
            if args.raw:
                return "".join(rows)
            else:
                return HTML("<pre>\n{0}\n</pre>".format("".join(rows)))

    @staticmethod
    def encoding_parser():
        """
        defines the way to parse the magic command ``%encoding``
        """
        parser = MagicCommandParser(prog="encoding",
                                    description='guess the encoding of a file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument(
            '-n',
            '--n',
            type=int,
            default=2**20,
            help='maximum number of lines to use to guess the encoding')
        return parser

    @line_magic
    def encoding(self, line):
        """
        defines ``%encoding``
        which guesses the encoding

        .. nbref::
            :tag: file
            :title: encoding

            The magic command ``%encoding`` is equivalent to::

                from pyensae.file_helper import file_head
                file_head(<filename>, <n>, <encoding>)
        """
        parser = self.get_parser(MagicFile.encoding_parser, "encoding")
        args = self.get_args(line, parser)

        if args is not None:
            res = file_encoding(args.f, args.n)
            return str(res)

    @staticmethod
    def grep_parser():
        """
        defines the way to parse the magic command ``%grep``
        """
        parser = MagicCommandParser(prog="grep",
                                    description='display the first lines of a text file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument('regex', type=str, help='regular expression')
        parser.add_argument(
            '-n',
            '--n',
            type=int,
            default=-1,
            help='number of lines to display, -1 for all')
        parser.add_argument(
            '-r',
            '--raw',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            '-e',
            '--encoding',
            default="utf8",
            help='file encoding')
        parser.add_argument(
            '-s',
            '--errors',
            default="",
            help='What about errors: "", strict, replace, surrogateescape, '
                 'xmlcharrefreplace, backslashreplace, namereplace')
        return parser

    @line_magic
    def grep(self, line):
        """
        defines ``%grep``
        which displays the first lines of a file

        .. nbref::
            :tag: file
            :title: grep

            The magic command ``%grep`` is equivalent to::

                from pyensae.file_helper import enumerate_grep
                list(enumerate_grep(<filename>, <regex>, <encoding>))
        """
        parser = self.get_parser(MagicFile.grep_parser, "grep")
        args = self.get_args(line, parser)

        if args is not None:
            errors = args.errors
            if errors is not None and len(errors) < 2:
                errors = None
            encoding = args.encoding
            if encoding is not None and len(encoding) < 2:
                encoding = None
            iter = enumerate_grep(args.f, args.regex,
                                  encoding, errors=errors)
            if args.n != -1:
                rows = []
                for r in iter:
                    if len(rows) >= args.n:
                        break
                    rows.append(r)
            else:
                rows = list(iter)

            if args.raw:
                return "".join(rows)
            else:
                return HTML("<pre>\n{0}\n</pre>".format("".join(rows)))

    @staticmethod
    def tail_parser():
        """
        defines the way to parse the magic command ``%tail``
        """
        parser = MagicCommandParser(prog="tail",
                                    description='display the last lines of a text file')
        parser.add_argument('f', type=str, help='filename')
        parser.add_argument(
            '-n',
            '--n',
            type=int,
            default=10,
            help='number of lines to display')
        parser.add_argument(
            '-r',
            '--raw',
            default=False,
            action='store_true',
            help='display raw text instead of HTML')
        parser.add_argument(
            '-e',
            '--encoding',
            default="utf8",
            help='file encoding')
        parser.add_argument(
            '-s',
            '--errors',
            default="",
            help='What about errors: "", strict, replace, surrogateescape, '
                 'xmlcharrefreplace, backslashreplace, namereplace')
        return parser

    @line_magic
    def tail(self, line):
        """
        defines ``%tail``
        which displays the last lines of a file

        .. nbref::
            :tag: file
            :title: tail

            The magic command ``%tail`` is equivalent to::

                from pyensae.file_helper import file_tail
                file_tail(<filename>, <n>, <encoding>)
        """
        parser = self.get_parser(MagicFile.tail_parser, "tail")
        args = self.get_args(line, parser)

        if args is not None:
            errors = args.errors
            if errors is not None and len(errors) < 2:
                errors = None
            encoding = args.encoding
            if encoding is not None and len(encoding) < 2:
                encoding = None
            rows = file_tail(args.f, args.n, encoding, errors=errors)
            if args.raw:
                return "".join(rows)
            else:
                return HTML("<pre>\n{0}\n</pre>".format("".join(rows)))

    @staticmethod
    def lsr_parser():
        """
        defines the way to parse the magic command ``%lsr``
        """
        parser = MagicCommandParser(prog="lsr",
                                    description='display the content of a folder as a dataframe')
        parser.add_argument(
            'path',
            type=str,
            nargs="?",
            help='path',
            default=".")
        parser.add_argument(
            '-f',
            '--filter',
            type=str,
            default=".*",
            help='filter, same syntax as a regular expression')
        return parser

    @line_magic
    def lsr(self, line):
        """
        define ``%lsr`` which returns the content of a folder,
        the method stops after around 10000 files --> you should precise the filter.

        .. nbref::
            :tag: file
            :title: lsr

            The magic command ``%lsr`` is almost equivalent to::

                from pyquickhelper.file_helper import explore_folder_iterfile
                res = explore_folder_iterfile(<filename>, <pattern>)
                for f in res:
                    print(f)
        """
        parser = self.get_parser(MagicFile.lsr_parser, "lsr")
        args = self.get_args(line, parser)

        if args is not None:
            if args.path is None or len(args.path) == 0:
                filename = "."
            else:
                filename = args.path
            pattern = args.filter

            if "*" in filename:
                pattern = filename
                filename = "."

            iter = explore_folder_iterfile(filename, pattern)
            rows = []
            for r in iter:
                d = os.path.isfile(r)
                if d:
                    st = os.stat(r)
                    r = {"name": r,
                         "size": format_file_size(st.st_size),
                         "last_modified": format_file_mtime(st.st_mtime),
                         "directory": False}
                else:
                    r = {"name": r, "directory": True}
                rows.append(r)
            return pandas.DataFrame(rows)

    @staticmethod
    def PYTHON_parser():
        """
        defines the way to parse the magic command ``%%PYTHON``
        """
        parser = MagicCommandParser(prog="PYTHON",
                                    description='the command stores the content of the cell as a local file.')
        parser.add_argument(
            'file',
            type=str,
            help='filename')
        return parser

    @cell_magic
    def PYTHON(self, line, cell=None):
        """
        defines command ``%%PYTHON``

        .. nbref::
            :title: PYTHON

            The magic command ``%%PYTHON`` is almost to:

            ::

                with open(<filename>, "w", encoding="utf8") as f:
                    f.write("# -*- coding: utf8 -*-\\n")
                    f.write(cell.replace("\\r", ""))
        """
        parser = self.get_parser(MagicFile.PYTHON_parser, "PYTHON")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            with open(filename, "w", encoding="utf8") as f:
                f.write("# -*- coding: utf8 -*-\n")
                f.write(cell.replace("\r", ""))

    @staticmethod
    def runpy_parser():
        """
        defines the way to parse the magic command ``%%runpy``
        """
        parser = MagicCommandParser(prog="runpy",
                                    description='run a python script which accepts standards input and produces standard outputs, a timeout is set up at 10s')
        parser.add_argument(
            'file',
            type=str,
            help='python file')
        parser.add_argument(
            'args',
            type=str,
            nargs="*",
            help='arguments for the scripts',
            default=".")
        return parser

    @cell_magic
    def runpy(self, line, cell=None):
        """
        defines command ``%%runpy``

        .. nbref::
            :title: runpy

            ``%%runpy`` runs  a python script which accepts
            standards input and produces standard outputs,
            a timeout is set up at 10s. It is almost equivalent to::

                from pyquickhelper.loghelper import run_cmd
                import sys
                cmd = sys.executable.replace(
                    "pythonw",
                    "python") + " " + filename + " " + args
                out, err = run_cmd(
                    cmd, wait=True, sin=cell, communicate=True, timeout=10, shell=False)

        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicFile.runpy_parser, "runpy")
        args = self.get_args(line, parser)

        if args is not None:
            filename = args.file
            if len(filename) == 0:
                self.runpy("")
            else:
                args = args.args
                cmd = sys.executable.replace("pythonw", "python")
                cmd += " " + filename + " "
                cmd += " ".join('"{0}"'.format(_)
                                for _ in args) if isinstance(args, list) else args
                tosend = cell
                out, err = run_cmd(
                    cmd, wait=True, sin=tosend, communicate=True, timeout=10, shell=False)
                if len(err) > 0:
                    return HTML(
                        '<font color="#DD0000">Error</font><br /><pre>\n%s\n</pre>' % err)
                else:
                    return HTML('<pre>\n%s\n</pre>' % out)

    @staticmethod
    def lsrepo_parser():
        """
        defines the way to parse the magic command ``%lsrepo``
        """
        parser = MagicCommandParser(prog="lsrepo",
                                    description='display the content of a repository (GIT or SVN)')
        parser.add_argument(
            'path',
            type=str,
            nargs="?",
            help='path',
            default=".")
        return parser

    @line_magic
    def lsrepo(self, line):
        """
        define ``%lsrepo``

        .. nbref::
            :tag: file
            :title: lsrepo

            The method returns the files present in a repository (GIT or SVN).
            The code is equivalent to::

                from pyquickhelper.filehelper import explore_folder_iterfile_repo
                res = explore_folder_iterfile_repo(<filename>, <pattern>)
                for f in res:
                    print(f)

        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicFile.lsrepo_parser, "lsrepo")
        args = self.get_args(line, parser)

        if args is not None:
            if args.path is None or len(args.path) == 0:
                filename = "."
            else:
                filename = args.path

            iter = explore_folder_iterfile_repo(filename)
            rows = []
            for r in iter:
                d = os.path.isfile(r)
                if d:
                    st = os.stat(r)
                    r = {"name": r,
                         "size": format_file_size(st.st_size),
                         "last_modified": format_file_mtime(st.st_mtime),
                         "directory": False}
                else:
                    r = {"name": r, "directory": True}
                rows.append(r)
            return pandas.DataFrame(rows)

    @staticmethod
    def hhelp_parser():
        """
        defines the way to parse the magic command ``%hhelp``

        .. versionadded:: 1.1
        """
        parser = MagicCommandParser(prog="hhelp",
                                    description='display help for an object in HTML format')
        parser.add_argument(
            'obj',
            type=str,
            help='a python object')
        parser.add_argument(
            '-f',
            '--format',
            type=str,
            default="html",
            help='format',
            choices=['text', 'html', 'rst', 'rawhtml'])
        parser.add_argument(
            '-np',
            '--no-print',
            action='store_true',
            help='by default, the magic command outputs everything on the standard output, '
                 'if specified, it returns a string')
        return parser

    @line_magic
    def hhelp(self, line):
        """
        define ``%hhelp``, it displays the help for an object in HTML

        .. nbref::
            :title: hhelp

            The magic command is equivalent to::

                from pyquickhelper import docstring2html
                docstring2html(obj, format=format)

        .. versionadded:: 1.1
        """
        parser = self.get_parser(MagicFile.hhelp_parser, "hhelp")
        args = self.get_args(line, parser)

        if args is not None:
            obj = args.obj
            format = args.format
            nop = args.no_print
            if nop or format == "html":
                return docstring2html(obj, format=format)
            else:
                print(docstring2html(obj, format=format))


def register_file_magics(ip=None):
    """
    register magics function, can be called from a notebook

    @param      ip      from ``get_ipython()``
    """
    if ip is None:
        from IPython import get_ipython
        ip = get_ipython()
    ip.register_magics(MagicFile)
