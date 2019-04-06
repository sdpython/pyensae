"""
@brief      test log(time=1s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyensae.sql.database_helper import import_flatfile_into_database
from pyensae.sql import InterfaceSQL, InterfaceSQLException


class TestInterfaceSQL (unittest.TestCase):

    def test_interface_sql(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        file = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data",
            "ACA.PA.txt")
        dbf = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_database_int.db3")
        if not os.path.exists(dbf):
            import_flatfile_into_database(dbf, file, fLOG=fLOG)
        assert os.path.exists(dbf)

        face = InterfaceSQL.create(dbf)
        face.connect()

        tbls = face.get_table_list()
        fLOG(tbls)
        assert 'ACAPA' in tbls

        cols = face.get_table_columns('ACAPA')
        fLOG(cols)
        assert cols == {0: ('Date', str),
                        1: ('Open', float),
                        2: ('High', float),
                        3: ('Low', float),
                        4: ('Close', float),
                        5: ('Volume', int),
                        6: ('Adj_Close', float)}

        assert face.CC.ACAPA._ == "ACAPA"
        assert face.CC.ACAPA.Date._ == "Date"

        sql = "SELECT COUNT(*) FROM ACAPA"
        df = face.execute(sql)
        fLOG(df)
        assert df.columns == ["COUNT(*)"]
        assert len(df) == 1
        assert df.values[0][0] == 2333

        sql = "SELECT COUNT(*) FROM DB.CC.ACAPA"
        face.execute(sql)
        fLOG(df)
        assert df.columns == ["COUNT(*)"]
        assert len(df) == 1
        assert df.values[0][0] == 2333

        def minc(x):
            return x + 1

        face.add_function(minc)
        sql = "SELECT minc(nb) FROM ( SELECT COUNT(*) AS nb FROM ACAPA )"
        df = face.execute(sql)
        assert df.values[0][0] == 2334

        if 'newtable' in face.get_table_list():
            face.drop_table('newtable')

        face.import_dataframe("newtable", df)
        assert "newtable" in face.get_table_list()

        sql = "SELECT blblable"
        try:
            df = face.execute(sql)
        except InterfaceSQLException:
            pass

        face.close()

    def test_import_sql(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        file = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data",
            "ACA.PA.txt")
        dbf = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "temp_database_inti.db3")
        if os.path.exists(dbf):
            os.remove(dbf)
        assert not os.path.exists(dbf)

        face = InterfaceSQL.create(dbf)
        face.connect()

        face.import_flat_file(file, "ACAPA2")
        assert face.CC.ACAPA2._ == "ACAPA2"

        face.close()


if __name__ == "__main__":
    unittest.main()
