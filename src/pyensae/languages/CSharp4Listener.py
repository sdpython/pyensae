# Generated from C:\xadupre\__home_\GitHub\pyensae\src\pyensae\languages\CSharp4.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CSharp4Parser import CSharp4Parser
else:
    from CSharp4Parser import CSharp4Parser

# This class defines a complete listener for a parse tree produced by CSharp4Parser.
class CSharp4Listener(ParseTreeListener):

    # Enter a parse tree produced by CSharp4Parser#namespace_name.
    def enterNamespace_name(self, ctx:CSharp4Parser.Namespace_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_name.
    def exitNamespace_name(self, ctx:CSharp4Parser.Namespace_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_name.
    def enterType_name(self, ctx:CSharp4Parser.Type_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_name.
    def exitType_name(self, ctx:CSharp4Parser.Type_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#identifier.
    def enterIdentifier(self, ctx:CSharp4Parser.IdentifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#identifier.
    def exitIdentifier(self, ctx:CSharp4Parser.IdentifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#namespace_or_type_name.
    def enterNamespace_or_type_name(self, ctx:CSharp4Parser.Namespace_or_type_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_or_type_name.
    def exitNamespace_or_type_name(self, ctx:CSharp4Parser.Namespace_or_type_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_argument_list_opt.
    def enterType_argument_list_opt(self, ctx:CSharp4Parser.Type_argument_list_optContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_argument_list_opt.
    def exitType_argument_list_opt(self, ctx:CSharp4Parser.Type_argument_list_optContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#any_type.
    def enterAny_type(self, ctx:CSharp4Parser.Any_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#any_type.
    def exitAny_type(self, ctx:CSharp4Parser.Any_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#base_type.
    def enterBase_type(self, ctx:CSharp4Parser.Base_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#base_type.
    def exitBase_type(self, ctx:CSharp4Parser.Base_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#simple_type.
    def enterSimple_type(self, ctx:CSharp4Parser.Simple_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#simple_type.
    def exitSimple_type(self, ctx:CSharp4Parser.Simple_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#numeric_type.
    def enterNumeric_type(self, ctx:CSharp4Parser.Numeric_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#numeric_type.
    def exitNumeric_type(self, ctx:CSharp4Parser.Numeric_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#integral_type.
    def enterIntegral_type(self, ctx:CSharp4Parser.Integral_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#integral_type.
    def exitIntegral_type(self, ctx:CSharp4Parser.Integral_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#floating_point_type.
    def enterFloating_point_type(self, ctx:CSharp4Parser.Floating_point_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#floating_point_type.
    def exitFloating_point_type(self, ctx:CSharp4Parser.Floating_point_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#nullable_type.
    def enterNullable_type(self, ctx:CSharp4Parser.Nullable_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#nullable_type.
    def exitNullable_type(self, ctx:CSharp4Parser.Nullable_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#non_nullable_value_type.
    def enterNon_nullable_value_type(self, ctx:CSharp4Parser.Non_nullable_value_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#non_nullable_value_type.
    def exitNon_nullable_value_type(self, ctx:CSharp4Parser.Non_nullable_value_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#reference_type.
    def enterReference_type(self, ctx:CSharp4Parser.Reference_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#reference_type.
    def exitReference_type(self, ctx:CSharp4Parser.Reference_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_type.
    def enterClass_type(self, ctx:CSharp4Parser.Class_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_type.
    def exitClass_type(self, ctx:CSharp4Parser.Class_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_type.
    def enterInterface_type(self, ctx:CSharp4Parser.Interface_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_type.
    def exitInterface_type(self, ctx:CSharp4Parser.Interface_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_type.
    def enterDelegate_type(self, ctx:CSharp4Parser.Delegate_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_type.
    def exitDelegate_type(self, ctx:CSharp4Parser.Delegate_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_argument_list.
    def enterType_argument_list(self, ctx:CSharp4Parser.Type_argument_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_argument_list.
    def exitType_argument_list(self, ctx:CSharp4Parser.Type_argument_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_arguments.
    def enterType_arguments(self, ctx:CSharp4Parser.Type_argumentsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_arguments.
    def exitType_arguments(self, ctx:CSharp4Parser.Type_argumentsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_argument.
    def enterType_argument(self, ctx:CSharp4Parser.Type_argumentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_argument.
    def exitType_argument(self, ctx:CSharp4Parser.Type_argumentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_void.
    def enterType_void(self, ctx:CSharp4Parser.Type_voidContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_void.
    def exitType_void(self, ctx:CSharp4Parser.Type_voidContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variable_reference.
    def enterVariable_reference(self, ctx:CSharp4Parser.Variable_referenceContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variable_reference.
    def exitVariable_reference(self, ctx:CSharp4Parser.Variable_referenceContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#argument_list.
    def enterArgument_list(self, ctx:CSharp4Parser.Argument_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#argument_list.
    def exitArgument_list(self, ctx:CSharp4Parser.Argument_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#argument.
    def enterArgument(self, ctx:CSharp4Parser.ArgumentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#argument.
    def exitArgument(self, ctx:CSharp4Parser.ArgumentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#argument_name.
    def enterArgument_name(self, ctx:CSharp4Parser.Argument_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#argument_name.
    def exitArgument_name(self, ctx:CSharp4Parser.Argument_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#argument_value.
    def enterArgument_value(self, ctx:CSharp4Parser.Argument_valueContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#argument_value.
    def exitArgument_value(self, ctx:CSharp4Parser.Argument_valueContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#primary_expression.
    def enterPrimary_expression(self, ctx:CSharp4Parser.Primary_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#primary_expression.
    def exitPrimary_expression(self, ctx:CSharp4Parser.Primary_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#primary_expression_start.
    def enterPrimary_expression_start(self, ctx:CSharp4Parser.Primary_expression_startContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#primary_expression_start.
    def exitPrimary_expression_start(self, ctx:CSharp4Parser.Primary_expression_startContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#bracket_expression.
    def enterBracket_expression(self, ctx:CSharp4Parser.Bracket_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#bracket_expression.
    def exitBracket_expression(self, ctx:CSharp4Parser.Bracket_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#simple_name.
    def enterSimple_name(self, ctx:CSharp4Parser.Simple_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#simple_name.
    def exitSimple_name(self, ctx:CSharp4Parser.Simple_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#parenthesized_expression.
    def enterParenthesized_expression(self, ctx:CSharp4Parser.Parenthesized_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#parenthesized_expression.
    def exitParenthesized_expression(self, ctx:CSharp4Parser.Parenthesized_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_access.
    def enterMember_access(self, ctx:CSharp4Parser.Member_accessContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_access.
    def exitMember_access(self, ctx:CSharp4Parser.Member_accessContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#predefined_type.
    def enterPredefined_type(self, ctx:CSharp4Parser.Predefined_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#predefined_type.
    def exitPredefined_type(self, ctx:CSharp4Parser.Predefined_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#expression_list.
    def enterExpression_list(self, ctx:CSharp4Parser.Expression_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#expression_list.
    def exitExpression_list(self, ctx:CSharp4Parser.Expression_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#this_access.
    def enterThis_access(self, ctx:CSharp4Parser.This_accessContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#this_access.
    def exitThis_access(self, ctx:CSharp4Parser.This_accessContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#base_access.
    def enterBase_access(self, ctx:CSharp4Parser.Base_accessContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#base_access.
    def exitBase_access(self, ctx:CSharp4Parser.Base_accessContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#object_creation_expression.
    def enterObject_creation_expression(self, ctx:CSharp4Parser.Object_creation_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#object_creation_expression.
    def exitObject_creation_expression(self, ctx:CSharp4Parser.Object_creation_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#object_or_collection_initializer.
    def enterObject_or_collection_initializer(self, ctx:CSharp4Parser.Object_or_collection_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#object_or_collection_initializer.
    def exitObject_or_collection_initializer(self, ctx:CSharp4Parser.Object_or_collection_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#object_initializer.
    def enterObject_initializer(self, ctx:CSharp4Parser.Object_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#object_initializer.
    def exitObject_initializer(self, ctx:CSharp4Parser.Object_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_initializer_list.
    def enterMember_initializer_list(self, ctx:CSharp4Parser.Member_initializer_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_initializer_list.
    def exitMember_initializer_list(self, ctx:CSharp4Parser.Member_initializer_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_initializer.
    def enterMember_initializer(self, ctx:CSharp4Parser.Member_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_initializer.
    def exitMember_initializer(self, ctx:CSharp4Parser.Member_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#initializer_value.
    def enterInitializer_value(self, ctx:CSharp4Parser.Initializer_valueContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#initializer_value.
    def exitInitializer_value(self, ctx:CSharp4Parser.Initializer_valueContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#collection_initializer.
    def enterCollection_initializer(self, ctx:CSharp4Parser.Collection_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#collection_initializer.
    def exitCollection_initializer(self, ctx:CSharp4Parser.Collection_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#element_initializer_list.
    def enterElement_initializer_list(self, ctx:CSharp4Parser.Element_initializer_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#element_initializer_list.
    def exitElement_initializer_list(self, ctx:CSharp4Parser.Element_initializer_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#element_initializer.
    def enterElement_initializer(self, ctx:CSharp4Parser.Element_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#element_initializer.
    def exitElement_initializer(self, ctx:CSharp4Parser.Element_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#array_creation_expression.
    def enterArray_creation_expression(self, ctx:CSharp4Parser.Array_creation_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#array_creation_expression.
    def exitArray_creation_expression(self, ctx:CSharp4Parser.Array_creation_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_creation_expression.
    def enterDelegate_creation_expression(self, ctx:CSharp4Parser.Delegate_creation_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_creation_expression.
    def exitDelegate_creation_expression(self, ctx:CSharp4Parser.Delegate_creation_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_object_creation_expression.
    def enterAnonymous_object_creation_expression(self, ctx:CSharp4Parser.Anonymous_object_creation_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_object_creation_expression.
    def exitAnonymous_object_creation_expression(self, ctx:CSharp4Parser.Anonymous_object_creation_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_object_initializer.
    def enterAnonymous_object_initializer(self, ctx:CSharp4Parser.Anonymous_object_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_object_initializer.
    def exitAnonymous_object_initializer(self, ctx:CSharp4Parser.Anonymous_object_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_declarator_list.
    def enterMember_declarator_list(self, ctx:CSharp4Parser.Member_declarator_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_declarator_list.
    def exitMember_declarator_list(self, ctx:CSharp4Parser.Member_declarator_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_declarator.
    def enterMember_declarator(self, ctx:CSharp4Parser.Member_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_declarator.
    def exitMember_declarator(self, ctx:CSharp4Parser.Member_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#typeof_expression.
    def enterTypeof_expression(self, ctx:CSharp4Parser.Typeof_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#typeof_expression.
    def exitTypeof_expression(self, ctx:CSharp4Parser.Typeof_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unbound_type_name.
    def enterUnbound_type_name(self, ctx:CSharp4Parser.Unbound_type_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unbound_type_name.
    def exitUnbound_type_name(self, ctx:CSharp4Parser.Unbound_type_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#generic_dimension_specifier.
    def enterGeneric_dimension_specifier(self, ctx:CSharp4Parser.Generic_dimension_specifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#generic_dimension_specifier.
    def exitGeneric_dimension_specifier(self, ctx:CSharp4Parser.Generic_dimension_specifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#commas.
    def enterCommas(self, ctx:CSharp4Parser.CommasContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#commas.
    def exitCommas(self, ctx:CSharp4Parser.CommasContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#checked_expression.
    def enterChecked_expression(self, ctx:CSharp4Parser.Checked_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#checked_expression.
    def exitChecked_expression(self, ctx:CSharp4Parser.Checked_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unchecked_expression.
    def enterUnchecked_expression(self, ctx:CSharp4Parser.Unchecked_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unchecked_expression.
    def exitUnchecked_expression(self, ctx:CSharp4Parser.Unchecked_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#default_value_expression.
    def enterDefault_value_expression(self, ctx:CSharp4Parser.Default_value_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#default_value_expression.
    def exitDefault_value_expression(self, ctx:CSharp4Parser.Default_value_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unary_expression.
    def enterUnary_expression(self, ctx:CSharp4Parser.Unary_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unary_expression.
    def exitUnary_expression(self, ctx:CSharp4Parser.Unary_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#scan_for_cast_generic_precedence.
    def enterScan_for_cast_generic_precedence(self, ctx:CSharp4Parser.Scan_for_cast_generic_precedenceContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#scan_for_cast_generic_precedence.
    def exitScan_for_cast_generic_precedence(self, ctx:CSharp4Parser.Scan_for_cast_generic_precedenceContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#cast_disambiguation_token.
    def enterCast_disambiguation_token(self, ctx:CSharp4Parser.Cast_disambiguation_tokenContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#cast_disambiguation_token.
    def exitCast_disambiguation_token(self, ctx:CSharp4Parser.Cast_disambiguation_tokenContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#pre_increment_expression.
    def enterPre_increment_expression(self, ctx:CSharp4Parser.Pre_increment_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#pre_increment_expression.
    def exitPre_increment_expression(self, ctx:CSharp4Parser.Pre_increment_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#pre_decrement_expression.
    def enterPre_decrement_expression(self, ctx:CSharp4Parser.Pre_decrement_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#pre_decrement_expression.
    def exitPre_decrement_expression(self, ctx:CSharp4Parser.Pre_decrement_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#cast_expression.
    def enterCast_expression(self, ctx:CSharp4Parser.Cast_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#cast_expression.
    def exitCast_expression(self, ctx:CSharp4Parser.Cast_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#multiplicative_expression.
    def enterMultiplicative_expression(self, ctx:CSharp4Parser.Multiplicative_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#multiplicative_expression.
    def exitMultiplicative_expression(self, ctx:CSharp4Parser.Multiplicative_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#additive_expression.
    def enterAdditive_expression(self, ctx:CSharp4Parser.Additive_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#additive_expression.
    def exitAdditive_expression(self, ctx:CSharp4Parser.Additive_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#shift_expression.
    def enterShift_expression(self, ctx:CSharp4Parser.Shift_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#shift_expression.
    def exitShift_expression(self, ctx:CSharp4Parser.Shift_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#relational_expression.
    def enterRelational_expression(self, ctx:CSharp4Parser.Relational_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#relational_expression.
    def exitRelational_expression(self, ctx:CSharp4Parser.Relational_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#scan_for_shift_generic_precedence.
    def enterScan_for_shift_generic_precedence(self, ctx:CSharp4Parser.Scan_for_shift_generic_precedenceContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#scan_for_shift_generic_precedence.
    def exitScan_for_shift_generic_precedence(self, ctx:CSharp4Parser.Scan_for_shift_generic_precedenceContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#shift_disambiguation_token.
    def enterShift_disambiguation_token(self, ctx:CSharp4Parser.Shift_disambiguation_tokenContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#shift_disambiguation_token.
    def exitShift_disambiguation_token(self, ctx:CSharp4Parser.Shift_disambiguation_tokenContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#isType.
    def enterIsType(self, ctx:CSharp4Parser.IsTypeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#isType.
    def exitIsType(self, ctx:CSharp4Parser.IsTypeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#is_disambiguation_token.
    def enterIs_disambiguation_token(self, ctx:CSharp4Parser.Is_disambiguation_tokenContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#is_disambiguation_token.
    def exitIs_disambiguation_token(self, ctx:CSharp4Parser.Is_disambiguation_tokenContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#equality_expression.
    def enterEquality_expression(self, ctx:CSharp4Parser.Equality_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#equality_expression.
    def exitEquality_expression(self, ctx:CSharp4Parser.Equality_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#and_expression.
    def enterAnd_expression(self, ctx:CSharp4Parser.And_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#and_expression.
    def exitAnd_expression(self, ctx:CSharp4Parser.And_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#exclusive_or_expression.
    def enterExclusive_or_expression(self, ctx:CSharp4Parser.Exclusive_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#exclusive_or_expression.
    def exitExclusive_or_expression(self, ctx:CSharp4Parser.Exclusive_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#inclusive_or_expression.
    def enterInclusive_or_expression(self, ctx:CSharp4Parser.Inclusive_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#inclusive_or_expression.
    def exitInclusive_or_expression(self, ctx:CSharp4Parser.Inclusive_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#conditional_and_expression.
    def enterConditional_and_expression(self, ctx:CSharp4Parser.Conditional_and_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#conditional_and_expression.
    def exitConditional_and_expression(self, ctx:CSharp4Parser.Conditional_and_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#conditional_or_expression.
    def enterConditional_or_expression(self, ctx:CSharp4Parser.Conditional_or_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#conditional_or_expression.
    def exitConditional_or_expression(self, ctx:CSharp4Parser.Conditional_or_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#null_coalescing_expression.
    def enterNull_coalescing_expression(self, ctx:CSharp4Parser.Null_coalescing_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#null_coalescing_expression.
    def exitNull_coalescing_expression(self, ctx:CSharp4Parser.Null_coalescing_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#conditional_expression.
    def enterConditional_expression(self, ctx:CSharp4Parser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#conditional_expression.
    def exitConditional_expression(self, ctx:CSharp4Parser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#lambda_expression.
    def enterLambda_expression(self, ctx:CSharp4Parser.Lambda_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#lambda_expression.
    def exitLambda_expression(self, ctx:CSharp4Parser.Lambda_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_method_expression.
    def enterAnonymous_method_expression(self, ctx:CSharp4Parser.Anonymous_method_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_method_expression.
    def exitAnonymous_method_expression(self, ctx:CSharp4Parser.Anonymous_method_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_function_signature.
    def enterAnonymous_function_signature(self, ctx:CSharp4Parser.Anonymous_function_signatureContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_function_signature.
    def exitAnonymous_function_signature(self, ctx:CSharp4Parser.Anonymous_function_signatureContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#explicit_anonymous_function_signature.
    def enterExplicit_anonymous_function_signature(self, ctx:CSharp4Parser.Explicit_anonymous_function_signatureContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#explicit_anonymous_function_signature.
    def exitExplicit_anonymous_function_signature(self, ctx:CSharp4Parser.Explicit_anonymous_function_signatureContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#explicit_anonymous_function_parameter_list.
    def enterExplicit_anonymous_function_parameter_list(self, ctx:CSharp4Parser.Explicit_anonymous_function_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#explicit_anonymous_function_parameter_list.
    def exitExplicit_anonymous_function_parameter_list(self, ctx:CSharp4Parser.Explicit_anonymous_function_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#explicit_anonymous_function_parameter.
    def enterExplicit_anonymous_function_parameter(self, ctx:CSharp4Parser.Explicit_anonymous_function_parameterContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#explicit_anonymous_function_parameter.
    def exitExplicit_anonymous_function_parameter(self, ctx:CSharp4Parser.Explicit_anonymous_function_parameterContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_function_parameter_modifier.
    def enterAnonymous_function_parameter_modifier(self, ctx:CSharp4Parser.Anonymous_function_parameter_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_function_parameter_modifier.
    def exitAnonymous_function_parameter_modifier(self, ctx:CSharp4Parser.Anonymous_function_parameter_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#implicit_anonymous_function_signature.
    def enterImplicit_anonymous_function_signature(self, ctx:CSharp4Parser.Implicit_anonymous_function_signatureContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#implicit_anonymous_function_signature.
    def exitImplicit_anonymous_function_signature(self, ctx:CSharp4Parser.Implicit_anonymous_function_signatureContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#implicit_anonymous_function_parameter_list.
    def enterImplicit_anonymous_function_parameter_list(self, ctx:CSharp4Parser.Implicit_anonymous_function_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#implicit_anonymous_function_parameter_list.
    def exitImplicit_anonymous_function_parameter_list(self, ctx:CSharp4Parser.Implicit_anonymous_function_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#implicit_anonymous_function_parameter.
    def enterImplicit_anonymous_function_parameter(self, ctx:CSharp4Parser.Implicit_anonymous_function_parameterContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#implicit_anonymous_function_parameter.
    def exitImplicit_anonymous_function_parameter(self, ctx:CSharp4Parser.Implicit_anonymous_function_parameterContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#anonymous_function_body.
    def enterAnonymous_function_body(self, ctx:CSharp4Parser.Anonymous_function_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#anonymous_function_body.
    def exitAnonymous_function_body(self, ctx:CSharp4Parser.Anonymous_function_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#query_expression.
    def enterQuery_expression(self, ctx:CSharp4Parser.Query_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#query_expression.
    def exitQuery_expression(self, ctx:CSharp4Parser.Query_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#from_clause.
    def enterFrom_clause(self, ctx:CSharp4Parser.From_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#from_clause.
    def exitFrom_clause(self, ctx:CSharp4Parser.From_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#query_body.
    def enterQuery_body(self, ctx:CSharp4Parser.Query_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#query_body.
    def exitQuery_body(self, ctx:CSharp4Parser.Query_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#query_body_clauses.
    def enterQuery_body_clauses(self, ctx:CSharp4Parser.Query_body_clausesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#query_body_clauses.
    def exitQuery_body_clauses(self, ctx:CSharp4Parser.Query_body_clausesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#query_body_clause.
    def enterQuery_body_clause(self, ctx:CSharp4Parser.Query_body_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#query_body_clause.
    def exitQuery_body_clause(self, ctx:CSharp4Parser.Query_body_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#let_clause.
    def enterLet_clause(self, ctx:CSharp4Parser.Let_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#let_clause.
    def exitLet_clause(self, ctx:CSharp4Parser.Let_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#where_clause.
    def enterWhere_clause(self, ctx:CSharp4Parser.Where_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#where_clause.
    def exitWhere_clause(self, ctx:CSharp4Parser.Where_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#join_clause.
    def enterJoin_clause(self, ctx:CSharp4Parser.Join_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#join_clause.
    def exitJoin_clause(self, ctx:CSharp4Parser.Join_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#join_into_clause.
    def enterJoin_into_clause(self, ctx:CSharp4Parser.Join_into_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#join_into_clause.
    def exitJoin_into_clause(self, ctx:CSharp4Parser.Join_into_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#combined_join_clause.
    def enterCombined_join_clause(self, ctx:CSharp4Parser.Combined_join_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#combined_join_clause.
    def exitCombined_join_clause(self, ctx:CSharp4Parser.Combined_join_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#orderby_clause.
    def enterOrderby_clause(self, ctx:CSharp4Parser.Orderby_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#orderby_clause.
    def exitOrderby_clause(self, ctx:CSharp4Parser.Orderby_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#orderings.
    def enterOrderings(self, ctx:CSharp4Parser.OrderingsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#orderings.
    def exitOrderings(self, ctx:CSharp4Parser.OrderingsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#ordering.
    def enterOrdering(self, ctx:CSharp4Parser.OrderingContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#ordering.
    def exitOrdering(self, ctx:CSharp4Parser.OrderingContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#ordering_direction.
    def enterOrdering_direction(self, ctx:CSharp4Parser.Ordering_directionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#ordering_direction.
    def exitOrdering_direction(self, ctx:CSharp4Parser.Ordering_directionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#select_or_group_clause.
    def enterSelect_or_group_clause(self, ctx:CSharp4Parser.Select_or_group_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#select_or_group_clause.
    def exitSelect_or_group_clause(self, ctx:CSharp4Parser.Select_or_group_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#select_clause.
    def enterSelect_clause(self, ctx:CSharp4Parser.Select_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#select_clause.
    def exitSelect_clause(self, ctx:CSharp4Parser.Select_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#group_clause.
    def enterGroup_clause(self, ctx:CSharp4Parser.Group_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#group_clause.
    def exitGroup_clause(self, ctx:CSharp4Parser.Group_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#query_continuation.
    def enterQuery_continuation(self, ctx:CSharp4Parser.Query_continuationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#query_continuation.
    def exitQuery_continuation(self, ctx:CSharp4Parser.Query_continuationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#assignment.
    def enterAssignment(self, ctx:CSharp4Parser.AssignmentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#assignment.
    def exitAssignment(self, ctx:CSharp4Parser.AssignmentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#assignment_operator.
    def enterAssignment_operator(self, ctx:CSharp4Parser.Assignment_operatorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#assignment_operator.
    def exitAssignment_operator(self, ctx:CSharp4Parser.Assignment_operatorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#expression.
    def enterExpression(self, ctx:CSharp4Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#expression.
    def exitExpression(self, ctx:CSharp4Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#non_assignment_expression.
    def enterNon_assignment_expression(self, ctx:CSharp4Parser.Non_assignment_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#non_assignment_expression.
    def exitNon_assignment_expression(self, ctx:CSharp4Parser.Non_assignment_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constant_expression.
    def enterConstant_expression(self, ctx:CSharp4Parser.Constant_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constant_expression.
    def exitConstant_expression(self, ctx:CSharp4Parser.Constant_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#boolean_expression.
    def enterBoolean_expression(self, ctx:CSharp4Parser.Boolean_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#boolean_expression.
    def exitBoolean_expression(self, ctx:CSharp4Parser.Boolean_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#statement.
    def enterStatement(self, ctx:CSharp4Parser.StatementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#statement.
    def exitStatement(self, ctx:CSharp4Parser.StatementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#embedded_statement.
    def enterEmbedded_statement(self, ctx:CSharp4Parser.Embedded_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#embedded_statement.
    def exitEmbedded_statement(self, ctx:CSharp4Parser.Embedded_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#simple_embedded_statement.
    def enterSimple_embedded_statement(self, ctx:CSharp4Parser.Simple_embedded_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#simple_embedded_statement.
    def exitSimple_embedded_statement(self, ctx:CSharp4Parser.Simple_embedded_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#block.
    def enterBlock(self, ctx:CSharp4Parser.BlockContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#block.
    def exitBlock(self, ctx:CSharp4Parser.BlockContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#statement_list.
    def enterStatement_list(self, ctx:CSharp4Parser.Statement_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#statement_list.
    def exitStatement_list(self, ctx:CSharp4Parser.Statement_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#empty_statement.
    def enterEmpty_statement(self, ctx:CSharp4Parser.Empty_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#empty_statement.
    def exitEmpty_statement(self, ctx:CSharp4Parser.Empty_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#labeled_statement.
    def enterLabeled_statement(self, ctx:CSharp4Parser.Labeled_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#labeled_statement.
    def exitLabeled_statement(self, ctx:CSharp4Parser.Labeled_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#declaration_statement.
    def enterDeclaration_statement(self, ctx:CSharp4Parser.Declaration_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#declaration_statement.
    def exitDeclaration_statement(self, ctx:CSharp4Parser.Declaration_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_declaration.
    def enterLocal_variable_declaration(self, ctx:CSharp4Parser.Local_variable_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_declaration.
    def exitLocal_variable_declaration(self, ctx:CSharp4Parser.Local_variable_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_type.
    def enterLocal_variable_type(self, ctx:CSharp4Parser.Local_variable_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_type.
    def exitLocal_variable_type(self, ctx:CSharp4Parser.Local_variable_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_declarators.
    def enterLocal_variable_declarators(self, ctx:CSharp4Parser.Local_variable_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_declarators.
    def exitLocal_variable_declarators(self, ctx:CSharp4Parser.Local_variable_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_declarator.
    def enterLocal_variable_declarator(self, ctx:CSharp4Parser.Local_variable_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_declarator.
    def exitLocal_variable_declarator(self, ctx:CSharp4Parser.Local_variable_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_initializer.
    def enterLocal_variable_initializer(self, ctx:CSharp4Parser.Local_variable_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_initializer.
    def exitLocal_variable_initializer(self, ctx:CSharp4Parser.Local_variable_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_constant_declaration.
    def enterLocal_constant_declaration(self, ctx:CSharp4Parser.Local_constant_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_constant_declaration.
    def exitLocal_constant_declaration(self, ctx:CSharp4Parser.Local_constant_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#expression_statement.
    def enterExpression_statement(self, ctx:CSharp4Parser.Expression_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#expression_statement.
    def exitExpression_statement(self, ctx:CSharp4Parser.Expression_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#statement_expression.
    def enterStatement_expression(self, ctx:CSharp4Parser.Statement_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#statement_expression.
    def exitStatement_expression(self, ctx:CSharp4Parser.Statement_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#selection_statement.
    def enterSelection_statement(self, ctx:CSharp4Parser.Selection_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#selection_statement.
    def exitSelection_statement(self, ctx:CSharp4Parser.Selection_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#ifBodyBlock.
    def enterIfBodyBlock(self, ctx:CSharp4Parser.IfBodyBlockContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#ifBodyBlock.
    def exitIfBodyBlock(self, ctx:CSharp4Parser.IfBodyBlockContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#ifBodySingle.
    def enterIfBodySingle(self, ctx:CSharp4Parser.IfBodySingleContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#ifBodySingle.
    def exitIfBodySingle(self, ctx:CSharp4Parser.IfBodySingleContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#if_statement.
    def enterIf_statement(self, ctx:CSharp4Parser.If_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#if_statement.
    def exitIf_statement(self, ctx:CSharp4Parser.If_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_statement.
    def enterSwitch_statement(self, ctx:CSharp4Parser.Switch_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_statement.
    def exitSwitch_statement(self, ctx:CSharp4Parser.Switch_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_block.
    def enterSwitch_block(self, ctx:CSharp4Parser.Switch_blockContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_block.
    def exitSwitch_block(self, ctx:CSharp4Parser.Switch_blockContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_sections.
    def enterSwitch_sections(self, ctx:CSharp4Parser.Switch_sectionsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_sections.
    def exitSwitch_sections(self, ctx:CSharp4Parser.Switch_sectionsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_section.
    def enterSwitch_section(self, ctx:CSharp4Parser.Switch_sectionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_section.
    def exitSwitch_section(self, ctx:CSharp4Parser.Switch_sectionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_labels.
    def enterSwitch_labels(self, ctx:CSharp4Parser.Switch_labelsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_labels.
    def exitSwitch_labels(self, ctx:CSharp4Parser.Switch_labelsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#switch_label.
    def enterSwitch_label(self, ctx:CSharp4Parser.Switch_labelContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#switch_label.
    def exitSwitch_label(self, ctx:CSharp4Parser.Switch_labelContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#iteration_statement.
    def enterIteration_statement(self, ctx:CSharp4Parser.Iteration_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#iteration_statement.
    def exitIteration_statement(self, ctx:CSharp4Parser.Iteration_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#while_statement.
    def enterWhile_statement(self, ctx:CSharp4Parser.While_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#while_statement.
    def exitWhile_statement(self, ctx:CSharp4Parser.While_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#do_statement.
    def enterDo_statement(self, ctx:CSharp4Parser.Do_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#do_statement.
    def exitDo_statement(self, ctx:CSharp4Parser.Do_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#for_statement.
    def enterFor_statement(self, ctx:CSharp4Parser.For_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#for_statement.
    def exitFor_statement(self, ctx:CSharp4Parser.For_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#for_initializer.
    def enterFor_initializer(self, ctx:CSharp4Parser.For_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#for_initializer.
    def exitFor_initializer(self, ctx:CSharp4Parser.For_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#for_condition.
    def enterFor_condition(self, ctx:CSharp4Parser.For_conditionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#for_condition.
    def exitFor_condition(self, ctx:CSharp4Parser.For_conditionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#for_iterator.
    def enterFor_iterator(self, ctx:CSharp4Parser.For_iteratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#for_iterator.
    def exitFor_iterator(self, ctx:CSharp4Parser.For_iteratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#statement_expression_list.
    def enterStatement_expression_list(self, ctx:CSharp4Parser.Statement_expression_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#statement_expression_list.
    def exitStatement_expression_list(self, ctx:CSharp4Parser.Statement_expression_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#foreach_statement.
    def enterForeach_statement(self, ctx:CSharp4Parser.Foreach_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#foreach_statement.
    def exitForeach_statement(self, ctx:CSharp4Parser.Foreach_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#jump_statement.
    def enterJump_statement(self, ctx:CSharp4Parser.Jump_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#jump_statement.
    def exitJump_statement(self, ctx:CSharp4Parser.Jump_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#break_statement.
    def enterBreak_statement(self, ctx:CSharp4Parser.Break_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#break_statement.
    def exitBreak_statement(self, ctx:CSharp4Parser.Break_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#continue_statement.
    def enterContinue_statement(self, ctx:CSharp4Parser.Continue_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#continue_statement.
    def exitContinue_statement(self, ctx:CSharp4Parser.Continue_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#goto_statement.
    def enterGoto_statement(self, ctx:CSharp4Parser.Goto_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#goto_statement.
    def exitGoto_statement(self, ctx:CSharp4Parser.Goto_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#return_statement.
    def enterReturn_statement(self, ctx:CSharp4Parser.Return_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#return_statement.
    def exitReturn_statement(self, ctx:CSharp4Parser.Return_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#throw_statement.
    def enterThrow_statement(self, ctx:CSharp4Parser.Throw_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#throw_statement.
    def exitThrow_statement(self, ctx:CSharp4Parser.Throw_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#try_statement.
    def enterTry_statement(self, ctx:CSharp4Parser.Try_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#try_statement.
    def exitTry_statement(self, ctx:CSharp4Parser.Try_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#catch_clauses.
    def enterCatch_clauses(self, ctx:CSharp4Parser.Catch_clausesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#catch_clauses.
    def exitCatch_clauses(self, ctx:CSharp4Parser.Catch_clausesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#specific_catch_clauses.
    def enterSpecific_catch_clauses(self, ctx:CSharp4Parser.Specific_catch_clausesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#specific_catch_clauses.
    def exitSpecific_catch_clauses(self, ctx:CSharp4Parser.Specific_catch_clausesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#specific_catch_clause.
    def enterSpecific_catch_clause(self, ctx:CSharp4Parser.Specific_catch_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#specific_catch_clause.
    def exitSpecific_catch_clause(self, ctx:CSharp4Parser.Specific_catch_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#general_catch_clause.
    def enterGeneral_catch_clause(self, ctx:CSharp4Parser.General_catch_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#general_catch_clause.
    def exitGeneral_catch_clause(self, ctx:CSharp4Parser.General_catch_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#finally_clause.
    def enterFinally_clause(self, ctx:CSharp4Parser.Finally_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#finally_clause.
    def exitFinally_clause(self, ctx:CSharp4Parser.Finally_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#checked_statement.
    def enterChecked_statement(self, ctx:CSharp4Parser.Checked_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#checked_statement.
    def exitChecked_statement(self, ctx:CSharp4Parser.Checked_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unchecked_statement.
    def enterUnchecked_statement(self, ctx:CSharp4Parser.Unchecked_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unchecked_statement.
    def exitUnchecked_statement(self, ctx:CSharp4Parser.Unchecked_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#lock_statement.
    def enterLock_statement(self, ctx:CSharp4Parser.Lock_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#lock_statement.
    def exitLock_statement(self, ctx:CSharp4Parser.Lock_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#using_statement.
    def enterUsing_statement(self, ctx:CSharp4Parser.Using_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#using_statement.
    def exitUsing_statement(self, ctx:CSharp4Parser.Using_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#resource_acquisition.
    def enterResource_acquisition(self, ctx:CSharp4Parser.Resource_acquisitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#resource_acquisition.
    def exitResource_acquisition(self, ctx:CSharp4Parser.Resource_acquisitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#yield_statement.
    def enterYield_statement(self, ctx:CSharp4Parser.Yield_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#yield_statement.
    def exitYield_statement(self, ctx:CSharp4Parser.Yield_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#parse.
    def enterParse(self, ctx:CSharp4Parser.ParseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#parse.
    def exitParse(self, ctx:CSharp4Parser.ParseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#namespace_declaration.
    def enterNamespace_declaration(self, ctx:CSharp4Parser.Namespace_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_declaration.
    def exitNamespace_declaration(self, ctx:CSharp4Parser.Namespace_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#qualified_identifier.
    def enterQualified_identifier(self, ctx:CSharp4Parser.Qualified_identifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#qualified_identifier.
    def exitQualified_identifier(self, ctx:CSharp4Parser.Qualified_identifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#namespace_body.
    def enterNamespace_body(self, ctx:CSharp4Parser.Namespace_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_body.
    def exitNamespace_body(self, ctx:CSharp4Parser.Namespace_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#extern_alias_directives.
    def enterExtern_alias_directives(self, ctx:CSharp4Parser.Extern_alias_directivesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#extern_alias_directives.
    def exitExtern_alias_directives(self, ctx:CSharp4Parser.Extern_alias_directivesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#extern_alias_directive.
    def enterExtern_alias_directive(self, ctx:CSharp4Parser.Extern_alias_directiveContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#extern_alias_directive.
    def exitExtern_alias_directive(self, ctx:CSharp4Parser.Extern_alias_directiveContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#using_directives.
    def enterUsing_directives(self, ctx:CSharp4Parser.Using_directivesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#using_directives.
    def exitUsing_directives(self, ctx:CSharp4Parser.Using_directivesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#using_directive.
    def enterUsing_directive(self, ctx:CSharp4Parser.Using_directiveContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#using_directive.
    def exitUsing_directive(self, ctx:CSharp4Parser.Using_directiveContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#using_alias_directive.
    def enterUsing_alias_directive(self, ctx:CSharp4Parser.Using_alias_directiveContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#using_alias_directive.
    def exitUsing_alias_directive(self, ctx:CSharp4Parser.Using_alias_directiveContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#using_namespace_directive.
    def enterUsing_namespace_directive(self, ctx:CSharp4Parser.Using_namespace_directiveContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#using_namespace_directive.
    def exitUsing_namespace_directive(self, ctx:CSharp4Parser.Using_namespace_directiveContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#namespace_member_declarations.
    def enterNamespace_member_declarations(self, ctx:CSharp4Parser.Namespace_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_member_declarations.
    def exitNamespace_member_declarations(self, ctx:CSharp4Parser.Namespace_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#namespace_member_declaration.
    def enterNamespace_member_declaration(self, ctx:CSharp4Parser.Namespace_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#namespace_member_declaration.
    def exitNamespace_member_declaration(self, ctx:CSharp4Parser.Namespace_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_declaration.
    def enterType_declaration(self, ctx:CSharp4Parser.Type_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_declaration.
    def exitType_declaration(self, ctx:CSharp4Parser.Type_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#qualified_alias_member.
    def enterQualified_alias_member(self, ctx:CSharp4Parser.Qualified_alias_memberContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#qualified_alias_member.
    def exitQualified_alias_member(self, ctx:CSharp4Parser.Qualified_alias_memberContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_declaration.
    def enterClass_declaration(self, ctx:CSharp4Parser.Class_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_declaration.
    def exitClass_declaration(self, ctx:CSharp4Parser.Class_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_modifiers.
    def enterClass_modifiers(self, ctx:CSharp4Parser.Class_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_modifiers.
    def exitClass_modifiers(self, ctx:CSharp4Parser.Class_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_modifier.
    def enterClass_modifier(self, ctx:CSharp4Parser.Class_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_modifier.
    def exitClass_modifier(self, ctx:CSharp4Parser.Class_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameter_list.
    def enterType_parameter_list(self, ctx:CSharp4Parser.Type_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameter_list.
    def exitType_parameter_list(self, ctx:CSharp4Parser.Type_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameters.
    def enterType_parameters(self, ctx:CSharp4Parser.Type_parametersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameters.
    def exitType_parameters(self, ctx:CSharp4Parser.Type_parametersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameter.
    def enterType_parameter(self, ctx:CSharp4Parser.Type_parameterContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameter.
    def exitType_parameter(self, ctx:CSharp4Parser.Type_parameterContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_base.
    def enterClass_base(self, ctx:CSharp4Parser.Class_baseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_base.
    def exitClass_base(self, ctx:CSharp4Parser.Class_baseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_type_list.
    def enterInterface_type_list(self, ctx:CSharp4Parser.Interface_type_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_type_list.
    def exitInterface_type_list(self, ctx:CSharp4Parser.Interface_type_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameter_constraints_clauses.
    def enterType_parameter_constraints_clauses(self, ctx:CSharp4Parser.Type_parameter_constraints_clausesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameter_constraints_clauses.
    def exitType_parameter_constraints_clauses(self, ctx:CSharp4Parser.Type_parameter_constraints_clausesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameter_constraints_clause.
    def enterType_parameter_constraints_clause(self, ctx:CSharp4Parser.Type_parameter_constraints_clauseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameter_constraints_clause.
    def exitType_parameter_constraints_clause(self, ctx:CSharp4Parser.Type_parameter_constraints_clauseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_parameter_constraints.
    def enterType_parameter_constraints(self, ctx:CSharp4Parser.Type_parameter_constraintsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_parameter_constraints.
    def exitType_parameter_constraints(self, ctx:CSharp4Parser.Type_parameter_constraintsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#primary_constraint.
    def enterPrimary_constraint(self, ctx:CSharp4Parser.Primary_constraintContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#primary_constraint.
    def exitPrimary_constraint(self, ctx:CSharp4Parser.Primary_constraintContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#secondary_constraints.
    def enterSecondary_constraints(self, ctx:CSharp4Parser.Secondary_constraintsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#secondary_constraints.
    def exitSecondary_constraints(self, ctx:CSharp4Parser.Secondary_constraintsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_constraint.
    def enterConstructor_constraint(self, ctx:CSharp4Parser.Constructor_constraintContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_constraint.
    def exitConstructor_constraint(self, ctx:CSharp4Parser.Constructor_constraintContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_body.
    def enterClass_body(self, ctx:CSharp4Parser.Class_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_body.
    def exitClass_body(self, ctx:CSharp4Parser.Class_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_member_declarations.
    def enterClass_member_declarations(self, ctx:CSharp4Parser.Class_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_member_declarations.
    def exitClass_member_declarations(self, ctx:CSharp4Parser.Class_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_member_declaration.
    def enterClass_member_declaration(self, ctx:CSharp4Parser.Class_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_member_declaration.
    def exitClass_member_declaration(self, ctx:CSharp4Parser.Class_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#all_member_modifiers.
    def enterAll_member_modifiers(self, ctx:CSharp4Parser.All_member_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#all_member_modifiers.
    def exitAll_member_modifiers(self, ctx:CSharp4Parser.All_member_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#all_member_modifier.
    def enterAll_member_modifier(self, ctx:CSharp4Parser.All_member_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#all_member_modifier.
    def exitAll_member_modifier(self, ctx:CSharp4Parser.All_member_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#common_member_declaration.
    def enterCommon_member_declaration(self, ctx:CSharp4Parser.Common_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#common_member_declaration.
    def exitCommon_member_declaration(self, ctx:CSharp4Parser.Common_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#typed_member_declaration.
    def enterTyped_member_declaration(self, ctx:CSharp4Parser.Typed_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#typed_member_declaration.
    def exitTyped_member_declaration(self, ctx:CSharp4Parser.Typed_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constant_declarators.
    def enterConstant_declarators(self, ctx:CSharp4Parser.Constant_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constant_declarators.
    def exitConstant_declarators(self, ctx:CSharp4Parser.Constant_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constant_declarator.
    def enterConstant_declarator(self, ctx:CSharp4Parser.Constant_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constant_declarator.
    def exitConstant_declarator(self, ctx:CSharp4Parser.Constant_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variable_declarators.
    def enterVariable_declarators(self, ctx:CSharp4Parser.Variable_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variable_declarators.
    def exitVariable_declarators(self, ctx:CSharp4Parser.Variable_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variable_declarator.
    def enterVariable_declarator(self, ctx:CSharp4Parser.Variable_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variable_declarator.
    def exitVariable_declarator(self, ctx:CSharp4Parser.Variable_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variable_initializer.
    def enterVariable_initializer(self, ctx:CSharp4Parser.Variable_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variable_initializer.
    def exitVariable_initializer(self, ctx:CSharp4Parser.Variable_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_declaration.
    def enterMethod_declaration(self, ctx:CSharp4Parser.Method_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_declaration.
    def exitMethod_declaration(self, ctx:CSharp4Parser.Method_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_header.
    def enterMethod_header(self, ctx:CSharp4Parser.Method_headerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_header.
    def exitMethod_header(self, ctx:CSharp4Parser.Method_headerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_modifiers.
    def enterMethod_modifiers(self, ctx:CSharp4Parser.Method_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_modifiers.
    def exitMethod_modifiers(self, ctx:CSharp4Parser.Method_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_modifier.
    def enterMethod_modifier(self, ctx:CSharp4Parser.Method_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_modifier.
    def exitMethod_modifier(self, ctx:CSharp4Parser.Method_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#return_type.
    def enterReturn_type(self, ctx:CSharp4Parser.Return_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#return_type.
    def exitReturn_type(self, ctx:CSharp4Parser.Return_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_name.
    def enterMember_name(self, ctx:CSharp4Parser.Member_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_name.
    def exitMember_name(self, ctx:CSharp4Parser.Member_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_body.
    def enterMethod_body(self, ctx:CSharp4Parser.Method_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_body.
    def exitMethod_body(self, ctx:CSharp4Parser.Method_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#formal_parameter_list.
    def enterFormal_parameter_list(self, ctx:CSharp4Parser.Formal_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#formal_parameter_list.
    def exitFormal_parameter_list(self, ctx:CSharp4Parser.Formal_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_parameters.
    def enterFixed_parameters(self, ctx:CSharp4Parser.Fixed_parametersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_parameters.
    def exitFixed_parameters(self, ctx:CSharp4Parser.Fixed_parametersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_parameter.
    def enterFixed_parameter(self, ctx:CSharp4Parser.Fixed_parameterContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_parameter.
    def exitFixed_parameter(self, ctx:CSharp4Parser.Fixed_parameterContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#default_argument.
    def enterDefault_argument(self, ctx:CSharp4Parser.Default_argumentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#default_argument.
    def exitDefault_argument(self, ctx:CSharp4Parser.Default_argumentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#parameter_modifier.
    def enterParameter_modifier(self, ctx:CSharp4Parser.Parameter_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#parameter_modifier.
    def exitParameter_modifier(self, ctx:CSharp4Parser.Parameter_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#parameter_array.
    def enterParameter_array(self, ctx:CSharp4Parser.Parameter_arrayContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#parameter_array.
    def exitParameter_array(self, ctx:CSharp4Parser.Parameter_arrayContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#property_declaration.
    def enterProperty_declaration(self, ctx:CSharp4Parser.Property_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#property_declaration.
    def exitProperty_declaration(self, ctx:CSharp4Parser.Property_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#property_modifiers.
    def enterProperty_modifiers(self, ctx:CSharp4Parser.Property_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#property_modifiers.
    def exitProperty_modifiers(self, ctx:CSharp4Parser.Property_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#property_modifier.
    def enterProperty_modifier(self, ctx:CSharp4Parser.Property_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#property_modifier.
    def exitProperty_modifier(self, ctx:CSharp4Parser.Property_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#accessor_declarations.
    def enterAccessor_declarations(self, ctx:CSharp4Parser.Accessor_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#accessor_declarations.
    def exitAccessor_declarations(self, ctx:CSharp4Parser.Accessor_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#get_accessor_declaration.
    def enterGet_accessor_declaration(self, ctx:CSharp4Parser.Get_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#get_accessor_declaration.
    def exitGet_accessor_declaration(self, ctx:CSharp4Parser.Get_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#set_accessor_declaration.
    def enterSet_accessor_declaration(self, ctx:CSharp4Parser.Set_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#set_accessor_declaration.
    def exitSet_accessor_declaration(self, ctx:CSharp4Parser.Set_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#accessor_modifier.
    def enterAccessor_modifier(self, ctx:CSharp4Parser.Accessor_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#accessor_modifier.
    def exitAccessor_modifier(self, ctx:CSharp4Parser.Accessor_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#accessor_body.
    def enterAccessor_body(self, ctx:CSharp4Parser.Accessor_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#accessor_body.
    def exitAccessor_body(self, ctx:CSharp4Parser.Accessor_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_declaration.
    def enterEvent_declaration(self, ctx:CSharp4Parser.Event_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_declaration.
    def exitEvent_declaration(self, ctx:CSharp4Parser.Event_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_modifiers.
    def enterEvent_modifiers(self, ctx:CSharp4Parser.Event_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_modifiers.
    def exitEvent_modifiers(self, ctx:CSharp4Parser.Event_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_modifier.
    def enterEvent_modifier(self, ctx:CSharp4Parser.Event_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_modifier.
    def exitEvent_modifier(self, ctx:CSharp4Parser.Event_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_accessor_declarations.
    def enterEvent_accessor_declarations(self, ctx:CSharp4Parser.Event_accessor_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_accessor_declarations.
    def exitEvent_accessor_declarations(self, ctx:CSharp4Parser.Event_accessor_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#add_accessor_declaration.
    def enterAdd_accessor_declaration(self, ctx:CSharp4Parser.Add_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#add_accessor_declaration.
    def exitAdd_accessor_declaration(self, ctx:CSharp4Parser.Add_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#remove_accessor_declaration.
    def enterRemove_accessor_declaration(self, ctx:CSharp4Parser.Remove_accessor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#remove_accessor_declaration.
    def exitRemove_accessor_declaration(self, ctx:CSharp4Parser.Remove_accessor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_declaration.
    def enterIndexer_declaration(self, ctx:CSharp4Parser.Indexer_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_declaration.
    def exitIndexer_declaration(self, ctx:CSharp4Parser.Indexer_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_modifiers.
    def enterIndexer_modifiers(self, ctx:CSharp4Parser.Indexer_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_modifiers.
    def exitIndexer_modifiers(self, ctx:CSharp4Parser.Indexer_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_modifier.
    def enterIndexer_modifier(self, ctx:CSharp4Parser.Indexer_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_modifier.
    def exitIndexer_modifier(self, ctx:CSharp4Parser.Indexer_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_declarator.
    def enterIndexer_declarator(self, ctx:CSharp4Parser.Indexer_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_declarator.
    def exitIndexer_declarator(self, ctx:CSharp4Parser.Indexer_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_declaration.
    def enterOperator_declaration(self, ctx:CSharp4Parser.Operator_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_declaration.
    def exitOperator_declaration(self, ctx:CSharp4Parser.Operator_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_modifiers.
    def enterOperator_modifiers(self, ctx:CSharp4Parser.Operator_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_modifiers.
    def exitOperator_modifiers(self, ctx:CSharp4Parser.Operator_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_modifier.
    def enterOperator_modifier(self, ctx:CSharp4Parser.Operator_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_modifier.
    def exitOperator_modifier(self, ctx:CSharp4Parser.Operator_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_declarator.
    def enterOperator_declarator(self, ctx:CSharp4Parser.Operator_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_declarator.
    def exitOperator_declarator(self, ctx:CSharp4Parser.Operator_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unary_operator_declarator.
    def enterUnary_operator_declarator(self, ctx:CSharp4Parser.Unary_operator_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unary_operator_declarator.
    def exitUnary_operator_declarator(self, ctx:CSharp4Parser.Unary_operator_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#overloadable_unary_operator.
    def enterOverloadable_unary_operator(self, ctx:CSharp4Parser.Overloadable_unary_operatorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#overloadable_unary_operator.
    def exitOverloadable_unary_operator(self, ctx:CSharp4Parser.Overloadable_unary_operatorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#binary_operator_declarator.
    def enterBinary_operator_declarator(self, ctx:CSharp4Parser.Binary_operator_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#binary_operator_declarator.
    def exitBinary_operator_declarator(self, ctx:CSharp4Parser.Binary_operator_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#overloadable_binary_operator.
    def enterOverloadable_binary_operator(self, ctx:CSharp4Parser.Overloadable_binary_operatorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#overloadable_binary_operator.
    def exitOverloadable_binary_operator(self, ctx:CSharp4Parser.Overloadable_binary_operatorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#overloadable_operator.
    def enterOverloadable_operator(self, ctx:CSharp4Parser.Overloadable_operatorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#overloadable_operator.
    def exitOverloadable_operator(self, ctx:CSharp4Parser.Overloadable_operatorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#conversion_operator_declarator.
    def enterConversion_operator_declarator(self, ctx:CSharp4Parser.Conversion_operator_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#conversion_operator_declarator.
    def exitConversion_operator_declarator(self, ctx:CSharp4Parser.Conversion_operator_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_body.
    def enterOperator_body(self, ctx:CSharp4Parser.Operator_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_body.
    def exitOperator_body(self, ctx:CSharp4Parser.Operator_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_declaration.
    def enterConstructor_declaration(self, ctx:CSharp4Parser.Constructor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_declaration.
    def exitConstructor_declaration(self, ctx:CSharp4Parser.Constructor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_modifiers.
    def enterConstructor_modifiers(self, ctx:CSharp4Parser.Constructor_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_modifiers.
    def exitConstructor_modifiers(self, ctx:CSharp4Parser.Constructor_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_modifier.
    def enterConstructor_modifier(self, ctx:CSharp4Parser.Constructor_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_modifier.
    def exitConstructor_modifier(self, ctx:CSharp4Parser.Constructor_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_declarator.
    def enterConstructor_declarator(self, ctx:CSharp4Parser.Constructor_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_declarator.
    def exitConstructor_declarator(self, ctx:CSharp4Parser.Constructor_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_initializer.
    def enterConstructor_initializer(self, ctx:CSharp4Parser.Constructor_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_initializer.
    def exitConstructor_initializer(self, ctx:CSharp4Parser.Constructor_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_body.
    def enterConstructor_body(self, ctx:CSharp4Parser.Constructor_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_body.
    def exitConstructor_body(self, ctx:CSharp4Parser.Constructor_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#static_constructor_declaration.
    def enterStatic_constructor_declaration(self, ctx:CSharp4Parser.Static_constructor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#static_constructor_declaration.
    def exitStatic_constructor_declaration(self, ctx:CSharp4Parser.Static_constructor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#static_constructor_modifiers.
    def enterStatic_constructor_modifiers(self, ctx:CSharp4Parser.Static_constructor_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#static_constructor_modifiers.
    def exitStatic_constructor_modifiers(self, ctx:CSharp4Parser.Static_constructor_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#static_constructor_body.
    def enterStatic_constructor_body(self, ctx:CSharp4Parser.Static_constructor_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#static_constructor_body.
    def exitStatic_constructor_body(self, ctx:CSharp4Parser.Static_constructor_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#destructor_declaration.
    def enterDestructor_declaration(self, ctx:CSharp4Parser.Destructor_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#destructor_declaration.
    def exitDestructor_declaration(self, ctx:CSharp4Parser.Destructor_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#destructor_body.
    def enterDestructor_body(self, ctx:CSharp4Parser.Destructor_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#destructor_body.
    def exitDestructor_body(self, ctx:CSharp4Parser.Destructor_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#body.
    def enterBody(self, ctx:CSharp4Parser.BodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#body.
    def exitBody(self, ctx:CSharp4Parser.BodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_declaration.
    def enterStruct_declaration(self, ctx:CSharp4Parser.Struct_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_declaration.
    def exitStruct_declaration(self, ctx:CSharp4Parser.Struct_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_modifiers.
    def enterStruct_modifiers(self, ctx:CSharp4Parser.Struct_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_modifiers.
    def exitStruct_modifiers(self, ctx:CSharp4Parser.Struct_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_modifier.
    def enterStruct_modifier(self, ctx:CSharp4Parser.Struct_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_modifier.
    def exitStruct_modifier(self, ctx:CSharp4Parser.Struct_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_interfaces.
    def enterStruct_interfaces(self, ctx:CSharp4Parser.Struct_interfacesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_interfaces.
    def exitStruct_interfaces(self, ctx:CSharp4Parser.Struct_interfacesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_body.
    def enterStruct_body(self, ctx:CSharp4Parser.Struct_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_body.
    def exitStruct_body(self, ctx:CSharp4Parser.Struct_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_member_declarations.
    def enterStruct_member_declarations(self, ctx:CSharp4Parser.Struct_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_member_declarations.
    def exitStruct_member_declarations(self, ctx:CSharp4Parser.Struct_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_member_declaration.
    def enterStruct_member_declaration(self, ctx:CSharp4Parser.Struct_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_member_declaration.
    def exitStruct_member_declaration(self, ctx:CSharp4Parser.Struct_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#array_type.
    def enterArray_type(self, ctx:CSharp4Parser.Array_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#array_type.
    def exitArray_type(self, ctx:CSharp4Parser.Array_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#non_array_type.
    def enterNon_array_type(self, ctx:CSharp4Parser.Non_array_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#non_array_type.
    def exitNon_array_type(self, ctx:CSharp4Parser.Non_array_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#rank_specifiers.
    def enterRank_specifiers(self, ctx:CSharp4Parser.Rank_specifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#rank_specifiers.
    def exitRank_specifiers(self, ctx:CSharp4Parser.Rank_specifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#rank_specifier.
    def enterRank_specifier(self, ctx:CSharp4Parser.Rank_specifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#rank_specifier.
    def exitRank_specifier(self, ctx:CSharp4Parser.Rank_specifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#dim_separators.
    def enterDim_separators(self, ctx:CSharp4Parser.Dim_separatorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#dim_separators.
    def exitDim_separators(self, ctx:CSharp4Parser.Dim_separatorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#array_initializer.
    def enterArray_initializer(self, ctx:CSharp4Parser.Array_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#array_initializer.
    def exitArray_initializer(self, ctx:CSharp4Parser.Array_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variable_initializer_list.
    def enterVariable_initializer_list(self, ctx:CSharp4Parser.Variable_initializer_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variable_initializer_list.
    def exitVariable_initializer_list(self, ctx:CSharp4Parser.Variable_initializer_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_declaration.
    def enterInterface_declaration(self, ctx:CSharp4Parser.Interface_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_declaration.
    def exitInterface_declaration(self, ctx:CSharp4Parser.Interface_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_modifiers.
    def enterInterface_modifiers(self, ctx:CSharp4Parser.Interface_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_modifiers.
    def exitInterface_modifiers(self, ctx:CSharp4Parser.Interface_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_modifier.
    def enterInterface_modifier(self, ctx:CSharp4Parser.Interface_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_modifier.
    def exitInterface_modifier(self, ctx:CSharp4Parser.Interface_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variant_type_parameter_list.
    def enterVariant_type_parameter_list(self, ctx:CSharp4Parser.Variant_type_parameter_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variant_type_parameter_list.
    def exitVariant_type_parameter_list(self, ctx:CSharp4Parser.Variant_type_parameter_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variant_type_parameters.
    def enterVariant_type_parameters(self, ctx:CSharp4Parser.Variant_type_parametersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variant_type_parameters.
    def exitVariant_type_parameters(self, ctx:CSharp4Parser.Variant_type_parametersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#variance_annotation.
    def enterVariance_annotation(self, ctx:CSharp4Parser.Variance_annotationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#variance_annotation.
    def exitVariance_annotation(self, ctx:CSharp4Parser.Variance_annotationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_base.
    def enterInterface_base(self, ctx:CSharp4Parser.Interface_baseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_base.
    def exitInterface_base(self, ctx:CSharp4Parser.Interface_baseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_body.
    def enterInterface_body(self, ctx:CSharp4Parser.Interface_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_body.
    def exitInterface_body(self, ctx:CSharp4Parser.Interface_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_member_declarations.
    def enterInterface_member_declarations(self, ctx:CSharp4Parser.Interface_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_member_declarations.
    def exitInterface_member_declarations(self, ctx:CSharp4Parser.Interface_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_member_declaration.
    def enterInterface_member_declaration(self, ctx:CSharp4Parser.Interface_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_member_declaration.
    def exitInterface_member_declaration(self, ctx:CSharp4Parser.Interface_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_method_declaration.
    def enterInterface_method_declaration(self, ctx:CSharp4Parser.Interface_method_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_method_declaration.
    def exitInterface_method_declaration(self, ctx:CSharp4Parser.Interface_method_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_property_declaration.
    def enterInterface_property_declaration(self, ctx:CSharp4Parser.Interface_property_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_property_declaration.
    def exitInterface_property_declaration(self, ctx:CSharp4Parser.Interface_property_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_accessors.
    def enterInterface_accessors(self, ctx:CSharp4Parser.Interface_accessorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_accessors.
    def exitInterface_accessors(self, ctx:CSharp4Parser.Interface_accessorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_event_declaration.
    def enterInterface_event_declaration(self, ctx:CSharp4Parser.Interface_event_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_event_declaration.
    def exitInterface_event_declaration(self, ctx:CSharp4Parser.Interface_event_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_indexer_declaration.
    def enterInterface_indexer_declaration(self, ctx:CSharp4Parser.Interface_indexer_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_indexer_declaration.
    def exitInterface_indexer_declaration(self, ctx:CSharp4Parser.Interface_indexer_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_declaration.
    def enterEnum_declaration(self, ctx:CSharp4Parser.Enum_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_declaration.
    def exitEnum_declaration(self, ctx:CSharp4Parser.Enum_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_base.
    def enterEnum_base(self, ctx:CSharp4Parser.Enum_baseContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_base.
    def exitEnum_base(self, ctx:CSharp4Parser.Enum_baseContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_body.
    def enterEnum_body(self, ctx:CSharp4Parser.Enum_bodyContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_body.
    def exitEnum_body(self, ctx:CSharp4Parser.Enum_bodyContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_modifiers.
    def enterEnum_modifiers(self, ctx:CSharp4Parser.Enum_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_modifiers.
    def exitEnum_modifiers(self, ctx:CSharp4Parser.Enum_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_modifier.
    def enterEnum_modifier(self, ctx:CSharp4Parser.Enum_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_modifier.
    def exitEnum_modifier(self, ctx:CSharp4Parser.Enum_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_member_declarations.
    def enterEnum_member_declarations(self, ctx:CSharp4Parser.Enum_member_declarationsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_member_declarations.
    def exitEnum_member_declarations(self, ctx:CSharp4Parser.Enum_member_declarationsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_member_declaration.
    def enterEnum_member_declaration(self, ctx:CSharp4Parser.Enum_member_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_member_declaration.
    def exitEnum_member_declaration(self, ctx:CSharp4Parser.Enum_member_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_declaration.
    def enterDelegate_declaration(self, ctx:CSharp4Parser.Delegate_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_declaration.
    def exitDelegate_declaration(self, ctx:CSharp4Parser.Delegate_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_modifiers.
    def enterDelegate_modifiers(self, ctx:CSharp4Parser.Delegate_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_modifiers.
    def exitDelegate_modifiers(self, ctx:CSharp4Parser.Delegate_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_modifier.
    def enterDelegate_modifier(self, ctx:CSharp4Parser.Delegate_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_modifier.
    def exitDelegate_modifier(self, ctx:CSharp4Parser.Delegate_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#global_attributes.
    def enterGlobal_attributes(self, ctx:CSharp4Parser.Global_attributesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#global_attributes.
    def exitGlobal_attributes(self, ctx:CSharp4Parser.Global_attributesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#global_attribute_sections.
    def enterGlobal_attribute_sections(self, ctx:CSharp4Parser.Global_attribute_sectionsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#global_attribute_sections.
    def exitGlobal_attribute_sections(self, ctx:CSharp4Parser.Global_attribute_sectionsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#global_attribute_section.
    def enterGlobal_attribute_section(self, ctx:CSharp4Parser.Global_attribute_sectionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#global_attribute_section.
    def exitGlobal_attribute_section(self, ctx:CSharp4Parser.Global_attribute_sectionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#global_attribute_target_specifier.
    def enterGlobal_attribute_target_specifier(self, ctx:CSharp4Parser.Global_attribute_target_specifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#global_attribute_target_specifier.
    def exitGlobal_attribute_target_specifier(self, ctx:CSharp4Parser.Global_attribute_target_specifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#global_attribute_target.
    def enterGlobal_attribute_target(self, ctx:CSharp4Parser.Global_attribute_targetContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#global_attribute_target.
    def exitGlobal_attribute_target(self, ctx:CSharp4Parser.Global_attribute_targetContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attributes.
    def enterAttributes(self, ctx:CSharp4Parser.AttributesContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attributes.
    def exitAttributes(self, ctx:CSharp4Parser.AttributesContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_sections.
    def enterAttribute_sections(self, ctx:CSharp4Parser.Attribute_sectionsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_sections.
    def exitAttribute_sections(self, ctx:CSharp4Parser.Attribute_sectionsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_section.
    def enterAttribute_section(self, ctx:CSharp4Parser.Attribute_sectionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_section.
    def exitAttribute_section(self, ctx:CSharp4Parser.Attribute_sectionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_target_specifier.
    def enterAttribute_target_specifier(self, ctx:CSharp4Parser.Attribute_target_specifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_target_specifier.
    def exitAttribute_target_specifier(self, ctx:CSharp4Parser.Attribute_target_specifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_target.
    def enterAttribute_target(self, ctx:CSharp4Parser.Attribute_targetContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_target.
    def exitAttribute_target(self, ctx:CSharp4Parser.Attribute_targetContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_list.
    def enterAttribute_list(self, ctx:CSharp4Parser.Attribute_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_list.
    def exitAttribute_list(self, ctx:CSharp4Parser.Attribute_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute.
    def enterAttribute(self, ctx:CSharp4Parser.AttributeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute.
    def exitAttribute(self, ctx:CSharp4Parser.AttributeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_name.
    def enterAttribute_name(self, ctx:CSharp4Parser.Attribute_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_name.
    def exitAttribute_name(self, ctx:CSharp4Parser.Attribute_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_arguments.
    def enterAttribute_arguments(self, ctx:CSharp4Parser.Attribute_argumentsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_arguments.
    def exitAttribute_arguments(self, ctx:CSharp4Parser.Attribute_argumentsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#positional_argument_list.
    def enterPositional_argument_list(self, ctx:CSharp4Parser.Positional_argument_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#positional_argument_list.
    def exitPositional_argument_list(self, ctx:CSharp4Parser.Positional_argument_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#positional_argument.
    def enterPositional_argument(self, ctx:CSharp4Parser.Positional_argumentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#positional_argument.
    def exitPositional_argument(self, ctx:CSharp4Parser.Positional_argumentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#named_argument_list.
    def enterNamed_argument_list(self, ctx:CSharp4Parser.Named_argument_listContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#named_argument_list.
    def exitNamed_argument_list(self, ctx:CSharp4Parser.Named_argument_listContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#named_argument.
    def enterNamed_argument(self, ctx:CSharp4Parser.Named_argumentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#named_argument.
    def exitNamed_argument(self, ctx:CSharp4Parser.Named_argumentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#attribute_argument_expression.
    def enterAttribute_argument_expression(self, ctx:CSharp4Parser.Attribute_argument_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#attribute_argument_expression.
    def exitAttribute_argument_expression(self, ctx:CSharp4Parser.Attribute_argument_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_modifier_unsafe.
    def enterClass_modifier_unsafe(self, ctx:CSharp4Parser.Class_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_modifier_unsafe.
    def exitClass_modifier_unsafe(self, ctx:CSharp4Parser.Class_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_modifier_unsafe.
    def enterStruct_modifier_unsafe(self, ctx:CSharp4Parser.Struct_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_modifier_unsafe.
    def exitStruct_modifier_unsafe(self, ctx:CSharp4Parser.Struct_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_modifier_unsafe.
    def enterInterface_modifier_unsafe(self, ctx:CSharp4Parser.Interface_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_modifier_unsafe.
    def exitInterface_modifier_unsafe(self, ctx:CSharp4Parser.Interface_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_modifier_unsafe.
    def enterDelegate_modifier_unsafe(self, ctx:CSharp4Parser.Delegate_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_modifier_unsafe.
    def exitDelegate_modifier_unsafe(self, ctx:CSharp4Parser.Delegate_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#field_modifier_unsafe.
    def enterField_modifier_unsafe(self, ctx:CSharp4Parser.Field_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#field_modifier_unsafe.
    def exitField_modifier_unsafe(self, ctx:CSharp4Parser.Field_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_modifier_unsafe.
    def enterMethod_modifier_unsafe(self, ctx:CSharp4Parser.Method_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_modifier_unsafe.
    def exitMethod_modifier_unsafe(self, ctx:CSharp4Parser.Method_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#property_modifier_unsafe.
    def enterProperty_modifier_unsafe(self, ctx:CSharp4Parser.Property_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#property_modifier_unsafe.
    def exitProperty_modifier_unsafe(self, ctx:CSharp4Parser.Property_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_modifier_unsafe.
    def enterEvent_modifier_unsafe(self, ctx:CSharp4Parser.Event_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_modifier_unsafe.
    def exitEvent_modifier_unsafe(self, ctx:CSharp4Parser.Event_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_modifier_unsafe.
    def enterIndexer_modifier_unsafe(self, ctx:CSharp4Parser.Indexer_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_modifier_unsafe.
    def exitIndexer_modifier_unsafe(self, ctx:CSharp4Parser.Indexer_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_modifier_unsafe.
    def enterOperator_modifier_unsafe(self, ctx:CSharp4Parser.Operator_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_modifier_unsafe.
    def exitOperator_modifier_unsafe(self, ctx:CSharp4Parser.Operator_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_modifier_unsafe.
    def enterConstructor_modifier_unsafe(self, ctx:CSharp4Parser.Constructor_modifier_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_modifier_unsafe.
    def exitConstructor_modifier_unsafe(self, ctx:CSharp4Parser.Constructor_modifier_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#destructor_declaration_unsafe.
    def enterDestructor_declaration_unsafe(self, ctx:CSharp4Parser.Destructor_declaration_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#destructor_declaration_unsafe.
    def exitDestructor_declaration_unsafe(self, ctx:CSharp4Parser.Destructor_declaration_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#static_constructor_modifiers_unsafe.
    def enterStatic_constructor_modifiers_unsafe(self, ctx:CSharp4Parser.Static_constructor_modifiers_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#static_constructor_modifiers_unsafe.
    def exitStatic_constructor_modifiers_unsafe(self, ctx:CSharp4Parser.Static_constructor_modifiers_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#embedded_statement_unsafe.
    def enterEmbedded_statement_unsafe(self, ctx:CSharp4Parser.Embedded_statement_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#embedded_statement_unsafe.
    def exitEmbedded_statement_unsafe(self, ctx:CSharp4Parser.Embedded_statement_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unsafe_statement.
    def enterUnsafe_statement(self, ctx:CSharp4Parser.Unsafe_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unsafe_statement.
    def exitUnsafe_statement(self, ctx:CSharp4Parser.Unsafe_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#type_unsafe.
    def enterType_unsafe(self, ctx:CSharp4Parser.Type_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#type_unsafe.
    def exitType_unsafe(self, ctx:CSharp4Parser.Type_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#pointer_type.
    def enterPointer_type(self, ctx:CSharp4Parser.Pointer_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#pointer_type.
    def exitPointer_type(self, ctx:CSharp4Parser.Pointer_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unmanaged_type.
    def enterUnmanaged_type(self, ctx:CSharp4Parser.Unmanaged_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unmanaged_type.
    def exitUnmanaged_type(self, ctx:CSharp4Parser.Unmanaged_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#primary_no_array_creation_expression_unsafe.
    def enterPrimary_no_array_creation_expression_unsafe(self, ctx:CSharp4Parser.Primary_no_array_creation_expression_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#primary_no_array_creation_expression_unsafe.
    def exitPrimary_no_array_creation_expression_unsafe(self, ctx:CSharp4Parser.Primary_no_array_creation_expression_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#unary_expression_unsafe.
    def enterUnary_expression_unsafe(self, ctx:CSharp4Parser.Unary_expression_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#unary_expression_unsafe.
    def exitUnary_expression_unsafe(self, ctx:CSharp4Parser.Unary_expression_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#pointer_indirection_expression.
    def enterPointer_indirection_expression(self, ctx:CSharp4Parser.Pointer_indirection_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#pointer_indirection_expression.
    def exitPointer_indirection_expression(self, ctx:CSharp4Parser.Pointer_indirection_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#addressof_expression.
    def enterAddressof_expression(self, ctx:CSharp4Parser.Addressof_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#addressof_expression.
    def exitAddressof_expression(self, ctx:CSharp4Parser.Addressof_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#sizeof_expression.
    def enterSizeof_expression(self, ctx:CSharp4Parser.Sizeof_expressionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#sizeof_expression.
    def exitSizeof_expression(self, ctx:CSharp4Parser.Sizeof_expressionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_statement.
    def enterFixed_statement(self, ctx:CSharp4Parser.Fixed_statementContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_statement.
    def exitFixed_statement(self, ctx:CSharp4Parser.Fixed_statementContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_pointer_declarators.
    def enterFixed_pointer_declarators(self, ctx:CSharp4Parser.Fixed_pointer_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_pointer_declarators.
    def exitFixed_pointer_declarators(self, ctx:CSharp4Parser.Fixed_pointer_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_pointer_declarator.
    def enterFixed_pointer_declarator(self, ctx:CSharp4Parser.Fixed_pointer_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_pointer_declarator.
    def exitFixed_pointer_declarator(self, ctx:CSharp4Parser.Fixed_pointer_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_pointer_initializer.
    def enterFixed_pointer_initializer(self, ctx:CSharp4Parser.Fixed_pointer_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_pointer_initializer.
    def exitFixed_pointer_initializer(self, ctx:CSharp4Parser.Fixed_pointer_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_member_declaration_unsafe.
    def enterStruct_member_declaration_unsafe(self, ctx:CSharp4Parser.Struct_member_declaration_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_member_declaration_unsafe.
    def exitStruct_member_declaration_unsafe(self, ctx:CSharp4Parser.Struct_member_declaration_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_size_buffer_declaration.
    def enterFixed_size_buffer_declaration(self, ctx:CSharp4Parser.Fixed_size_buffer_declarationContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_size_buffer_declaration.
    def exitFixed_size_buffer_declaration(self, ctx:CSharp4Parser.Fixed_size_buffer_declarationContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_size_buffer_modifiers.
    def enterFixed_size_buffer_modifiers(self, ctx:CSharp4Parser.Fixed_size_buffer_modifiersContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_size_buffer_modifiers.
    def exitFixed_size_buffer_modifiers(self, ctx:CSharp4Parser.Fixed_size_buffer_modifiersContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_size_buffer_modifier.
    def enterFixed_size_buffer_modifier(self, ctx:CSharp4Parser.Fixed_size_buffer_modifierContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_size_buffer_modifier.
    def exitFixed_size_buffer_modifier(self, ctx:CSharp4Parser.Fixed_size_buffer_modifierContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#buffer_element_type.
    def enterBuffer_element_type(self, ctx:CSharp4Parser.Buffer_element_typeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#buffer_element_type.
    def exitBuffer_element_type(self, ctx:CSharp4Parser.Buffer_element_typeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_size_buffer_declarators.
    def enterFixed_size_buffer_declarators(self, ctx:CSharp4Parser.Fixed_size_buffer_declaratorsContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_size_buffer_declarators.
    def exitFixed_size_buffer_declarators(self, ctx:CSharp4Parser.Fixed_size_buffer_declaratorsContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#fixed_size_buffer_declarator.
    def enterFixed_size_buffer_declarator(self, ctx:CSharp4Parser.Fixed_size_buffer_declaratorContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#fixed_size_buffer_declarator.
    def exitFixed_size_buffer_declarator(self, ctx:CSharp4Parser.Fixed_size_buffer_declaratorContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#local_variable_initializer_unsafe.
    def enterLocal_variable_initializer_unsafe(self, ctx:CSharp4Parser.Local_variable_initializer_unsafeContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#local_variable_initializer_unsafe.
    def exitLocal_variable_initializer_unsafe(self, ctx:CSharp4Parser.Local_variable_initializer_unsafeContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#stackalloc_initializer.
    def enterStackalloc_initializer(self, ctx:CSharp4Parser.Stackalloc_initializerContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#stackalloc_initializer.
    def exitStackalloc_initializer(self, ctx:CSharp4Parser.Stackalloc_initializerContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#from_contextual_keyword.
    def enterFrom_contextual_keyword(self, ctx:CSharp4Parser.From_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#from_contextual_keyword.
    def exitFrom_contextual_keyword(self, ctx:CSharp4Parser.From_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#let_contextual_keyword.
    def enterLet_contextual_keyword(self, ctx:CSharp4Parser.Let_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#let_contextual_keyword.
    def exitLet_contextual_keyword(self, ctx:CSharp4Parser.Let_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#where_contextual_keyword.
    def enterWhere_contextual_keyword(self, ctx:CSharp4Parser.Where_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#where_contextual_keyword.
    def exitWhere_contextual_keyword(self, ctx:CSharp4Parser.Where_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#join_contextual_keyword.
    def enterJoin_contextual_keyword(self, ctx:CSharp4Parser.Join_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#join_contextual_keyword.
    def exitJoin_contextual_keyword(self, ctx:CSharp4Parser.Join_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#on_contextual_keyword.
    def enterOn_contextual_keyword(self, ctx:CSharp4Parser.On_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#on_contextual_keyword.
    def exitOn_contextual_keyword(self, ctx:CSharp4Parser.On_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#equals_contextual_keyword.
    def enterEquals_contextual_keyword(self, ctx:CSharp4Parser.Equals_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#equals_contextual_keyword.
    def exitEquals_contextual_keyword(self, ctx:CSharp4Parser.Equals_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#into_contextual_keyword.
    def enterInto_contextual_keyword(self, ctx:CSharp4Parser.Into_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#into_contextual_keyword.
    def exitInto_contextual_keyword(self, ctx:CSharp4Parser.Into_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#orderby_contextual_keyword.
    def enterOrderby_contextual_keyword(self, ctx:CSharp4Parser.Orderby_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#orderby_contextual_keyword.
    def exitOrderby_contextual_keyword(self, ctx:CSharp4Parser.Orderby_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#ascending_contextual_keyword.
    def enterAscending_contextual_keyword(self, ctx:CSharp4Parser.Ascending_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#ascending_contextual_keyword.
    def exitAscending_contextual_keyword(self, ctx:CSharp4Parser.Ascending_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#descending_contextual_keyword.
    def enterDescending_contextual_keyword(self, ctx:CSharp4Parser.Descending_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#descending_contextual_keyword.
    def exitDescending_contextual_keyword(self, ctx:CSharp4Parser.Descending_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#select_contextual_keyword.
    def enterSelect_contextual_keyword(self, ctx:CSharp4Parser.Select_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#select_contextual_keyword.
    def exitSelect_contextual_keyword(self, ctx:CSharp4Parser.Select_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#group_contextual_keyword.
    def enterGroup_contextual_keyword(self, ctx:CSharp4Parser.Group_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#group_contextual_keyword.
    def exitGroup_contextual_keyword(self, ctx:CSharp4Parser.Group_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#by_contextual_keyword.
    def enterBy_contextual_keyword(self, ctx:CSharp4Parser.By_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#by_contextual_keyword.
    def exitBy_contextual_keyword(self, ctx:CSharp4Parser.By_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#partial_contextual_keyword.
    def enterPartial_contextual_keyword(self, ctx:CSharp4Parser.Partial_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#partial_contextual_keyword.
    def exitPartial_contextual_keyword(self, ctx:CSharp4Parser.Partial_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#alias_contextual_keyword.
    def enterAlias_contextual_keyword(self, ctx:CSharp4Parser.Alias_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#alias_contextual_keyword.
    def exitAlias_contextual_keyword(self, ctx:CSharp4Parser.Alias_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#yield_contextual_keyword.
    def enterYield_contextual_keyword(self, ctx:CSharp4Parser.Yield_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#yield_contextual_keyword.
    def exitYield_contextual_keyword(self, ctx:CSharp4Parser.Yield_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#get_contextual_keyword.
    def enterGet_contextual_keyword(self, ctx:CSharp4Parser.Get_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#get_contextual_keyword.
    def exitGet_contextual_keyword(self, ctx:CSharp4Parser.Get_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#set_contextual_keyword.
    def enterSet_contextual_keyword(self, ctx:CSharp4Parser.Set_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#set_contextual_keyword.
    def exitSet_contextual_keyword(self, ctx:CSharp4Parser.Set_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#add_contextual_keyword.
    def enterAdd_contextual_keyword(self, ctx:CSharp4Parser.Add_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#add_contextual_keyword.
    def exitAdd_contextual_keyword(self, ctx:CSharp4Parser.Add_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#remove_contextual_keyword.
    def enterRemove_contextual_keyword(self, ctx:CSharp4Parser.Remove_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#remove_contextual_keyword.
    def exitRemove_contextual_keyword(self, ctx:CSharp4Parser.Remove_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#dynamic_contextual_keyword.
    def enterDynamic_contextual_keyword(self, ctx:CSharp4Parser.Dynamic_contextual_keywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#dynamic_contextual_keyword.
    def exitDynamic_contextual_keyword(self, ctx:CSharp4Parser.Dynamic_contextual_keywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#arglist.
    def enterArglist(self, ctx:CSharp4Parser.ArglistContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#arglist.
    def exitArglist(self, ctx:CSharp4Parser.ArglistContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#right_arrow.
    def enterRight_arrow(self, ctx:CSharp4Parser.Right_arrowContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#right_arrow.
    def exitRight_arrow(self, ctx:CSharp4Parser.Right_arrowContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#right_shift.
    def enterRight_shift(self, ctx:CSharp4Parser.Right_shiftContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#right_shift.
    def exitRight_shift(self, ctx:CSharp4Parser.Right_shiftContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#right_shift_assignment.
    def enterRight_shift_assignment(self, ctx:CSharp4Parser.Right_shift_assignmentContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#right_shift_assignment.
    def exitRight_shift_assignment(self, ctx:CSharp4Parser.Right_shift_assignmentContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#literal.
    def enterLiteral(self, ctx:CSharp4Parser.LiteralContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#literal.
    def exitLiteral(self, ctx:CSharp4Parser.LiteralContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#boolean_literal.
    def enterBoolean_literal(self, ctx:CSharp4Parser.Boolean_literalContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#boolean_literal.
    def exitBoolean_literal(self, ctx:CSharp4Parser.Boolean_literalContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#keyword.
    def enterKeyword(self, ctx:CSharp4Parser.KeywordContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#keyword.
    def exitKeyword(self, ctx:CSharp4Parser.KeywordContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#class_definition.
    def enterClass_definition(self, ctx:CSharp4Parser.Class_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#class_definition.
    def exitClass_definition(self, ctx:CSharp4Parser.Class_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#struct_definition.
    def enterStruct_definition(self, ctx:CSharp4Parser.Struct_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#struct_definition.
    def exitStruct_definition(self, ctx:CSharp4Parser.Struct_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_definition.
    def enterInterface_definition(self, ctx:CSharp4Parser.Interface_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_definition.
    def exitInterface_definition(self, ctx:CSharp4Parser.Interface_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#enum_definition.
    def enterEnum_definition(self, ctx:CSharp4Parser.Enum_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#enum_definition.
    def exitEnum_definition(self, ctx:CSharp4Parser.Enum_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#delegate_definition.
    def enterDelegate_definition(self, ctx:CSharp4Parser.Delegate_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#delegate_definition.
    def exitDelegate_definition(self, ctx:CSharp4Parser.Delegate_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#event_declaration2.
    def enterEvent_declaration2(self, ctx:CSharp4Parser.Event_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#event_declaration2.
    def exitEvent_declaration2(self, ctx:CSharp4Parser.Event_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#field_declaration2.
    def enterField_declaration2(self, ctx:CSharp4Parser.Field_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#field_declaration2.
    def exitField_declaration2(self, ctx:CSharp4Parser.Field_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#property_declaration2.
    def enterProperty_declaration2(self, ctx:CSharp4Parser.Property_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#property_declaration2.
    def exitProperty_declaration2(self, ctx:CSharp4Parser.Property_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#constant_declaration2.
    def enterConstant_declaration2(self, ctx:CSharp4Parser.Constant_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#constant_declaration2.
    def exitConstant_declaration2(self, ctx:CSharp4Parser.Constant_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#indexer_declaration2.
    def enterIndexer_declaration2(self, ctx:CSharp4Parser.Indexer_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#indexer_declaration2.
    def exitIndexer_declaration2(self, ctx:CSharp4Parser.Indexer_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#destructor_definition.
    def enterDestructor_definition(self, ctx:CSharp4Parser.Destructor_definitionContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#destructor_definition.
    def exitDestructor_definition(self, ctx:CSharp4Parser.Destructor_definitionContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#constructor_declaration2.
    def enterConstructor_declaration2(self, ctx:CSharp4Parser.Constructor_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#constructor_declaration2.
    def exitConstructor_declaration2(self, ctx:CSharp4Parser.Constructor_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_declaration2.
    def enterMethod_declaration2(self, ctx:CSharp4Parser.Method_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_declaration2.
    def exitMethod_declaration2(self, ctx:CSharp4Parser.Method_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_member_name.
    def enterMethod_member_name(self, ctx:CSharp4Parser.Method_member_nameContext):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_member_name.
    def exitMethod_member_name(self, ctx:CSharp4Parser.Method_member_nameContext):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_member_name2.
    def enterMethod_member_name2(self, ctx:CSharp4Parser.Method_member_name2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_member_name2.
    def exitMethod_member_name2(self, ctx:CSharp4Parser.Method_member_name2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#operator_declaration2.
    def enterOperator_declaration2(self, ctx:CSharp4Parser.Operator_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#operator_declaration2.
    def exitOperator_declaration2(self, ctx:CSharp4Parser.Operator_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_method_declaration2.
    def enterInterface_method_declaration2(self, ctx:CSharp4Parser.Interface_method_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_method_declaration2.
    def exitInterface_method_declaration2(self, ctx:CSharp4Parser.Interface_method_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_property_declaration2.
    def enterInterface_property_declaration2(self, ctx:CSharp4Parser.Interface_property_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_property_declaration2.
    def exitInterface_property_declaration2(self, ctx:CSharp4Parser.Interface_property_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_event_declaration2.
    def enterInterface_event_declaration2(self, ctx:CSharp4Parser.Interface_event_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_event_declaration2.
    def exitInterface_event_declaration2(self, ctx:CSharp4Parser.Interface_event_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#interface_indexer_declaration2.
    def enterInterface_indexer_declaration2(self, ctx:CSharp4Parser.Interface_indexer_declaration2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#interface_indexer_declaration2.
    def exitInterface_indexer_declaration2(self, ctx:CSharp4Parser.Interface_indexer_declaration2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#member_access2.
    def enterMember_access2(self, ctx:CSharp4Parser.Member_access2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#member_access2.
    def exitMember_access2(self, ctx:CSharp4Parser.Member_access2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#method_invocation2.
    def enterMethod_invocation2(self, ctx:CSharp4Parser.Method_invocation2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#method_invocation2.
    def exitMethod_invocation2(self, ctx:CSharp4Parser.Method_invocation2Context):
        pass


    # Enter a parse tree produced by CSharp4Parser#object_creation_expression2.
    def enterObject_creation_expression2(self, ctx:CSharp4Parser.Object_creation_expression2Context):
        pass

    # Exit a parse tree produced by CSharp4Parser#object_creation_expression2.
    def exitObject_creation_expression2(self, ctx:CSharp4Parser.Object_creation_expression2Context):
        pass


