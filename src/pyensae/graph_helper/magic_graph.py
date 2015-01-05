#-*- coding: utf-8 -*-
"""
@file
@brief Magic commands about graphs

.. versionadded:: 1.1
"""
import sys, os, pandas

from IPython.core.magic import Magics, magics_class, line_magic, cell_magic
from IPython.core.magic import line_cell_magic
from IPython.core.display import HTML

from pyquickhelper import MagicCommandParser, MagicClassWithHelpers
from .matplotlib_helper import mpl_switch_style

@magics_class
class MagicGraph(MagicClassWithHelpers):
    """
    Defines magic commands to list the content of a folder

    .. versionadded:: 1.1
    """

    @staticmethod
    def mpl_style_parser():
        """
        defines the way to parse the magic command ``%mpl_style``
        """
        parser = MagicCommandParser(description='changes matplotlib style')
        parser.add_argument('style', type=str, help='style, ggplot for exemple', default="ggplot")
        return parser

    @line_magic
    def mpl_style(self, line):
        """
        defines ``%mpl_style``
        which changes the style of matplotlib graphs, example: ``%mpl_style ggplot``
        """
        parser = self.get_parser(MagicGraph.mpl_style_parser, "mpl_style")
        args = self.get_args(line, parser)

        if args is not None:
            style = args.style
            mpl_switch_style(style)


def register_graph_magics():
    """
    register magics function, can be called from a notebook
    """
    from IPython import get_ipython
    ip = get_ipython()
    ip.register_magics(MagicGraph)