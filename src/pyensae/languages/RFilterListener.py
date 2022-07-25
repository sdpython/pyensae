# Generated from \RFilter.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RFilter import RFilter
else:
    from RFilter import RFilter

# This class defines a complete listener for a parse tree produced by RFilter.


class RFilterListener(ParseTreeListener):

    # Enter a parse tree produced by RFilter#stream.
    def enterStream(self, ctx: RFilter.StreamContext):
        pass

    # Exit a parse tree produced by RFilter#stream.
    def exitStream(self, ctx: RFilter.StreamContext):
        pass

    # Enter a parse tree produced by RFilter#eat.
    def enterEat(self, ctx: RFilter.EatContext):
        pass

    # Exit a parse tree produced by RFilter#eat.
    def exitEat(self, ctx: RFilter.EatContext):
        pass

    # Enter a parse tree produced by RFilter#elem.
    def enterElem(self, ctx: RFilter.ElemContext):
        pass

    # Exit a parse tree produced by RFilter#elem.
    def exitElem(self, ctx: RFilter.ElemContext):
        pass

    # Enter a parse tree produced by RFilter#atom.
    def enterAtom(self, ctx: RFilter.AtomContext):
        pass

    # Exit a parse tree produced by RFilter#atom.
    def exitAtom(self, ctx: RFilter.AtomContext):
        pass

    # Enter a parse tree produced by RFilter#op.
    def enterOp(self, ctx: RFilter.OpContext):
        pass

    # Exit a parse tree produced by RFilter#op.
    def exitOp(self, ctx: RFilter.OpContext):
        pass


del RFilter
