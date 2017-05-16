"""
@brief      test log(time=7s)
"""

import sys
import os
import unittest
import pandas
import numpy

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
from src.pyensae.pandas_helper import add_missing_indices


class TestPandasMissing(unittest.TestCase):

    def test_cross_join(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        df = pandas.DataFrame(
            [{"x": 3, "y": 4, "z": 1}, {"x": 5, "y": 6, "z": 2}])
        df2 = add_missing_indices(
            df, "x", values=["y", "z"], all_values=[3, 4, 5, 6])
        self.assertEqual(df2.shape, (4, 3))
        df2 = add_missing_indices(
            df, "x", values=["y"], all_values=[3, 4, 5, 6])
        self.assertEqual(df2.shape, (8, 3))
        df2 = add_missing_indices(
            df, "x", values=None, all_values=[3, 4, 5, 6])
        self.assertEqual(df2.shape, (8, 3))
        df2 = add_missing_indices(
            df, "x", values=None, all_values=pandas.Series([3, 4, 5, 6]))
        self.assertEqual(df2.shape, (8, 3))
        df2 = add_missing_indices(
            df, "x", values=None, all_values=numpy.array([3, 4, 5, 6]))
        self.assertEqual(df2.shape, (8, 3))
        df2 = add_missing_indices(
            df, "x", values=None, all_values=pandas.DataFrame(dict(x=[3, 4, 5, 6])))
        self.assertEqual(df2.shape, (8, 3))


if __name__ == "__main__":
    unittest.main()
