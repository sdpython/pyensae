# Generated from \SimpleWorkflow.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 41, 274, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        2, 14, 7, 14, 2, 15, 7, 15, 2, 16, 7, 16, 2, 17, 7, 17, 2, 18, 7, 18, 2, 19, 7, 19, 2, 20,
        7, 20, 2, 21, 7, 21, 2, 22, 7, 22, 2, 23, 7, 23, 2, 24, 7, 24, 2, 25, 7, 25, 2, 26, 7, 26,
        2, 27, 7, 27, 2, 28, 7, 28, 2, 29, 7, 29, 2, 30, 7, 30, 2, 31, 7, 31, 1, 0, 5, 0, 66, 8, 0,
        10, 0, 12, 0, 69, 9, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 3, 1, 77, 8, 1, 1, 2, 1, 2, 1, 2,
        1, 3, 1, 3, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 1, 4, 4, 4, 95, 8, 4, 11,
        4, 12, 4, 96, 1, 4, 1, 4, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 4, 5, 107, 8, 5, 11, 5, 12, 5,
        108, 1, 5, 1, 5, 1, 5, 1, 5, 4, 5, 115, 8, 5, 11, 5, 12, 5, 116, 1, 5, 1, 5, 3, 5, 121, 8,
        5, 1, 6, 1, 6, 1, 7, 1, 7, 1, 7, 1, 7, 1, 7, 3, 7, 130, 8, 7, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 1,
        8, 1, 8, 1, 8, 1, 8, 1, 8, 1, 8, 3, 8, 143, 8, 8, 1, 9, 1, 9, 1, 9, 3, 9, 148, 8, 9, 1, 9, 1,
        9, 5, 9, 152, 8, 9, 10, 9, 12, 9, 155, 9, 9, 1, 9, 1, 9, 1, 10, 1, 10, 1, 11, 1, 11, 1, 12,
        1, 12, 1, 13, 1, 13, 1, 13, 1, 14, 1, 14, 1, 14, 3, 14, 171, 8, 14, 1, 15, 1, 15, 1, 15,
        1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 1, 15, 3, 15, 185, 8, 15, 1, 16,
        1, 16, 1, 16, 3, 16, 190, 8, 16, 1, 17, 1, 17, 1, 17, 3, 17, 195, 8, 17, 1, 18, 1, 18, 1,
        18, 1, 18, 1, 19, 1, 19, 1, 19, 1, 19, 1, 20, 1, 20, 1, 20, 1, 20, 1, 20, 1, 21, 1, 21, 1,
        22, 3, 22, 213, 8, 22, 1, 22, 1, 22, 5, 22, 217, 8, 22, 10, 22, 12, 22, 220, 9, 22, 1,
        23, 1, 23, 1, 23, 1, 23, 1, 24, 1, 24, 1, 25, 1, 25, 1, 26, 1, 26, 1, 26, 1, 26, 1, 27, 1,
        27, 1, 27, 1, 27, 1, 28, 1, 28, 1, 28, 3, 28, 241, 8, 28, 1, 29, 1, 29, 1, 30, 3, 30, 246,
        8, 30, 1, 30, 1, 30, 1, 31, 3, 31, 251, 8, 31, 1, 31, 1, 31, 1, 31, 1, 31, 1, 31, 3, 31,
        258, 8, 31, 1, 31, 3, 31, 261, 8, 31, 1, 31, 3, 31, 264, 8, 31, 1, 31, 1, 31, 1, 31, 3,
        31, 269, 8, 31, 1, 31, 3, 31, 272, 8, 31, 1, 31, 0, 0, 32, 0, 2, 4, 6, 8, 10, 12, 14, 16,
        18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60,
        62, 0, 4, 1, 0, 13, 25, 2, 0, 13, 14, 26, 26, 1, 0, 28, 29, 2, 0, 35, 35, 37, 37, 273, 0,
        67, 1, 0, 0, 0, 2, 76, 1, 0, 0, 0, 4, 78, 1, 0, 0, 0, 6, 81, 1, 0, 0, 0, 8, 86, 1, 0, 0, 0, 10,
        100, 1, 0, 0, 0, 12, 122, 1, 0, 0, 0, 14, 129, 1, 0, 0, 0, 16, 142, 1, 0, 0, 0, 18, 144,
        1, 0, 0, 0, 20, 158, 1, 0, 0, 0, 22, 160, 1, 0, 0, 0, 24, 162, 1, 0, 0, 0, 26, 164, 1, 0,
        0, 0, 28, 170, 1, 0, 0, 0, 30, 184, 1, 0, 0, 0, 32, 186, 1, 0, 0, 0, 34, 191, 1, 0, 0, 0,
        36, 196, 1, 0, 0, 0, 38, 200, 1, 0, 0, 0, 40, 204, 1, 0, 0, 0, 42, 209, 1, 0, 0, 0, 44, 212,
        1, 0, 0, 0, 46, 221, 1, 0, 0, 0, 48, 225, 1, 0, 0, 0, 50, 227, 1, 0, 0, 0, 52, 229, 1, 0,
        0, 0, 54, 233, 1, 0, 0, 0, 56, 240, 1, 0, 0, 0, 58, 242, 1, 0, 0, 0, 60, 245, 1, 0, 0, 0,
        62, 271, 1, 0, 0, 0, 64, 66, 3, 2, 1, 0, 65, 64, 1, 0, 0, 0, 66, 69, 1, 0, 0, 0, 67, 65, 1,
        0, 0, 0, 67, 68, 1, 0, 0, 0, 68, 70, 1, 0, 0, 0, 69, 67, 1, 0, 0, 0, 70, 71, 5, 0, 0, 1, 71,
        1, 1, 0, 0, 0, 72, 77, 3, 10, 5, 0, 73, 77, 3, 8, 4, 0, 74, 77, 3, 4, 2, 0, 75, 77, 3, 26,
        13, 0, 76, 72, 1, 0, 0, 0, 76, 73, 1, 0, 0, 0, 76, 74, 1, 0, 0, 0, 76, 75, 1, 0, 0, 0, 77,
        3, 1, 0, 0, 0, 78, 79, 3, 6, 3, 0, 79, 80, 5, 1, 0, 0, 80, 5, 1, 0, 0, 0, 81, 82, 5, 2, 0, 0,
        82, 83, 3, 20, 10, 0, 83, 84, 5, 3, 0, 0, 84, 85, 3, 14, 7, 0, 85, 7, 1, 0, 0, 0, 86, 87,
        5, 4, 0, 0, 87, 88, 5, 5, 0, 0, 88, 89, 3, 20, 10, 0, 89, 90, 5, 6, 0, 0, 90, 91, 3, 18, 9,
        0, 91, 92, 5, 7, 0, 0, 92, 94, 5, 8, 0, 0, 93, 95, 3, 2, 1, 0, 94, 93, 1, 0, 0, 0, 95, 96,
        1, 0, 0, 0, 96, 94, 1, 0, 0, 0, 96, 97, 1, 0, 0, 0, 97, 98, 1, 0, 0, 0, 98, 99, 5, 9, 0, 0,
        99, 9, 1, 0, 0, 0, 100, 101, 5, 10, 0, 0, 101, 102, 5, 5, 0, 0, 102, 103, 3, 14, 7, 0, 103,
        104, 5, 7, 0, 0, 104, 106, 5, 8, 0, 0, 105, 107, 3, 2, 1, 0, 106, 105, 1, 0, 0, 0, 107,
        108, 1, 0, 0, 0, 108, 106, 1, 0, 0, 0, 108, 109, 1, 0, 0, 0, 109, 110, 1, 0, 0, 0, 110,
        120, 5, 9, 0, 0, 111, 112, 5, 11, 0, 0, 112, 114, 5, 8, 0, 0, 113, 115, 3, 2, 1, 0, 114,
        113, 1, 0, 0, 0, 115, 116, 1, 0, 0, 0, 116, 114, 1, 0, 0, 0, 116, 117, 1, 0, 0, 0, 117,
        118, 1, 0, 0, 0, 118, 119, 5, 9, 0, 0, 119, 121, 1, 0, 0, 0, 120, 111, 1, 0, 0, 0, 120,
        121, 1, 0, 0, 0, 121, 11, 1, 0, 0, 0, 122, 123, 5, 35, 0, 0, 123, 13, 1, 0, 0, 0, 124, 130,
        3, 16, 8, 0, 125, 126, 3, 16, 8, 0, 126, 127, 3, 22, 11, 0, 127, 128, 3, 14, 7, 0, 128,
        130, 1, 0, 0, 0, 129, 124, 1, 0, 0, 0, 129, 125, 1, 0, 0, 0, 130, 15, 1, 0, 0, 0, 131, 143,
        3, 56, 28, 0, 132, 143, 3, 20, 10, 0, 133, 143, 3, 32, 16, 0, 134, 135, 5, 5, 0, 0, 135,
        136, 3, 14, 7, 0, 136, 137, 5, 7, 0, 0, 137, 143, 1, 0, 0, 0, 138, 139, 3, 24, 12, 0, 139,
        140, 3, 16, 8, 0, 140, 143, 1, 0, 0, 0, 141, 143, 3, 18, 9, 0, 142, 131, 1, 0, 0, 0, 142,
        132, 1, 0, 0, 0, 142, 133, 1, 0, 0, 0, 142, 134, 1, 0, 0, 0, 142, 138, 1, 0, 0, 0, 142,
        141, 1, 0, 0, 0, 143, 17, 1, 0, 0, 0, 144, 145, 3, 12, 6, 0, 145, 147, 5, 5, 0, 0, 146,
        148, 3, 14, 7, 0, 147, 146, 1, 0, 0, 0, 147, 148, 1, 0, 0, 0, 148, 153, 1, 0, 0, 0, 149,
        150, 5, 12, 0, 0, 150, 152, 3, 14, 7, 0, 151, 149, 1, 0, 0, 0, 152, 155, 1, 0, 0, 0, 153,
        151, 1, 0, 0, 0, 153, 154, 1, 0, 0, 0, 154, 156, 1, 0, 0, 0, 155, 153, 1, 0, 0, 0, 156,
        157, 5, 7, 0, 0, 157, 19, 1, 0, 0, 0, 158, 159, 5, 35, 0, 0, 159, 21, 1, 0, 0, 0, 160, 161,
        7, 0, 0, 0, 161, 23, 1, 0, 0, 0, 162, 163, 7, 1, 0, 0, 163, 25, 1, 0, 0, 0, 164, 165, 3,
        28, 14, 0, 165, 166, 5, 1, 0, 0, 166, 27, 1, 0, 0, 0, 167, 171, 3, 30, 15, 0, 168, 171,
        3, 36, 18, 0, 169, 171, 3, 38, 19, 0, 170, 167, 1, 0, 0, 0, 170, 168, 1, 0, 0, 0, 170,
        169, 1, 0, 0, 0, 171, 29, 1, 0, 0, 0, 172, 173, 5, 27, 0, 0, 173, 174, 3, 32, 16, 0, 174,
        175, 7, 2, 0, 0, 175, 176, 3, 34, 17, 0, 176, 185, 1, 0, 0, 0, 177, 178, 5, 27, 0, 0, 178,
        179, 5, 5, 0, 0, 179, 180, 3, 32, 16, 0, 180, 181, 5, 12, 0, 0, 181, 182, 3, 34, 17, 0,
        182, 183, 5, 7, 0, 0, 183, 185, 1, 0, 0, 0, 184, 172, 1, 0, 0, 0, 184, 177, 1, 0, 0, 0,
        185, 31, 1, 0, 0, 0, 186, 189, 3, 42, 21, 0, 187, 188, 5, 30, 0, 0, 188, 190, 3, 50, 25,
        0, 189, 187, 1, 0, 0, 0, 189, 190, 1, 0, 0, 0, 190, 33, 1, 0, 0, 0, 191, 194, 3, 42, 21,
        0, 192, 193, 5, 30, 0, 0, 193, 195, 3, 50, 25, 0, 194, 192, 1, 0, 0, 0, 194, 195, 1, 0,
        0, 0, 195, 35, 1, 0, 0, 0, 196, 197, 3, 42, 21, 0, 197, 198, 5, 3, 0, 0, 198, 199, 3, 54,
        27, 0, 199, 37, 1, 0, 0, 0, 200, 201, 3, 42, 21, 0, 201, 202, 5, 3, 0, 0, 202, 203, 3,
        40, 20, 0, 203, 39, 1, 0, 0, 0, 204, 205, 3, 52, 26, 0, 205, 206, 5, 5, 0, 0, 206, 207,
        3, 44, 22, 0, 207, 208, 5, 7, 0, 0, 208, 41, 1, 0, 0, 0, 209, 210, 5, 35, 0, 0, 210, 43,
        1, 0, 0, 0, 211, 213, 3, 46, 23, 0, 212, 211, 1, 0, 0, 0, 212, 213, 1, 0, 0, 0, 213, 218,
        1, 0, 0, 0, 214, 215, 5, 12, 0, 0, 215, 217, 3, 46, 23, 0, 216, 214, 1, 0, 0, 0, 217, 220,
        1, 0, 0, 0, 218, 216, 1, 0, 0, 0, 218, 219, 1, 0, 0, 0, 219, 45, 1, 0, 0, 0, 220, 218, 1,
        0, 0, 0, 221, 222, 3, 48, 24, 0, 222, 223, 5, 3, 0, 0, 223, 224, 3, 14, 7, 0, 224, 47,
        1, 0, 0, 0, 225, 226, 5, 35, 0, 0, 226, 49, 1, 0, 0, 0, 227, 228, 5, 35, 0, 0, 228, 51,
        1, 0, 0, 0, 229, 230, 5, 31, 0, 0, 230, 231, 5, 30, 0, 0, 231, 232, 7, 3, 0, 0, 232, 53,
        1, 0, 0, 0, 233, 234, 5, 32, 0, 0, 234, 235, 5, 30, 0, 0, 235, 236, 7, 3, 0, 0, 236, 55,
        1, 0, 0, 0, 237, 241, 3, 60, 30, 0, 238, 241, 3, 62, 31, 0, 239, 241, 3, 58, 29, 0, 240,
        237, 1, 0, 0, 0, 240, 238, 1, 0, 0, 0, 240, 239, 1, 0, 0, 0, 241, 57, 1, 0, 0, 0, 242, 243,
        5, 37, 0, 0, 243, 59, 1, 0, 0, 0, 244, 246, 5, 36, 0, 0, 245, 244, 1, 0, 0, 0, 245, 246,
        1, 0, 0, 0, 246, 247, 1, 0, 0, 0, 247, 248, 5, 34, 0, 0, 248, 61, 1, 0, 0, 0, 249, 251,
        5, 36, 0, 0, 250, 249, 1, 0, 0, 0, 250, 251, 1, 0, 0, 0, 251, 252, 1, 0, 0, 0, 252, 253,
        5, 34, 0, 0, 253, 254, 5, 30, 0, 0, 254, 260, 5, 34, 0, 0, 255, 257, 5, 33, 0, 0, 256,
        258, 5, 36, 0, 0, 257, 256, 1, 0, 0, 0, 257, 258, 1, 0, 0, 0, 258, 259, 1, 0, 0, 0, 259,
        261, 5, 34, 0, 0, 260, 255, 1, 0, 0, 0, 260, 261, 1, 0, 0, 0, 261, 272, 1, 0, 0, 0, 262,
        264, 5, 36, 0, 0, 263, 262, 1, 0, 0, 0, 263, 264, 1, 0, 0, 0, 264, 265, 1, 0, 0, 0, 265,
        266, 5, 34, 0, 0, 266, 268, 5, 33, 0, 0, 267, 269, 5, 36, 0, 0, 268, 267, 1, 0, 0, 0, 268,
        269, 1, 0, 0, 0, 269, 270, 1, 0, 0, 0, 270, 272, 5, 34, 0, 0, 271, 250, 1, 0, 0, 0, 271,
        263, 1, 0, 0, 0, 272, 63, 1, 0, 0, 0, 24, 67, 76, 96, 108, 116, 120, 129, 142, 147, 153,
        170, 184, 189, 194, 212, 218, 240, 245, 250, 257, 260, 263, 268, 271
    ]


