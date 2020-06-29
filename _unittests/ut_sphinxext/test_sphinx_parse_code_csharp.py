"""
@brief      test log(time=3s)

You should indicate a time in seconds. The program ``run_unittests.py``
will sort all test files by increasing time and run them.
"""
import unittest
from pyquickhelper.pycode import ExtTestCase
from pyensae.sphinxext import CSharpParser


class TestSphinxParseCodeCSharp(ExtTestCase):

    def test_csharp_parse(self):
        code = """
        namespace hello_dom
        {
            public static class world
            {
                /// <summary>
                /// Documentation of one function
                /// </summary>
                /// <param name="x">first real</param>
                /// <param name="y">second real</param>
                /// <return>real</return>
                public static double functionz(double x, double y)
                { return x+y ; }
            }
            public class world_nostatic
            {
                public virtual double functionz(double x, double y)
                { return x+y ; }
            }
            /// <summary>
            /// Documentation
            /// </summary>
            public class world_nostatic2: world_nostatic
            {
                public int JJ => myj;
                int myj;
                public world_nostatic2(int j) { myj = j; }
                /// <desc>
                /// DOCDOC
                /// </desc>
                public override double functionz(double x, double y)
                { return base.function(x, y); }
            }
        }
        """
        p = CSharpParser()
        els = p.parse(code)
        self.assertNotEmpty(els)
        self.assertEqual(els[0].__class__.__name__, "CSharpDomain")
        self.assertEqual(str(els[0]), "namespace world_nostatic")


if __name__ == "__main__":
    unittest.main()
