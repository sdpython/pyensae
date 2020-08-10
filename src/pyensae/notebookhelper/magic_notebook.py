# -*- coding: utf-8 -*-
"""
@file
@brief Magic command to help within notebooks
"""
from IPython.core.magic import magics_class, line_magic
try:
    import qgrid
except ImportError:
    # We ignore that error since it is not
    # part of the mandatory requirements.
    qgrid = None
from jyquickhelper import add_notebook_menu
from pyquickhelper.ipythonhelper import MagicCommandParser, MagicClassWithHelpers


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

        .. nbref::
            :title: nb_menu

            The magic command ``%nb_menu`` displays a menu in a notebook.
            It parses a notebook and displays a menu gathering all sections
            within that notebook. The code is the following::

                from pyquickhelper.ipythonhelper import add_notebook_menu
                js = add_notebook_menu(menu_id=<menu_id>, header=<title>, format=<format>,
                                    first_level=<level1>, last_level=<level2>,
                                    raw=<raw>)
        """
        parser = self.get_parser(MagicNotebook.nb_menu_parser, "nb_menu")
        args = self.get_args(line, parser)

        if args is not None:
            js = add_notebook_menu(menu_id=args.menu_id, header=args.title, format=args.format,
                                   first_level=args.level1, last_level=args.level2, raw=args.raw)
            return js

    @staticmethod
    def jsdf_parser():
        """
        defines the way to parse the magic command ``%jsdf``
        """
        parser = MagicCommandParser(
            description='display a pandas DataFrame based on module qgrid', prog="jsdf")
        parser.add_argument(
            'df',
            help='dataframe to display')
        parser.add_argument(
            '--defaultColumnWidth',
            type=int,
            default=80,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--enableColumnReorder',
            type=bool,
            default=True,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--multiColumnSort',
            type=bool,
            default=False,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--rowHeight',
            type=int,
            default=25,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--showHeaderRow',
            type=bool,
            default=False,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--forceFitColumns',
            type=bool,
            default=False,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--autoHeight',
            type=bool,
            default=False,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--enableCellNavigation',
            type=bool,
            default=True,
            help='see https://github.com/mleibman/SlickGrid/wiki/Grid-Options')
        parser.add_argument(
            '--precision',
            type=int,
            default=4,
            help='see function qgrid.set_defaults')
        parser.add_argument(
            '--editable',
            type=bool,
            default=True,
            help='make the output editable')
        return parser

    @line_magic
    def jsdf(self, line):
        """
        defines ``%jsdf``
        which displays a pandas dataframe into a notebook using qgrid (javascript)

        .. nbref::
            :title: jsdf

            The magic command ``%jsdf`` displays a dataframe using
            `qgrid <https://qgrid.readthedocs.io/en/latest/>`_ module.
            The code is the following::

                import qgrid
                if firt_call:
                    qgrid.set_defaults(precision=<precision>)
                    self.first_jsdf_call = False

                df = args.df
                grid_options = dict(defaultColumnWidth=<defaultColumnWidth>,
                                    enableColumnReorder=<enableColumnReorder>,
                                    multiColumnSort=<multiColumnSort>,
                                    rowHeight=<rowHeight>,
                                    showHeaderRow=<showHeaderRow>,
                                    forceFitColumns=<forceFitColumns>,
                                    autoHeight=<autoHeight>,
                                    enableCellNavigation=<enableCellNavigation>)
                qgrid.show_grid(df, grid_options=grid_options)
        """
        parser = self.get_parser(MagicNotebook.jsdf_parser, "jsdf")
        args = self.get_args(line, parser)

        if qgrid is None:
            return "qgrid is not installed."

        if not hasattr(self, "first_jsdf_call") or self.first_jsdf_call:
            if args is not None:
                qgrid.set_defaults(precision=args.precision)
            else:
                qgrid.set_defaults()
            self.first_jsdf_call = False

        if args is not None:
            df = args.df
            grid_options = dict(defaultColumnWidth=args.defaultColumnWidth,
                                enableColumnReorder=args.enableColumnReorder,
                                multiColumnSort=args.multiColumnSort,
                                rowHeight=args.rowHeight,
                                showHeaderRow=args.showHeaderRow,
                                forceFitColumns=args.forceFitColumns,
                                autoHeight=args.autoHeight,
                                enableCellNavigation=args.enableCellNavigation,
                                editable=args.editable)
            res = qgrid.show_grid(df, grid_options=grid_options)
            return "" if res is None else res


def register_notebook_magics(ip=None):
    """
    register magics function, can be called from a notebook

    @param      ip      from ``get_ipython()``
    """
    if ip is None:
        from IPython import get_ipython
        ip = get_ipython()
    ip.register_magics(MagicNotebook)
