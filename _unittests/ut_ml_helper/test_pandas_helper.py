"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import pandas
import numpy


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


from pyquickhelper.pycode import ExtTestCase
from src.pyensae.ml_helper import pandas_groupby_nan, numpy_types


class TestPandasHelper(ExtTestCase):

    def test_pandas_groupbynan(self):
        types = [(int, -10), (float, -20.2), (str, "e"),
                 (bytes, bytes("a", "ascii"))]
        skip = (numpy.bool_, numpy.complex64, numpy.complex128)
        types += [(_, _(5)) for _ in numpy_types() if _ not in skip]

        for ty in types:
            data = [{"this": "cst", "type": "tt1=" + str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "tt2=" +
                        str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "row_for_nan"}]
            df = pandas.DataFrame(data)
            gr = pandas_groupby_nan(df, "value")
            co = gr.sum()
            li = list(co["value"])
            try:
                self.assertIsInstance(li[-1], float)
            except AssertionError as e:
                raise AssertionError("Issue with {0}".format(ty)) from e
            try:
                self.assertTrue(numpy.isnan(li[-1]))
            except AssertionError as e:
                raise AssertionError("Issue with value {0}\n--df--\n{1}\n--co--\n{2}".format(li, df, co)) from e

        for ty in types:
            data = [{"this": "cst", "type": "tt1=" + str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "tt2=" +
                        str(ty[0]), "value": ty[1]},
                    {"this": "cst", "type": "row_for_nan"}]
            df = pandas.DataFrame(data)
            try:
                gr = pandas_groupby_nan(df, ("value", "this"))
                t = True
                raise Exception("---")
            except TypeError:
                t = False
            if t:
                co = gr.sum()
                li = list(co["value"])
                self.assertIsInstance(li[-1], float)
                self.assertTrue(numpy.isnan(li[-1]))
            try:
                gr = pandas_groupby_nan(df, ["value", "this"])
                t = True
            except (TypeError, NotImplementedError):
                t = False
                pass

            if t:
                co = gr.sum()
                li = list(co["value"])
                self.assertEqual(len(li), 2)

    def test_pandas_groupbynan_tuple(self):
        data = [dict(a="a", b="b", c="c", n=1), dict(
            b="b", n=2), dict(a="a", n=3), dict(c="c", n=4)]
        df = pandas.DataFrame(data)
        gr = df.groupby(["a", "b", "c"]).sum()
        self.assertEqual(gr.shape, (1, 1))

        for nanback in [True, False]:
            try:
                gr2_ = pandas_groupby_nan(
                    df, ["a", "b", "c"], nanback=nanback, suffix="NAN")
            except NotImplementedError:
                continue
            gr2 = gr2_.sum().sort_values("n")
            self.assertEqual(gr2.shape, (4, 4))
            d = gr2.to_dict("records")
            self.assertEqual(d[0]["a"], "a")
            self.assertEqual(d[0]["b"], "b")
            self.assertEqual(d[0]["c"], "c")
            self.assertEqual(d[0]["n"], 1)
            self.assertEqual(d[1]["a"], "NAN")


if __name__ == "__main__":
    unittest.main()
