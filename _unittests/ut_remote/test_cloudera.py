"""
@brief      test log(time=140s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest
import pandas


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG, run_cmd
from src.pyensae import ASSHClient

thisfold = os.path.abspath(os.path.split(__file__)[0])
thiscomm = os.path.join(thisfold, "..")
sys.path.append(thiscomm)
from common import get_codes


class TestCloudera (unittest.TestCase):

    def setUp(self):
        codes = get_codes() [-3:]
        cl = ASSHClient(*codes)
        cl.connect()
        self.client = cl

    def tearDown(self):
        self.client.close()

    def test_ls(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        df = self.client.ls(".")
        fLOG(df)
        assert isinstance(df, pandas.DataFrame)

    def test_hdfs_dfs_ls(self):
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        df = self.client.dfs_ls(".")
        fLOG(df)
        assert isinstance(df, pandas.DataFrame)

    def test_upload_download(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        data = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "data")
        fold = os.path.join(data, "..", "temp_updown")
        if not os.path.exists(fold): os.mkdir(fold)
        for _ in os.listdir(fold):
            _ = os.path.join(fold,_)
            if os.path.isfile(_): os.remove(_)

        files = os.listdir(data)
        files = [ os.path.join(data,_) for _ in files ]
        files = [ _ for _ in files if os.path.isfile(_) and "paris" in _ ]

        if not self.client.dfs_exists("unittest"):
            self.client.dfs_mkdir("unittest")
        else:
            df = self.client.dfs_ls("unittest")
            for name in df["name"]:
                self.client.dfs_rm(name)

        content = self.client.dfs_ls("unittest")
        fLOG("u",list(content["name"]))
        assert len(content) == 0

        assert self.client.dfs_exists("unittest")
        fLOG("****",files)
        self.client.upload_cluster( files, "unittest")

        fLOG("after\n",df["name"])
        assert len(df) >= 3

        self.client.download_cluster( df["name"], fold)
        l = os.listdir(fold)
        fLOG(l)
        assert len(l) >= 3

    def test_script_pig(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        data = os.path.join(os.path.abspath(os.path.split(__file__)[0]), "data")

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
                """.replace("                    ","")

        fold = os.path.join(data, "..", "temp_pypig")
        if not os.path.exists(fold): os.mkdir(fold)

        pyfile = os.path.join(fold, "pystream.py")
        with open(pyfile,"w", encoding="utf8") as f : f.write(pyth)

        tosend = """[{'address': "52 RUE D'ENGHIEN / ANGLE RUE DU FAUBOURG POISSONIERE - 75010 PARIS", 'collect_date': datetime.datetime(2014, 11, 11, 22, 1, 18, 331070), 'lng': 2.348395236282807, 'contract_name': 'Paris', 'name': '10042 - POISSONNIÈRE - ENGHIEN', 'banking': 0, 'lat': 48.87242006305313, 'bonus': 0, 'status': 'OPEN', 'available_bikes': 32, 'last_update': datetime.datetime(2014, 11, 11, 21, 59, 5), 'number': 10042, 'available_bike_stands': 1, 'bike_stands': 33}]"""

        cmd = sys.executable.replace("pythonw", "python") + " " + pyfile + " name"
        out,err = run_cmd(cmd, wait=True, sin=tosend, communicate=True, timeout=3, shell=False)
        fLOG("OUT\n",out)
        fLOG("ERR\n",err)
        assert len(out) > 0


        # PIG script

        pig = """
                DEFINE pystream `python pystream.py bonus available_bike_stands available_bikes lat lng name status` SHIP ('pystream.py') INPUT(stdin USING PigStreaming(',')) OUTPUT (stdout USING PigStreaming(','));

                jspy = LOAD 'unittest2/*.txt' USING PigStorage('\t') AS (arow:chararray);

                DUMP jspy ;

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

                STORE matrice INTO 'unittest2/results.txt' USING PigStorage('\t') ;
            """.replace("                ","")

        pigfile = os.path.join(fold, "pystream.pig")
        with open(pigfile, "w", encoding="utf8") as f : f.write(pig)

        # we upload some files

        files = os.listdir(data)
        files = [ os.path.join(data,_) for _ in files ]
        files = [ _ for _ in files if os.path.isfile(_) and "paris" in _ ]

        if not self.client.dfs_exists("unittest2"):
            self.client.dfs_mkdir("unittest2")

        content = self.client.dfs_ls("unittest2")
        if len(content)==0:
            self.client.upload_cluster( files, "unittest2")

        if self.client.dfs_exists("unittest2/results.txt"):
            self.client.dfs_rm("unittest2/results.txt", True)

        # we upload the scripts
        self.client.upload( [ pyfile, pigfile ], ".")

        # we test the syntax
        out, err = self.client.execute_command("pig -check pystream.pig", no_exception = True)
        fLOG("OUT\n",out)
        fLOG("ERR\n",err)
        assert "pystream.pig syntax OK" in err

        # we submit the job
        out, err = self.client.execute_command("pig -execute -stop_on_failure -f pystream.pig", no_exception = True)
        fLOG("OUT\n",out)
        fLOG("ERR\n",err)
        assert "Total records written : 4" in err

        dest = os.path.join(fold, "out_merged.txt")
        fLOG("dest=",dest)
        if os.path.exists(dest): os.remove(dest)
        self.client.download_cluster("unittest2/results.txt", dest, merge=True)
        assert os.path.exists(dest)
        with open (dest, "r", encoding="utf8") as f : content = f.read()
        fLOG("-----\n",content)
        assert len(content.strip(" \n\r\t")) > 0


if __name__ == "__main__"  :
    unittest.main ()