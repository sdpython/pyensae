"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
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

from pyquickhelper.loghelper import fLOG, run_cmd
from src.pyensae.remote import ASSHClient


class TestOutConnected (unittest.TestCase):

    def test_parsels(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        out = """Found 6 items
                                    drwx------   - xavierdupre xavierdupre          0 2014-11-18 01:00 .Trash
                                    drwx------   - xavierdupre xavierdupre          0 2014-11-16 02:38 .staging
                                    -rw-r--r--   3 xavierdupre xavierdupre    129.6 K 2014-11-16 02:37 ConfLongDemo_JSI.small.example.txt
                                    drwxr-xr-x   - xavierdupre xavierdupre          0 2014-11-16 02:38 ConfLongDemo_JSI.small.example2.walking.txt
                                    -rw-r--r--   3 xavierdupre xavierdupre    450.6 K 2014-11-20 01:33 paris.2014-11-11_22-00-18.331391.txt
                                    drwxr-xr-x   - xavierdupre xavierdupre          0 2014-11-20 01:53 velib_1hjs""".replace("                                    ", "")
        fLOG(out)
        for _ in out.split("\n"):
            __ = _.split()
            fLOG(len(__), __)
        parse = ASSHClient.parse_lsout(out)
        fLOG(parse.columns)
        assert list(
            parse.columns) == [
            'attributes',
            'code',
            'alias',
            'folder',
            'size',
            'unit',
            'name',
            'isdir']
        assert len(parse) > 0

    def test_script_pig(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        data = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data")

        pyth = """
                    import sys, datetime
                    cols = [ _ for _ in sys.argv if ".py" not in _ ]
                    for row in sys.stdin:
                        js = eval(row)
                        for station in js:
                            vals = [ station[c] for c in cols ]
                            sys.stdout.write(",".join(vals))
                            sys.stdout.write("\\n")
                            sys.stdout.flush()
                """.replace("                    ", "")

        fold = os.path.join(data, "..", "temp_pypig_out")
        if not os.path.exists(fold):
            os.mkdir(fold)

        pyfile = os.path.join(fold, "pystream.py")
        with open(pyfile, "w", encoding="utf8") as f:
            f.write(pyth)

        tosend = """[{'address': "52 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE - 75010 PARIS", 'collect_date': datetime.datetime(2014, 11, 11, 22, 1, 18, 331070), 'lng': 2.348395236282807, 'contract_name': """ + \
                 """'Paris', 'name': '10042 - POISSONNIÈRE - ENGHIEN', 'banking': 0, 'lat': 48.87242006305313, 'bonus': 0, 'status': 'OPEN', 'available_bikes': 32, 'last_update': datetime.datetime(2014, 11, 11, 21, 59, 5), """ + \
                 """'number': 10042, 'available_bike_stands': 1, 'bike_stands': 33}]"""

        cmd = sys.executable.replace(
            "pythonw",
            "python") + " " + pyfile + " name"
        out, err = run_cmd(cmd, wait=True, sin=tosend,
                           communicate=True, timeout=3, shell=False)
        fLOG("OUT\n", out)
        fLOG("ERR\n", err)
        assert len(out) > 0


if __name__ == "__main__":
    unittest.main()
