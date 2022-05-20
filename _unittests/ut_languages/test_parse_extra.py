"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import os
import unittest
import warnings
from pyquickhelper.loghelper import fLOG


class TestParseCode (unittest.TestCase):

    def test_build_parser_extra(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        try:
            clparser, cllexer = get_parser_lexer("language")
            return
        except ImportError:
            pass

        folder = os.path.dirname(source_parser.__file__)

        for lang in ["language"]:
            gr = os.path.join(folder, lang + ".g4")
            if not os.path.exists(gr):
                warnings.warn("'{0}' does not exists.".format(gr))
                continue
            build_grammar(lang, fLOG=fLOG)

    def test_extra(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
        example of the language
        """
        try:
            from pyensae.languages.LanguageLexer import LanguageLexer
            from pyensae.languages.LanguageParser import LanguageParser
        except ImportError:
            return

        parser = parse_code(code, LanguageParser, LanguageLexer)
        tree = parser.compilation_unit()
        st = get_tree_string(tree, parser)
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0


if __name__ == "__main__":
    unittest.main()
