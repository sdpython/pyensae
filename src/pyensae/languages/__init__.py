"""
@file
@brief Shortcuts to languages.
"""

from .antlr_grammar_build import build_grammar
from .antlr_grammar_use import get_parser_lexer, parse_code, get_tree_string, get_tree_graph
from .rconverter import r2python
from .tree_string_listener import TreeStringListener
