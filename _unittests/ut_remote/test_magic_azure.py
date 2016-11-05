"""
@brief      test log(time=140s)

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
from src.pyensae.remote.magic_azure import MagicAzure

thisfold = os.path.abspath(os.path.split(__file__)[0])
thiscomm = os.path.join(thisfold, "..")
sys.path.append(thiscomm)


class MockObject:
    pass


class TestMagicAzure(unittest.TestCase):

    def test_blob_path(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mg = MagicAzure()
        mg.shell = MockObject()
        mg.shell.user_ns = {"remote_azure_client": MockObject(),
                            "remote_azure_blob": MockObject()}
        mg.shell.user_ns["remote_azure_client"].account_name = "ACC"
        cmd = "/part1/part2"
        fLOG("**", cmd)
        res = mg.blob_path(cmd)
        fLOG(res)
        self.assertEqual(res, ('ACC', 'part1/part2'))
        res = mg.blob_path("part1/part2")
        fLOG(res)
        self.assertEqual(res, ('part1', 'part2'))


if __name__ == "__main__":
    unittest.main()
