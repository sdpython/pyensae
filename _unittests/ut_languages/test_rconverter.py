"""
@brief      test log(time=3s)

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

        data = os.path.join(temp, "..", "data")
        files = os.listdir(data)
        rfiles = [os.path.join(data, _) for _ in sorted(files) if ".r" in _]
        pyfiles = [os.path.join(data, _) for _ in sorted(files) if ".pyr" in _]
        self.assertEqual(len(rfiles), len(pyfiles))
        self.assertTrue(len(rfiles) > 0)

        i = 0
        for exp, script in zip(pyfiles, rfiles):
            fLOG(os.path.split(script)[-1])
            with open(script, "r", encoding="utf-8") as f:
                code = f.read()

            try:
                pycode = r2python(code, pep8=True)
            except Exception as e:
                fLOG(code)
                pycode = r2python(code, pep8=True, fLOG=fLOG)
                raise e

            new_file = os.path.join(
                temp, "pr" + str(i) + os.path.splitext(script)[-1] + ".py")
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(pycode)

            try:
                comp = compile(pycode, new_file, "exec")
            except Exception as e:
                fLOG(pycode)
                pycode = r2python(code, pep8=True, fLOG=fLOG)
                raise e

            self.assertTrue(comp is not None)

            with open(exp, "r", encoding="utf-8") as f:
                expcode = f.read()

            self.maxDiff = None
            if expcode.strip(" \n") != pycode.strip(" \n"):
                fLOG(pycode)
                pycode = r2python(code, pep8=True, fLOG=fLOG)
            self.assertEqual(expcode.strip(" \n"), pycode.strip(" \n"))


if __name__ == "__main__":
    unittest.main()
