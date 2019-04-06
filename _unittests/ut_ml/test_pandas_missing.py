"""
@brief      test log(time=7s)
"""
import unittest
import pandas
import numpy
from pyensae.mlhelper import add_missing_indices


class TestPandasMissing(unittest.TestCase):

    def test_missing_indices(self):
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

    def test_missing_indices_examples(self):
        df = pandas.DataFrame(
            [{"x": 3, "y": 4, "z": 1}, {"x": 5, "y": 6, "z": 2}])
        df2 = add_missing_indices(df, "x", [3, 4, 5, 6])
        self.assertEqual(df2.shape, (8, 3))

        df = pandas.DataFrame(
            [{"x": 3, "y": 4, "z": 1}, {"x": 5, "y": 6, "z": 2}])
        df2 = add_missing_indices(
            df, "x", values=["y"], all_values=[3, 4, 5, 6])
        self.assertEqual(df2.shape, (8, 3))


if __name__ == "__main__":
    unittest.main()
