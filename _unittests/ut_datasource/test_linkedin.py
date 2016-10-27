"""
@brief      test log(time=13s)

"""


import sys
import os
import unittest
import warnings


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


try:
    import linkedin as skip__
except ImportError:
    path = os.path.normpath(
        os.path.abspath(
            os.path.join(
                os.path.split(__file__)[0],
                "..",
                "..",
                "..",
                "python-linkedin")))
    if path not in sys.path:
        sys.path.append(path)
    import linkedin as skip__

from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import is_travis_or_appveyor
from src.pyensae.datasource.linkedin_access import LinkedInAccess


class TestLinkedIn (unittest.TestCase):

    s = """
        Application Details
        Company:
        ENSAE Alumni
        Application Name:
        ensae_alumni
        API Key:
        ????????????
        Secret Key:
        ????????????????
        OAuth User Token:
        ????????-????-????-????-????????????
        OAuth User Secret:
        ????????-????-????-????-????????????
    """

    my_url = "http://www.linkedin.com/profile/view?id=2288976"
    my_id = "9nsW-6OsQF"

    def start(self):
        import linkedin as skip___

    def get_access_token(self):
        import keyring
        machine = os.environ.get(
            "COMPUTERNAME", os.environ.get("HOSTNAME", "CI"))
        res = []
        for k in ["APIKey", "SecretKey", "User", "Secret"]:
            try:
                res.append(keyring.get_password("linkedin", machine + k))
            except RuntimeError:
                res.append(None)
        if not is_travis_or_appveyor() and res[0] is None:
            raise ValueError("cannot retrieve credentials for Linkedin")
        if res[0] is None:
            return None
        return res

    def test_linkedin(self):
        self.start()
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        token = self.get_access_token()
        if token is None:
            warnings.warn("no credential, unable to test linkedin")
            return
        linkedin = LinkedInAccess(*token)
        res = linkedin.connect()
        fLOG("***", res)
        try:
            prof = linkedin.get_profile()
        except Exception as e:
            if "Expired access token." in str(e):
                warnings.warn(str(e))
                return
            else:
                raise e
        fLOG("prof", prof)
        assert prof["lastName"] == "Dupre"
        fLOG("------")
        prof = []
        se = linkedin.search_profile(
            params={
                "last-name": "dupre",
                "first-name": "xavier"})
        for _ in se["people"]["values"]:
            fLOG(_)
            assert 'id' in _
            try:
                prof.append(linkedin.get_profile(id=_['id']))
            except Exception as e:
                fLOG("error", e)

        fLOG("----")
        assert len(se["people"]["values"]) > 1
        assert len(prof) > 0
        for p in prof:
            fLOG(p)

    def test_linkedin_basic(self):
        self.start()
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        token = self.get_access_token()
        if token is None:
            warnings.warn("no credential, unable to test linkedin")
            return
        linkedin = LinkedInAccess(*token)
        res = linkedin.connect(False)
        fLOG("***", res)
        try:
            prof = linkedin.get_profile()
        except Exception as e:
            if "Expired access token." in str(e):
                warnings.warn(str(e))
                return
            else:
                raise e
        fLOG("prof", prof)
        assert prof["lastName"] == "Dupre"
        fLOG("------")
        prof = []
        se = linkedin.search_profile(
            params={
                "last-name": "dupre",
                "first-name": "xavier"})
        for _ in se["people"]["values"]:
            fLOG(_)
            assert 'id' in _
            try:
                prof.append(linkedin.get_profile(id=_['id']))
            except Exception as e:
                fLOG("error", e)

        fLOG("----")
        assert len(se["people"]["values"]) > 1
        assert len(prof) > 0
        for p in prof:
            fLOG(p)

    def test_linkedin_search_key(self):
        self.start()
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        token = self.get_access_token()
        if token is None:
            warnings.warn("no credential, unable to test linkedin")
            return
        linkedin = LinkedInAccess(*token)
        res = linkedin.connect()
        if __name__ == "__main__":
            if False:
                for year in range(2010, 2014):
                    fLOG("**** year ", year)
                    se = linkedin.search_profile(
                        params={"keywords": "ensae %d" % year},
                        count=-1,
                        as_table=True)
                    if se is not None:
                        temp_file = os.path.abspath(
                            os.path.join(
                                os.path.split(__file__)[0],
                                "temp_ensae_%d.txt" %
                                year))
                        fLOG("writing ", len(se))
                        se.save(temp_file, encoding="utf8")

                se = linkedin.search_profile(
                    params={"keywords": "ensae"},
                    count=-1,
                    as_table=True)
                temp_file = os.path.abspath(
                    os.path.join(
                        os.path.split(__file__)[0],
                        "temp_ensae2.txt"))
                fLOG("writing ", len(se))
                se.save(temp_file, encoding="utf8")

            if True:

                for key in "new-york paris londres singapour montreal pekin shangai tokyo kyoto san francisco boston bank research economy statistics insurance".split():
                    fLOG("**** key ", key)
                    se = linkedin.search_profile(
                        params={"keywords": "ensae %s" % key},
                        count=-1,
                        as_df=True)
                    if se is not None:
                        temp_file = os.path.abspath(
                            os.path.join(
                                os.path.split(__file__)[0],
                                "temp_ensae_%s.txt" %
                                key))
                        fLOG("writing ", len(se))
                        se.save(temp_file, encoding="utf8")

        else:
            fLOG("***", res)
            try:
                prof = linkedin.get_profile()
            except Exception as e:
                if "Expired access token." in str(e):
                    return
                else:
                    raise e
            fLOG("prof", prof)
            assert prof["lastName"] == "Dupre"
            fLOG("------")
            prof = []
            se = linkedin.search_profile(
                params={
                    "keywords": "ensae"},
                as_table=True)
            fLOG(se)
            assert "headline" in se.header
            assert len(se) > 0

    def test_linkedin_connection(self):
        self.start()
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        token = self.get_access_token()
        if token is None:
            warnings.warn("no credential, unable to test linkedin")
            return
        linkedin = LinkedInAccess(*token)
        res = linkedin.connect()
        fLOG("***", res)
        try:
            prof = linkedin.get_connections(member_id=TestLinkedIn.my_id)
        except Exception as e:
            if "Expired access token." in str(e):
                warnings.warn(str(e))
                return
            else:
                raise e
        values = prof["values"]
        assert len(values) > 0
        for v in values:
            fLOG(v)


if __name__ == "__main__":
    unittest.main()
