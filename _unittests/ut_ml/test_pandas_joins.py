"""
@brief      test log(time=7s)
"""
import unittest
import pandas
from pyquickhelper.loghelper import fLOG
from pyensae.mlhelper import df_crossjoin


class TestPandasJoins (unittest.TestCase):

    def test_cross_join(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        df = pandas.DataFrame([{"x": 3, "y": 4}, {"x": 5, "y": 6}])
        jj = df_crossjoin(df, df.copy())
        self.assertEqual(list(jj.columns), ["x_x", "y_x", "x_y", "y_y"])
        self.assertEqual(jj.shape, (4, 4))


if __name__ == "__main__":
    unittest.main()
