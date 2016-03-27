"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper as skip_
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
    import pyquickhelper as skip_

from pyquickhelper.loghelper import fLOG
from src.pyensae.datasource.http_retrieve import download_data


class TestResources (unittest.TestCase):

    def test_import_one(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_http")
        if not os.path.exists(fold):
            os.mkdir(fold)
        exp = ["VOEUX01.txt", "voeux.zip"]
        for f in exp:
            g = os.path.join(fold, f)
            if os.path.exists(g):
                os.remove(g)
        one = "voeux.zip"
        res = download_data(one, website="xd", whereTo=fold, fLOG=fLOG)
        fLOG(len(res), res)
        assert len(res) == 14
        assert "VOEUX01.txt" in res[0]
        for f in exp:
            g = os.path.join(fold, f)
            assert os.path.exists(g)

    def test_import_all(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        all = [" "]
        if __name__ == "__main__":
            # we only test all the resources if this file is the main file
            # otherwise it takes too much time
            for a in all:
                pass


if __name__ == "__main__":
    unittest.main()
