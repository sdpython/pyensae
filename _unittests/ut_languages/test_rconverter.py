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

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder
from src.pyensae.languages.rconverter import r2python


class TestPRConverter(unittest.TestCase):

    def test_rconverter(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_rconverter")

        scripts = [os.path.join(temp, "..", "data", "r2.r"),
                   os.path.join(temp, "..", "data", "r1.r")]

        exps = ["""
                    from python2r_helper import within

                    # some comments


                    def test_machine_chouette_something():

                        # some other comment

                        def func(infile, csch, predmod):

                            impnode = zoo_test(infile="$infile", dot="$dotdot", csch=csch)
                            obj = waouh(
                                impnode, nono, trnode, inputs=list(
                                    infile=infile), outputs=list(
                                    predmod=predmod))

                            # one
                            # comment
                            exjs = epr(unclass(tojs(obj)))
                            exjs = epr(tojs(obj))
                            exjs = epr(obj)

                        env(func) . asNamespace("namesp")

                        # last
                        bdf = within(iris, " spec == \\\"setosa\\\" ")
                        bf = tempfile("bf", fet=".txt")
                        ds(bdf, btx, ow=True)
                """.replace("                    ", ""),
                """
                    # example
                    a = 2
                    b = 3


                    def mySecFun(v, M):

                        u = tuple(0, 0, 0, 0)

                        for i in range(1, length(v)):

                            if i == 1:

                                u[i] = myFirstFun(v[i])

                            else:

                                u[i] = mySecondFun(v[i]) + 2

                                u[i + 1] = myThirdFun(v[i])

                        return u


                    Sqv = mySecFun(v)
                    Sqv
                """.replace("                    ", ""),
                ]

        for exp, script in zip(exps, scripts):
            with open(script, "r", encoding="utf-8") as f:
                code = f.read()
            pycode = r2python(code, pep8=True)
            new_file = os.path.join(temp, os.path.split(script)[-1] + ".py")
            with open(new_file, "w", encoding="utf-8") as f:
                f.write(pycode)
            self.maxDiff = None
            self.assertEqual(exp.strip(" \n"), pycode.strip(" \n"))


if __name__ == "__main__":
    unittest.main()
