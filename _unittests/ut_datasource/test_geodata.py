"""
@brief      test log(time=3s)
"""
import unittest
from pyquickhelper.pycode import ExtTestCase, get_temp_folder
from pyensae.datasource import load_french_departements


class TestGeoData(ExtTestCase):

    def test_load_french_departements(self):
        temp = get_temp_folder(__file__, "temp_load_french_departements")
        df = load_french_departements(cache=temp)
        cols = set(['geometry', 'CODE_DEPT', 'CODE_REG', 'CODE_CHF', 'ID_GEOFLA', 'NOM_CHF',
                    'NOM_DEPT', 'NOM_REG', 'X_CENTROID', 'X_CHF_LIEU', 'Y_CENTROID',
                    'Y_CHF_LIEU'])
        self.assertEqual(df.shape, (96, 12))
        self.assertEqual(cols, set(df.columns))


if __name__ == "__main__":
    unittest.main()
