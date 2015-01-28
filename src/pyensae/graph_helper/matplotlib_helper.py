#-*- coding: utf-8 -*-
"""
@file
@brief Various functions about matplotlib
"""



def mpl_switch_style(style="ggplot"):
    """
    changes the graph style

    @param      style       see `Customizing plots with style sheets <http://matplotlib.org/users/style_sheets.html>`_

    .. versionadded:: 1.1
    """
    # this import was moved here because ths code is executed when
    # the module is imported and for some reasons, it overides some of the settings
    # sphinx is doing and graphs are not part of the documentation but show up
    # in a separate window
    if "plt" not in sys.modules:
        import matplotlib.pyplot as plt
    plt.style.use(style)