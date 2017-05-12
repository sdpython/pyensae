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
from pyquickhelper.pycode import get_temp_folder
from src.pyensae.languages.rconverter import r2python


class TestPRConverter(unittest.TestCase):

    def test_rconverter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_rconverter")
        scripts = [os.path.join(temp, "..", "data", "r1.r")]
        for script in scripts:
            with open(script, "r", encoding="utf-8") as f:
                code = f.read()
            pycode = r2python(code)
            new_file = os.path.join(temp, os.path.split(script)[-1] + ".py")
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(pycode)
            fLOG(pycode)


if __name__ == "__main__":
    unittest.main()
