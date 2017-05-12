# Generated from \R.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .RParser import RParser
else:
    from RParser import RParser

# This class defines a complete listener for a parse tree produced by RParser.


class RListener(ParseTreeListener):

    # Enter a parse tree produced by RParser#parse.
    def enterParse(self, ctx: RParser.ParseContext):
        pass

    # Exit a parse tree produced by RParser#parse.
    def exitParse(self, ctx: RParser.ParseContext):
        pass

    # Enter a parse tree produced by RParser#expr.
    def enterExpr(self, ctx: RParser.ExprContext):
        pass

    # Exit a parse tree produced by RParser#expr.
    def exitExpr(self, ctx: RParser.ExprContext):
        pass

    # Enter a parse tree produced by RParser#exprlist.
    def enterExprlist(self, ctx: RParser.ExprlistContext):
        pass

    # Exit a parse tree produced by RParser#exprlist.
    def exitExprlist(self, ctx: RParser.ExprlistContext):
        pass

    # Enter a parse tree produced by RParser#formlist.
    def enterFormlist(self, ctx: RParser.FormlistContext):
        pass

    # Exit a parse tree produced by RParser#formlist.
    def exitFormlist(self, ctx: RParser.FormlistContext):
        pass

    # Enter a parse tree produced by RParser#form.
    def enterForm(self, ctx: RParser.FormContext):
        pass

    # Exit a parse tree produced by RParser#form.
    def exitForm(self, ctx: RParser.FormContext):
        pass

    # Enter a parse tree produced by RParser#sublist.
    def enterSublist(self, ctx: RParser.SublistContext):
        pass

    # Exit a parse tree produced by RParser#sublist.
    def exitSublist(self, ctx: RParser.SublistContext):
        pass

    # Enter a parse tree produced by RParser#sub.
    def enterSub(self, ctx: RParser.SubContext):
        pass

    # Exit a parse tree produced by RParser#sub.
    def exitSub(self, ctx: RParser.SubContext):
        pass

    # Enter a parse tree produced by RParser#constant.
    def enterConstant(self, ctx: RParser.ConstantContext):
        pass

    # Exit a parse tree produced by RParser#constant.
    def exitConstant(self, ctx: RParser.ConstantContext):
        pass

    # Enter a parse tree produced by RParser#boolean.
    def enterBoolean(self, ctx: RParser.BooleanContext):
        pass

    # Exit a parse tree produced by RParser#boolean.
    def exitBoolean(self, ctx: RParser.BooleanContext):
        pass

    # Enter a parse tree produced by RParser#nextexpr.
    def enterNextexpr(self, ctx: RParser.NextexprContext):
        pass

    # Exit a parse tree produced by RParser#nextexpr.
    def exitNextexpr(self, ctx: RParser.NextexprContext):
        pass

    # Enter a parse tree produced by RParser#repeatexpr.
    def enterRepeatexpr(self, ctx: RParser.RepeatexprContext):
        pass

    # Exit a parse tree produced by RParser#repeatexpr.
    def exitRepeatexpr(self, ctx: RParser.RepeatexprContext):
        pass

    # Enter a parse tree produced by RParser#whileexpr.
    def enterWhileexpr(self, ctx: RParser.WhileexprContext):
        pass

    # Exit a parse tree produced by RParser#whileexpr.
    def exitWhileexpr(self, ctx: RParser.WhileexprContext):
        pass

    # Enter a parse tree produced by RParser#forexpr.
    def enterForexpr(self, ctx: RParser.ForexprContext):
        pass

    # Exit a parse tree produced by RParser#forexpr.
    def exitForexpr(self, ctx: RParser.ForexprContext):
        pass

    # Enter a parse tree produced by RParser#ifexpr.
    def enterIfexpr(self, ctx: RParser.IfexprContext):
        pass

    # Exit a parse tree produced by RParser#ifexpr.
    def exitIfexpr(self, ctx: RParser.IfexprContext):
        pass

    # Enter a parse tree produced by RParser#ifelseexpr.
    def enterIfelseexpr(self, ctx: RParser.IfelseexprContext):
        pass

    # Exit a parse tree produced by RParser#ifelseexpr.
    def exitIfelseexpr(self, ctx: RParser.IfelseexprContext):
        pass

    # Enter a parse tree produced by RParser#returnexpr.
    def enterReturnexpr(self, ctx: RParser.ReturnexprContext):
        pass

    # Exit a parse tree produced by RParser#returnexpr.
    def exitReturnexpr(self, ctx: RParser.ReturnexprContext):
        pass

    # Enter a parse tree produced by RParser#functioncall.
    def enterFunctioncall(self, ctx: RParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by RParser#functioncall.
    def exitFunctioncall(self, ctx: RParser.FunctioncallContext):
        pass

    # Enter a parse tree produced by RParser#affectop.
    def enterAffectop(self, ctx: RParser.AffectopContext):
        pass

    # Exit a parse tree produced by RParser#affectop.
    def exitAffectop(self, ctx: RParser.AffectopContext):
        pass

    # Enter a parse tree produced by RParser#functiondef.
    def enterFunctiondef(self, ctx: RParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by RParser#functiondef.
    def exitFunctiondef(self, ctx: RParser.FunctiondefContext):
        pass

    # Enter a parse tree produced by RParser#identifier.
    def enterIdentifier(self, ctx: RParser.IdentifierContext):
        pass

    # Exit a parse tree produced by RParser#identifier.
    def exitIdentifier(self, ctx: RParser.IdentifierContext):
        pass

    # Enter a parse tree produced by RParser#formop.
    def enterFormop(self, ctx: RParser.FormopContext):
        pass

    # Exit a parse tree produced by RParser#formop.
    def exitFormop(self, ctx: RParser.FormopContext):
        pass

    # Enter a parse tree produced by RParser#rangeop.
    def enterRangeop(self, ctx: RParser.RangeopContext):
        pass

    # Exit a parse tree produced by RParser#rangeop.
    def exitRangeop(self, ctx: RParser.RangeopContext):
        pass

    # Enter a parse tree produced by RParser#dotop.
    def enterDotop(self, ctx: RParser.DotopContext):
        pass

    # Exit a parse tree produced by RParser#dotop.
    def exitDotop(self, ctx: RParser.DotopContext):
        pass

    # Enter a parse tree produced by RParser#operator.
    def enterOperator(self, ctx: RParser.OperatorContext):
        pass

    # Exit a parse tree produced by RParser#operator.
    def exitOperator(self, ctx: RParser.OperatorContext):
        pass

    # Enter a parse tree produced by RParser#comparison.
    def enterComparison(self, ctx: RParser.ComparisonContext):
        pass

    # Exit a parse tree produced by RParser#comparison.
    def exitComparison(self, ctx: RParser.ComparisonContext):
        pass
