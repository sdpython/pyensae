"""
@brief      test log(time=110s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import sys
import os
import unittest
import pandas
import warnings
from urllib3.exceptions import NewConnectionError
from requests.exceptions import ConnectionError
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

from pyquickhelper.loghelper import fLOG, run_cmd
from src.pyensae.remote import AzureClient


class TestAzure (unittest.TestCase):

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

    def test_ls(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        if self.client is None:
            return
        import azure.common
        try:
            df = self.client.ls(self.blob_serv, None)
        except azure.common.AzureException as e:
            warnings.warn(
                "Unable to test azure, storage is still up?\n" + str(e))
            return
        fLOG(df)
        assert isinstance(df, pandas.DataFrame)

    def test_upload_download(self):
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
        fold = os.path.join(data, "..", "temp_updown")
        if not os.path.exists(fold):
            os.mkdir(fold)
        for _ in os.listdir(fold):
            _ = os.path.join(fold, _)
            if os.path.isfile(_):
                os.remove(_)

        files = os.listdir(data)
        files = [os.path.join(data, _) for _ in files]
        files = [_ for _ in files if os.path.isfile(_) and "paris" in _]

        import azure.common
        try:
            if not self.client.exists(self.blob_serv, self.container, "unittest"):
                # no folder creation
                pass
            else:
                df = self.client.ls(self.blob_serv, self.container, "unittest")
                for name in df["name"]:
                    self.client.delete_blob(
                        self.blob_serv, self.container, name)
        except azure.common.AzureException as e:
            warnings.warn(
                "Unable to test azure, storage is still up?\n" + str(e))
            return

        content = self.client.ls(self.blob_serv, self.container, "unittest")
        fLOG(content.columns)
        fLOG("u", list(content["name"]))
        assert len(content) == 0

        assert not self.client.exists(
            self.blob_serv,
            self.container,
            "unittest")
        fLOG("****", files)
        self.client.upload(self.blob_serv, self.container, "unittest", files)

        df = self.client.ls(self.blob_serv, self.container, "unittest")
        fLOG("after\n", df["name"])
        assert len(df) >= 3

        self.client.download(self.blob_serv, self.container, df["name"], fold)
        ld = os.listdir(fold)
        fLOG(ld)
        assert len(ld) >= 3

    def test_script_pig(self):
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

        fold = os.path.join(data, "..", "temp_pypig_az")
        if not os.path.exists(fold):
            os.mkdir(fold)

        # python script

        pyth = """
                    import sys, datetime
                    cols = [ _ for _ in sys.argv if ".py" not in _ ]
                    for row in sys.stdin:
                        row = row.strip()
                        if len(row) == 0 :
                            continue
                        js = eval(row)
                        for station in js:
                            vals = [ str(station[c]).strip() for c in cols ]
                            sys.stdout.write(",".join(vals))
                            sys.stdout.write("\\n")
                            sys.stdout.flush()
                """.replace("                    ", "")

        pyfile = os.path.join(fold, "pystream.py")
        with open(pyfile, "w", encoding="utf8") as f:
            f.write(pyth)

        tosend = """[{'address': "52 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE - 75010 PARIS", 'collect_date': datetime.datetime(2014, 11, 11, 22, 1, 18, 331070), """ + \
                 """'lng': 2.348395236282807, 'contract_name': 'Paris', 'name': '10042 - POISSONNIÈRE - ENGHIEN', 'banking': 0, 'lat': 48.87242006305313, 'bonus': 0, 'status': """ + \
                 """'OPEN', 'available_bikes': 32, 'last_update': datetime.datetime(2014, 11, 11, 21, 59, 5), 'number': 10042, 'available_bike_stands': 1, 'bike_stands': 33},""" + \
                 """{'address': "52 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE - 75010 PARIS", 'collect_date': datetime.datetime(2014, 11, 11, 22, 1, 18, 331070), """ + \
                 """'lng': 2.348395236282807, 'contract_name': 'Paris', 'name': '10042 - POISSONNIÈRE - ENGHIEN', 'banking': 0, 'lat': 48.87242006305313, 'bonus': 0, 'status': """ + \
                 """'OPEN', 'available_bikes': 32, 'last_update': datetime.datetime(2014, 11, 11, 21, 59, 5), 'number': 10042, 'available_bike_stands': 1, 'bike_stands': 33}]"""

        cmd = sys.executable.replace(
            "pythonw",
            "python") + " " + pyfile + " name"
        out, err = run_cmd(
            cmd, wait=True, sin=tosend, communicate=True, timeout=3, shell=False)
        out = out.strip("\n\r ")
        spl = out.split("\n")
        if len(spl) != 2:
            raise Exception(
                "len:{2}\nOUT:\n{0}\nERR:\n{1}".format(
                    out,
                    err,
                    len(out)))

        # PIG script

        pig = """
                DEFINE pystream `python pystream.py bonus available_bike_stands available_bikes lat lng name status`
                        SHIP ('pystream.py')
                        INPUT(stdin USING PigStreaming(',')) OUTPUT (stdout USING PigStreaming(','));

                jspy = LOAD '$CONTAINER/$UTT/*.txt' USING PigStorage('\t') AS (arow:chararray);

                --DUMP jspy ;

                matrice = STREAM jspy THROUGH pystream AS
                                (   bonus:chararray,
                                    available_bike_stands:double,
                                    available_bikes:double,
                                    lat:double,
                                    lng:double,
                                    name:chararray,
                                    status:chararray) ;

                DUMP matrice ;

                DESCRIBE jspy ;
                DESCRIBE matrice ;

                STORE matrice INTO '$CONTAINER/$PSEUDO/unittest2/results.txt' USING PigStorage('\t') ;
            """.replace("                ", "")

        pigfile = os.path.join(fold, "pystream.pig")
        with open(pigfile, "w", encoding="utf8") as f:
            f.write(pig)

        # we upload some files

        files = os.listdir(data)
        files = [os.path.join(data, _) for _ in files]
        files = [_ for _ in files if os.path.isfile(_) and "paris" in _]

        import azure.common
        try:
            content = self.client.ls(
                self.blob_serv, self.container, "unittest2")
        except azure.common.AzureException as e:
            warnings.warn(
                "Unable to test azure, storage is still up?\n" + str(e))
            return

        if len(content) == 0:
            self.client.upload(
                self.blob_serv,
                self.container,
                "unittest2",
                files)

        if self.client.exists(
                self.blob_serv, self.container, "unittest2/results.txt"):
            self.client.delete_folder(
                self.blob_serv,
                self.container,
                "unittest2/results.txt")

        # we submit the job
        recall = None
        if recall is None:
            try:
                job = self.client.pig_submit(self.blob_serv, self.container,
                                             pigfile, dependencies=[pyfile],
                                             params=dict(UTT="unittest2"))
            except (ConnectionError, NewConnectionError):
                # the cluster is probably not set up
                warnings.warn("hadoop cluster is not set up")
                return
            job_id = job["id"]
        else:
            job_id = recall

        status = self.client.wait_job(job_id, fLOG=fLOG)

        out, err = self.client.standard_outputs(
            status, self.blob_serv, self.container, fold)

        if "Total records written : 4" not in err:
            raise Exception("OUT:\n{0}\nERR:\n{1}".format(out, err))

        dest = os.path.join(fold, "out_merged.txt")
        fLOG("dest=", dest)
        if os.path.exists(dest):
            os.remove(dest)
        self.client.download_merge(
            self.blob_serv,
            self.container,
            "$PSEUDO/unittest2/results.txt",
            dest)

        if not os.path.exists(dest):
            raise FileNotFoundError(dest)
        with open(dest, "r", encoding="utf8") as f:
            content = f.read()
        fLOG("-----\n", content)
        assert len(content.strip(" \n\r\t")) > 0

        df = self.client.df_head(self.blob_serv, self.container,
                                 "$PSEUDO/unittest2/results.txt", sep=",", merge=True)
        fLOG(df)
        assert len(df) > 0


if __name__ == "__main__":
    unittest.main()
