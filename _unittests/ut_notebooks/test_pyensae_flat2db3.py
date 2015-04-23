"""
@brief      test log(time=132s)
"""

import sys
import os
import unittest
import re

try:
    import src
    import pyquickhelper
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
    import pyquickhelper


from pyquickhelper.ipythonhelper.notebook_helper import run_notebook
from pyquickhelper import get_temp_folder, fLOG


class TestNotebookRunnerFlat2Db3 (unittest.TestCase):

    def test_notebook_runner_flat2db3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        notebook = os.path.split(
            __file__)[-1].replace(".ipynb", "").replace(".py", "")[5:]
        temp = get_temp_folder(__file__, "temp_" + notebook)
        nbfile = os.path.join(
            temp,
            "..",
            "..",
            "..",
            "_doc",
            "notebooks",
            "%s.ipynb" %
            notebook)
        if not os.path.exists(nbfile):
            raise FileNotFoundError(nbfile)
        addpath = [os.path.normpath(os.path.join(temp, "..", "..", "..", "src")),
                   os.path.normpath(
            os.path.join(
                temp,
                "..",
                "..",
                "..",
                "..",
                "pyquickhelper",
                "src")),
            os.path.normpath(
            os.path.join(
                temp,
                "..",
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")),
        ]
        outfile = os.path.join(temp, "out_notebook.ipynb")
        assert not os.path.exists(outfile)
        valid = lambda code: 'run_cmd("SQLiteSpy.exe velib_vanves.db3")' not in code

        if "travis" in sys.executable:
            return

        out = run_notebook(nbfile, working_dir=temp, outfilename=outfile, additional_path=addpath,
                           valid=valid, fLOG=fLOG)
        fLOG(out)
        assert os.path.exists(outfile)


if __name__ == "__main__":
    unittest.main()
