"""
@brief      test log(time=0s)
"""
import os
import unittest
import re
from pyensae import __version__


class TestVersion (unittest.TestCase):

    def test_version(self):
        setup = os.path.join(
            os.path.split(__file__)[0],
            "..",
            "..",
            "setup.py")
        with open(setup, "r") as f:
            c = f.read()
        reg = re.compile("sversion *= \\\"(.*)\\\"")

        f = reg.findall(c)
        if len(f) != 1:
            raise Exception("not only one version")
        assert f[0] == __version__


if __name__ == "__main__":
    unittest.main()
