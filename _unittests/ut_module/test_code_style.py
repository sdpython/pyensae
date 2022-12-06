"""
@brief      test log(time=100s)
"""
import sys
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import ExtTestCase, is_travis_or_appveyor


class TestCodeStyle(ExtTestCase):

    def test_style_src(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae._pylint_common import _private_test_style_src
        run_lint = is_travis_or_appveyor(env=['NAME_JENKINS']) is None
        _private_test_style_src(fLOG, run_lint, verbose='-v' in sys.argv)

    def test_style_test(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        from pyensae._pylint_common import _private_test_style_test
        run_lint = is_travis_or_appveyor(env=['NAME_JENKINS']) is None
        _private_test_style_test(fLOG, run_lint, verbose='-v' in sys.argv)


if __name__ == "__main__":
    unittest.main()
