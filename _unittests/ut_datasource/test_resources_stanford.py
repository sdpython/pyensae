"""
@brief      test log(time=2s)
"""


import sys
import os
import unittest
from pyquickhelper.pycode import ExtTestCase, get_temp_folder


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

from src.pyensae.datasource.http_retrieve import download_data


class TestResourcesStanford(ExtTestCase):

    def test_tar_gz(self):
        fold = get_temp_folder(__file__, "temp_tar_gz")
        files = download_data("facebook.tar.gz", website="xd", whereTo=fold)
        sh = [g for g in files if g.endswith("3980.egofeat")]
        self.assertNotEmpty(files)
        self.assertEqual(len(sh), 1)

    def test_gz(self):
        fold = get_temp_folder(__file__, "temp_gz")
        files = download_data("facebook_combined.txt.gz",
                              website="xd", whereTo=fold)
        self.assertNotEmpty(files)


if __name__ == "__main__":
    unittest.main()
