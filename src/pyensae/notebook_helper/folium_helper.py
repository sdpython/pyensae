#-*- coding: utf-8 -*-
"""
@file
@brief Module *folium* does not have any output to a notebook, addresses that issue
"""

from IPython.display import HTML
import folium


def folium_inline_map(map):
    """
    Embeds the HTML source of the map directly into the IPython notebook.

    @param      map     folium map
    @return             HTML (IPython)

    This method will not work if the map depends on any files (json data). Also this uses
    the HTML5 srcdoc attribute, which may not be supported in all browsers.

    Source: `folium_base.py <https://gist.github.com/psychemedia/f7385255f89137c503b5>`_

    @exemple(Display an inline map with folium in a notebook)
    @code
    import folium
    map_osm = folium.Map(location=[48.85, 2.34])
    from pyensae.notebook_helper import folium_inline_map
    map_osm.polygon_marker(location=[48.824338, 2.302641], popup='ENSAE',
                           fill_color='#132b5e', num_sides=3, radius=10)
    folium_inline_map(map_osm)
    @endcode
    @endexample
    """
    map._build_map()
    return HTML('<iframe srcdoc="{srcdoc}" style="width: 100%; height: 510px; border: none"></iframe>'.format(srcdoc=map.HTML.replace('"', '&quot;')))


def folium_embed_map(map, path="map.html"):
    """
    @param      map     folium map
    @param      path    where to store the temporary map
    @return             HTML (IPython)

    Embeds a linked iframe to the map into the IPython notebook.

    Note: this method will not capture the source of the map into the notebook.
    This method should work for all maps (as long as they use relative urls).

    Source: `folium_base.py <https://gist.github.com/psychemedia/f7385255f89137c503b5>`_
    """
    map.create_map(path=path)
    return HTML('<iframe src="files/{path}" style="width: 100%; height: 510px; border: none"></iframe>'.format(path=path))
