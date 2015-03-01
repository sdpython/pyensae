"""
@brief      test log(time=28s)
"""


import sys
import os
import unittest
import datetime
import pandas
import datetime


try:
    import src
    import pyquickhelper
    import pymyinstall
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
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "pymyinstall",
                "src")))
    if path not in sys.path:
        sys.path.append(path)
    import src
    import pyquickhelper
    import pymyinstall

from pyquickhelper import fLOG
from src.pyensae.datasource.data_velib import DataVelibCollect


class TestDataVelibOffline (unittest.TestCase):

    def test_data_velib_contract(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")
        fold = os.path.abspath(os.path.split(__file__)[0])
        data = os.path.join(fold, "data")

        df = DataVelibCollect.to_df(data)
        # fLOG(df.head())
        assert len(df) > 0

        stations = df[["name", "lat", "lng"]]
        gr = stations.groupby(["name", "lat", "lng"], as_index=False).sum()
        # fLOG(gr.head())
        assert len(gr) >= 30

        df.to_csv(os.path.join(fold, "out_data.txt"), sep="\t", index=False)
        dt = datetime.datetime(2014, 5, 22, 11, 49, 27, 523164)
        sub = df[df["collect_date"] == dt]
        fig, ax, plt = DataVelibCollect.draw(sub)

    def test_data_velib_animation(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__",
            LogFile="temp_hal_log2.txt")
        fold = os.path.abspath(os.path.split(__file__)[0])
        data = os.path.join(fold, "data")

        if "travis" in sys.executable:
            return

        try:
            from JSAnimation import IPython_display
        except ImportError:
            import pymyinstall
            pymyinstall.ModuleInstall(
                "JSAnimation",
                "github",
                "jakevdp").install(
                temp_folder="c:\\temp")

        df = DataVelibCollect.to_df(data)
        anime = DataVelibCollect.js_animation(df)
        
        from JSAnimation import HTMLWriter
        wr = HTMLWriter(embed_frames=False)
        anime.save(os.path.join(fold, "out_animation.html"), writer=wr)

if __name__ == "__main__":
    unittest.main()
