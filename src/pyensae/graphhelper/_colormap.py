"""
@file
@brief CorrPlot functionalities.

It comes from `corrplot.py <https://raw.githubusercontent.com/biokit/biokit/master/biokit/viz/corrplot.py>`_
which I copied here because the module does not properly work on Python 3 (import issues).
See also `biokit license <https://github.com/biokit/biokit/blob/master/LICENSE>`_.

:author: Thomas Cokelaer
:references: http://cran.r-project.org/web/packages/corrplot/vignettes/corrplot-intro.html
"""
import numpy as np


class Color:
    """
    Lists of known colors.
    """

    colors = {
        'red': (1., 0., 0.),
        'green': (0., 1., 0.),
        'blue': (0., 0., 1.),
        'white': (1., 1., 1.),
        'black': (0., 0., 0.),
        'darkblue': '#00008b',
    }

    def __init__(self, name):
        """
        @param  name    hexadecimal or name
        """
        if len(name) == 7 and name[0] == '#':
            self.set_hex(name)
        else:
            value = Color.colors.get(name, None)
            if value is None:
                raise ValueError("Unknown color name '{}'.".format(name))
            if len(value) == 7:
                self.set_hex(value)
            else:
                self.red, self.green, self.blue = value

    def set_hex(self, name):
        """
        Converts a string like ``#AABBCC`` into `(red, green, blue)`.
        """
        self.red = float.fromhex('0x' + name[1:3].lower()) / 255
        self.green = float.fromhex('0x' + name[3:5].lower()) / 255
        self.blue = float.fromhex('0x' + name[5:7].lower()) / 255


class Colormap:
    """
    Snippets of code from `colormap/colors.py
    <https://github.com/cokelaer/colormap/blob/master/src/colormap/colors.py>`_,
    `LICENSE <https://github.com/cokelaer/colormap/blob/master/LICENSE>`_.
    """
    # Source:

    def _get_colormap_mpl(self):
        try:
            from matplotlib.pyplot import colormaps as _cmaps
            return _cmaps()
        except ImportError:
            return []
    colormaps = property(_get_colormap_mpl)

    def _get_diverging_black(self):
        return ['red_black_sky', 'red_black_blue', 'red_black_green', 'yellow_black_blue',
                'yellow_black_sky', 'red_black_orange', 'pink_black_green(w3c)']
    diverging_black = property(_get_diverging_black)

    def cmap_linear(self, color1, color2, color3, reverse=False, N=256):
        """
        Provides 3 colors in format accepted by :class:`Color`
        ::
            red = Color('red')
            cmap = cmap_linear(red, 'white', '#0000FF')
        """
        c1 = Color(color1)
        c2 = Color(color2)
        c3 = Color(color3)
        dico = {'red': [c1.red, c2.red, c3.red],
                'green': [c1.green, c2.green, c3.green],
                'blue': [c1.blue, c2.blue, c3.blue]}

        return self.cmap(dico, reverse=reverse, N=N)

    def cmap(self, colors=None, reverse=False, N=256):
        """
        Returns a colormap object to be used within matplotlib
        :param dict colors: a dictionary that defines the RGB colors to be
            used in the colormap. See :meth:`get_cmap_heat` for an example.
        :param bool reverse: reverse the colormap is  set to True (defaults to False)
        :param int N: Defaults to 50
        """
        # matplotlib colormaps
        if colors in self.colormaps:
            if reverse and colors.endswith("_r") is False:
                colors += "_r"
            from matplotlib.cm import get_cmap
            return get_cmap(colors)
        # custom ones
        if colors in self.diverging_black:
            c1, c2, c3 = colors.split("_")
            # special case of sky, which does not exists
            c3 = c3.replace("sky", "deep sky blue")
            return self.cmap_linear(c1, c2, c3)
        if colors == 'heat':
            return self.get_cmap_heat()
        if colors == 'heat_r':
            return self.get_cmap_heat_r()

        if reverse:
            for k in colors.keys():
                colors[k].reverse()

        # If index not given, RGB colors are evenly-spaced in colormap.
        index = np.linspace(0, 1, len(colors['red']))

        # Adapt color_data to the form expected by LinearSegmentedColormap.
        color_data = dict((key, [(x, y, y) for x, y in zip(index, value)])
                          for key, value in list(colors.items()))

        import matplotlib.colors
        m = matplotlib.colors.LinearSegmentedColormap(
            'my_color_map', color_data, N)
        return m


def cmap_builder(name, name2=None, name3=None):
    """
    Returns a colormap object compatible with matplotlib
    If only parameter **name** is provided, it should be a known matplotlib
    colormap name (e.g., jet). If **name2** is provided, then a new colormap
    is created going from the color **name** to the color **name2** with a
    linear scale. Finally, if **name3** is provided, a linear scaled colormap
    is built from color **name** to color **name3** with the intermediate color
    being the **name2**.
    Matplotlib colormap map names
    Source: `colormap/get_cmap.py
    <https://github.com/cokelaer/colormap/blob/master/src/colormap/get_cmap.py>`_,
    `LICENSE <https://github.com/cokelaer/colormap/blob/master/LICENSE>`_).
    """
    c = Colormap()
    # an R colormap
    if name and name2 and name3:
        return c.cmap_linear(name, name2, name3)
    if name and name2:
        return c.cmap_bicolor(name, name2)
    if name == 'heat':
        return c.get_cmap_heat()
    if name == 'heat_r':
        return c.get_cmap_heat_r()
    # matplotlic colormaps
    if name in c.colormaps:
        return c.cmap(name)
    # some custom diverging colormaps with black in the middle.
    if name in c.diverging_black:
        return c.cmap(name)
    if name.count("_") == 2:
        name1, name2, name3 = name.split("_")
        return c.cmap_linear(name1, name2, name3)

    # valid = c.colormaps + c.diverging_black
    txt = "name provided {0} is not recognised. ".format(name)
    txt += "\n valid name can be found in colormap.colormap_names"
    raise ValueError(txt)
