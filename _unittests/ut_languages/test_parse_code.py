"""
@brief      test log(time=2s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""


import sys, os, unittest


try :
    import src
    import pyquickhelper
except ImportError :
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..")))
    if path not in sys.path : sys.path.append (path)
    path = os.path.normpath(os.path.abspath( os.path.join( os.path.split(__file__)[0], "..", "..", "..", "pyquickhelper", "src")))
    if path not in sys.path : sys.path.append (path)
    import src
    import pyquickhelper

from pyquickhelper import fLOG
from src.pyensae.languages.antlr_grammar_use import get_parser_lexer, get_tree_string, parse_code

class TestParseCode (unittest.TestCase):
    
    def test_r(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        
        code = """
        a = 4 ;
        b = 5 ;
        c = a + b ;
        """
        
        clparser,cllexer = get_parser_lexer("R")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser)
        assert len(st)>0
        st = get_tree_string(tree, parser, None)
        fLOG(st.replace("\\n","\n"))
        assert len(st)>0

    def test_sql(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        
        code = """
        SELECT a,tbl.b,nb FROM tbl 
        INNER JOIN (
            SELECT b, COUNT(*) AS nb FROM tbl
            ) AS tblG
        ON tbl.b == tblG.b ;
        """
        
        clparser,cllexer = get_parser_lexer("SQLite")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser, None)
        fLOG(st.replace("\\n","\n"))
        assert len(st)>0

    def test_error(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        
        code = """
        SELECT a,tbl.b,nb$ FROM tbl 
        INNER JOIN (
            SELECT b, COUNT(*) AS nb FROM tbl
            ) AS tblG
        ON tbl.b == tblG.b ;
        """
        
        clparser,cllexer = get_parser_lexer("SQLite")
        parser = parse_code(code, clparser, cllexer)
        try:
            tree = parser.parse()
        except SyntaxError as e :
            fLOG(e)
            return
            
        raise Exception("should not be here")

    def test_pig(self) :
        fLOG (__file__, self._testMethodName, OutputPrint = __name__ == "__main__")
        
        code = """
        A = LOAD 'filename.txt' USING PigStorage('\t');
        STORE A INTO 'samefile.txt' ;
        """
        
        clparser,cllexer = get_parser_lexer("Pig")
        parser = parse_code(code, clparser, cllexer)
        tree = parser.parse()
        st = get_tree_string(tree, parser, None)
        fLOG(st.replace("\\n","\n"))
        assert len(st)>0

        
        

if __name__ == "__main__"  :
    unittest.main ()    
