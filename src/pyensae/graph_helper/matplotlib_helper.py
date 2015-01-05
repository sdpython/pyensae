#-*- coding: utf-8 -*-
"""
@file
@brief Various functions about matplotlib
"""

import matplotlib.pyplot


def mpl_switch_style(style="ggplot"):
    """
    changes the graph style

    @param      style       see `Customizing plots with style sheets <http://matplotlib.org/users/style_sheets.html>`_

    .. versionadded:: 1.1
    """
    matplotlib.pyplot.style.use(style)