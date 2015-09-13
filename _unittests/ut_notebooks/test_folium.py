"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import re
import warnings

try:
    import src
    import pyquickhelper
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper


from pyquickhelper import get_temp_folder, fLOG
from src.pyensae.notebook_helper import folium_inline_map


class TestNotebookFolium (unittest.TestCase):

    def test_notebook_folium(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_folium")
        outfile = os.path.join(temp, 'osm.html')

        if sys.platform.startswith("win") and ("anaconda" in sys.base_prefix or \
                "_condavir" in sys.executable):
            # an expected error
            # jinja2.exceptions.TemplateNotFound: tiles\openstreetmap\tiles.txt
            warnings.warn("test_notebook_folium not run on Anaconda, it raises that error: jinja2.exceptions.TemplateNotFound: tiles/openstreetmap/tiles.txt")
            return

        import folium
        map_osm = folium.Map(location=[48.85, 2.34])
        map_osm.create_map(path=outfile)
        assert os.path.exists(outfile)
        folium_inline_map(map_osm)
        fLOG("done")


if __name__ == "__main__":
    unittest.main()
