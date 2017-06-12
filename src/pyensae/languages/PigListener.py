# Generated from \Pig.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .PigParser import PigParser
else:
    from PigParser import PigParser

# This class defines a complete listener for a parse tree produced by PigParser.


class PigListener(ParseTreeListener):

    # Enter a parse tree produced by PigParser#parse.
    def enterParse(self, ctx: PigParser.ParseContext):
        pass

    # Exit a parse tree produced by PigParser#parse.
    def exitParse(self, ctx: PigParser.ParseContext):
        pass

    # Enter a parse tree produced by PigParser#query.
    def enterQuery(self, ctx: PigParser.QueryContext):
        pass

    # Exit a parse tree produced by PigParser#query.
    def exitQuery(self, ctx: PigParser.QueryContext):
        pass

    # Enter a parse tree produced by PigParser#statement.
    def enterStatement(self, ctx: PigParser.StatementContext):
        pass

    # Exit a parse tree produced by PigParser#statement.
    def exitStatement(self, ctx: PigParser.StatementContext):
        pass

    # Enter a parse tree produced by PigParser#alias.
    def enterAlias(self, ctx: PigParser.AliasContext):
        pass

    # Exit a parse tree produced by PigParser#alias.
    def exitAlias(self, ctx: PigParser.AliasContext):
        pass

    # Enter a parse tree produced by PigParser#op_clause.
    def enterOp_clause(self, ctx: PigParser.Op_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#op_clause.
    def exitOp_clause(self, ctx: PigParser.Op_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#load_clause.
    def enterLoad_clause(self, ctx: PigParser.Load_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#load_clause.
    def exitLoad_clause(self, ctx: PigParser.Load_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#filename.
    def enterFilename(self, ctx: PigParser.FilenameContext):
        pass

    # Exit a parse tree produced by PigParser#filename.
    def exitFilename(self, ctx: PigParser.FilenameContext):
        pass

    # Enter a parse tree produced by PigParser#as_clause.
    def enterAs_clause(self, ctx: PigParser.As_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#as_clause.
    def exitAs_clause(self, ctx: PigParser.As_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#tuple_def.
    def enterTuple_def(self, ctx: PigParser.Tuple_defContext):
        pass

    # Exit a parse tree produced by PigParser#tuple_def.
    def exitTuple_def(self, ctx: PigParser.Tuple_defContext):
        pass

    # Enter a parse tree produced by PigParser#field.
    def enterField(self, ctx: PigParser.FieldContext):
        pass

    # Exit a parse tree produced by PigParser#field.
    def exitField(self, ctx: PigParser.FieldContext):
        pass

    # Enter a parse tree produced by PigParser#type_.
    def enterType_(self, ctx: PigParser.Type_Context):
        pass

    # Exit a parse tree produced by PigParser#type_.
    def exitType_(self, ctx: PigParser.Type_Context):
        pass

    # Enter a parse tree produced by PigParser#simple_type.
    def enterSimple_type(self, ctx: PigParser.Simple_typeContext):
        pass

    # Exit a parse tree produced by PigParser#simple_type.
    def exitSimple_type(self, ctx: PigParser.Simple_typeContext):
        pass

    # Enter a parse tree produced by PigParser#tuple_type.
    def enterTuple_type(self, ctx: PigParser.Tuple_typeContext):
        pass

    # Exit a parse tree produced by PigParser#tuple_type.
    def exitTuple_type(self, ctx: PigParser.Tuple_typeContext):
        pass

    # Enter a parse tree produced by PigParser#bag_type.
    def enterBag_type(self, ctx: PigParser.Bag_typeContext):
        pass

    # Exit a parse tree produced by PigParser#bag_type.
    def exitBag_type(self, ctx: PigParser.Bag_typeContext):
        pass

    # Enter a parse tree produced by PigParser#map_type.
    def enterMap_type(self, ctx: PigParser.Map_typeContext):
        pass

    # Exit a parse tree produced by PigParser#map_type.
    def exitMap_type(self, ctx: PigParser.Map_typeContext):
        pass

    # Enter a parse tree produced by PigParser#func_clause.
    def enterFunc_clause(self, ctx: PigParser.Func_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#func_clause.
    def exitFunc_clause(self, ctx: PigParser.Func_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#func_name.
    def enterFunc_name(self, ctx: PigParser.Func_nameContext):
        pass

    # Exit a parse tree produced by PigParser#func_name.
    def exitFunc_name(self, ctx: PigParser.Func_nameContext):
        pass

    # Enter a parse tree produced by PigParser#func_args.
    def enterFunc_args(self, ctx: PigParser.Func_argsContext):
        pass

    # Exit a parse tree produced by PigParser#func_args.
    def exitFunc_args(self, ctx: PigParser.Func_argsContext):
        pass

    # Enter a parse tree produced by PigParser#store_clause.
    def enterStore_clause(self, ctx: PigParser.Store_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#store_clause.
    def exitStore_clause(self, ctx: PigParser.Store_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#filter_clause.
    def enterFilter_clause(self, ctx: PigParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#filter_clause.
    def exitFilter_clause(self, ctx: PigParser.Filter_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#cond.
    def enterCond(self, ctx: PigParser.CondContext):
        pass

    # Exit a parse tree produced by PigParser#cond.
    def exitCond(self, ctx: PigParser.CondContext):
        pass

    # Enter a parse tree produced by PigParser#or_cond.
    def enterOr_cond(self, ctx: PigParser.Or_condContext):
        pass

    # Exit a parse tree produced by PigParser#or_cond.
    def exitOr_cond(self, ctx: PigParser.Or_condContext):
        pass

    # Enter a parse tree produced by PigParser#and_cond.
    def enterAnd_cond(self, ctx: PigParser.And_condContext):
        pass

    # Exit a parse tree produced by PigParser#and_cond.
    def exitAnd_cond(self, ctx: PigParser.And_condContext):
        pass

    # Enter a parse tree produced by PigParser#unary_cond.
    def enterUnary_cond(self, ctx: PigParser.Unary_condContext):
        pass

    # Exit a parse tree produced by PigParser#unary_cond.
    def exitUnary_cond(self, ctx: PigParser.Unary_condContext):
        pass

    # Enter a parse tree produced by PigParser#not_cond.
    def enterNot_cond(self, ctx: PigParser.Not_condContext):
        pass

    # Exit a parse tree produced by PigParser#not_cond.
    def exitNot_cond(self, ctx: PigParser.Not_condContext):
        pass

    # Enter a parse tree produced by PigParser#null_check_cond.
    def enterNull_check_cond(self, ctx: PigParser.Null_check_condContext):
        pass

    # Exit a parse tree produced by PigParser#null_check_cond.
    def exitNull_check_cond(self, ctx: PigParser.Null_check_condContext):
        pass

    # Enter a parse tree produced by PigParser#expr.
    def enterExpr(self, ctx: PigParser.ExprContext):
        pass

    # Exit a parse tree produced by PigParser#expr.
    def exitExpr(self, ctx: PigParser.ExprContext):
        pass

    # Enter a parse tree produced by PigParser#add_expr.
    def enterAdd_expr(self, ctx: PigParser.Add_exprContext):
        pass

    # Exit a parse tree produced by PigParser#add_expr.
    def exitAdd_expr(self, ctx: PigParser.Add_exprContext):
        pass

    # Enter a parse tree produced by PigParser#multi_expr.
    def enterMulti_expr(self, ctx: PigParser.Multi_exprContext):
        pass

    # Exit a parse tree produced by PigParser#multi_expr.
    def exitMulti_expr(self, ctx: PigParser.Multi_exprContext):
        pass

    # Enter a parse tree produced by PigParser#cast_expr.
    def enterCast_expr(self, ctx: PigParser.Cast_exprContext):
        pass

    # Exit a parse tree produced by PigParser#cast_expr.
    def exitCast_expr(self, ctx: PigParser.Cast_exprContext):
        pass

    # Enter a parse tree produced by PigParser#unary_expr.
    def enterUnary_expr(self, ctx: PigParser.Unary_exprContext):
        pass

    # Exit a parse tree produced by PigParser#unary_expr.
    def exitUnary_expr(self, ctx: PigParser.Unary_exprContext):
        pass

    # Enter a parse tree produced by PigParser#eval_expr.
    def enterEval_expr(self, ctx: PigParser.Eval_exprContext):
        pass

    # Exit a parse tree produced by PigParser#eval_expr.
    def exitEval_expr(self, ctx: PigParser.Eval_exprContext):
        pass

    # Enter a parse tree produced by PigParser#var_expr.
    def enterVar_expr(self, ctx: PigParser.Var_exprContext):
        pass

    # Exit a parse tree produced by PigParser#var_expr.
    def exitVar_expr(self, ctx: PigParser.Var_exprContext):
        pass

    # Enter a parse tree produced by PigParser#projectable_expr.
    def enterProjectable_expr(self, ctx: PigParser.Projectable_exprContext):
        pass

    # Exit a parse tree produced by PigParser#projectable_expr.
    def exitProjectable_expr(self, ctx: PigParser.Projectable_exprContext):
        pass

    # Enter a parse tree produced by PigParser#dot_proj.
    def enterDot_proj(self, ctx: PigParser.Dot_projContext):
        pass

    # Exit a parse tree produced by PigParser#dot_proj.
    def exitDot_proj(self, ctx: PigParser.Dot_projContext):
        pass

    # Enter a parse tree produced by PigParser#pound_proj.
    def enterPound_proj(self, ctx: PigParser.Pound_projContext):
        pass

    # Exit a parse tree produced by PigParser#pound_proj.
    def exitPound_proj(self, ctx: PigParser.Pound_projContext):
        pass

    # Enter a parse tree produced by PigParser#bin_expr.
    def enterBin_expr(self, ctx: PigParser.Bin_exprContext):
        pass

    # Exit a parse tree produced by PigParser#bin_expr.
    def exitBin_expr(self, ctx: PigParser.Bin_exprContext):
        pass

    # Enter a parse tree produced by PigParser#neg_expr.
    def enterNeg_expr(self, ctx: PigParser.Neg_exprContext):
        pass

    # Exit a parse tree produced by PigParser#neg_expr.
    def exitNeg_expr(self, ctx: PigParser.Neg_exprContext):
        pass

    # Enter a parse tree produced by PigParser#distinct_clause.
    def enterDistinct_clause(self, ctx: PigParser.Distinct_clauseContext):
        pass

    # Exit a parse tree produced by PigParser#distinct_clause.
    def exitDistinct_clause(self, ctx: PigParser.Distinct_clauseContext):
        pass

    # Enter a parse tree produced by PigParser#col_ref.
    def enterCol_ref(self, ctx: PigParser.Col_refContext):
        pass

    # Exit a parse tree produced by PigParser#col_ref.
    def exitCol_ref(self, ctx: PigParser.Col_refContext):
        pass

    # Enter a parse tree produced by PigParser#alias_col_ref.
    def enterAlias_col_ref(self, ctx: PigParser.Alias_col_refContext):
        pass

    # Exit a parse tree produced by PigParser#alias_col_ref.
    def exitAlias_col_ref(self, ctx: PigParser.Alias_col_refContext):
        pass

    # Enter a parse tree produced by PigParser#dollar_col_ref.
    def enterDollar_col_ref(self, ctx: PigParser.Dollar_col_refContext):
        pass

    # Exit a parse tree produced by PigParser#dollar_col_ref.
    def exitDollar_col_ref(self, ctx: PigParser.Dollar_col_refContext):
        pass

    # Enter a parse tree produced by PigParser#infix_expr.
    def enterInfix_expr(self, ctx: PigParser.Infix_exprContext):
        pass

    # Exit a parse tree produced by PigParser#infix_expr.
    def exitInfix_expr(self, ctx: PigParser.Infix_exprContext):
        pass

    # Enter a parse tree produced by PigParser#const_expr.
    def enterConst_expr(self, ctx: PigParser.Const_exprContext):
        pass

    # Exit a parse tree produced by PigParser#const_expr.
    def exitConst_expr(self, ctx: PigParser.Const_exprContext):
        pass

    # Enter a parse tree produced by PigParser#scalar.
    def enterScalar(self, ctx: PigParser.ScalarContext):
        pass

    # Exit a parse tree produced by PigParser#scalar.
    def exitScalar(self, ctx: PigParser.ScalarContext):
        pass

    # Enter a parse tree produced by PigParser#map_.
    def enterMap_(self, ctx: PigParser.Map_Context):
        pass

    # Exit a parse tree produced by PigParser#map_.
    def exitMap_(self, ctx: PigParser.Map_Context):
        pass

    # Enter a parse tree produced by PigParser#keyvalue.
    def enterKeyvalue(self, ctx: PigParser.KeyvalueContext):
        pass

    # Exit a parse tree produced by PigParser#keyvalue.
    def exitKeyvalue(self, ctx: PigParser.KeyvalueContext):
        pass

    # Enter a parse tree produced by PigParser#string_val.
    def enterString_val(self, ctx: PigParser.String_valContext):
        pass

    # Exit a parse tree produced by PigParser#string_val.
    def exitString_val(self, ctx: PigParser.String_valContext):
        pass

    # Enter a parse tree produced by PigParser#bag.
    def enterBag(self, ctx: PigParser.BagContext):
        pass

    # Exit a parse tree produced by PigParser#bag.
    def exitBag(self, ctx: PigParser.BagContext):
        pass

    # Enter a parse tree produced by PigParser#tuple_.
    def enterTuple_(self, ctx: PigParser.Tuple_Context):
        pass

    # Exit a parse tree produced by PigParser#tuple_.
    def exitTuple_(self, ctx: PigParser.Tuple_Context):
        pass
