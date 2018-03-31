"""
@brief      test log(time=12s)

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
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from src.pyensae.file_helper.decompress_helper import decompress_bz2


class TestFilesBz2(ExtTestCase):

    def test_bz2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        temp = get_temp_folder(__file__, "temp_bz2")
        data = os.path.join(temp, "..", "data", "lines_utf8.txt.bz2")
        res = decompress_bz2(data, temp)
        self.assertFalse(res[0].endswith('.'))
        self.assertExists(res[0])


if __name__ == "__main__":
    unittest.main()
