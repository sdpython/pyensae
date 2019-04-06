"""
@brief      test log(time=3s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
import warnings
from pyquickhelper.pycode import ExtTestCase
from pyensae.languages.antlr_grammar_use import get_parser_lexer, get_tree_string, parse_code
from pyensae.languages.antlr_grammar_build import build_grammar
import pyensae.languages.antlr_grammar_use as source_parser


class TestParseCodeCSharp(ExtTestCase):

    def test_csharp_parse(self):
        code = """
        namespace hello
        {
            public static class world
            {
                public static double function(double x, double y)
                { return x+y ; }
            }
            public class world_nostatic
            {
                public virtual double function(double x, double y)
                { return x+y ; }
            }
            /// <summary>
            /// Documentation
            /// </summary>
            public class world_nostatic2: world_nostatic
            {
                public int J => myj;
                int myj;
                public world_nostatic2(int j) { myj = j; }
                /// <desc>
                /// DOCDOC
                /// </desc>
                public override double function(double x, double y)
                { return base.function(x, y); }
            }
        }
        """

        clparser, cllexer = get_parser_lexer("C#")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        self.assertNotEmpty(st)
        self.assertIn("/// <summary>", st)


if __name__ == "__main__":
    unittest.main()
