"""
@file
@brief Check code style.

.. versionadded:: 1.8
"""
import os
from pyquickhelper.pycode import check_pep8


def _private_test_style_src(fLOG, run_lint, verbose=False, pattern=".*[.]py$"):
    thi = os.path.abspath(os.path.dirname(__file__))
    src_ = os.path.normpath(os.path.join(thi, ".."))
    check_pep8(src_, fLOG=fLOG, neg_pattern='.*((Parser)|(Lexer)|(Listener)|(antlr_grammar_use))[.]py$',
               verbose=verbose, pattern=pattern, run_lint=run_lint,
               pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                              'C0111', 'W0622', 'W0612', 'C0412', 'W0621',
                              'W0212', 'R1704', 'W0622', 'W0201', 'R1710',
                              'W0703', 'R1703', 'R0911', 'R0912', 'R0915',
                              'E0203', 'C0302', 'C0200', 'R1702', 'E1101',
                              'R0914', 'W0123', 'W0123', 'W0107', 'C0415'),
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
                     "R0401: Cyclic import (pyensae.sql.sql_interface",
                     "database_core2.py:230: R1714",
                     "RFilter.py",
                     ])


def _private_test_style_test(fLOG, run_lint, verbose=False, pattern=".*[.]py$"):
    thi = os.path.abspath(os.path.dirname(__file__))
    test_ = os.path.normpath(os.path.join(thi, "..", "..", '_unittests'))
    check_pep8(test_, fLOG=fLOG, neg_pattern="(temp_.*)|(.*test_parse_code.*[.]py)",
               verbose=verbose, pattern=pattern, run_lint=run_lint,
               pylint_ignore=('C0103', 'C1801', 'R0201', 'R1705', 'W0108', 'W0613',
                              'C0111', 'W0622', 'W0612', 'C0412', 'W0621',
                              'W0125', 'E1127', 'E1101', 'W1402', 'W0212',
                              'C0415'),
               skip=[])
