"""
@brief      test log(time=110s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import sys
import os
import unittest
import requests
import warnings
thisfold = os.path.abspath(os.path.split(__file__)[0])
thiscomm = os.path.join(thisfold, "..")
sys.path.append(thiscomm)
from common import get_codes

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
from src.pyensae.remote import AzureClient


class TestAzureHive(unittest.TestCase):

    def setUp(self):
        res = get_codes("CRAZURE")
        if res is None:
            self.client = None
        else:
            codes = res
            cl = AzureClient(
                codes[0],
                codes[1],
                codes[2],
                codes[3],
                "admin",
                "test_user")
            self.client = cl
            self.blob_serv = cl.open_blob_service()
            self.container = codes[0]

    def tearDown(self):
        pass

    def test_script_hive(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if self.client is None:
            return
        data = os.path.join(
            os.path.abspath(
                os.path.split(__file__)[0]),
            "data")

        fold = os.path.join(data, "..", "temp_pyhive_az")
        if not os.path.exists(fold):
            os.mkdir(fold)

        hive = """
            DROP TABLE IF EXISTS bankfull;
            CREATE TABLE bankfull (age float, job string, marital string, education string,
                              default2 string, balance float, housing string, loan string,
                              contact string, day float, month string, duration float,
                              campaign float, pdays float, previous float, poutcome string, y string);
            LOAD DATA INPATH "$CONTAINER/unittesthive/bank_full_tab.txt" INTO TABLE bankfull;

            INSERT OVERWRITE TABLE batting
            SELECT  age, job FROM bankfull;
            EXPORT TABLE batting TO "$CONTAINER/unittesthive/example";
            """

        hivefile = os.path.join(fold, "pyex.hive")
        with open(hivefile, "w", encoding="utf8") as f:
            f.write(hive)

        fLOG("submit")
        import azure.common
        try:
            job = self.client.hive_submit(self.blob_serv, self.container,
                                          hivefile, params=dict(UTT="unittest3"))
        except (requests.exceptions.ConnectionError, azure.common.AzureException) as e:
            warnings.warn("Cluster not available\n{0}".format(e))
            return
        fLOG(job)
        #not working


if __name__ == "__main__":
    unittest.main()
