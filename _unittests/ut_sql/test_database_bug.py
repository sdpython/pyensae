"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import random
import pandas


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

from pyquickhelper import fLOG
from src.pyensae.sql.database_helper import import_flatfile_into_database
from src.pyensae.sql.database_main import Database


class TestDatabaseBug (unittest.TestCase):

    def test_import_flatflit(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fold = os.path.abspath(os.path.split(__file__)[0])
        temp = os.path.join(fold, "temp_db_bug")
        if not os.path.exists(temp):
            os.mkdir(temp)

        text = [
            "one",
            "two",
            "three",
            "four",
            "five",
            "six",
            "seven",
            "eight",
            "nine",
            "ten"]
        data = [{"name": text[random.randint(0, 9)], "number": random.randint(0, 99)}
                for i in range(0, 10000)]

        filename = os.path.join(temp, "out_flatfile_tab_pos2.txt")

        datatab = data[:1] + [{"name": " one\ttab", "number": 100}] + data[1:]
        df = pandas.DataFrame(datatab)
        df.to_csv(
            filename,
            sep="\t",
            encoding="utf8",
            header=True,
            index=False)
        with open(filename, "r", encoding="utf8") as f:
            content = f.read()
        content = content.replace('"', '')
        with open(filename + ".2.txt", "w", encoding="utf8") as f:
            f.write(content)

        dbfile = os.path.join(fold, "out_db.db3")
        if os.path.exists(dbfile):
            os.remove(dbfile)

        import_flatfile_into_database(
            dbfile,
            filename +
            ".2.txt",
            table="example",
            fLOG=fLOG)

        db = Database(dbfile, LOG=fLOG)
        db.connect()
        count = db.get_table_nb_lines("example")
        sch = db.get_table_columns("example")
        values = db.execute_view("SELECT * FROM example")
        db.close()

        if count != 10001:
            rows = [str(v) for v in values][:10]
            mes = "\n".join(rows)
            fLOG(datatab[:3])
            raise Exception(
                "expect:10001 not {0}\nROWS:\n{1}".format(
                    count,
                    mes))

        exp = [('name', str), ('number', int)]
        if sch != exp:
            raise Exception("{0}!={1} ({2})".format(sch, exp, len(datatab)))


if __name__ == "__main__":
    unittest.main()
