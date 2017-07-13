"""
@brief      test log(time=201s)

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

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, is_travis_or_appveyor
from src.pyensae.file_helper import run_jython, is_java_installed, download_java_standalone
from src.pyensae.remote.magic_azure import MagicAzure
from src.pyensae.file_helper.magic_file import MagicFile


class TestJython (unittest.TestCase):

    def test_simple_jython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            return

        download_java_standalone()
        assert is_java_installed()

        this = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.join(this, "temp_jython")
        if not os.path.exists(temp):
            os.mkdir(temp)

        jyt = os.path.join(temp, "jy1.py")
        with open(jyt, "w", encoding="utf8") as f:
            f.write('print("first try with jython")')

        out, err = run_jython(jyt, fLOG=fLOG)
        if "first try with jython" not in out:
            raise Exception("OUT:\n{0}\nERR:\n{1}\n".format(out, err))

    def test_complex_jython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            # to avoid timeout on appveyor
            return

        download_java_standalone()
        self.assertTrue(is_java_installed())

        this = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.join(this, "temp_jython")
        if not os.path.exists(temp):
            os.mkdir(temp)

        jyt = os.path.join(temp, "jy2.py")
        with open(jyt, "w", encoding="utf8") as f:
            f.write('''
                            if __name__ != '__lib__':
                                def outputSchema(dont_care):
                                    def wrapper(func):
                                        def inner(*args, **kwargs):
                                            return func(*args, **kwargs)
                                        return inner
                                    return wrapper

                            import datetime

                            #@outputSchema("brow: (available_bike_stands:chararray, available_bikes:chararray, lat:chararray, lng:chararray, name:chararray, status:chararray)")
                            @outputSchema("brow:chararray")
                            def extract_columns_from_js(row):
                                cols = ["available_bike_stands","available_bikes","lat","lng","name","status"]
                                js = eval(row)
                                res = [ ]
                                for station in js:
                                    vals = [ str(station[c]) for c in cols ]
                                    res.append( tuple(vals) )
                                return res
                            if __name__ != '__lib__':
                                import sys
                                for row in sys.stdin:
                                    row = row.strip()
                                    res = extract_columns_from_js(row)
                                    sys.stdout.write(str(res))
                                    sys.stdout.write("\\n")
                                    sys.stdout.flush()
                    '''.replace("                            ", ""))

        sin = '''
                    [{'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET', 'collect_date': datetime.datetime(2014, 11, 11, 22, 2, 18, 47270), 'lng': 2.416170724425901, 'contract_name': 'Paris', 'name': '31705 - CHAMPEAUX (BAGNOLET)', 'banking': 0, 'lat': 48.8645278209514, 'bonus': 0, 'status': 'OPEN', 'available_bikes': 1, 'last_update': datetime.datetime(2014, 11, 11, 21, 55, 22), 'number': 31705, 'available_bike_stands': 49, 'bike_stands': 50}]
                    [{'address': 'RUE DES CHAMPEAUX (PRES DE LA GARE ROUTIERE) - 93170 BAGNOLET', 'collect_date': datetime.datetime(2014, 11, 11, 22, 2, 18, 47270), 'lng': 2.416170724425901, 'contract_name': 'Paris', 'name': '31705 - CHAMPEAUX (BAGNOLET)', 'banking': 0, 'lat': 48.8645278209514, 'bonus': 0, 'status': 'OPEN', 'available_bikes': 1, 'last_update': datetime.datetime(2014, 11, 11, 21, 55, 22), 'number': 31705, 'available_bike_stands': 49, 'bike_stands': 50}]
                    '''.replace("                    ", "").strip("\r\n ")
        out, err = run_jython(jyt, sin=sin, fLOG=fLOG)
        fLOG("OUT:\n", out)
        fLOG("ERR:\n", err)
        exp = "[('49', '1', '48.864527821',"
        if exp not in out:
            raise Exception("OUT:\n{0}\nERR:\n{1}\n".format(out, err))

    def test_magic_command_jython(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if "travis" in sys.executable:
            return

        temp = get_temp_folder(__file__, "temp_magic_command_jython")

        download_java_standalone()
        assert is_java_installed()

        script = """
                    import random

                    @schemaFunction("rsSchema")
                    def rsSchema(input):
                        return input

                    @outputSchemaFunction("rsSchema")
                    def reservoir_sampling(ensemble):
                        ensemble = eval(ensemble)
                        k = 10
                        N = len(ensemble)
                        echantillon = []
                        for i, e in enumerate(ensemble):
                            if len(echantillon) < k:
                                echantillon.append(e)
                            else:
                                j = random.randint(0, i)
                                if j < k:
                                    echantillon[j] = e
                        return echantillon
                    """.replace("                    ", "")

        dest = os.path.join(temp, "script.py")
        mg = MagicFile()
        cmd = dest
        fLOG("**", cmd)
        res = mg.PYTHON(cmd, cell=script)
        fLOG(res)
        assert os.path.exists(dest)

        mg = MagicAzure()
        cmd = dest + " reservoir_sampling"
        cell = '{(100001,"AAAAAA"),(99999,"D99999"),(99998,"C99998")}\n'
        res = mg.jython(cmd, cell=cell)
        fLOG(res)
        assert res


if __name__ == "__main__":
    unittest.main()
