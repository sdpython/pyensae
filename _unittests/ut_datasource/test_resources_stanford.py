"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG


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


class TestResourcesStanford (unittest.TestCase):

    def test_tar_gz(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_stand")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for f in os.listdir(fold):
            if os.path.isfile(f):
                os.remove(os.path.join(fold, f))
        files = download_data(
            "facebook.tar.gz",
            website="xd",
            fLOG=fLOG,
            whereTo=fold)
        fLOG(files)
        sh = [g for g in files if g.endswith("3980.egofeat")]
        assert len(files) > 0
        assert len(sh) == 1

    def test_gz(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_stand")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for f in os.listdir(fold):
            if os.path.isfile(f):
                os.remove(os.path.join(fold, f))
        files = download_data(
            "facebook_combined.txt.gz",
            website="xd",
            fLOG=fLOG,
            whereTo=fold)
        fLOG(files)


if __name__ == "__main__":
    unittest.main()
