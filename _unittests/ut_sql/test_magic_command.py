"""
@brief      test log(time=10s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import random


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
from src.pyensae.sql.magic_sql import MagicSQL


class TestMagicCommand(unittest.TestCase):

    def test_command_magic(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_magic_command")
        data = os.path.join(temp, "..", "data", "velib_vanves.txt")
        dbfile = os.path.join(temp, "temp_magic.db3")

        # connect
        magic = MagicSQL()
        magic.add_context({"unittest": None})
        magic.SQL_connect(dbfile)
        assert "DB" in magic.Context

        # import
        fLOG("import")
        magic.SQL_import_tsv(data)
        tables = magic.SQL_tables()
        assert "velib_vanves" in tables

        # schema
        fLOG("schema")
        sch = magic.SQL_schema("velib_vanves --as_list")
        magic.SQL_refresh_completion()
        fLOG(sch)
        assert sch is not None
        assert sch[0] == ('address', str)

        # view
        fLOG("view")
        head = magic.SQL("--df=dfo", "SELECT * FROM velib_vanves")
        fLOG(head.shape)
        dbo = magic.Context["dfo"]
        fLOG(dbo.shape)

        # view 2
        fLOG("view 2")
        full = magic.SQL('-q "SELECT * FROM velib_vanves"')
        fLOG(full.shape)
        assert full.shape == dbo.shape

        # import df
        fLOG("import df")
        magic.Context["ttt"] = full
        magic.SQL_import_df("ttt")
        tables = magic.SQL_tables()
        assert "ttt" in tables

        # add function
        fLOG("add function")

        def binomiale(p):
            return 1 if random.random() > p else 0
        magic.add_context({"binomiale": binomiale})
        magic.SQL_add_function("binomiale")
        full = magic.SQL(
            '', "SELECT SUM(bin) AS total FROM (SELECT *, binomiale(0.5) AS bin FROM velib_vanves)")
        if full.values[0][0] > 8000:
            raise Exception(str(full.values[0][0]))

        # close
        magic.SQL_drop_table("velib_vanves")
        tables = magic.SQL_tables()
        if "velib_vanves" in tables:
            raise Exception(tables)
        magic.SQL_close()


if __name__ == "__main__":
    unittest.main()
