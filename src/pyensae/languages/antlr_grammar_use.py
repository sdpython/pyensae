"""
@file
@brief Use grammar
This module requires `antlr4-python3-runtime <https://pypi.python.org/pypi/antlr4-python3-runtime/>`_.
"""
import os
from antlr4 import ParseTreeWalker, CommonTokenStream, InputStream
from .tree_string_listener import TreeStringListener
from .tree_graph_listener import TreeGraphListener


def get_parser_lexer(language):
    """
    Returns two classes, a parser and a lexer from :epkg:`antlr4`.

    @param      language    to analyse
    @return                 Parser, Lexer
    """
    try:
        if language == "C#" or language == "CSharp":
            language = "CSharp4"

        if language == "R":
            from .RLexer import RLexer
            from .RParser import RParser
            return RParser, RLexer
        elif language == "CSharp4":
            from .CSharp4Lexer import CSharp4Lexer
            from .CSharp4Parser import CSharp4Parser
            return CSharp4Parser, CSharp4Lexer
        elif language == "SQLite":
            from .SQLiteLexer import SQLiteLexer
            from .SQLiteParser import SQLiteParser
            return SQLiteParser, SQLiteLexer
        elif language == "DOT":
            from .DOTLexer import DOTLexer
            from .DOTParser import DOTParser
            return DOTParser, DOTLexer
        elif language == "Pig":
            raise ImportError("Pig is not available yet")
            # from .PigLexer import PigLexer
            # from .PigParser import PigParser
            # return PigParser, PigLexer
        elif language == "Python3":
            from .Python3Lexer import Python3Lexer
            from .Python3Parser import Python3Parser
            return Python3Parser, Python3Lexer
        elif language == "SimpleWorkflow":
            from .SimpleWorkflowLexer import SimpleWorkflowLexer
            from .SimpleWorkflowParser import SimpleWorkflowParser
            return SimpleWorkflowParser, SimpleWorkflowLexer
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

    .. exref::
        :title: Check the syntax of a script PIG

        ::

            code = '''
            A = LOAD 'filename.txt' USING PigStorage('\t');
            STORE A INTO 'samefile.txt' ;
            '''

            clparser,cllexer = get_parser_lexer("Pig")
            parser = parse_code(code, clparser, cllexer)
            tree = parser.parse()
            st = get_tree_string(tree, parser, None)
            print(st)
    """
    if isinstance(code, str):
        # we assume it is a string
        code = InputStream(code)

    lexer = class_lexer(code)
    stream = CommonTokenStream(lexer)
    parser = class_parser(stream)
    return parser


def get_tree_string(tree, parser, format=TreeStringListener):
    """
    returns a string which shows the parsed tree

    @param      tree        from @see fn parse_code
    @param      parser      the parser used to build the tree, output of @see fn parse_code
    @param      format      None or a class `ParseTreeListener <https://github.com/antlr/antlr4-python3/blob/master/src/antlr4/tree/Tree.py>`_
    @return                 string
    """
    if format is None:
        return tree.toStringTree()
    else:
        walker = ParseTreeWalker()
        listen = format(parser)
        walker.walk(listen, tree)
        return str(listen)


def get_tree_graph(tree, parser, format=TreeGraphListener):
    """
    returns a graph with networkx

    @param      tree        from @see fn parse_code
    @param      parser      the parser used to build the tree, output of @see fn parse_code
    @param      format      None or a class `ParseTreeListener <https://github.com/antlr/antlr4-python3/blob/master/src/antlr4/tree/Tree.py>`_
    @return                 string
    """
    if format is None:
        raise TypeError("format cannot be None")
    walker = ParseTreeWalker()
    listen = format(parser)
    walker.walk(listen, tree)
    return listen
