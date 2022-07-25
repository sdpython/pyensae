# Generated from \SQLiteParser.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SQLiteParser import SQLiteParser
else:
    from SQLiteParser import SQLiteParser

# This class defines a complete listener for a parse tree produced by SQLiteParser.


class SQLiteParserListener(ParseTreeListener):

    # Enter a parse tree produced by SQLiteParser#parse.
    def enterParse(self, ctx: SQLiteParser.ParseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#parse.
    def exitParse(self, ctx: SQLiteParser.ParseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#sql_stmt_list.
    def enterSql_stmt_list(self, ctx: SQLiteParser.Sql_stmt_listContext):
        pass

    # Exit a parse tree produced by SQLiteParser#sql_stmt_list.
    def exitSql_stmt_list(self, ctx: SQLiteParser.Sql_stmt_listContext):
        pass

    # Enter a parse tree produced by SQLiteParser#sql_stmt.
    def enterSql_stmt(self, ctx: SQLiteParser.Sql_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#sql_stmt.
    def exitSql_stmt(self, ctx: SQLiteParser.Sql_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#alter_table_stmt.
    def enterAlter_table_stmt(self, ctx: SQLiteParser.Alter_table_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#alter_table_stmt.
    def exitAlter_table_stmt(self, ctx: SQLiteParser.Alter_table_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#analyze_stmt.
    def enterAnalyze_stmt(self, ctx: SQLiteParser.Analyze_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#analyze_stmt.
    def exitAnalyze_stmt(self, ctx: SQLiteParser.Analyze_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#attach_stmt.
    def enterAttach_stmt(self, ctx: SQLiteParser.Attach_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#attach_stmt.
    def exitAttach_stmt(self, ctx: SQLiteParser.Attach_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#begin_stmt.
    def enterBegin_stmt(self, ctx: SQLiteParser.Begin_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#begin_stmt.
    def exitBegin_stmt(self, ctx: SQLiteParser.Begin_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#commit_stmt.
    def enterCommit_stmt(self, ctx: SQLiteParser.Commit_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#commit_stmt.
    def exitCommit_stmt(self, ctx: SQLiteParser.Commit_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#rollback_stmt.
    def enterRollback_stmt(self, ctx: SQLiteParser.Rollback_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#rollback_stmt.
    def exitRollback_stmt(self, ctx: SQLiteParser.Rollback_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#savepoint_stmt.
    def enterSavepoint_stmt(self, ctx: SQLiteParser.Savepoint_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#savepoint_stmt.
    def exitSavepoint_stmt(self, ctx: SQLiteParser.Savepoint_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#release_stmt.
    def enterRelease_stmt(self, ctx: SQLiteParser.Release_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#release_stmt.
    def exitRelease_stmt(self, ctx: SQLiteParser.Release_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#create_index_stmt.
    def enterCreate_index_stmt(self, ctx: SQLiteParser.Create_index_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#create_index_stmt.
    def exitCreate_index_stmt(self, ctx: SQLiteParser.Create_index_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#indexed_column.
    def enterIndexed_column(self, ctx: SQLiteParser.Indexed_columnContext):
        pass

    # Exit a parse tree produced by SQLiteParser#indexed_column.
    def exitIndexed_column(self, ctx: SQLiteParser.Indexed_columnContext):
        pass

    # Enter a parse tree produced by SQLiteParser#create_table_stmt.
    def enterCreate_table_stmt(self, ctx: SQLiteParser.Create_table_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#create_table_stmt.
    def exitCreate_table_stmt(self, ctx: SQLiteParser.Create_table_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#column_def.
    def enterColumn_def(self, ctx: SQLiteParser.Column_defContext):
        pass

    # Exit a parse tree produced by SQLiteParser#column_def.
    def exitColumn_def(self, ctx: SQLiteParser.Column_defContext):
        pass

    # Enter a parse tree produced by SQLiteParser#type_name.
    def enterType_name(self, ctx: SQLiteParser.Type_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#type_name.
    def exitType_name(self, ctx: SQLiteParser.Type_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#column_constraint.
    def enterColumn_constraint(self, ctx: SQLiteParser.Column_constraintContext):
        pass

    # Exit a parse tree produced by SQLiteParser#column_constraint.
    def exitColumn_constraint(self, ctx: SQLiteParser.Column_constraintContext):
        pass

    # Enter a parse tree produced by SQLiteParser#signed_number.
    def enterSigned_number(self, ctx: SQLiteParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by SQLiteParser#signed_number.
    def exitSigned_number(self, ctx: SQLiteParser.Signed_numberContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_constraint.
    def enterTable_constraint(self, ctx: SQLiteParser.Table_constraintContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_constraint.
    def exitTable_constraint(self, ctx: SQLiteParser.Table_constraintContext):
        pass

    # Enter a parse tree produced by SQLiteParser#foreign_key_clause.
    def enterForeign_key_clause(self, ctx: SQLiteParser.Foreign_key_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#foreign_key_clause.
    def exitForeign_key_clause(self, ctx: SQLiteParser.Foreign_key_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#conflict_clause.
    def enterConflict_clause(self, ctx: SQLiteParser.Conflict_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#conflict_clause.
    def exitConflict_clause(self, ctx: SQLiteParser.Conflict_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#create_trigger_stmt.
    def enterCreate_trigger_stmt(self, ctx: SQLiteParser.Create_trigger_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#create_trigger_stmt.
    def exitCreate_trigger_stmt(self, ctx: SQLiteParser.Create_trigger_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#create_view_stmt.
    def enterCreate_view_stmt(self, ctx: SQLiteParser.Create_view_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#create_view_stmt.
    def exitCreate_view_stmt(self, ctx: SQLiteParser.Create_view_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#create_virtual_table_stmt.
    def enterCreate_virtual_table_stmt(self, ctx: SQLiteParser.Create_virtual_table_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#create_virtual_table_stmt.
    def exitCreate_virtual_table_stmt(self, ctx: SQLiteParser.Create_virtual_table_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#with_clause.
    def enterWith_clause(self, ctx: SQLiteParser.With_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#with_clause.
    def exitWith_clause(self, ctx: SQLiteParser.With_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#cte_table_name.
    def enterCte_table_name(self, ctx: SQLiteParser.Cte_table_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#cte_table_name.
    def exitCte_table_name(self, ctx: SQLiteParser.Cte_table_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#recursive_cte.
    def enterRecursive_cte(self, ctx: SQLiteParser.Recursive_cteContext):
        pass

    # Exit a parse tree produced by SQLiteParser#recursive_cte.
    def exitRecursive_cte(self, ctx: SQLiteParser.Recursive_cteContext):
        pass

    # Enter a parse tree produced by SQLiteParser#common_table_expression.
    def enterCommon_table_expression(self, ctx: SQLiteParser.Common_table_expressionContext):
        pass

    # Exit a parse tree produced by SQLiteParser#common_table_expression.
    def exitCommon_table_expression(self, ctx: SQLiteParser.Common_table_expressionContext):
        pass

    # Enter a parse tree produced by SQLiteParser#delete_stmt.
    def enterDelete_stmt(self, ctx: SQLiteParser.Delete_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#delete_stmt.
    def exitDelete_stmt(self, ctx: SQLiteParser.Delete_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#delete_stmt_limited.
    def enterDelete_stmt_limited(self, ctx: SQLiteParser.Delete_stmt_limitedContext):
        pass

    # Exit a parse tree produced by SQLiteParser#delete_stmt_limited.
    def exitDelete_stmt_limited(self, ctx: SQLiteParser.Delete_stmt_limitedContext):
        pass

    # Enter a parse tree produced by SQLiteParser#detach_stmt.
    def enterDetach_stmt(self, ctx: SQLiteParser.Detach_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#detach_stmt.
    def exitDetach_stmt(self, ctx: SQLiteParser.Detach_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#drop_stmt.
    def enterDrop_stmt(self, ctx: SQLiteParser.Drop_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#drop_stmt.
    def exitDrop_stmt(self, ctx: SQLiteParser.Drop_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#expr.
    def enterExpr(self, ctx: SQLiteParser.ExprContext):
        pass

    # Exit a parse tree produced by SQLiteParser#expr.
    def exitExpr(self, ctx: SQLiteParser.ExprContext):
        pass

    # Enter a parse tree produced by SQLiteParser#raise_function.
    def enterRaise_function(self, ctx: SQLiteParser.Raise_functionContext):
        pass

    # Exit a parse tree produced by SQLiteParser#raise_function.
    def exitRaise_function(self, ctx: SQLiteParser.Raise_functionContext):
        pass

    # Enter a parse tree produced by SQLiteParser#literal_value.
    def enterLiteral_value(self, ctx: SQLiteParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by SQLiteParser#literal_value.
    def exitLiteral_value(self, ctx: SQLiteParser.Literal_valueContext):
        pass

    # Enter a parse tree produced by SQLiteParser#insert_stmt.
    def enterInsert_stmt(self, ctx: SQLiteParser.Insert_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#insert_stmt.
    def exitInsert_stmt(self, ctx: SQLiteParser.Insert_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#returning_clause.
    def enterReturning_clause(self, ctx: SQLiteParser.Returning_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#returning_clause.
    def exitReturning_clause(self, ctx: SQLiteParser.Returning_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#upsert_clause.
    def enterUpsert_clause(self, ctx: SQLiteParser.Upsert_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#upsert_clause.
    def exitUpsert_clause(self, ctx: SQLiteParser.Upsert_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#pragma_stmt.
    def enterPragma_stmt(self, ctx: SQLiteParser.Pragma_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#pragma_stmt.
    def exitPragma_stmt(self, ctx: SQLiteParser.Pragma_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#pragma_value.
    def enterPragma_value(self, ctx: SQLiteParser.Pragma_valueContext):
        pass

    # Exit a parse tree produced by SQLiteParser#pragma_value.
    def exitPragma_value(self, ctx: SQLiteParser.Pragma_valueContext):
        pass

    # Enter a parse tree produced by SQLiteParser#reindex_stmt.
    def enterReindex_stmt(self, ctx: SQLiteParser.Reindex_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#reindex_stmt.
    def exitReindex_stmt(self, ctx: SQLiteParser.Reindex_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#select_stmt.
    def enterSelect_stmt(self, ctx: SQLiteParser.Select_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#select_stmt.
    def exitSelect_stmt(self, ctx: SQLiteParser.Select_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#join_clause.
    def enterJoin_clause(self, ctx: SQLiteParser.Join_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#join_clause.
    def exitJoin_clause(self, ctx: SQLiteParser.Join_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#select_core.
    def enterSelect_core(self, ctx: SQLiteParser.Select_coreContext):
        pass

    # Exit a parse tree produced by SQLiteParser#select_core.
    def exitSelect_core(self, ctx: SQLiteParser.Select_coreContext):
        pass

    # Enter a parse tree produced by SQLiteParser#factored_select_stmt.
    def enterFactored_select_stmt(self, ctx: SQLiteParser.Factored_select_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#factored_select_stmt.
    def exitFactored_select_stmt(self, ctx: SQLiteParser.Factored_select_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#simple_select_stmt.
    def enterSimple_select_stmt(self, ctx: SQLiteParser.Simple_select_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#simple_select_stmt.
    def exitSimple_select_stmt(self, ctx: SQLiteParser.Simple_select_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#compound_select_stmt.
    def enterCompound_select_stmt(self, ctx: SQLiteParser.Compound_select_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#compound_select_stmt.
    def exitCompound_select_stmt(self, ctx: SQLiteParser.Compound_select_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_or_subquery.
    def enterTable_or_subquery(self, ctx: SQLiteParser.Table_or_subqueryContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_or_subquery.
    def exitTable_or_subquery(self, ctx: SQLiteParser.Table_or_subqueryContext):
        pass

    # Enter a parse tree produced by SQLiteParser#result_column.
    def enterResult_column(self, ctx: SQLiteParser.Result_columnContext):
        pass

    # Exit a parse tree produced by SQLiteParser#result_column.
    def exitResult_column(self, ctx: SQLiteParser.Result_columnContext):
        pass

    # Enter a parse tree produced by SQLiteParser#join_operator.
    def enterJoin_operator(self, ctx: SQLiteParser.Join_operatorContext):
        pass

    # Exit a parse tree produced by SQLiteParser#join_operator.
    def exitJoin_operator(self, ctx: SQLiteParser.Join_operatorContext):
        pass

    # Enter a parse tree produced by SQLiteParser#join_constraint.
    def enterJoin_constraint(self, ctx: SQLiteParser.Join_constraintContext):
        pass

    # Exit a parse tree produced by SQLiteParser#join_constraint.
    def exitJoin_constraint(self, ctx: SQLiteParser.Join_constraintContext):
        pass

    # Enter a parse tree produced by SQLiteParser#compound_operator.
    def enterCompound_operator(self, ctx: SQLiteParser.Compound_operatorContext):
        pass

    # Exit a parse tree produced by SQLiteParser#compound_operator.
    def exitCompound_operator(self, ctx: SQLiteParser.Compound_operatorContext):
        pass

    # Enter a parse tree produced by SQLiteParser#update_stmt.
    def enterUpdate_stmt(self, ctx: SQLiteParser.Update_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#update_stmt.
    def exitUpdate_stmt(self, ctx: SQLiteParser.Update_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#column_name_list.
    def enterColumn_name_list(self, ctx: SQLiteParser.Column_name_listContext):
        pass

    # Exit a parse tree produced by SQLiteParser#column_name_list.
    def exitColumn_name_list(self, ctx: SQLiteParser.Column_name_listContext):
        pass

    # Enter a parse tree produced by SQLiteParser#update_stmt_limited.
    def enterUpdate_stmt_limited(self, ctx: SQLiteParser.Update_stmt_limitedContext):
        pass

    # Exit a parse tree produced by SQLiteParser#update_stmt_limited.
    def exitUpdate_stmt_limited(self, ctx: SQLiteParser.Update_stmt_limitedContext):
        pass

    # Enter a parse tree produced by SQLiteParser#qualified_table_name.
    def enterQualified_table_name(self, ctx: SQLiteParser.Qualified_table_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#qualified_table_name.
    def exitQualified_table_name(self, ctx: SQLiteParser.Qualified_table_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#vacuum_stmt.
    def enterVacuum_stmt(self, ctx: SQLiteParser.Vacuum_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#vacuum_stmt.
    def exitVacuum_stmt(self, ctx: SQLiteParser.Vacuum_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#filter_clause.
    def enterFilter_clause(self, ctx: SQLiteParser.Filter_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#filter_clause.
    def exitFilter_clause(self, ctx: SQLiteParser.Filter_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#window_defn.
    def enterWindow_defn(self, ctx: SQLiteParser.Window_defnContext):
        pass

    # Exit a parse tree produced by SQLiteParser#window_defn.
    def exitWindow_defn(self, ctx: SQLiteParser.Window_defnContext):
        pass

    # Enter a parse tree produced by SQLiteParser#over_clause.
    def enterOver_clause(self, ctx: SQLiteParser.Over_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#over_clause.
    def exitOver_clause(self, ctx: SQLiteParser.Over_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#frame_spec.
    def enterFrame_spec(self, ctx: SQLiteParser.Frame_specContext):
        pass

    # Exit a parse tree produced by SQLiteParser#frame_spec.
    def exitFrame_spec(self, ctx: SQLiteParser.Frame_specContext):
        pass

    # Enter a parse tree produced by SQLiteParser#frame_clause.
    def enterFrame_clause(self, ctx: SQLiteParser.Frame_clauseContext):
        pass

    # Exit a parse tree produced by SQLiteParser#frame_clause.
    def exitFrame_clause(self, ctx: SQLiteParser.Frame_clauseContext):
        pass

    # Enter a parse tree produced by SQLiteParser#simple_function_invocation.
    def enterSimple_function_invocation(self, ctx: SQLiteParser.Simple_function_invocationContext):
        pass

    # Exit a parse tree produced by SQLiteParser#simple_function_invocation.
    def exitSimple_function_invocation(self, ctx: SQLiteParser.Simple_function_invocationContext):
        pass

    # Enter a parse tree produced by SQLiteParser#aggregate_function_invocation.
    def enterAggregate_function_invocation(self, ctx: SQLiteParser.Aggregate_function_invocationContext):
        pass

    # Exit a parse tree produced by SQLiteParser#aggregate_function_invocation.
    def exitAggregate_function_invocation(self, ctx: SQLiteParser.Aggregate_function_invocationContext):
        pass

    # Enter a parse tree produced by SQLiteParser#window_function_invocation.
    def enterWindow_function_invocation(self, ctx: SQLiteParser.Window_function_invocationContext):
        pass

    # Exit a parse tree produced by SQLiteParser#window_function_invocation.
    def exitWindow_function_invocation(self, ctx: SQLiteParser.Window_function_invocationContext):
        pass

    # Enter a parse tree produced by SQLiteParser#common_table_stmt.
    def enterCommon_table_stmt(self, ctx: SQLiteParser.Common_table_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#common_table_stmt.
    def exitCommon_table_stmt(self, ctx: SQLiteParser.Common_table_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#order_by_stmt.
    def enterOrder_by_stmt(self, ctx: SQLiteParser.Order_by_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#order_by_stmt.
    def exitOrder_by_stmt(self, ctx: SQLiteParser.Order_by_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#limit_stmt.
    def enterLimit_stmt(self, ctx: SQLiteParser.Limit_stmtContext):
        pass

    # Exit a parse tree produced by SQLiteParser#limit_stmt.
    def exitLimit_stmt(self, ctx: SQLiteParser.Limit_stmtContext):
        pass

    # Enter a parse tree produced by SQLiteParser#ordering_term.
    def enterOrdering_term(self, ctx: SQLiteParser.Ordering_termContext):
        pass

    # Exit a parse tree produced by SQLiteParser#ordering_term.
    def exitOrdering_term(self, ctx: SQLiteParser.Ordering_termContext):
        pass

    # Enter a parse tree produced by SQLiteParser#asc_desc.
    def enterAsc_desc(self, ctx: SQLiteParser.Asc_descContext):
        pass

    # Exit a parse tree produced by SQLiteParser#asc_desc.
    def exitAsc_desc(self, ctx: SQLiteParser.Asc_descContext):
        pass

    # Enter a parse tree produced by SQLiteParser#frame_left.
    def enterFrame_left(self, ctx: SQLiteParser.Frame_leftContext):
        pass

    # Exit a parse tree produced by SQLiteParser#frame_left.
    def exitFrame_left(self, ctx: SQLiteParser.Frame_leftContext):
        pass

    # Enter a parse tree produced by SQLiteParser#frame_right.
    def enterFrame_right(self, ctx: SQLiteParser.Frame_rightContext):
        pass

    # Exit a parse tree produced by SQLiteParser#frame_right.
    def exitFrame_right(self, ctx: SQLiteParser.Frame_rightContext):
        pass

    # Enter a parse tree produced by SQLiteParser#frame_single.
    def enterFrame_single(self, ctx: SQLiteParser.Frame_singleContext):
        pass

    # Exit a parse tree produced by SQLiteParser#frame_single.
    def exitFrame_single(self, ctx: SQLiteParser.Frame_singleContext):
        pass

    # Enter a parse tree produced by SQLiteParser#window_function.
    def enterWindow_function(self, ctx: SQLiteParser.Window_functionContext):
        pass

    # Exit a parse tree produced by SQLiteParser#window_function.
    def exitWindow_function(self, ctx: SQLiteParser.Window_functionContext):
        pass

    # Enter a parse tree produced by SQLiteParser#offset.
    def enterOffset(self, ctx: SQLiteParser.OffsetContext):
        pass

    # Exit a parse tree produced by SQLiteParser#offset.
    def exitOffset(self, ctx: SQLiteParser.OffsetContext):
        pass

    # Enter a parse tree produced by SQLiteParser#default_value.
    def enterDefault_value(self, ctx: SQLiteParser.Default_valueContext):
        pass

    # Exit a parse tree produced by SQLiteParser#default_value.
    def exitDefault_value(self, ctx: SQLiteParser.Default_valueContext):
        pass

    # Enter a parse tree produced by SQLiteParser#partition_by.
    def enterPartition_by(self, ctx: SQLiteParser.Partition_byContext):
        pass

    # Exit a parse tree produced by SQLiteParser#partition_by.
    def exitPartition_by(self, ctx: SQLiteParser.Partition_byContext):
        pass

    # Enter a parse tree produced by SQLiteParser#order_by_expr.
    def enterOrder_by_expr(self, ctx: SQLiteParser.Order_by_exprContext):
        pass

    # Exit a parse tree produced by SQLiteParser#order_by_expr.
    def exitOrder_by_expr(self, ctx: SQLiteParser.Order_by_exprContext):
        pass

    # Enter a parse tree produced by SQLiteParser#order_by_expr_asc_desc.
    def enterOrder_by_expr_asc_desc(self, ctx: SQLiteParser.Order_by_expr_asc_descContext):
        pass

    # Exit a parse tree produced by SQLiteParser#order_by_expr_asc_desc.
    def exitOrder_by_expr_asc_desc(self, ctx: SQLiteParser.Order_by_expr_asc_descContext):
        pass

    # Enter a parse tree produced by SQLiteParser#expr_asc_desc.
    def enterExpr_asc_desc(self, ctx: SQLiteParser.Expr_asc_descContext):
        pass

    # Exit a parse tree produced by SQLiteParser#expr_asc_desc.
    def exitExpr_asc_desc(self, ctx: SQLiteParser.Expr_asc_descContext):
        pass

    # Enter a parse tree produced by SQLiteParser#initial_select.
    def enterInitial_select(self, ctx: SQLiteParser.Initial_selectContext):
        pass

    # Exit a parse tree produced by SQLiteParser#initial_select.
    def exitInitial_select(self, ctx: SQLiteParser.Initial_selectContext):
        pass

    # Enter a parse tree produced by SQLiteParser#recursive_select.
    def enterRecursive_select(self, ctx: SQLiteParser.Recursive_selectContext):
        pass

    # Exit a parse tree produced by SQLiteParser#recursive_select.
    def exitRecursive_select(self, ctx: SQLiteParser.Recursive_selectContext):
        pass

    # Enter a parse tree produced by SQLiteParser#unary_operator.
    def enterUnary_operator(self, ctx: SQLiteParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by SQLiteParser#unary_operator.
    def exitUnary_operator(self, ctx: SQLiteParser.Unary_operatorContext):
        pass

    # Enter a parse tree produced by SQLiteParser#error_message.
    def enterError_message(self, ctx: SQLiteParser.Error_messageContext):
        pass

    # Exit a parse tree produced by SQLiteParser#error_message.
    def exitError_message(self, ctx: SQLiteParser.Error_messageContext):
        pass

    # Enter a parse tree produced by SQLiteParser#module_argument.
    def enterModule_argument(self, ctx: SQLiteParser.Module_argumentContext):
        pass

    # Exit a parse tree produced by SQLiteParser#module_argument.
    def exitModule_argument(self, ctx: SQLiteParser.Module_argumentContext):
        pass

    # Enter a parse tree produced by SQLiteParser#column_alias.
    def enterColumn_alias(self, ctx: SQLiteParser.Column_aliasContext):
        pass

    # Exit a parse tree produced by SQLiteParser#column_alias.
    def exitColumn_alias(self, ctx: SQLiteParser.Column_aliasContext):
        pass

    # Enter a parse tree produced by SQLiteParser#keyword.
    def enterKeyword(self, ctx: SQLiteParser.KeywordContext):
        pass

    # Exit a parse tree produced by SQLiteParser#keyword.
    def exitKeyword(self, ctx: SQLiteParser.KeywordContext):
        pass

    # Enter a parse tree produced by SQLiteParser#name.
    def enterName(self, ctx: SQLiteParser.NameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#name.
    def exitName(self, ctx: SQLiteParser.NameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#function_name.
    def enterFunction_name(self, ctx: SQLiteParser.Function_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#function_name.
    def exitFunction_name(self, ctx: SQLiteParser.Function_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#schema_name.
    def enterSchema_name(self, ctx: SQLiteParser.Schema_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#schema_name.
    def exitSchema_name(self, ctx: SQLiteParser.Schema_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_name.
    def enterTable_name(self, ctx: SQLiteParser.Table_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_name.
    def exitTable_name(self, ctx: SQLiteParser.Table_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_or_index_name.
    def enterTable_or_index_name(self, ctx: SQLiteParser.Table_or_index_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_or_index_name.
    def exitTable_or_index_name(self, ctx: SQLiteParser.Table_or_index_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#new_table_name.
    def enterNew_table_name(self, ctx: SQLiteParser.New_table_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#new_table_name.
    def exitNew_table_name(self, ctx: SQLiteParser.New_table_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#column_name.
    def enterColumn_name(self, ctx: SQLiteParser.Column_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#column_name.
    def exitColumn_name(self, ctx: SQLiteParser.Column_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#collation_name.
    def enterCollation_name(self, ctx: SQLiteParser.Collation_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#collation_name.
    def exitCollation_name(self, ctx: SQLiteParser.Collation_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#foreign_table.
    def enterForeign_table(self, ctx: SQLiteParser.Foreign_tableContext):
        pass

    # Exit a parse tree produced by SQLiteParser#foreign_table.
    def exitForeign_table(self, ctx: SQLiteParser.Foreign_tableContext):
        pass

    # Enter a parse tree produced by SQLiteParser#index_name.
    def enterIndex_name(self, ctx: SQLiteParser.Index_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#index_name.
    def exitIndex_name(self, ctx: SQLiteParser.Index_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#trigger_name.
    def enterTrigger_name(self, ctx: SQLiteParser.Trigger_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#trigger_name.
    def exitTrigger_name(self, ctx: SQLiteParser.Trigger_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#view_name.
    def enterView_name(self, ctx: SQLiteParser.View_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#view_name.
    def exitView_name(self, ctx: SQLiteParser.View_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#module_name.
    def enterModule_name(self, ctx: SQLiteParser.Module_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#module_name.
    def exitModule_name(self, ctx: SQLiteParser.Module_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#pragma_name.
    def enterPragma_name(self, ctx: SQLiteParser.Pragma_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#pragma_name.
    def exitPragma_name(self, ctx: SQLiteParser.Pragma_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#savepoint_name.
    def enterSavepoint_name(self, ctx: SQLiteParser.Savepoint_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#savepoint_name.
    def exitSavepoint_name(self, ctx: SQLiteParser.Savepoint_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_alias.
    def enterTable_alias(self, ctx: SQLiteParser.Table_aliasContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_alias.
    def exitTable_alias(self, ctx: SQLiteParser.Table_aliasContext):
        pass

    # Enter a parse tree produced by SQLiteParser#transaction_name.
    def enterTransaction_name(self, ctx: SQLiteParser.Transaction_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#transaction_name.
    def exitTransaction_name(self, ctx: SQLiteParser.Transaction_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#window_name.
    def enterWindow_name(self, ctx: SQLiteParser.Window_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#window_name.
    def exitWindow_name(self, ctx: SQLiteParser.Window_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#alias.
    def enterAlias(self, ctx: SQLiteParser.AliasContext):
        pass

    # Exit a parse tree produced by SQLiteParser#alias.
    def exitAlias(self, ctx: SQLiteParser.AliasContext):
        pass

    # Enter a parse tree produced by SQLiteParser#filename.
    def enterFilename(self, ctx: SQLiteParser.FilenameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#filename.
    def exitFilename(self, ctx: SQLiteParser.FilenameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#base_window_name.
    def enterBase_window_name(self, ctx: SQLiteParser.Base_window_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#base_window_name.
    def exitBase_window_name(self, ctx: SQLiteParser.Base_window_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#simple_func.
    def enterSimple_func(self, ctx: SQLiteParser.Simple_funcContext):
        pass

    # Exit a parse tree produced by SQLiteParser#simple_func.
    def exitSimple_func(self, ctx: SQLiteParser.Simple_funcContext):
        pass

    # Enter a parse tree produced by SQLiteParser#aggregate_func.
    def enterAggregate_func(self, ctx: SQLiteParser.Aggregate_funcContext):
        pass

    # Exit a parse tree produced by SQLiteParser#aggregate_func.
    def exitAggregate_func(self, ctx: SQLiteParser.Aggregate_funcContext):
        pass

    # Enter a parse tree produced by SQLiteParser#table_function_name.
    def enterTable_function_name(self, ctx: SQLiteParser.Table_function_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#table_function_name.
    def exitTable_function_name(self, ctx: SQLiteParser.Table_function_nameContext):
        pass

    # Enter a parse tree produced by SQLiteParser#any_name.
    def enterAny_name(self, ctx: SQLiteParser.Any_nameContext):
        pass

    # Exit a parse tree produced by SQLiteParser#any_name.
    def exitAny_name(self, ctx: SQLiteParser.Any_nameContext):
        pass


del SQLiteParser
