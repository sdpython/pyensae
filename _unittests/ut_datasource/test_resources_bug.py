"""
@brief      test log(time=2s)
"""
import os
import unittest
from pyquickhelper.pycode import get_temp_folder, ExtTestCase
from pyensae.datasource.http_retrieve import download_data


class TestResourcesBug(ExtTestCase):

    def test_damir(self):
        temp = get_temp_folder(__file__, "temp_damir")
        res = download_data("A201612_small.csv.gz", whereTo=temp)
        self.assertEqual(len(res), 1)
        checks = [os.path.join(temp, _)
                  for _ in ["A201612_small.csv", "A201612_small.csv.gz"]]
        self.assertExists(checks[0])
        self.assertExists(checks[1])


if __name__ == "__main__":
    unittest.main()
