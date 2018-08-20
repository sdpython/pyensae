# -*- coding: utf-8 -*-
"""
@brief      test log(time=43s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from pyquickhelper.ipythonhelper import execute_notebook_list, execute_notebook_list_finalize_ut


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


import src.pyensae


class TestRunNotebooks(unittest.TestCase):

    def test_run_notebook(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_run_notebooks")

        fnb = os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "_doc", "notebooks"))
        keepnote = []
        for nb in os.listdir(fnb):
            if ".ipynb" in nb and "velib" not in nb and "azure" not in nb and \
                    "ssh" not in nb and "checkpoints" not in nb and "hadoop" not in nb:
                keepnote.append(os.path.join(fnb, nb))

        def valid(cell):
            if "snakeviz" in cell:
                return False
            if 'run_cmd("SQLiteSpy.exe velib_vanves.db3")' in cell:
                return False
            if 'pandas.read_csv("flatfile_tab_pos2.txt"' in cell:
                return False
            return True

        def replace_cell(cell):
            return cell.replace("%encoding pyensae_sql_magic.ipynb",
                                "%encoding {0}/pyensae_sql_magic.ipynb".format(fnb))

        addpaths = [os.path.normpath(os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "..", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "pyquickhelper", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "jyquickhelper", "src")),
            os.path.normpath(os.path.join(
                os.path.abspath(os.path.dirname(__file__)), "..", "..", "..", "pymyinstall", "src"))
        ]

        res = execute_notebook_list(
            temp, keepnote, fLOG=fLOG, valid=valid, additional_path=addpaths,
            clean_function=replace_cell)
        execute_notebook_list_finalize_ut(
            res, fLOG=fLOG, dump=src.pyensae)


if __name__ == "__main__":
    unittest.main()
