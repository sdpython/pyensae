"""
@file
@brief Helpers around language grammar.
This module requires `antlr4 <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
import os
from antlr4 import *


def get_parser_lexer(language):
    """
    returns two classes, a parser and a lexer from antlr4

    @param      language    to analyse
    @return                 Parser, Lexer
    """
    try:
        if language == "R":
            from .RLexer import RLexer
            from .RParser import RParser
            return RParser, RLexer
        elif language == "SQLite":
            from .SQLiteLexer import SQLiteLexer
            from .SQLiteParser import SQLiteParser
            return SQLiteParser, SQLiteLexer
        elif language == "Pig":
            from .PigLexer import PigLexer
            from .PigParser import PigParser
            return PigParser, PigLexer
        else:
            folder = os.path.dirname(__file__)
            if folder == "":
                folder = "."
            files = os.listdir(folder)
            raise ImportError(
                "unable to import parsers for language: " +
                language +
                "\navailable files:\n{0}".format(
                    "\n".join(files)))
    except ImportError as e:
        folder = os.path.dirname(__file__)
        if folder == "":
            folder = "."
        files = os.listdir(folder)
        raise ImportError(
            "unable to import parsers for language: " +
            language +
            "\navailable files:\n{0}".format(
                "\n".join(files))) from e


def parse_code(code, class_parser, class_lexer):
    """
    parse a code and returns a tree

    @param      code                code to parse
    @param      class_parser        parser
    @param      class_lexer         lexer
    @return                         parsed code

    @example(Check the syntax of a script PIG)
    @code
    code = '''
    A = LOAD 'filename.txt' USING PigStorage('\t');
    STORE A INTO 'samefile.txt' ;
    '''

    clparser,cllexer = get_parser_lexer("Pig")
    parser = parse_code(code, clparser, cllexer)
    tree = parser.parse()
    st = get_tree_string(tree, parser, None)
    print(st)
    @endcode
    @endexample
    """
    from antlr4 import CommonTokenStream, InputStream

    if isinstance(code, str):
        # we assume it is a string
        code = InputStream.InputStream(code)

    lexer = class_lexer(code)
    stream = CommonTokenStream(lexer)
    parser = class_parser(stream)
    return parser


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
        super()
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
                ctx.ruleIndex] + ", LT(1)=" + parser._input.LT(1).text
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
                self.parser.ruleNames[
                ctx.ruleIndex] + ", LT(1)=" + parser._input.LT(1).text
        else:
            text = ("    " * self.level) + "- " + \
                ", LT(1)=" + self.parser._input.LT(1).text
        self.buffer.append(text)

    def __str__(self):
        """
        usual
        """
        return "\n".join(self.buffer)


def get_tree_string(tree, parser, format=TreeStringListener):
    """
    returns a string which shows the parsed tree

    @param      tree        from @see fn parse_code
    @param      parser      the parser used to build the tree
    @param      format      None or a class ParseTreeListener
    @return                 string
    """
    if format is None:
        return tree.toStringTree()
    else:
        walker = ParseTreeWalker()
        listen = TreeStringListener(parser)
        walker.walk(listen, tree)
        return str(listen)
