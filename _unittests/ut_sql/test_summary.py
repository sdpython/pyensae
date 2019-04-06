# -*- coding: utf-8 -*-
"""
@brief      test log(time=13s)
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG, unzip
from pyquickhelper.pycode import get_temp_folder
from pyensae.sql import Database
from pyensae.sql.file_text_binary import TextFile


class TestSummary(unittest.TestCase):

    def test_summary(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        filename = os.path.join(os.path.split(
            __file__)[0], "data", "database_linked.zip")
        temp = get_temp_folder(__file__, "temp_summary")
        filename = unzip(filename, temp)
        assert os.path.exists(filename)

        db = Database(filename, LOG=fLOG)
        db.connect()

        res = db.summary()
        assert len(res) > 0
        db.close()

    def test_join(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")
        file1 = os.path.join(os.path.split(
            __file__)[0], "data", "tour1_2007.txt")
        file2 = os.path.join(os.path.split(
            __file__)[0], "data", "tour2_2007.txt")
        obj = TextFile(file1)
        temp = get_temp_folder(__file__, "temp_join")
        out = os.path.join(temp, "outjoin.txt")
        obj.join([(file2, "nom du département")], output=out)
        assert os.path.exists(out)


if __name__ == "__main__":
    unittest.main()
