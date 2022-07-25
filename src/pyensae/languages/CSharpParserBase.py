from antlr4 import *


class CSharpParserBase(Parser):
    def __init__(self, input, output):
        Parser.__init__(self, input, output)

    def IsLocalVariableDeclaration(self):
        # as Test.CSharpParser.Local_variable_declarationContext
        local_var_decl = self.Context
        if local_var_decl is None:
            return True
        local_variable_type = local_var_decl.local_variable_type()
        if local_variable_type is None:
            return True
        if local_variable_type.GetText() == "var":
            return False
        return True
