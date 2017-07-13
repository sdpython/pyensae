"""
@brief      test log(time=203s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import random


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
from pyquickhelper.pycode import is_travis_or_appveyor
from src.pyensae.file_helper import download_java_standalone, is_java_installed
from src.pyensae.file_helper.pig_helper import run_pig, download_pig_standalone


class TestPig (unittest.TestCase):

    def test_simple_pig(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        if is_travis_or_appveyor():
            return

        download_java_standalone()
        assert is_java_installed()

        try:
            download_pig_standalone(fLOG=fLOG)
        except FileNotFoundError:
            # for some unknown reason, it requires to be done twice
            # due to FileNotFoundError: [Errno 2] No such file or directory:
            # 'pyensae\\src\\pyensae\\file_helper\\pigjar\\pig-0.15.0\\contrib\\piggybank\\java\\build\\classes\\org\\apache\\pig\\piggybank\\storage\\IndexedStorage$IndexedStorageInputFormat$IndexedStorageRecordReader$IndexedStorageRecordReaderComparator.class'
            download_pig_standalone(fLOG=fLOG)

        # it does not work for the time being
        return

        this = os.path.abspath(os.path.dirname(__file__))
        temp = os.path.join(this, "temp_pig")
        if not os.path.exists(temp):
            os.mkdir(temp)

        rnd = os.path.join(temp, "random.sample.txt")
        with open(rnd, "w") as f:
            for i in range(0, 1000):
                x = random.random()
                f.write(str(x) + "\n")

        pg = os.path.normpath(os.path.join(temp, "..", "p1.pig"))
        tf = "file:/" + rnd.replace("\\", "/")
        with open(pg, "w", encoding="utf8") as f:
            f.write('''
                        values = LOAD '%s' USING PigStorage('\t') AS (x:double);
                        values_h = FOREACH values GENERATE x, ((int)(x / 0.1)) * 0.1 AS h ;
                        hist_group = GROUP values_h BY h ;
                        hist = FOREACH hist_group GENERATE group, COUNT(values_h) AS nb ;
                        STORE hist INTO '%s' USING PigStorage('\t') ;
                        '''.replace("                        ", "") %
                    (tf, tf + ".out.txt"))

        out, err = run_pig(pg, fLOG=fLOG, logpath=temp)
        if "first try with pig" not in out:
            raise Exception("OUT:\n{0}\nERR:\n{1}".format(out, err))


if __name__ == "__main__":
    unittest.main()
