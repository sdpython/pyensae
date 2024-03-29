"""
@brief      test log(time=3s)
"""
import os
import sys
import unittest
import warnings
from pyquickhelper.pycode import ExtTestCase


class TestParseCode(ExtTestCase):

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_build_parser(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        langs = ["DOT", "CSharp4", "SQLite", "R"]  # , "Python3"]

        for lang in langs:
            with self.subTest(lang=lang):
                try:
                    get_parser_lexer(lang)
                    return
                except ImportError:
                    pass

        folder = os.path.dirname(source_parser.__file__)

        rows = []

        def local_print(*s):
            rows.append(' '.join(map(str, s)))

        for lang in langs:
            gr = os.path.join(folder, lang + ".g4")
            assert os.path.exists(gr)
            final = build_grammar(lang, fLOG=local_print)
            fLOG(final)

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_r(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        code = """
        a = 4 ;
        b = 5 ;
        c = a + b ;
        """

        clparser, cllexer = get_parser_lexer("R")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        assert len(st) > 0
        st = get_tree_string(tree, parser, None)
        assert len(st) > 0

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_sql(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        code = """
        SELECT a,tbl.b,nb FROM tbl
        INNER JOIN (
            SELECT b, COUNT(*) AS nb FROM tbl
            ) AS tblG
        ON tbl.b == tblG.b ;
        """

        clparser, cllexer = get_parser_lexer("SQLite")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser, None)
        assert len(st) > 0

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_error(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        code = """
        SELECT
                a,
                tbl.b,
                nb$
            FROM tbl
        INNER JOIN (
            SELECT b, COUNT(*) AS nb FROM tbl
            ) AS tblG
        ON tbl.b == tblG.b ;
        """

        clparser, cllexer = get_parser_lexer("SQLite")
        parser = parse_code(code, clparser, cllexer)
        parser.parse()

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_csharp(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        code = """
        namespace hello
        {
            public static class world
            {
                public static double function(double x, doubly y)
                {
                    return x+y ;
                }
            }
        }
        """

        clparser, cllexer = get_parser_lexer("C#")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.compilation_unit()
        st = get_tree_string(tree, parser)
        assert len(st) > 0

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_python3(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        # the grammar does not fully compile

        code = """
        def addition(x, y):
            return x + y
        """

        try:
            clparser, cllexer = get_parser_lexer("Python3")
        except ImportError:
            warnings.warn("Grammar for Python3 not ready yet.")
            return
        parser = parse_code(code, clparser, cllexer)
        try:
            tree = parser.single_input()
        except NameError as e:
            warnings.warn("Grammar for Python3 not ready yet: {0}".format(e))
            return
        st = get_tree_string(tree, parser)
        assert len(st) > 0

    @unittest.skipIf(sys.version_info[:2] < (3, 10),
                     reason="grammars compiled on python 3.10")
    def test_DOT(self):
        from pyensae.languages.antlr_grammar_use import (
            get_parser_lexer, get_tree_string, parse_code)
        from pyensae.languages.antlr_grammar_build import build_grammar
        import pyensae.languages.antlr_grammar_use as source_parser

        # the grammar does not fully compile

        code = """
        digraph {
            A [label="a"] ;
            B [label="b"] ;
            A -> B ;
        """

        clparser, cllexer = get_parser_lexer("DOT")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.graph()
        st = get_tree_string(tree, parser)
        assert len(st) > 0


if __name__ == "__main__":
    TestParseCode().test_csharp()
    unittest.main()
