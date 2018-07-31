"""
@brief      test log(time=4s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys
import os
import unittest
from pyquickhelper.loghelper import fLOG
from pyquickhelper.pycode import get_temp_folder


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

from src.pyensae.languages.antlr_grammar_use import get_parser_lexer, get_tree_string, parse_code, get_tree_graph
from src.pyensae.languages.antlr_grammar_build import build_grammar
from src.pyensae.graphhelper import run_dot
import src.pyensae.languages.antlr_grammar_use as source_parser


class TestParseCodeSimpleWorkflow (unittest.TestCase):

    def test_build_parser_simple_workflow(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        langs = ["SimpleWorkflow"]

        try:
            for lang in langs:
                clparser, cllexer = get_parser_lexer(lang)
            return
        except ImportError:
            pass

        folder = os.path.dirname(source_parser.__file__)

        for lang in langs:
            fLOG("generate for LANG", lang)
            gr = os.path.join(folder, lang + ".g4")
            assert os.path.exists(gr)
            final = build_grammar(lang, fLOG=fLOG)
            fLOG(final)

    def test_simple_workflow(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
        set varconst = 10 ;
        data_a = flowdata.DataCloud ;
        modb = flowmodule.RandomFilter(
                    n= 100
                    ) ;
        connect data_a to modb.input ;

        if ( positive_number(modb.average, varconst)) {
            modc = flowmodule.Classify(model="LinearRegression") ;
            connect ( modb.data , modc.train_data ) ;
        }
        """

        clparser, cllexer = get_parser_lexer("SimpleWorkflow")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        assert len(st) > 0
        st = get_tree_graph(tree, parser)
        dot = st.to_dot()
        assert len(dot) > 0

        if "travis" not in sys.executable:
            temp = get_temp_folder(__file__, "temp_simpleworkflow_grammar")
            name = os.path.join(temp, "graph.dot")
            with open(name, "w") as f:
                f.write(dot)
            img = os.path.join(temp, "graph.png")
            run_dot(name, img)
            assert os.path.exists(img)

    def test_simple_for_workflow(self):
        fLOG(
            __file__,
            self._testMethodName,
            OutputPrint=__name__ == "__main__")

        code = """
        data_a = flowdata.DataCloud ;
        modb = flowmodule.RandomFilter(
                    n= 100
                    ) ;
        connect data_a to modb.input ;

        if ( positive_number(modb.average)) {
            modc = flowmodule.Classify(model="LinearRegression") ;
            connect ( modb.data , modc.train_data ) ;

            if ( positive_number(modc.number)) {
                modc2 = flowmodule.Classify(model="SVM") ;
                connect ( modc.data , mod2.input ) ;

                for ( loopv in range(10) ) {
                    modcl = flowmodule.Classify(model=loopv) ;
                    connect ( modc2.data , modcl.output ) ;
                }

            }
        }
        """

        clparser, cllexer = get_parser_lexer("SimpleWorkflow")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        assert len(st) > 0
        st = get_tree_graph(tree, parser)
        dot = st.to_dot()
        assert len(dot) > 0

        if "travis" not in sys.executable:
            temp = get_temp_folder(__file__, "temp_simpleworkflow_grammar_for")
            name = os.path.join(temp, "graph.dot")
            with open(name, "w") as f:
                f.write(dot)
            img = os.path.join(temp, "graph.png")
            run_dot(name, img)
            assert os.path.exists(img)


if __name__ == "__main__":
    unittest.main()
