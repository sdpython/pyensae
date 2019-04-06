"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, ExtTestCase, skipif_travis
from pyensae.graphhelper import run_dot


class TestDot(ExtTestCase):

    @skipif_travis("No such file or directory: 'dot': 'dot'")
    def test_graph_style(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        temp = get_temp_folder(__file__, "temp_dot")

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
        self.assertExists(img)


if __name__ == "__main__":
    unittest.main()
