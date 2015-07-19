"""
@file
@brief Helpers around language grammar.
This module requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
from antlr4 import ParseTreeListener


class TreeStringListener(ParseTreeListener):

    """
    this class is an attempt to run through the tree
    but it is not complete
    """

    def __init__(self, parser):
        """
        constructor

        @param      parser      parser used to parse the code
        """
        ParseTreeListener.__init__(self)
        self.buffer = []
        self.level = 0
        self.parser = parser

    def visitTerminal(self, node):
        """
        event
        """
        text = ("    " * self.level) + "v " + str(node.symbol)
        self.buffer.append(text)

    def visitErrorNode(self, node):
        """
        event
        """
        text = ("    " * self.level) + "error: " + str(node)
        self.buffer.append(text)

    def enterEveryRule(self, ctx):
        """
        event
        """
        if "ruleIndex" in ctx.__dict__:
            text = ("    " * self.level) + "+ " + \
                self.parser.ruleNames[
                ctx.ruleIndex] + ", LT(1)=" + self.parser._input.LT(1).text
        else:
            text = ("    " * self.level) + "+ " + \
                ", LT(1)=" + self.parser._input.LT(1).text
        self.buffer.append(text)
        self.level += 1

    def exitEveryRule(self, ctx):
        """
        event
        """
        self.level -= 1
        if "ruleIndex" in ctx.__dict__:
            text = ("    " * self.level) + "- " + \
                self.parser.ruleNames[ctx.ruleIndex] + \
                ", LT(1)=" + self.parser._input.LT(1).text
        else:
            text = ("    " * self.level) + "- " + \
                ", LT(1)=" + self.parser._input.LT(1).text
        self.buffer.append(text)

    def __str__(self):
        """
        usual
        """
        return "\n".join(self.buffer)
