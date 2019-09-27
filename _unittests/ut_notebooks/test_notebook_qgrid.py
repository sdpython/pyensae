"""
@brief      test log(time=1s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
import pandas
import traitlets
from pyquickhelper.loghelper import fLOG
from pyensae.notebookhelper.magic_notebook import MagicNotebook


class TestNotebookQGrid(unittest.TestCase):

    def test_qgrid(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")
        df = pandas.DataFrame([{"x": 2, "y": 3}, {"x": 4, "y": 5}])
        mg = MagicNotebook()
        mg.add_context({"df": df})
        try:
            res = mg.jsdf("df --editable=False")
            fLOG(res)
        except traitlets.traitlets.TraitError:
            # qgrid needs a true notebook as the grid is editable
            pass
        except TypeError as e:
            import qgrid  # pylint: disable=C0415
            raise Exception("qgrid: {0}".format(qgrid.__version__)) from e
        except AttributeError as e:
            if "'NoneType' object has no attribute 'session'" not in str(e):
                raise e
        try:
            res = mg.jsdf("df --editable=False")
            fLOG(res)
            assert res is not None
        except traitlets.traitlets.TraitError:
            # qgrid needs a true notebook as the grid is editable
            pass
        except AttributeError as e:
            if "'NoneType' object has no attribute 'session'" not in str(e):
                raise e


if __name__ == "__main__":
    unittest.main()
