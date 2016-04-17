"""
@brief      test log(time=11s)
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


from pyquickhelper.loghelper import fLOG, unzip
from pyquickhelper.pycode import get_temp_folder
from src.pyensae.sql import Database


class TestDatabaseJoinMultiple (unittest.TestCase):

    def test_join_multiple2(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_join_multiple2")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        where = {"bucket": ("==", "bu###1")}
        n1 = db.JoinTreeNode("profile_QSSH", where=where,
                             parent_key="query", key="query")
        n2 = db.JoinTreeNode("url_QSSH", where=where,
                             parent_key=('url', 'pos'), key=('url', 'pos'))
        n1.append(n2)

        sql, fields = db.inner_joins(n1, execute=False, create_index=False)

        view = db.execute_view(sql)
        assert view == [('facebbooklogin', 1, 0, 'bu###1', 86, 0,
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         1, 0, 1, 1, 0, 0, 0, 0)]
        assert "WHERE" in sql

        db.close()

    def test_join_multiple2bis(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_join_multiple2bis")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        where = {("profile_QSSH", "bucket"): ("==", "bu###1")}
        n1 = db.JoinTreeNode("profile_QSSH", where=where,
                             parent_key="query", key="query")
        n2 = db.JoinTreeNode("url_QSSH", where=where,
                             parent_key=('url', 'pos'), key=('url', 'pos'))
        n1.append(n2)

        sql, fields = db.inner_joins(n1, execute=False, create_index=False)

        view = db.execute_view(sql)
        assert "WHERE" in sql
        assert view == [('facebbooklogin', 1, 0, 'bu###1', 86, 0,
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         1, 0, 1, 1, 0, 0, 0, 0)]

        where = {("profile_QSSH.bucket"): ("==", "bu###1")}
        n1 = db.JoinTreeNode("profile_QSSH", where=where,
                             parent_key="query", key="query")
        n2 = db.JoinTreeNode("url_QSSH", where=where,
                             parent_key=('url', 'pos'), key=('url', 'pos'))
        n1.append(n2)

        sql, fields = db.inner_joins(n1, execute=False, create_index=False)

        view = db.execute_view(sql)
        assert "WHERE" in sql
        assert view == [('facebbooklogin', 1, 0,
                         'bu###1', 86, 0,
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs',
                         1, 0, 1, 1, 0, 0, 0, 0)]

        db.close()

    def test_join_multiple3(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_join_multiple3")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        where = {"bucket": ("==", "bu###1")}
        root = db.JoinTreeNode("query_QSSH", where=where)
        n1 = db.JoinTreeNode("profile_QSSH", where=where,
                             parent_key="query", key="query")
        n2 = db.JoinTreeNode("url_QSSH", where=where,
                             parent_key=('url', 'pos'), key=('url', 'pos'))
        root.append(n1)
        n1.append(n2)

        sql, fields = db.inner_joins(root,
                                     execute=False,
                                     create_index=False)

        view = db.execute_view(sql)
        assert view == [('facebbooklogin', 'bu###1', 86, 157, 520, 0, 63, 0, 503, 0, 619, 1, 3906365, 'facebbooklogin', 1, 0, 'bu###1', 86, 0,
                         'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs', 'digg.com/security/Hackers_Put_Social_Networks_In_Crosshairs', 1, 0, 1, 1, 0, 0, 0, 0)]
        assert fields == [('query', 'query_QSSH', 'query'), ('bucket', 'query_QSSH', 'bucket'), ('nbq', 'query_QSSH', 'nbq'), ('sum_num', 'query_QSSH', 'sum_num'), ('sum_view_url', 'query_QSSH', 'sum_view_url'),
                          ('sum_click_url', 'query_QSSH', 'sum_click_url'), ('sum_rewrite', 'query_QSSH', 'sum_rewrite'), (
                              'sum_click_ads', 'query_QSSH', 'sum_click_ads'), ('sum_max_pos_view', 'query_QSSH', 'sum_max_pos_view'),
                          ('sum_max_pos_click', 'query_QSSH', 'sum_max_pos_click'), (
                              'sum_duration', 'query_QSSH', 'sum_duration'),
                          ('sum_unknown', 'query_QSSH', 'sum_unknown'), ('sum_daysec',
                                                                         'query_QSSH', 'sum_daysec'), ('aquery', 'profile_QSSH', 'query'),
                          ('apos', 'profile_QSSH', 'pos'), ('atype',
                                                            'profile_QSSH', 'type'),
                          ('abucket', 'profile_QSSH', 'bucket'), ('amax_nb', 'profile_QSSH', 'max_nb'), ('asum_difftime',
                                                                                                         'profile_QSSH', 'sum_difftime'), ('aurl', 'profile_QSSH', 'url'), ('aaurl', 'url_QSSH', 'url'),
                          ('aapos', 'url_QSSH', 'pos'), ('aaco', 'url_QSSH', 'co'), ('aanb_view',
                                                                                     'url_QSSH', 'nb_view'), ('aasum_nb_view', 'url_QSSH', 'sum_nb_view'),
                          ('aasum_difftime_view', 'url_QSSH', 'sum_difftime_view'), ('aanb_click', 'url_QSSH', 'nb_click'), ('aasum_nb_click', 'url_QSSH', 'sum_nb_click'), ('aasum_difftime_click', 'url_QSSH', 'sum_difftime_click')]
        assert "WHERE" in sql
        db.close()


if __name__ == "__main__":
    unittest.main()
