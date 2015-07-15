#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to help within notebooks
"""
from IPython.core.magic import magics_class, line_magic
from pyquickhelper.ipythonhelper import add_notebook_menu, MagicCommandParser, MagicClassWithHelpers


@magics_class
class MagicNotebook(MagicClassWithHelpers):

    """
    Defines magic commands to help with notebooks

    .. versionadded:: 1.1
    """

    @staticmethod
    def nb_menu_parser():
        """
        defines the way to parse the magic command ``%nb_menu``
        """
        parser = MagicCommandParser(
            description='display a menu in the notebook based on javascript', prog="nb_menu")
        parser.add_argument(
            '-t',
            '--title',
            type=str,
            default="Plan",
            help='title before the menu')
        parser.add_argument(
            '-i',
            '--menu-id',
            type=str,
            default="my_menu_id",
            help='menu id used to locate the corresponding HTML tag div')
        parser.add_argument(
            '-f',
            '--format',
            type=str,
            default="html",
            help='format to consider, html or rst')
        parser.add_argument(
            '-l1',
            '--level1',
            type=int,
            default=2,
            help='first level to consider in the menu')
        parser.add_argument(
            '-l2',
            '--level2',
            type=int,
            default=4,
            help='last level to consider in the menu')
        parser.add_argument(
            '-r',
            '--raw',
            type=bool,
            default=False,
            help='if true, displays the javascript, otherwise the html')
        return parser

    @line_magic
    def nb_menu(self, line):
        """
        defines ``%nb_menu``
        which displays a menu
        """
        parser = self.get_parser(MagicNotebook.nb_menu_parser, "nb_menu")
        args = self.get_args(line, parser)

        if args is not None:
            js = add_notebook_menu(menu_id=args.menu_id, header=args.title, format=args.format,
                                   first_level=args.level1, last_level=args.level2, raw=args.raw)
            return js


def register_notebook_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicNotebook)
