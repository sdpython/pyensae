# -*- coding: utf-8 -*-
"""
@file
@brief Module *folium* does not have any output to a notebook, addresses that issue. The module
does not explicitely import *folium*.
"""

from IPython.display import HTML


def folium_html_map(mapf, width=None, height=None, asobj=True):
    """
    Embeds the HTML source of the map directly into the IPython notebook.

    @param      mapf    folium map
    @param      width   width
    @param      height  height
    @param      asobj   return an object which implements ``_repr_html_``
    @return             HTML (IPython)

    This method will not work if the map depends on any files (json data). Also this uses
    the HTML5 srcdoc attribute, which may not be supported in all browsers.

    Source: `folium_base.py <https://gist.github.com/psychemedia/f7385255f89137c503b5>`_

    .. exref::
        :title: Display an inline map with folium in a notebook

        ::

            import folium
            map_osm = folium.Map(location=[48.85, 2.34])
            from pyensae.notebook_helper import folium_html_map
            map_osm.polygon_marker(location=[48.824338, 2.302641], popup='ENSAE',
                                fill_color='#132b5e', num_sides=3, radius=10)
            folium_html_map(map_osm)

        With folium version 0.2, this becomes easier:

        ::

            import folium
            map_osm = folium.Map(location=[48.85, 2.34])
            from pyensae.notebook_helper import folium_html_map
            map_osm.polygon_marker(location=[48.824338, 2.302641], popup='ENSAE',
                                fill_color='#132b5e', num_sides=3, radius=10)
            map_osm

    .. versionchanged:: 1.1
        Add parameters *width* and *height* to change the size of the map within a notebook.
        Hopefully, they will be added in folium.
    """
    res = mapf._repr_html_()
    if width or height:
        look = '<div style="width:100%;">'
        if not res.startswith(look):
            raise ValueError(
                "Folium has changed its HTML form, it used to start with: '{0}'.\n{1}".format(look, res))
        size = ""
        if width:
            size += "width:" + width + ";"
        if height:
            size += "height:" + height + ";"
        newlook = '<div style="{size}">'.format(size=size)
        res = newlook + res[len(look):]
    if asobj:
        class CustomFoliumMap:

            def __init__(self, res, map):
                self.res = res
                self.map = map

            def _repr_html_(self):
                return self.res

        return CustomFoliumMap(res, map)
    else:
        return res


def folium_embed_map(mapf, path="map.html", width="100%", height="510px"):
    """
    @param      mapf    folium map
    @param      path    where to store the temporary map
    @return             HTML (IPython)

    Embeds a linked iframe to the map into the IPython notebook.

    Note: this method will not capture the source of the map into the notebook.
    This method should work for all maps (as long as they use relative urls).

    Source: `folium_base.py <https://gist.github.com/psychemedia/f7385255f89137c503b5>`_
    """
    mapf.save(path)
    return HTML('<iframe src="files/{path}" style="width: {width}; height: {height}; border: none">' +
                '</iframe>'.format(path=path, width=width, height=height))
