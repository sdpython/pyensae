"""
@brief      test log(time=132s)
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


from pyquickhelper.ipythonhelper.notebook_helper import install_python_kernel_for_unittest
from pyquickhelper.ipythonhelper import run_notebook
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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

        def valid(code):
            return 'run_cmd("SQLiteSpy.exe velib_vanves.db3")' not in code

        if "travis" in sys.executable:
            return

        kernel_name = None if "travis" in sys.executable else install_python_kernel_for_unittest(
            "pyensae")

        out = run_notebook(nbfile,
                           working_dir=temp,
                           outfilename=outfile,
                           additional_path=addpath,
                           valid=valid,
                           fLOG=fLOG,
                           kernel_name=kernel_name)
        fLOG(out)
        assert os.path.exists(outfile)


if __name__ == "__main__":
    unittest.main()
