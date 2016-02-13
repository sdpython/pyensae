"""
@brief      test log(time=13s)
"""

import sys
import os
import unittest

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


from pyquickhelper import fLOG, get_temp_folder, unzip
from src.pyensae.sql import Database


class TestDatabaseJoin (unittest.TestCase):

    _memo_SQL1 = """SELECT query               AS query,
           profile_QSSH.pos    AS profile_QSSH_pos,
           type                AS type,
           bucket              AS bucket,
           max_nb              AS max_nb,
           sum_difftime        AS sum_difftime,
           profile_QSSH.url    AS url,
           url_QSSH.pos        AS url_QSSH_pos,
           co                  AS co,
           nb_view             AS nb_view,
           sum_nb_view         AS sum_nb_view,
           sum_difftime_view   AS sum_difftime_view,
           nb_click            AS nb_click,
           sum_nb_click        AS sum_nb_click,
           sum_difftime_click  AS sum_difftime_click
        FROM profile_QSSH
        JOIN url_QSSH
        ON     profile_QSSH.url == url_QSSH.url
        """

    _memo_SQL2 = """SELECT query               AS query,
           profile_QSSH.pos    AS pos,
           type                AS type,
           bucket              AS bucket,
           max_nb              AS max_nb,
           sum_difftime        AS sum_difftime,
           profile_QSSH.url    AS url,
           co                  AS co,
           nb_view             AS nb_view,
           sum_nb_view         AS sum_nb_view,
           sum_difftime_view   AS sum_difftime_view,
           nb_click            AS nb_click,
           sum_nb_click        AS sum_nb_click,
           sum_difftime_click  AS sum_difftime_click
        FROM profile_QSSH
        INNER JOIN url_QSSH
        ON     profile_QSSH.url == url_QSSH.url
           AND profile_QSSH.pos == url_QSSH.pos
        WHERE bucket == 'bu###1'
        """

    def test_join_bis(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_join_bis")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        sql = "SELECT COUNT(*) FROM profile_QSSH"
        exe = db.execute_view(sql)
        assert exe[0][0] == 16

        sql, fields = db.inner_join("profile_QSSH", "url_QSSH",
                                    "url", None,
                                    execute=False,
                                    create_index=False,
                                    unique=False)
        sql = sql.strip(" \n\r\t")
        tep = TestDatabaseJoin._memo_SQL1.strip(" \n\r\t")
        if sql.replace(" ", "") != tep.replace(" ", ""):
            print(sql)
            raise Exception("sql queries should be identifical")

        assert fields == [('query', 'query'), ('profile_QSSH.pos', 'profile_QSSH_pos'), ('type', 'type'), ('bucket', 'bucket'), ('max_nb', 'max_nb'), ('sum_difftime', 'sum_difftime'), ('profile_QSSH.url', 'url'), ('url_QSSH.pos', 'url_QSSH_pos'),
                          ('co', 'co'), ('nb_view', 'nb_view'), ('sum_nb_view', 'sum_nb_view'), ('sum_difftime_view', 'sum_difftime_view'), ('nb_click', 'nb_click'), ('sum_nb_click', 'sum_nb_click'), ('sum_difftime_click', 'sum_difftime_click')]
        view = db.execute_view(sql)
        assert len(view) == 2

        sql, fields = db.inner_join("profile_QSSH", "url_QSSH",
                                    ("url", "pos"), None,
                                    execute=False,
                                    create_index=False,
                                    where="bucket == 'bu###1'")
        sql = sql.strip(" \n\r\t")
        tep = TestDatabaseJoin._memo_SQL2.strip(" \n\r\t")
        if sql.replace(" ", "") != tep.replace(" ", ""):
            for a, b in zip(sql.split("\n"), tep.split("\n")):
                print("res", a)
                print("exp", b)
                print(a == b)
        assert sql.replace(" ", "") == tep.replace(" ", "")
        assert fields == [('query', 'query'), ('profile_QSSH.pos', 'pos'), ('type', 'type'), ('bucket', 'bucket'), ('max_nb', 'max_nb'), ('sum_difftime', 'sum_difftime'), ('profile_QSSH.url', 'url'), ('co', 'co'), (
            'nb_view', 'nb_view'), ('sum_nb_view', 'sum_nb_view'), ('sum_difftime_view', 'sum_difftime_view'), ('nb_click', 'nb_click'), ('sum_nb_click', 'sum_nb_click'), ('sum_difftime_click', 'sum_difftime_click')]
        view = db.execute_view(sql)
        assert len(view) == 1

        db.close()

    def test_histogram(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_histogram")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        sql = db.histogram("url_QRW2",
                           col_sums=["sum_nb_click"],
                           columns=("pos", "url"))
        view = db.execute_view(sql)
        assert len(view) == 38216

        sql = db.histogram("url_QRW2",
                           col_sums=["sum_nb_click"],
                           columns="url")
        view = db.execute_view(sql)
        assert len(view) == 28436

        sql = db.histogram("url_QRW2",
                           col_sums=["sum_nb_click"],
                           columns="pos",
                           values=[1, 2, 3, 4, 5])
        view = db.execute_view(sql)
        assert view == [(1, 2370, 87049), (2, 5734, 11522),
                        (3, 4009, 5383), (4, 4304, 1778), (5, 21799, 3588)]

        sql = db.histogram("url_QRW2",
                           col_sums=["sum_nb_click"],
                           columns="pos",
                           values={"pos123": [1, 2, 3], "others": [4, 5, 6, 7, 8, 9, 10]})
        view = db.execute_view(sql)
        assert view == [('none', 21, 0), ('others', 26082,
                                          5366), ('pos123', 12113, 103954)]

        db.close()

    def test_histogram2(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_histogram2")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        sql = db.histogram("url_QRW2",
                           values={"cat1": [(1, 1), (1, 0)], "cat2": [
                               (1, 10), (2, 10), (2, 1)]},
                           col_sums=["sum_nb_click"],
                           columns=("pos", "co"))
        view = db.execute_view(sql)
        assert view == [('cat1', 1115, 15), ('cat2', 3792,
                                             411), ('none', 33309, 108894)]

        db.close()


if __name__ == "__main__":
    unittest.main()
