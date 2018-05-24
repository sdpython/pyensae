"""
@brief      test log(time=3s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
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

from src.pyensae.datasource.http_retrieve import download_data, DownloadDataException


class TestResources(ExtTestCase):

    def test_download_data(self):
        fold = get_temp_folder(__file__, "temp_download_data")
        exp = ["VOEUX01.txt", "voeux.zip"]
        res = download_data(["voeux.zip"], website="xd",
                            whereTo=fold, timeout=10)
        self.assertEqual(len(res), 14)
        self.assertIn("VOEUX01.txt", res[0])
        for f in exp:
            g = os.path.join(fold, f)
            self.assertExists(g)

    def test_download_data2(self):
        fold = get_temp_folder(__file__, "temp_download_data2")
        exp = ["VOEUX01.txt", "voeux.zip"]
        res = download_data(["voeux.zip"], website=["xd"],
                            whereTo=fold, timeout=10)
        self.assertEqual(len(res), 14)
        self.assertIn("VOEUX01.txt", res[0])
        for f in exp:
            g = os.path.join(fold, f)
            self.assertExists(g)

    def test_download_data_failures(self):
        fold = get_temp_folder(__file__, "temp_download_data_failures")
        one = "voeux2.zip"
        self.assertRaise(lambda: download_data(one, website="xd", whereTo=fold, timeout=10),
                         DownloadDataException)


if __name__ == "__main__":
    unittest.main()
