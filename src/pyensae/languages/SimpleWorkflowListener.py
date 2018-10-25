# Generated from \SimpleWorkflow.g4 by ANTLR 4.7.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SimpleWorkflowParser import SimpleWorkflowParser
else:
    from SimpleWorkflowParser import SimpleWorkflowParser

# This class defines a complete listener for a parse tree produced by SimpleWorkflowParser.


class SimpleWorkflowListener(ParseTreeListener):

    # Enter a parse tree produced by SimpleWorkflowParser#parse.
    def enterParse(self, ctx: SimpleWorkflowParser.ParseContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#parse.
    def exitParse(self, ctx: SimpleWorkflowParser.ParseContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#final_stmt.
    def enterFinal_stmt(self, ctx: SimpleWorkflowParser.Final_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#final_stmt.
    def exitFinal_stmt(self, ctx: SimpleWorkflowParser.Final_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#affectation_stmt_comma.
    def enterAffectation_stmt_comma(self, ctx: SimpleWorkflowParser.Affectation_stmt_commaContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#affectation_stmt_comma.
    def exitAffectation_stmt_comma(self, ctx: SimpleWorkflowParser.Affectation_stmt_commaContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#affectation_stmt.
    def enterAffectation_stmt(self, ctx: SimpleWorkflowParser.Affectation_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#affectation_stmt.
    def exitAffectation_stmt(self, ctx: SimpleWorkflowParser.Affectation_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#for_stmt.
    def enterFor_stmt(self, ctx: SimpleWorkflowParser.For_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#for_stmt.
    def exitFor_stmt(self, ctx: SimpleWorkflowParser.For_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#if_stmt.
    def enterIf_stmt(self, ctx: SimpleWorkflowParser.If_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#if_stmt.
    def exitIf_stmt(self, ctx: SimpleWorkflowParser.If_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#evaluation_function.
    def enterEvaluation_function(self, ctx: SimpleWorkflowParser.Evaluation_functionContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#evaluation_function.
    def exitEvaluation_function(self, ctx: SimpleWorkflowParser.Evaluation_functionContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#expression.
    def enterExpression(self, ctx: SimpleWorkflowParser.ExpressionContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#expression.
    def exitExpression(self, ctx: SimpleWorkflowParser.ExpressionContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#expression_no_binary.
    def enterExpression_no_binary(self, ctx: SimpleWorkflowParser.Expression_no_binaryContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#expression_no_binary.
    def exitExpression_no_binary(self, ctx: SimpleWorkflowParser.Expression_no_binaryContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#function_call.
    def enterFunction_call(self, ctx: SimpleWorkflowParser.Function_callContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#function_call.
    def exitFunction_call(self, ctx: SimpleWorkflowParser.Function_callContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#variable_name.
    def enterVariable_name(self, ctx: SimpleWorkflowParser.Variable_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#variable_name.
    def exitVariable_name(self, ctx: SimpleWorkflowParser.Variable_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#binary_operator.
    def enterBinary_operator(self, ctx: SimpleWorkflowParser.Binary_operatorContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#binary_operator.
    def exitBinary_operator(self, ctx: SimpleWorkflowParser.Binary_operatorContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#unary_operator.
    def enterUnary_operator(self, ctx: SimpleWorkflowParser.Unary_operatorContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#unary_operator.
    def exitUnary_operator(self, ctx: SimpleWorkflowParser.Unary_operatorContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#stmt_comma.
    def enterStmt_comma(self, ctx: SimpleWorkflowParser.Stmt_commaContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#stmt_comma.
    def exitStmt_comma(self, ctx: SimpleWorkflowParser.Stmt_commaContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#stmt.
    def enterStmt(self, ctx: SimpleWorkflowParser.StmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#stmt.
    def exitStmt(self, ctx: SimpleWorkflowParser.StmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#connect_stmt.
    def enterConnect_stmt(self, ctx: SimpleWorkflowParser.Connect_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#connect_stmt.
    def exitConnect_stmt(self, ctx: SimpleWorkflowParser.Connect_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#data_or_module_output.
    def enterData_or_module_output(self, ctx: SimpleWorkflowParser.Data_or_module_outputContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#data_or_module_output.
    def exitData_or_module_output(self, ctx: SimpleWorkflowParser.Data_or_module_outputContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#module_input.
    def enterModule_input(self, ctx: SimpleWorkflowParser.Module_inputContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#module_input.
    def exitModule_input(self, ctx: SimpleWorkflowParser.Module_inputContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#data_stmt.
    def enterData_stmt(self, ctx: SimpleWorkflowParser.Data_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#data_stmt.
    def exitData_stmt(self, ctx: SimpleWorkflowParser.Data_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#module_stmt.
    def enterModule_stmt(self, ctx: SimpleWorkflowParser.Module_stmtContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#module_stmt.
    def exitModule_stmt(self, ctx: SimpleWorkflowParser.Module_stmtContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#module_call.
    def enterModule_call(self, ctx: SimpleWorkflowParser.Module_callContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#module_call.
    def exitModule_call(self, ctx: SimpleWorkflowParser.Module_callContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#element_name.
    def enterElement_name(self, ctx: SimpleWorkflowParser.Element_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#element_name.
    def exitElement_name(self, ctx: SimpleWorkflowParser.Element_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#list_param_affectation.
    def enterList_param_affectation(self, ctx: SimpleWorkflowParser.List_param_affectationContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#list_param_affectation.
    def exitList_param_affectation(self, ctx: SimpleWorkflowParser.List_param_affectationContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#param_affectation.
    def enterParam_affectation(self, ctx: SimpleWorkflowParser.Param_affectationContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#param_affectation.
    def exitParam_affectation(self, ctx: SimpleWorkflowParser.Param_affectationContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#param_name.
    def enterParam_name(self, ctx: SimpleWorkflowParser.Param_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#param_name.
    def exitParam_name(self, ctx: SimpleWorkflowParser.Param_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#inout_name.
    def enterInout_name(self, ctx: SimpleWorkflowParser.Inout_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#inout_name.
    def exitInout_name(self, ctx: SimpleWorkflowParser.Inout_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#module_name.
    def enterModule_name(self, ctx: SimpleWorkflowParser.Module_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#module_name.
    def exitModule_name(self, ctx: SimpleWorkflowParser.Module_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#data_name.
    def enterData_name(self, ctx: SimpleWorkflowParser.Data_nameContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#data_name.
    def exitData_name(self, ctx: SimpleWorkflowParser.Data_nameContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#constant.
    def enterConstant(self, ctx: SimpleWorkflowParser.ConstantContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#constant.
    def exitConstant(self, ctx: SimpleWorkflowParser.ConstantContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#string_literal.
    def enterString_literal(self, ctx: SimpleWorkflowParser.String_literalContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#string_literal.
    def exitString_literal(self, ctx: SimpleWorkflowParser.String_literalContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#integer_number.
    def enterInteger_number(self, ctx: SimpleWorkflowParser.Integer_numberContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#integer_number.
    def exitInteger_number(self, ctx: SimpleWorkflowParser.Integer_numberContext):
        pass

    # Enter a parse tree produced by SimpleWorkflowParser#real_number.
    def enterReal_number(self, ctx: SimpleWorkflowParser.Real_numberContext):
        pass

    # Exit a parse tree produced by SimpleWorkflowParser#real_number.
    def exitReal_number(self, ctx: SimpleWorkflowParser.Real_numberContext):
        pass
