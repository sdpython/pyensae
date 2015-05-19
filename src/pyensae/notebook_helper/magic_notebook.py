#-*- coding: utf-8 -*-
"""
@file
@brief Magic command to help within notebooks
"""
from IPython.core.magic import magics_class, line_magic

from pyquickhelper.ipythonhelper import add_notebook_menu
from pyquickhelper import MagicCommandParser, MagicClassWithHelpers


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
            description='display a menu in the notebook based on javascript')
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
        return parser

    @line_magic
    def nb_menu(self, line):
        """
        defines ``%head``
        which displays the first lines of a file
        """
        parser = self.get_parser(MagicNotebook.nb_menu_parser, "nb_menu")
        args = self.get_args(line, parser)

        if args is not None:
            js = add_notebook_menu(menu_id=args.menu_id, header=args.title)
            return js


def register_notebook_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicNotebook)
