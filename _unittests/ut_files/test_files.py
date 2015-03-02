"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import shlex


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

from pyquickhelper import fLOG, get_temp_folder, docstring2html
from src.pyensae.file_helper.magic_file import MagicFile
from src.pyensae import file_tail
from src.pyensae import Database


class TestFiles (unittest.TestCase):

    def test_shlex(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        this = r"c:\rep1\rep2\frep\_urep.py rrr c:\rr\i.py"
        r = shlex.split(this, posix=False)
        fLOG(r)
        assert r[0] == r"c:\rep1\rep2\frep\_urep.py"

    def test_files(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.dirname(__file__))
        mg = MagicFile()
        cmd = path + " -f .*[.]py"
        fLOG("**", cmd)
        res = mg.lsr(cmd)
        fLOG(res)
        if len(res) == 0:
            raise FileNotFoundError("cmd: " + cmd)
        res = mg.lsr("")
        fLOG(res)
        assert len(res) > 0

    def test_head(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fp = os.path.abspath(__file__)
        mg = MagicFile()
        fLOG("--", fp)
        res = mg.head("{0} -n 3".format(fp))
        fLOG("*****", res)
        assert "test log" in res.data
        res = mg.head("{0} --n 3 -e ascii".format(fp))
        res = mg.head("{0} --n 3 -e utf8".format(fp))

    def test_head2(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fp = os.path.join(
            os.path.dirname(
                os.path.abspath(__file__)),
            "data",
            "Exportutf8.txt")
        mg = MagicFile()
        fLOG("--", fp)
        res = mg.head("{0} -n 3".format(fp))
        fLOG("*****", res)
        res = mg.head("{0} -n=3".format(fp))
        fLOG("*****", res)
        res = mg.head("{0}".format(fp))
        fLOG("*****", res)
        assert "9.0" in res.data
        res = mg.head("{0} --n 3 -e utf8".format(fp))

        try:
            res = mg.head("Exportutf8.txt")
        except FileNotFoundError:
            pass

    def test_tail(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        fp = os.path.abspath(__file__)
        mg = MagicFile()
        fLOG("--", fp)
        res = mg.tail("{0} -n 3".format(fp))
        fLOG("*****", res)
        assert "unittest.main" in res.data
        res = mg.tail("{0} --n 3 -e ascii".format(fp))
        res = mg.tail("{0} --n 3 -e utf8".format(fp))
        res = file_tail(fp, threshold=300, nbline=3)
        res = [_ for _ in res if len(_) > 0]
        fLOG("#####", res)
        if "unittest.main" not in res[-1]:
            raise Exception("unittest.main not in " + str(res[-1]))

    def test_files_repo(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        path = os.path.abspath(os.path.dirname(__file__))
        mg = MagicFile()
        cmd = path
        fLOG("**", cmd)
        res = mg.lsrepo(cmd)
        fLOG(res)
        if len(res) == 0:
            raise FileNotFoundError("cmd: " + cmd)
        res = mg.lsrepo("")
        fLOG(res)
        assert len(res) > 0

    def test_files_compress(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        this = os.path.abspath(__file__)
        temp = get_temp_folder(__file__, "temp_compress")
        dest = os.path.join(temp, "temp_this.zip")

        mg = MagicFile()
        cmd = "dest [this]"
        fLOG("**", cmd)
        assert not os.path.exists(dest)
        mg.add_context({"this": this, "dest": dest})
        res = mg.compress(cmd)
        fLOG(res)
        assert os.path.exists(dest)
        assert res == 1

    def test_htmlhelp(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        mg = MagicFile()
        mg.add_context(
            {"file_tail": file_tail, "Database": Database, "text": 3})
        cmd = "-np -f rawhtml file_tail"
        res = mg.hhelp(cmd)
        assert "<p>extracts the first nbline of a file " in res
        res = mg.hhelp("-np -f rst file_tail")
        assert ":param      threshold:" in res
        res = mg.hhelp("-np -f rawhtml Database")
        assert "SQL file which can be empty or not," in res
        doc = docstring2html(Database.__init__, format="rawhtml")
        assert "it can also contain several files separated by" in doc
        fLOG("----------")
        res = mg.hhelp("-np -f rst Database.__init__")
        assert "it can also contain several files separated by" in res
        res = mg.hhelp("Database.__init__")
        assert res is not None
        res = mg.hhelp("-np -f text Database.__init__")
        assert "it can also contain several files separated by" in res
        assert "@param" in res


if __name__ == "__main__":
    unittest.main()
