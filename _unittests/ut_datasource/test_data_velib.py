"""
@brief      test log(time=28s)
"""


import sys
import os
import unittest
import datetime
import pandas


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
from src.pyensae.datasource.data_velib import DataVelibCollect


class TestDataVelib (unittest.TestCase):

    def get_private_key(self):
        """
        retrive the key, this key is private and must not be shared through the source

        look at the code to see where I chose to put this key not shared in this file
        """
        file = os.path.abspath(os.path.split(__file__)[0])
        file = os.path.join(
            file,
            "..",
            "..",
            "..",
            "..",
            "_perso",
            "velib_password.txt")
        file = os.path.normpath(file)
        if not os.path.exists(file):
            fLOG("unable to find password at: " + file)
            return None
        with open(file, "r") as f:
            row = f.readlines()
        return row[0].strip(" \n\r\t")

    def test_datetime(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")
        f = 1368121860000.0
        d = datetime.datetime.fromtimestamp(f / 1000)
        if d != datetime.datetime(2013, 5, 9, 19, 51, 0):
            # issue with time (not the same local)
            if d.year != 2013 and d.month != 5 and d.day != 9:
                raise Exception("difference: " + str(d))

    def test_data_velib_json(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")

        fold = os.path.abspath(os.path.split(__file__)[0])
        tempfold = os.path.join(fold, "temp_data_i")
        if not os.path.exists(tempfold):
            os.mkdir(tempfold)

        temp_file = os.path.join(tempfold, "data_velib.txt")
        if os.path.exists(temp_file):
            os.remove(temp_file)
        assert not os.path.exists(temp_file)

        key = self.get_private_key()
        if key is None:
            return

        velib = DataVelibCollect(key)
        js = velib.get_json("Paris")

        assert isinstance(js, list)
        fLOG(type(js))
        nb = 0
        for o in js:
            fLOG(o)
            nb += 1
            if nb > 10:
                break
        assert nb > 0
        assert len(js) > 0

        tbl = pandas.DataFrame(js)
        tbl.to_csv(temp_file, sep="\t")
        assert os.path.exists(temp_file)
        fLOG(tbl[:10])

    def test_data_velib_json_collect(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")

        fold = os.path.abspath(os.path.split(__file__)[0])
        tempfold = os.path.join(fold, "temp_data_i2")
        if not os.path.exists(tempfold):
            os.mkdir(tempfold)

        for _ in os.listdir(tempfold):
            os.remove(os.path.join(tempfold, _))

        temp_file = os.path.join(tempfold, "data_velib.txt")

        delay = datetime.datetime.fromtimestamp(
            5.0) - datetime.datetime.fromtimestamp(0.)
        dt = datetime.datetime.now() + delay

        key = self.get_private_key()
        if key is None:
            return

        velib = DataVelibCollect(key)
        velib.collecting_data(
            "Paris",
            1000,
            temp_file,
            stop_datetime=dt,
            log_every=1,
            fLOG=fLOG)

        assert os.path.exists(temp_file)
        with open(temp_file, "r", encoding="utf8") as f:
            lines = f.readlines()
        if len(lines) < 1:
            raise Exception(
                "len(lines)<1: %d\n%s" %
                (len(lines), "\n".join(lines)))
        assert len(lines) < 10
        assert "\t" in lines[0]

        dt = datetime.datetime.now() + delay
        velib.collecting_data("Paris", 1000, temp_file, stop_datetime=dt,
                              single_file=False, log_every=1, fLOG=fLOG)
        res = os.listdir(tempfold)
        if len(res) <= 2:
            raise Exception(str(res))

    def test_data_velib_json_collect_func(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")

        fold = os.path.abspath(os.path.split(__file__)[0])
        tempfold = os.path.join(fold, "temp_data_func")
        if not os.path.exists(tempfold):
            os.mkdir(tempfold)

        for _ in os.listdir(tempfold):
            os.remove(os.path.join(tempfold, _))

        temp_file = os.path.join(tempfold, "data_velib.txt")

        delay = datetime.datetime.fromtimestamp(
            5.0) - datetime.datetime.fromtimestamp(0.)
        dt = datetime.datetime.now() + delay

        key = self.get_private_key()
        if key is None:
            return

        DataVelibCollect.run_collection(key,
                                        contract="Paris",
                                        delayms=1000,
                                        folder_file=temp_file,
                                        single_file=True,
                                        stop_datetime=dt,
                                        log_every=1,
                                        fLOG=fLOG)

        assert os.path.exists(temp_file)
        with open(temp_file, "r", encoding="utf8") as f:
            lines = f.readlines()
        if len(lines) < 1:
            raise Exception(
                "len(lines)<1: %d\n%s" %
                (len(lines), "\n".join(lines)))
        assert len(lines) < 10
        assert "\t" in lines[0]

    def test_data_velib_json_collect_func_besancon(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")

        fold = os.path.abspath(os.path.split(__file__)[0])
        tempfold = os.path.join(fold, "temp_data_func_bes")
        if not os.path.exists(tempfold):
            os.mkdir(tempfold)

        for _ in os.listdir(tempfold):
            os.remove(os.path.join(tempfold, _))

        temp_file = os.path.join(tempfold, "data_velib.txt")

        delay = datetime.datetime.fromtimestamp(
            5.0) - datetime.datetime.fromtimestamp(0.)
        dt = datetime.datetime.now() + delay

        key = self.get_private_key()
        if key is None:
            return

        DataVelibCollect.run_collection(key,
                                        contract="Besancon",
                                        delayms=1000,
                                        folder_file=temp_file,
                                        single_file=True,
                                        stop_datetime=dt,
                                        log_every=1,
                                        fLOG=fLOG)

        assert os.path.exists(temp_file)
        with open(temp_file, "r", encoding="utf8") as f:
            lines = f.readlines()
        if len(lines) < 1:
            raise Exception(
                "len(lines)<1: %d\n%s" %
                (len(lines), "\n".join(lines)))
        assert len(lines) < 10
        assert "\t" in lines[0]

    def test_data_velib_contract(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")

        key = self.get_private_key()
        if key is None:
            return

        velib = DataVelibCollect(key)
        cont = velib.get_contracts()
        fLOG("**", cont)
        assert len(cont) > 0


if __name__ == "__main__":
    unittest.main()
