"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase, is_travis_or_appveyor

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

from src.pyensae._pylint_common import _private_test_style_src, _private_test_style_test


class TestCodeStyle(ExtTestCase):

    def test_src_import(self):
        """for pylint"""
        self.assertTrue(src is not None)

    def test_style_src(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        run_lint = is_travis_or_appveyor(env=['NAME_JENKINS']) is None
        _private_test_style_src(fLOG, run_lint, verbose='-v' in sys.argv)

    def test_style_test(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        run_lint = is_travis_or_appveyor(env=['NAME_JENKINS']) is None
        _private_test_style_test(fLOG, run_lint, verbose='-v' in sys.argv)


if __name__ == "__main__":
    unittest.main()
