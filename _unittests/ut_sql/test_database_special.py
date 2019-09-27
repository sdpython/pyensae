"""
@brief      test log(time=13s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG, unzip
from pyquickhelper.pycode import get_temp_folder
from pyensae.sql import Database


class TestDatabaseSpecial (unittest.TestCase):

    def test_cross_1(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ ==
             "__main__", LogFile="temp_hal_log2.txt")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_cross_1")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        sql = """CROSS pos PLACE nb_click,url FROM url_QSSH ORDER BY nb_click -- comment
                    DESC LIMIT 100"""
        cur = db.execute(sql)
        mat = list(cur)
        view = db.execute_view(sql, add_column_name=True)
        self.assertEqual(len(view), len(mat) + 1)
        self.assertEqual(view[0], ['1;nb_click', '1;url', '2;nb_click', '2;url', '3;nb_click', '3;url',
                                   '4;nb_click', '4;url', '5;nb_click', '5;url', '6;nb_click', '6;url', '7;nb_click',
                                   '7;url', '8;nb_click', '8;url', '9;nb_click',
                                   '9;url', '10;nb_click', '10;url', '11;nb_click', '11;url', '12;nb_click',
                                   '12;url', '13;nb_click', '13;url', '14;nb_click',
                                   '14;url', '15;nb_click', '15;url', '16;nb_click', '16;url', '18;nb_click', '18;url'])
        self.assertEqual(len(view[0]), len(view[1]))

        exp = {
            1: [268.0, 'www.facebook.com/login.php', 97.0, 'www.friendster.com/login.php',
                29.0, 'https://login.facebook.com/login.php', 15.0,
                'https://login.yahoo.com/', 10.0, 'https://login.facebook.com/login.php', 10.0,
                'lite.facebook.com/login/?next=http%3A%2F%2Flite.facebook.com%2Ftheamloong%2Fvideo%2Fof%2FTNT-sanshou',
                13.0, 'lite.facebook.com/login/?next=http%3A%2F%2Flite.facebook.com%2Ftheamloong%2Fvideo%2Fof%2FTNT-sanshou',
                5.0, 'https://login.verizonwireless.com/amserver/UI/Login', 6.0, 'https://login.facebook.com/login.php', 2.0,
                'https://login.comcast.net/', 0.0, 'HottieMatchUp.com/matchcomlogin', 0.0,
                'FreshPCFix.com/loginscreen', 0.0, 'FreshPCFix.com/loginscreen', 0.0,
                'login.marketingblacksmith.com', 0.0, 'sites.managerslogin.com', 0.0,
                'sites.managerslogin.com', 0.0, 'sites.managerslogin.com'],
            -1: [3.0, 'https://sso.uboc.com/obc/forms/login.fcc?user_type=R', 3.0,
                 'https://www.atitesting.com/login.aspx', 1.0, 'askabouttech.com/how-to-bypass-login-password-on-windows-vista/',
                 1.0, 'homegrownfreaks.net/forums/login.html',
                 1.0, 'https://trade.htsc.com.cn/webtrade/login/loginAction1.do?method=preLogin2&opType=TD',
                 1.0, 'moodle.dist113.org/login/in/in.php?p=addicting+games+the+impossible+quiz',
                 1.0, 'www.edweek.org/login.html?source=http://www.edweek.org/ew/articles/2009/08/25/02sat.h29.html&destina',
                 1.0, 'www.gifs.net/image/Holidays/Birthday/Cake/9451?n=login.php3',
                 1.0, 'www.grazeit.com/pages/blackplanet-com-login-1814/', 1.0, 'www.myspace-login.us/',
                 None, None, None, None, None, None, None, None, None, None, None, None, None, None],
        }

        for k, v in exp.items():
            if view[k] != v:
                if len(view[k]) != len(v):
                    raise Exception(
                        "exp[%d] and view [%d] have different lengths" % (k, k))
                for a, b in zip(v, view[k]):
                    if a != b:
                        raise Exception(
                            "k=%d, different values\nexp %s\n != %s" % (k, str(a), str(b)))

        self.assertEqual(len(view[0]), len(view[-1]))

        sql = """CROSS pos PLACE nb_click FROM url_QSSH ORDER BY nb_click -- comment
                    DESC LIMIT 100"""
        cur = db.execute(sql)
        mat = list(cur)
        view = db.execute_view(sql, add_column_name=True)
        self.assertEqual(len(view), len(mat) + 1)
        self.assertEqual(len(view[0]), len(view[1]))

        sql = """CROSS pos,pos PLACE nb_click FROM url_QSSH ORDER BY nb_click -- comment
                    DESC LIMIT 100"""
        cur = db.execute(sql)
        mat = list(cur)
        view = db.execute_view(sql, add_column_name=True)
        self.assertEqual(len(view), len(mat) + 1)
        self.assertEqual(len(view[0]), len(view[1]))

        db.close()

    def test_unicode(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ ==
             "__main__", LogFile="temp_hal_log2.txt")
        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_unicode")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        file = os.path.join(os.path.split(__file__)[0], "data", "unicode.txt")
        assert os.path.exists(file)

        def filter_case(s):
            return s.replace(" ", "")

        db.import_table_from_flat_file(
            file, "uni", columns=None, header=True, filter_case=filter_case)

        sql = "select * from uni limit 2"
        view = db.execute_view(sql)
        exp = [[(b'.\u904a\u6232\u6a5f\u5730'.decode("utf8"),
                 b'.\u904a\u6232\u57fa\u5730'.decode("utf8"),
                 0.66666666666700003, 4, 6, 0.0, 0.0, 0, 0.0, 1, 0.0, 0,
                 0.25, 1, 999999999, 999999999, 0, 1, 3, 1,
                 0.66666666666700003),
                (b'0401\u5f71\u97f3live\u79c0'.decode("utf8"),
                 b'0401\u5f71\u97f3\u8996\u8a0a'.decode("utf8"),
                 0.41666666666699997, 5, 12, 0.0, 0.45454545454500001,
                 5, 0.27272727272699998, 1, 0.5, 4, 0.5, 2, 999999999,
                 999999999, 0, 1, 2, 0, 1.0)],
               [(b'.\xe9\x81\x8a\xe6\x88\xb2\xe6\xa9\x9f\xe5\x9c\xb0'.decode("utf8"),
                 b'.\xe9\x81\x8a\xe6\x88\xb2\xe5\x9f\xba\xe5\x9c\xb0'.decode(
                   "utf8"),
                   0.666666666666667, 4, 6, 0.0, 0.0, 0, 0.0, 1, 0.0, 0, 0.25, 1, 999999999, 999999999, 0, 1, 3, 1, 0.666666666666667),
                (b'0401\xe5\xbd\xb1\xe9\x9f\xb3live\xe7\xa7\x80'.decode("utf8"),
                   b'0401\xe5\xbd\xb1\xe9\x9f\xb3\xe8\xa6\x96\xe8\xa8\x8a'.decode(
                    "utf8"),
                   0.416666666666667, 5, 12, 0.0, 0.454545454545455, 5, 0.272727272727273,
                   1, 0.5, 4, 0.5, 2, 999999999, 999999999, 0, 1, 2, 0, 1.0)],
               ]
        if view not in exp:
            print("2", str(view).encode("utf8"))
            i = 0
            for a, b in zip(exp[1], view):
                if a != b:
                    print("i", i)
                    if isinstance(a, tuple):
                        for c, d in zip(a, b):
                            print("1", c)
                            print("2", d)
                    else:
                        print("1", a)
                        print("2", b)
                i += 1
            raise Exception("problem")

        db.close()

    def test_attach_database(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ ==
             "__main__", LogFile="temp_hal_log2.txt")

        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_attach_database")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        file2 = os.path.join(os.path.split(__file__)[
                             0], "data", "database_linked_cor.zip")
        temp = get_temp_folder(__file__, "temp_attach_database")
        file2 = unzip(file2, temp)
        assert os.path.exists(file2)

        # method 1
        attach = {"seco": file2}

        db = Database(filename, attach=attach, LOG=fLOG)
        db.connect()

        sql = "SELECT COUNT(*) FROM seco.word_QSSH"
        vie = db.execute_view(sql)
        self.assertEqual(len(vie), 1)
        db.close()

        # method 2
        all = filename + " ; seco , " + file2

        db = Database(all, LOG=fLOG)
        db.connect()

        sql = "SELECT COUNT(*) FROM seco.word_QSSH"
        vi2 = db.execute_view(sql)
        self.assertEqual(len(vi2), 1)
        self.assertEqual(vi2, vie)

        att = db.get_attached_database_list()
        self.assertEqual(att, ['seco'])
        ts = db.get_table_list(True)
        self.assertEqual(ts, ['seco.query',
                              'seco.idx_query_query', 'seco.qtok', 'seco.idx_qtok_qtok',
                              'seco.pairs', 'seco.pairs_query___q1', 'seco.bucket', 'seco.idx_bucket_bucket',
                              'seco.url', 'seco.idx_url_url', 'seco.profile', 'seco.profile_query___',
                              'seco.profile_QRW2', 'seco.profile_QRW2_query___', 'seco.profile_QSSH',
                              'seco.profile_QSSH_query___', 'seco.query_QRW2', 'seco.query_QRW2_query___',
                              'seco.query_QSSH', 'seco.query_QSSH_query___', 'seco.url_QRW2', 'seco.url_QRW2_url___',
                              'seco.url_QSSH', 'seco.url_QSSH_url___', 'seco.word', 'seco.idx_word_word',
                              'seco.word_QRW2', 'seco.word_QRW2_word___', 'seco.word_QSSH', 'seco.word_QSSH_word___'])

        assert "db.attach_database" in db.get_python_code()[1]
        assert db.has_table("seco.word_QSSH_word___")
        files = db.get_file(True)

        file = db.get_file()
        assert file in files
        for alias, file in db.get_attached_database_list(True):
            assert alias in files
            assert file in files

        db2 = Database(files, LOG=fLOG)
        db2.connect()
        db2.close()

        db.close()


if __name__ == "__main__":
    unittest.main()
