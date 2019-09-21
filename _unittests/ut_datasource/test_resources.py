"""
@brief      test log(time=3s)
"""
import os
import unittest
import zipfile
from pyquickhelper.pycode import ExtTestCase, get_temp_folder
from pyensae.datasource.http_retrieve import download_data, DownloadDataException


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
                         (DownloadDataException, zipfile.BadZipFile, RuntimeError))


if __name__ == "__main__":
    unittest.main()
