"""
@file
@brief Convert R into Python
"""
from antlr4 import ParseTreeListener, ParseTreeWalker
from .RParser import RParser
from .RLexer import RLexer
from .antlr_grammar_use import parse_code


def r2python(code: str) -> str:
    """
    Converts a R script into Python.

    @param      code        R string
    @return                 Python string
    """
    parser = parse_code(code, RParser, RLexer)
    parsed = parser.parse()
    listen = TreeStringListener(parsed)
    walker = ParseTreeWalker()
    walker.walk(listen, parsed)
    return str(listen)


class TreeStringListener(ParseTreeListener):

    """
    This class is an attempt to run through the tree and convert it into
    a string.
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
        text = ("    " * self.level) + str(node.symbol)
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
        kind = str(type(ctx)).split(
            ".")[-1].strip("'<>").replace("Context", "")
        text = ("    " * self.level) + "+ {0}".format(kind)
        self.buffer.append(text)
        self.level += 1

    def exitEveryRule(self, ctx):
        """
        event
        """
        self.level -= 1
        text = ("    " * self.level) + "- "
        self.buffer.append(text)

    def __str__(self):
        """
        usual
        """
        return "\n".join(self.buffer)
