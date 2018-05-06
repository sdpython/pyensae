"""
@brief      test log(time=2s)

"""


import sys
import os
import unittest
import pandas
from pandas.testing import assert_frame_equal


try:
    import src
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..")))
    if path not in sys.path:
        sys.path.append(path)
    import src

try:
    import pyquickhelper as skip_
except ImportError:
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
    import pyquickhelper as skip_


from pyquickhelper.loghelper import fLOG
from src.pyensae.ml_helper import TableFormula


class TestTableFormula(unittest.TestCase):

    def test_TableFormula_groupby(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        table = TableFormula(data=dict(name="kA kA kB".split(),
                                       d_a=[1, 2, 3], d_b=[1.1, 2.1, 3.1], d_c=[3, 4, 5]))

        group = table.fgroupby(lambda v: v["name"],
                               [lambda v: v["d_a"], lambda v: v["d_b"]],
                               ["sum_d_a", "sum_d_b"])

        exp = pandas.DataFrame(dict(sum_d_a=[3, 3], sum_d_b=[3.2, 3.1]))
        exp.sort_index(inplace=True)
        group.sort_index(inplace=True)
        exp.sort_index(inplace=True, axis=1)
        group.sort_index(inplace=True, axis=1)
        assert_frame_equal(group, exp)

        groupmax = table.fgroupby(lambda v: v["name"],
                                  [lambda v: v["d_a"], lambda v: v["d_b"]],
                                  ["max_d_a", "max_d_b"],
                                  [max, max])
        exp = pandas.DataFrame(dict(max_d_a=[2, 3], max_d_b=[2.1, 3.1]))
        exp.sort_index(inplace=True)
        groupmax.sort_index(inplace=True)
        exp.sort_index(inplace=True, axis=1)
        groupmax.sort_index(inplace=True, axis=1)
        assert_frame_equal(groupmax, exp)

        group = table.fgroupby(lambda v: v["name"],
                               [lambda v: v["d_a"]],
                               ["sum_d_a"],
                               [lambda vec, w: sum(vec) / w],
                               lambda v: v["d_b"])
        exp = pandas.DataFrame(dict(sum_d_a=[0.84127, 1.47619]))
        exp.sort_index(inplace=True)
        group.sort_index(inplace=True)
        exp.sort_index(inplace=True, axis=1)
        group.sort_index(inplace=True, axis=1)
        assert_frame_equal(group, exp)

    def test_TableFormula_add(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        table = TableFormula()
        table["A"] = [0, 1]
        table.add_column_index([4, 5])
        table.add_column_vector("B", [6, 7])
        table.addc("C", lambda row: row["A"] * row["B"])
        exp = pandas.DataFrame(dict(sum_d_a=[0.84127, 1.47619]))
        exp = pandas.DataFrame(
            dict(A=[0, 1], B=[6, 7], C=[0, 7], __key__=[4, 5]))
        exp.set_index("__key__", inplace=True)
        exp.index.rename(None, inplace=True)
        assert_frame_equal(table, exp)

    def test_TableFormula_sort(self):
        fLOG(__file__, self._testMethodName, OutputPrint=__name__ == "__main__")

        table = TableFormula()
        table["A"] = [0, 1]
        table.add_column_vector("B", [6, 7])
        table.sort(lambda row: -row["B"])
        exp = pandas.DataFrame(dict(A=[1, 0], B=[7, 6], C=[1, 0]))
        exp = exp.set_index("C")
        exp.index.rename(None, inplace=True)
        assert_frame_equal(table, exp, check_index_type=False)


if __name__ == "__main__":
    unittest.main()
