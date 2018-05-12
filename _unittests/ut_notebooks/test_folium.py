"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder

try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src


from src.pyensae.notebook_helper import folium_html_map, folium_embed_map


class TestNotebookFolium (unittest.TestCase):

    def test_notebook_folium(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_folium")
        outfile = os.path.join(temp, 'osm.html')

        if sys.platform.startswith("win") and ("anaconda" in sys.base_prefix or
                                               "_condavir" in sys.executable):
            # an expected error
            # jinja2.exceptions.TemplateNotFound: tiles\openstreetmap\tiles.txt
            warnings.warn(
                "test_notebook_folium not run on Anaconda, it raises that error: " +
                "jinja2.exceptions.TemplateNotFound: tiles/openstreetmap/tiles.txt")
            return

        import folium
        map_osm = folium.Map(location=[48.85, 2.34])
        map_osm.save(outfile)
        assert os.path.exists(outfile)
        folium_embed_map(map_osm, path=outfile.replace(".html", "2.html"))
        ht = folium_html_map(map_osm, asobj=False)
        fLOG("done")
        assert len(ht) > 0
        assert "<div" in ht

        ht = folium_html_map(map_osm, width="50%", asobj=True)
        fLOG("done")
        assert len(ht.res) > 0
        assert "<div" in ht.res


if __name__ == "__main__":
    unittest.main()
