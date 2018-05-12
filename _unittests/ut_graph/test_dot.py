"""
@brief      test log(time=1s)

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
from src.pyensae.graph_helper import run_dot


class TestDot (unittest.TestCase):

    def test_graph_style(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_dot")

        if "travis" not in sys.executable:
            # still some issues with scipy and fortran compiler + graphviz
            # dependency
            from sklearn.datasets import load_iris
            from sklearn import tree

            clf = tree.DecisionTreeClassifier()
            iris = load_iris()
            clf = clf.fit(iris.data, iris.target)
            outfile = os.path.join(temp, "out_tree.dot")
            tree.export_graphviz(clf, out_file=outfile)
            img = os.path.join(temp, "out_tree.png")
            try:
                run_dot(outfile, img)
            except FileNotFoundError as e:
                p = os.environ.get("PATH", None)
                raise Exception("PATH={0}".format(p)) from e
            assert os.path.exists(img)


if __name__ == "__main__":
    unittest.main()