class SimpleWorkflowParser (Parser):

    grammarFileName = "SimpleWorkflow.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "';'", "'set'", "'='", "'for'", "'('",
                    "'in'", "')'", "'{'", "'}'", "'if'", "'else'", "','",
                    "'+'", "'-'", "'*'", "'/'", "'%'", "'&&'", "'||'",
                    "'=='", "'!='", "'<='", "'>='", "'>'", "'<'", "'!'",
                    "'connect'", "'to'", "'->'", "'.'", "'flowmodule'",
                    "'flowdata'", "'e'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "Digits", "Identifier",
                     "Sign", "STRING", "STRING_DOUBLE_QUOTE", "STRING_QUOTE",
                     "LINE_COMMENT", "WS"]

    RULE_parse = 0
    RULE_final_stmt = 1
    RULE_affectation_stmt_comma = 2
    RULE_affectation_stmt = 3
    RULE_for_stmt = 4
    RULE_if_stmt = 5
    RULE_evaluation_function = 6
    RULE_expression = 7
    RULE_expression_no_binary = 8
    RULE_function_call = 9
    RULE_variable_name = 10
    RULE_binary_operator = 11
    RULE_unary_operator = 12
    RULE_stmt_comma = 13
    RULE_stmt = 14
    RULE_connect_stmt = 15
    RULE_data_or_module_output = 16
    RULE_module_input = 17
    RULE_data_stmt = 18
    RULE_module_stmt = 19
    RULE_module_call = 20
    RULE_element_name = 21
    RULE_list_param_affectation = 22
    RULE_param_affectation = 23
    RULE_param_name = 24
    RULE_inout_name = 25
    RULE_module_name = 26
    RULE_data_name = 27
    RULE_constant = 28
    RULE_string_literal = 29
    RULE_integer_number = 30
    RULE_real_number = 31

    ruleNames = ["parse", "final_stmt", "affectation_stmt_comma", "affectation_stmt",
                 "for_stmt", "if_stmt", "evaluation_function", "expression",
                 "expression_no_binary", "function_call", "variable_name",
                 "binary_operator", "unary_operator", "stmt_comma", "stmt",
                 "connect_stmt", "data_or_module_output", "module_input",
                 "data_stmt", "module_stmt", "module_call", "element_name",
                 "list_param_affectation", "param_affectation", "param_name",
                 "inout_name", "module_name", "data_name", "constant",
                 "string_literal", "integer_number", "real_number"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    T__19 = 20
    T__20 = 21
    T__21 = 22
    T__22 = 23
    T__23 = 24
    T__24 = 25
    T__25 = 26
    T__26 = 27
    T__27 = 28
    T__28 = 29
    T__29 = 30
    T__30 = 31
    T__31 = 32
    T__32 = 33
    Digits = 34
    Identifier = 35
    Sign = 36
    STRING = 37
    STRING_DOUBLE_QUOTE = 38
    STRING_QUOTE = 39
    LINE_COMMENT = 40
    WS = 41

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ParseContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleWorkflowParser.EOF, 0)

        def final_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_parse

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParse"):
                listener.enterParse(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParse"):
                listener.exitParse(self)

    def parse(self):

        localctx = SimpleWorkflowParser.ParseContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__9) | (1 << SimpleWorkflowParser.T__26) | (1 << SimpleWorkflowParser.Identifier))) != 0):
                self.state = 64
                self.final_stmt()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 70
            self.match(SimpleWorkflowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Final_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.If_stmtContext, 0)

        def for_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.For_stmtContext, 0)

        def affectation_stmt_comma(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Affectation_stmt_commaContext, 0)

        def stmt_comma(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Stmt_commaContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_final_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFinal_stmt"):
                listener.enterFinal_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFinal_stmt"):
                listener.exitFinal_stmt(self)

    def final_stmt(self):

        localctx = SimpleWorkflowParser.Final_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_final_stmt)
        try:
            self.state = 76
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [SimpleWorkflowParser.T__9]:
                self.enterOuterAlt(localctx, 1)
                self.state = 72
                self.if_stmt()
                pass
            elif token in [SimpleWorkflowParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.for_stmt()
                pass
            elif token in [SimpleWorkflowParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 74
                self.affectation_stmt_comma()
                pass
            elif token in [SimpleWorkflowParser.T__26, SimpleWorkflowParser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 75
                self.stmt_comma()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Affectation_stmt_commaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def affectation_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Affectation_stmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_affectation_stmt_comma

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAffectation_stmt_comma"):
                listener.enterAffectation_stmt_comma(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAffectation_stmt_comma"):
                listener.exitAffectation_stmt_comma(self)

    def affectation_stmt_comma(self):

        localctx = SimpleWorkflowParser.Affectation_stmt_commaContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_affectation_stmt_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 78
            self.affectation_stmt()
            self.state = 79
            self.match(SimpleWorkflowParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Affectation_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Variable_nameContext, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_affectation_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAffectation_stmt"):
                listener.enterAffectation_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAffectation_stmt"):
                listener.exitAffectation_stmt(self)

    def affectation_stmt(self):

        localctx = SimpleWorkflowParser.Affectation_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_affectation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 81
            self.match(SimpleWorkflowParser.T__1)
            self.state = 82
            self.variable_name()
            self.state = 83
            self.match(SimpleWorkflowParser.T__2)
            self.state = 84
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Variable_nameContext, 0)

        def function_call(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Function_callContext, 0)

        def final_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_for_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFor_stmt"):
                listener.enterFor_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFor_stmt"):
                listener.exitFor_stmt(self)

    def for_stmt(self):

        localctx = SimpleWorkflowParser.For_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_for_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SimpleWorkflowParser.T__3)
            self.state = 87
            self.match(SimpleWorkflowParser.T__4)
            self.state = 88
            self.variable_name()
            self.state = 89
            self.match(SimpleWorkflowParser.T__5)
            self.state = 90
            self.function_call()
            self.state = 91
            self.match(SimpleWorkflowParser.T__6)
            self.state = 92
            self.match(SimpleWorkflowParser.T__7)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.final_stmt()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__9) | (1 << SimpleWorkflowParser.T__26) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                    break

            self.state = 98
            self.match(SimpleWorkflowParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, 0)

        def final_stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_if_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIf_stmt"):
                listener.enterIf_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIf_stmt"):
                listener.exitIf_stmt(self)

    def if_stmt(self):

        localctx = SimpleWorkflowParser.If_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_if_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.match(SimpleWorkflowParser.T__9)
            self.state = 101
            self.match(SimpleWorkflowParser.T__4)
            self.state = 102
            self.expression()
            self.state = 103
            self.match(SimpleWorkflowParser.T__6)
            self.state = 104
            self.match(SimpleWorkflowParser.T__7)
            self.state = 106
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 105
                self.final_stmt()
                self.state = 108
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__9) | (1 << SimpleWorkflowParser.T__26) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                    break

            self.state = 110
            self.match(SimpleWorkflowParser.T__8)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__10:
                self.state = 111
                self.match(SimpleWorkflowParser.T__10)
                self.state = 112
                self.match(SimpleWorkflowParser.T__7)
                self.state = 114
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 113
                    self.final_stmt()
                    self.state = 116
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__9) | (1 << SimpleWorkflowParser.T__26) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                        break

                self.state = 118
                self.match(SimpleWorkflowParser.T__8)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Evaluation_functionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_evaluation_function

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEvaluation_function"):
                listener.enterEvaluation_function(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEvaluation_function"):
                listener.exitEvaluation_function(self)

    def evaluation_function(self):

        localctx = SimpleWorkflowParser.Evaluation_functionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_evaluation_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 122
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression_no_binary(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Expression_no_binaryContext, 0)

        def binary_operator(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Binary_operatorContext, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_expression

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression"):
                listener.enterExpression(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression"):
                listener.exitExpression(self)

    def expression(self):

        localctx = SimpleWorkflowParser.ExpressionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expression)
        try:
            self.state = 129
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 6, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                self.expression_no_binary()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 125
                self.expression_no_binary()
                self.state = 126
                self.binary_operator()
                self.state = 127
                self.expression()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Expression_no_binaryContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def constant(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ConstantContext, 0)

        def variable_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Variable_nameContext, 0)

        def data_or_module_output(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_outputContext, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, 0)

        def unary_operator(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Unary_operatorContext, 0)

        def expression_no_binary(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Expression_no_binaryContext, 0)

        def function_call(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Function_callContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_expression_no_binary

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterExpression_no_binary"):
                listener.enterExpression_no_binary(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitExpression_no_binary"):
                listener.exitExpression_no_binary(self)

    def expression_no_binary(self):

        localctx = SimpleWorkflowParser.Expression_no_binaryContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_expression_no_binary)
        try:
            self.state = 142
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 7, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.constant()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 132
                self.variable_name()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 133
                self.data_or_module_output()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 134
                self.match(SimpleWorkflowParser.T__4)
                self.state = 135
                self.expression()
                self.state = 136
                self.match(SimpleWorkflowParser.T__6)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 138
                self.unary_operator()
                self.state = 139
                self.expression_no_binary()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 141
                self.function_call()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evaluation_function(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Evaluation_functionContext, 0)

        def expression(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_function_call

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterFunction_call"):
                listener.enterFunction_call(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitFunction_call"):
                listener.exitFunction_call(self)

    def function_call(self):

        localctx = SimpleWorkflowParser.Function_callContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_call)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.evaluation_function()
            self.state = 145
            self.match(SimpleWorkflowParser.T__4)
            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__4) | (1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.T__13) | (1 << SimpleWorkflowParser.T__25) | (1 << SimpleWorkflowParser.Digits) | (1 << SimpleWorkflowParser.Identifier) | (1 << SimpleWorkflowParser.Sign) | (1 << SimpleWorkflowParser.STRING))) != 0):
                self.state = 146
                self.expression()

            self.state = 153
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SimpleWorkflowParser.T__11:
                self.state = 149
                self.match(SimpleWorkflowParser.T__11)
                self.state = 150
                self.expression()
                self.state = 155
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 156
            self.match(SimpleWorkflowParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_variable_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterVariable_name"):
                listener.enterVariable_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitVariable_name"):
                listener.exitVariable_name(self)

    def variable_name(self):

        localctx = SimpleWorkflowParser.Variable_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Binary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_binary_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterBinary_operator"):
                listener.enterBinary_operator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitBinary_operator"):
                listener.exitBinary_operator(self)

    def binary_operator(self):

        localctx = SimpleWorkflowParser.Binary_operatorContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_binary_operator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.T__13) | (1 << SimpleWorkflowParser.T__14) | (1 << SimpleWorkflowParser.T__15) | (1 << SimpleWorkflowParser.T__16) | (1 << SimpleWorkflowParser.T__17) | (1 << SimpleWorkflowParser.T__18) | (1 << SimpleWorkflowParser.T__19) | (1 << SimpleWorkflowParser.T__20) | (1 << SimpleWorkflowParser.T__21) | (1 << SimpleWorkflowParser.T__22) | (1 << SimpleWorkflowParser.T__23) | (1 << SimpleWorkflowParser.T__24))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_operatorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_unary_operator

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterUnary_operator"):
                listener.enterUnary_operator(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitUnary_operator"):
                listener.exitUnary_operator(self)

    def unary_operator(self):

        localctx = SimpleWorkflowParser.Unary_operatorContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_unary_operator)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 162
            _la = self._input.LA(1)
            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.T__13) | (1 << SimpleWorkflowParser.T__25))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stmt_commaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.StmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_stmt_comma

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt_comma"):
                listener.enterStmt_comma(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt_comma"):
                listener.exitStmt_comma(self)

    def stmt_comma(self):

        localctx = SimpleWorkflowParser.Stmt_commaContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_stmt_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self.stmt()
            self.state = 165
            self.match(SimpleWorkflowParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connect_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Connect_stmtContext, 0)

        def data_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_stmtContext, 0)

        def module_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_stmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

    def stmt(self):

        localctx = SimpleWorkflowParser.StmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_stmt)
        try:
            self.state = 170
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 167
                self.connect_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 168
                self.data_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 169
                self.module_stmt()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Connect_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_or_module_output(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_outputContext, 0)

        def module_input(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_inputContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_connect_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConnect_stmt"):
                listener.enterConnect_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConnect_stmt"):
                listener.exitConnect_stmt(self)

    def connect_stmt(self):

        localctx = SimpleWorkflowParser.Connect_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_connect_stmt)
        self._la = 0  # Token type
        try:
            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 11, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 172
                self.match(SimpleWorkflowParser.T__26)
                self.state = 173
                self.data_or_module_output()
                self.state = 174
                _la = self._input.LA(1)
                if not (_la == SimpleWorkflowParser.T__27 or _la == SimpleWorkflowParser.T__28):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 175
                self.module_input()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.match(SimpleWorkflowParser.T__26)
                self.state = 178
                self.match(SimpleWorkflowParser.T__4)
                self.state = 179
                self.data_or_module_output()
                self.state = 180
                self.match(SimpleWorkflowParser.T__11)
                self.state = 181
                self.module_input()
                self.state = 182
                self.match(SimpleWorkflowParser.T__6)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_or_module_outputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def inout_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Inout_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_or_module_output

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterData_or_module_output"):
                listener.enterData_or_module_output(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitData_or_module_output"):
                listener.exitData_or_module_output(self)

    def data_or_module_output(self):

        localctx = SimpleWorkflowParser.Data_or_module_outputContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_data_or_module_output)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.element_name()
            self.state = 189
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__29:
                self.state = 187
                self.match(SimpleWorkflowParser.T__29)
                self.state = 188
                self.inout_name()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_inputContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def inout_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Inout_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_input

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModule_input"):
                listener.enterModule_input(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModule_input"):
                listener.exitModule_input(self)

    def module_input(self):

        localctx = SimpleWorkflowParser.Module_inputContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_module_input)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            self.element_name()
            self.state = 194
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__29:
                self.state = 192
                self.match(SimpleWorkflowParser.T__29)
                self.state = 193
                self.inout_name()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def data_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterData_stmt"):
                listener.enterData_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitData_stmt"):
                listener.exitData_stmt(self)

    def data_stmt(self):

        localctx = SimpleWorkflowParser.Data_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_data_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 196
            self.element_name()
            self.state = 197
            self.match(SimpleWorkflowParser.T__2)
            self.state = 198
            self.data_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def module_call(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_callContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModule_stmt"):
                listener.enterModule_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModule_stmt"):
                listener.exitModule_stmt(self)

    def module_stmt(self):

        localctx = SimpleWorkflowParser.Module_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_module_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 200
            self.element_name()
            self.state = 201
            self.match(SimpleWorkflowParser.T__2)
            self.state = 202
            self.module_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_nameContext, 0)

        def list_param_affectation(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.List_param_affectationContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_call

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModule_call"):
                listener.enterModule_call(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModule_call"):
                listener.exitModule_call(self)

    def module_call(self):

        localctx = SimpleWorkflowParser.Module_callContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_module_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.module_name()
            self.state = 205
            self.match(SimpleWorkflowParser.T__4)
            self.state = 206
            self.list_param_affectation()
            self.state = 207
            self.match(SimpleWorkflowParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Element_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_element_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterElement_name"):
                listener.enterElement_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitElement_name"):
                listener.exitElement_name(self)

    def element_name(self):

        localctx = SimpleWorkflowParser.Element_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_element_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 209
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_param_affectationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_affectation(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Param_affectationContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Param_affectationContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_list_param_affectation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterList_param_affectation"):
                listener.enterList_param_affectation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitList_param_affectation"):
                listener.exitList_param_affectation(self)

    def list_param_affectation(self):

        localctx = SimpleWorkflowParser.List_param_affectationContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_list_param_affectation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.Identifier:
                self.state = 211
                self.param_affectation()

            self.state = 218
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SimpleWorkflowParser.T__11:
                self.state = 214
                self.match(SimpleWorkflowParser.T__11)
                self.state = 215
                self.param_affectation()
                self.state = 220
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_affectationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Param_nameContext, 0)

        def expression(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ExpressionContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_param_affectation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParam_affectation"):
                listener.enterParam_affectation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParam_affectation"):
                listener.exitParam_affectation(self)

    def param_affectation(self):

        localctx = SimpleWorkflowParser.Param_affectationContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param_affectation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.param_name()
            self.state = 222
            self.match(SimpleWorkflowParser.T__2)
            self.state = 223
            self.expression()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_param_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterParam_name"):
                listener.enterParam_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitParam_name"):
                listener.exitParam_name(self)

    def param_name(self):

        localctx = SimpleWorkflowParser.Param_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_param_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inout_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_inout_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInout_name"):
                listener.enterInout_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInout_name"):
                listener.exitInout_name(self)

    def inout_name(self):

        localctx = SimpleWorkflowParser.Inout_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_inout_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterModule_name"):
                listener.enterModule_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitModule_name"):
                listener.exitModule_name(self)

    def module_name(self):

        localctx = SimpleWorkflowParser.Module_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_module_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 229
            self.match(SimpleWorkflowParser.T__30)
            self.state = 230
            self.match(SimpleWorkflowParser.T__29)
            self.state = 231
            _la = self._input.LA(1)
            if not (_la == SimpleWorkflowParser.Identifier or _la == SimpleWorkflowParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_name

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterData_name"):
                listener.enterData_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitData_name"):
                listener.exitData_name(self)

    def data_name(self):

        localctx = SimpleWorkflowParser.Data_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_data_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 233
            self.match(SimpleWorkflowParser.T__31)
            self.state = 234
            self.match(SimpleWorkflowParser.T__29)
            self.state = 235
            _la = self._input.LA(1)
            if not (_la == SimpleWorkflowParser.Identifier or _la == SimpleWorkflowParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_number(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Integer_numberContext, 0)

        def real_number(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Real_numberContext, 0)

        def string_literal(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.String_literalContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_constant

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterConstant"):
                listener.enterConstant(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitConstant"):
                listener.exitConstant(self)

    def constant(self):

        localctx = SimpleWorkflowParser.ConstantContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_constant)
        try:
            self.state = 240
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 16, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 237
                self.integer_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 238
                self.real_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 239
                self.string_literal()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_literalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_string_literal

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterString_literal"):
                listener.enterString_literal(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitString_literal"):
                listener.exitString_literal(self)

    def string_literal(self):

        localctx = SimpleWorkflowParser.String_literalContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 242
            self.match(SimpleWorkflowParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Integer_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self):
            return self.getToken(SimpleWorkflowParser.Digits, 0)

        def Sign(self):
            return self.getToken(SimpleWorkflowParser.Sign, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_integer_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterInteger_number"):
                listener.enterInteger_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitInteger_number"):
                listener.exitInteger_number(self)

    def integer_number(self):

        localctx = SimpleWorkflowParser.Integer_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_integer_number)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.Sign:
                self.state = 244
                self.match(SimpleWorkflowParser.Sign)

            self.state = 247
            self.match(SimpleWorkflowParser.Digits)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Real_numberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self, i: int = None):
            if i is None:
                return self.getTokens(SimpleWorkflowParser.Digits)
            else:
                return self.getToken(SimpleWorkflowParser.Digits, i)

        def Sign(self, i: int = None):
            if i is None:
                return self.getTokens(SimpleWorkflowParser.Sign)
            else:
                return self.getToken(SimpleWorkflowParser.Sign, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_real_number

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterReal_number"):
                listener.enterReal_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitReal_number"):
                listener.exitReal_number(self)

    def real_number(self):

        localctx = SimpleWorkflowParser.Real_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_real_number)
        self._la = 0  # Token type
        try:
            self.state = 271
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 23, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 250
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 249
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 252
                self.match(SimpleWorkflowParser.Digits)
                self.state = 253
                self.match(SimpleWorkflowParser.T__29)
                self.state = 254
                self.match(SimpleWorkflowParser.Digits)
                self.state = 260
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.T__32:
                    self.state = 255
                    self.match(SimpleWorkflowParser.T__32)
                    self.state = 257
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la == SimpleWorkflowParser.Sign:
                        self.state = 256
                        self.match(SimpleWorkflowParser.Sign)

                    self.state = 259
                    self.match(SimpleWorkflowParser.Digits)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 263
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 262
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 265
                self.match(SimpleWorkflowParser.Digits)
                self.state = 266
                self.match(SimpleWorkflowParser.T__32)
                self.state = 268
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 267
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 270
                self.match(SimpleWorkflowParser.Digits)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
