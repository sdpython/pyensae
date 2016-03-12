"""
@brief      test log(time=3s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest


try:
    import src
    import pyquickhelper
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
    import pyquickhelper

from pyquickhelper import fLOG
from src.pyensae.languages.antlr_grammar_use import get_parser_lexer, get_tree_string, parse_code
from src.pyensae.languages.antlr_grammar_build import build_grammar
import src.pyensae.languages.antlr_grammar_use as source_parser


class TestParseCode (unittest.TestCase):

    def test_build_parser(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        langs = ["DOT", "CSharp4", "SQLite", "R"]  # , "Python3", "Pig"]

        try:
            for lang in langs:
                clparser, cllexer = get_parser_lexer(lang)
            return
        except ImportError as e:
            pass

        folder = os.path.dirname(source_parser.__file__)

        for lang in langs:
            fLOG("generate for LANG", lang)
            gr = os.path.join(folder, lang + ".g4")
            assert os.path.exists(gr)
            final = build_grammar(lang, fLOG=fLOG)
            fLOG(final)

    def test_r(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

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
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0

    def test_sql(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

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
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0

    def test_error(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
        SELECT a,tbl.b,nb$ FROM tbl
        INNER JOIN (
            SELECT b, COUNT(*) AS nb FROM tbl
            ) AS tblG
        ON tbl.b == tblG.b ;
        """

        clparser, cllexer = get_parser_lexer("SQLite")
        parser = parse_code(code, clparser, cllexer)
        try:
            tree = parser.parse()
        except SyntaxError as e:
            fLOG(e)
            return

        raise Exception("should not be here")

    def test_pig(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # does not work yet
        return

        code = """
        A = LOAD 'filename.txt' USING PigStorage('\t');
        STORE A INTO 'samefile.txt' ;
        """

        clparser, cllexer = get_parser_lexer("Pig")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser, None)
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0

    def test_csharp(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

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
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0

    def test_python3(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # the grammar does not fully compile
        return

        code = """
        def addition(x, y):
            return x + y
        """

        clparser, cllexer = get_parser_lexer("Python3")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0

    def test_DOT(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        # the grammar does not fully compile
        return

        code = """
        digraph {
            A [label="a"] ;
            B [label="b"] ;
            A -> B ;
        """

        clparser, cllexer = get_parser_lexer("DOT")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        fLOG(st.replace("\\n", "\n"))
        assert len(st) > 0


if __name__ == "__main__":
    unittest.main()
