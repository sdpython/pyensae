"""
@brief      test log(time=0s)
"""

import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import check_pep8, ExtTestCase

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


class TestCodeStyle(ExtTestCase):

    def test_style_src(self):
        fLOG(OutputPrint=True)
        thi = os.path.abspath(os.path.dirname(__file__))
        src_ = os.path.normpath(os.path.join(thi, "..", "..", "src"))
        check_pep8(src_, fLOG=fLOG, neg_pattern='.*((Parser)|(Lexer)|(Listener)|(antlr_grammar_use))[.]py$',
                   verbose=True,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0622', 'W0612', 'C0412', 'W0621',
                                  'W0212', 'R1704', 'W0622', 'W0201', 'R1710',
                                  'W0703', 'R1703', 'R0911', 'R0912', 'R0915',
                                  'E0203', 'C0302', 'C0200', 'R1702', 'E1101',
                                  'R0914', 'W0123', 'W0123'),
                   skip=["http_retrieve.py:191: W0703",
                         "astock.py:135: W0703",
                         "astock.py:229: W0703",
                         "http_retrieve.py:192: W0703",
                         "Class 'DatabaseCore' has no 'SCRIPT_LOOKUP'",
                         "sql_interface.py:18: W0231",
                         "file_text_binary.py:680: W0102",
                         "sql_interface_database.py:20: W0231",
                         "table_formula.py:108: W0631",
                         "R0401: Cyclic import (src.pyensae.sql.sql_interface",
                         ])

    def test_style_test(self):
        fLOG(OutputPrint=True)
        thi = os.path.abspath(os.path.dirname(__file__))
        test = os.path.normpath(os.path.join(thi, "..", ))
        check_pep8(test, fLOG=fLOG, neg_pattern="(temp_.*)|(.*test_parse_code.*[.]py)",
                   verbose=True,
                   pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                                  'C0111', 'W0622', 'W0612', 'C0412', 'W0621',
                                  'W0125', 'E1127', 'E1101', 'W1402', 'W0212',),
                   skip=["src' imported but unused",
                         "skip_' imported but unused",
                         "skip__' imported but unused",
                         "skip___' imported but unused",
                         "Unused variable 'skip_'",
                         "imported as skip_",
                         "Unused import src",
                         ])


if __name__ == "__main__":
    unittest.main()
