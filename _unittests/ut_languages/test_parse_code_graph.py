"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder, fix_tkinter_issues_virtualenv
from pyensae.languages.antlr_grammar_use import get_parser_lexer, get_tree_graph, parse_code
from pyensae.graphhelper import run_dot


class TestParseCodeGraph (unittest.TestCase):

    def test_charp_graph_networkx(self):
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
        st = get_tree_graph(tree, parser)

        if "travis" in sys.executable:
            # no networkx
            return

        st.draw()

        fix_tkinter_issues_virtualenv()
        import matplotlib.pyplot as plt
        if __name__ == "__main__":
            plt.show()

        plt.close('all')

    def test_graph_graphviz(self):
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
        st = get_tree_graph(tree, parser)
        dot = st.to_dot()
        # fLOG(dot)
        assert len(dot) > 0

        if "travis" not in sys.executable:
            temp = get_temp_folder(__file__, "temp_dot_grammar")
            name = os.path.join(temp, "graph.dot")
            with open(name, "w") as f:
                f.write(dot)
            img = os.path.join(temp, "graph.png")
            run_dot(name, img)
            assert os.path.exists(img)


if __name__ == "__main__":
    unittest.main()
