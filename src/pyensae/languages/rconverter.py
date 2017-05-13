"""
@file
@brief Convert R into Python
"""
from antlr4 import ParseTreeListener, ParseTreeWalker
from pyquickhelper.pycode import remove_extra_spaces_and_pep8
from .RParser import RParser
from .RLexer import RLexer
from .antlr_grammar_use import parse_code


class R2PyConversionError(Exception):
    """
    Raised when conversion cannot be done.
    """

    def __init__(self, node, message, sofar, sostack):
        """
        """
        try:
            text = node.symbol.text
        except AttributeError:
            text = "ERROR"
        mes = "Unable to convert\n'{0}'\n{1}\n{2}\nPARENT\n'{3}'\n{4}\nSOFAR\n{5}\nSOSTACK\n{5}".format(
            text, type(node), node, node.parentCtx, type(node.parentCtx), sofar, sostack)
        mes += "\n------------\n" + message
        Exception.__init__(self, mes)


def r2python(code: str, pep8=False, fLOG=None) -> str:
    """
    Converts a R script into Python.

    @param      code        R string
    @param      pep8        modify the output to be compliant with pep8
    @param      fLOG        logging function
    @return                 Python string

    The function uses a customized R grammar implemented with Antlr4.
    Formula becomes strings. They should be handled with
    `patsy <http://patsy.readthedocs.io/en/latest/>`_.
    """
    if fLOG:
        fLOG("[r2python] parse ", len(code), "bytes")
    parser = parse_code(code, RParser, RLexer)
    if fLOG:
        fLOG("[r2python] parse continue")
    parsed = parser.parse()
    if fLOG:
        fLOG("[r2python] listen")
    listen = TreeStringListener(parsed, fLOG=fLOG)
    walker = ParseTreeWalker()
    if fLOG:
        fLOG("[r2python] walk")
    walker.walk(listen, parsed)
    if fLOG:
        fLOG("[r2python] get code")
    code = listen.get_python()
    if pep8:
        if fLOG:
            fLOG("[r2python] pep8")
        code = remove_extra_spaces_and_pep8(code, aggressive=True)
    return code


class TreeStringListener(ParseTreeListener):

    """
    This class is an attempt to run through the tree and convert it into
    a string.
    """

    def __init__(self, parser, fLOG=None):
        """
        constructor

        @param      parser      parser used to parse the code
        """
        ParseTreeListener.__init__(self)
        self.buffer = []
        self.level = 0
        self.parser = parser
        self.stack = []
        self.elements = []
        self.indent = 0
        self.block = []
        self.memo = []
        self.imports = set()
        self.in_formula = False
        self._fLOG = fLOG

    def fLOG(self, *l, **p):
        """
        logging
        """
        if self._fLOG:
            self._fLOG(*l, **p)

    def get_python(self):
        """
        Get the Python code for the R code.

        @return     Python code
        """
        def modify(s):
            if s.startswith("from"):
                return s
            else:
                return "import {0}".format(s)
        imports = "\n".join(modify(i) for i in sorted(self.imports))
        if len(imports) > 0:
            imports += "\n\n"
        return imports + "".join(self.elements)

    def add_code(self, node):
        """
        Converts one node into python.
        """
        name = self.terminal_node_name(node)
        text = node.symbol.text

        if self.in_formula:
            if text in (",", "\n"):
                self.stack.append(("Formop", '"'))
                self.in_formula = False
            self.fLOG("[TreeStringListener]", len(self.block),
                      "~" if self.in_formula else " ", name, text)
        else:
            self.fLOG("[TreeStringListener]", len(self.block), " ", name, text)

        if name == "Parse":
            if text.startswith("#"):
                # Comment
                self.elements.append(text.strip("\n"))
                self.elements.append("\n")
                return self.add_code_final()
            elif text in (";", "\n"):
                # End of an instruction
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return self.add_code_final()
            elif text == "<EOF>":
                return self.add_code_final()
            elif len(text.strip()) == 0:
                return self.add_code_final()
        elif name == "Identifier":
            name_parent = self.terminal_node_name(node.parentCtx)
            if name_parent == "Formula_simple_A":
                if self.in_formula:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.stack.append(("Formop", '"'))
                self.in_formula = True
            self.stack.append((name, node))
            return self.add_code_final()
        elif name in ("Affectop", "Comparison"):
            self.stack.append((name, node))
            return self.add_code_final()
        elif name == "Constant":
            self.stack.append((name, node))
            return self.add_code_final()
        elif name == "Boolean":
            self.stack.append((name, node))
            return self.add_code_final()
        elif name == "Functiondef":
            self.stack.append((name, node))
            return self.add_code_final()
        elif name == "Expr":
            if text.startswith("#"):
                # Comment
                self.elements.append("    " * self.indent)
                self.elements.append(text.strip("\n"))
                self.elements.append("\n")
                return self.add_code_final()
            if text in ('(', ')', '[', ']', "+", "-", "|", "&", "||", "&&", "[[", "]]"):
                self.stack.append((None, node))
                return self.add_code_final()
            if text == "!":
                self.stack.append(("Not", node))
                return self.add_code_final()
            if text == "\n":
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return self.add_code_final()
            if text == "%in%":
                self.stack.append((None, "in"))
                return self.add_code_final()
            if text == "{":
                self.empty_stack()
                if len(self.block) == 0:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.block[-1] = True
                return self.add_code_final()
            if text == "}":
                self.empty_stack()
                if len(self.block) == 0:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.block.pop()
                self.indent -= 1
                return self.add_code_final()
        elif name == "Form":
            self.stack.append((None, node))
            return self.add_code_final()
        elif name == "Formlist":
            self.stack.append((None, node))
            return self.add_code_final()
        elif name == "Functioncall":
            if text in ('(', ')'):
                self.stack.append((name, node))
                return self.add_code_final()
            if text == '\n':
                return self.add_code_final()
        elif name == "Sublist":
            if text == ",":
                self.stack.append((name, node))
                return self.add_code_final()
            if text == '\n':
                return self.add_code_final()
        elif name == "Exprlist":
            if text in (";", "\n"):
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return self.add_code_final()
        elif name == "Ifelseexpr" or name == "Ifexpr":
            if text == "if":
                self.stack.append((name, node))
                return self.add_code_final()
            elif text == "else":
                self.stack.append((name, node))
                self.stack.append((":EOL", None))
                return self.add_code_final()
            elif text == ")":
                self.stack.append((":EOL", None))
                return self.add_code_final()
            elif text in ('(', "\n"):
                return self.add_code_final()
        elif name == "Forexpr":
            if text == "for":
                self.stack.append((name, node))
                return self.add_code_final()
            elif text in ('(', ')'):
                return self.add_code_final()
            elif text == "in":
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Rangeop":
            if text == ":":
                self.memo.append("range")
                self.stack.append((name, node))
                return self.add_code_final()
            elif text == ":::":
                self.stack.append(("Dotop_static", node))
                return self.add_code_final()
        elif name == "Returnexpr":
            if text == "return":
                self.stack.append((name, node))
                return self.add_code_final()
            if text in ('(', ')'):
                return self.add_code_final()
        elif name == "Formop":
            if text == "~":
                self.imports.add("patsy")
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Sublistadd":
            if text == "+":
                self.stack.append((name, node))
                return self.add_code_final()
            elif text == "\n":
                return self.add_code_final()
        elif name == "Dotop":
            if text in ("$", "@"):
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Formula_simple_A":
            if text == ".":
                self.stack.append((None, "."))
                return self.add_code_final()
        elif name == "Formula_simple_C":
            if text in ("(", ")", "~"):
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Formula_simple_B":
            if text == "within":
                self.imports.add("from python2r_helper import within")
                self.stack.append((name, node))
                return self.add_code_final()
            elif text in ("(", ",", ")"):
                self.stack.append((name, node))
                return self.add_code_final()
            elif text == "{":
                self.stack.append(("Formop", '"'))
                return self.add_code_final()
            elif text == "}":
                self.stack.append(("Formop", '"'))
                return self.add_code_final()
        elif name == "Operator":
            self.stack.append((name, node))
            return self.add_code_final()

        if text.startswith("#"):
            # Comment
            self.elements.append("    " * self.indent)
            self.elements.append(text.strip("\n"))
            self.elements.append("\n")
            return self.add_code_final()

        raise R2PyConversionError(node, name, "".join(
            self.elements), "\n".join(str(_) for _ in self.stack))

    def add_code_final(self):
        """
        Add extra characters if needed.
        """
        pass

    def empty_stack(self):
        """
        Empty the stack. We assume it contains one instruction.
        """
        if len(self.stack) > 0 and len(self.block) > 0 and not self.block[-1]:
            self.indent -= 1
            self.block.pop()

        is_function_def = False
        is_for = False
        as_namespace = False
        for name, node in self.stack:
            if name == "Functiondef":
                is_function_def = True
                break
            elif name == "Forexpr":
                is_for = True
                break
            elif name == "Identifier":
                text = node.symbol.text
                if text == "asNamespace":
                    as_namespace = True
                    break

        if self.indent > 0:
            self.elements.append("    " * self.indent)

        if is_function_def:
            self.elements.append("\n")
            function_name = self.stack[0][1].symbol.text
            self.elements.append("    " * self.indent)
            self.elements.append("def")
            self.elements.append(" ")
            self.elements.append(function_name.strip('"').replace('.', "_"))
            self.stack = self.stack[3:]
            last = self.stack[-1][1].symbol.text
            if last != ")":
                last = self.stack[-1]
                raise R2PyConversionError(last[0], last[1], "".join(
                    self.elements), "\n".join(str(_) for _ in self.stack))

        for name, node in self.stack:
            converted = self.to_python(name, node)
            if name == "Identifier":
                converted = converted.replace(".", "_")
            if as_namespace and converted == "=":
                converted = "."
            self.elements.append(converted)
            self.elements.append(" ")
            if is_for and len(self.memo) > 0 and converted == "in":
                self.elements.append(self.memo[-1])
                self.elements.append('(')
            if name == ":EOL":
                self.elements.append(":")
                self.elements.append("\n")
                self.indent += 1
                self.block.append(False)

        if is_function_def or is_for:
            if is_for and len(self.memo) > 0:
                self.elements.append(")")
            self.elements.append(":")
            self.elements.append("\n")
            self.indent += 1
            self.block.append(False)

        self.stack.clear()
        self.memo.clear()

    def to_python(self, name, node):
        """
        Convert a couple (name, node) into Python.
        """
        if name == "Affectop":
            return "="
        elif name == "Not":
            return " not "
        elif name == "Boolean":
            text = node.symbol.text
            return text[0] + text[1:].lower()
        elif name == "Dotop":
            return "."
        elif name == "Dotop_static":
            return ".static."
        elif name == "Identifier":
            text = node.symbol.text
            if text == "c":
                # This is a tuple.
                return "tuple"
            else:
                return text.replace(".", "_")
        elif name == "Constant":
            text = node.symbol.text
            is_formula = False
            n = node.parentCtx
            while n is not None:
                na = self.terminal_node_name(n)
                if "Formula" in na:
                    is_formula = True
                    break
                n = n.parentCtx
            if is_formula and text[0] == '"' and text[-1] == '"':
                return '\\"{0}\\"'.format(text[1:-1])
            else:
                return text
        elif name == "Rangeop":
            text = node.symbol.text
            if text == ":":
                return ","
            else:
                return text
        elif isinstance(node, str):
            return node
        elif node is None:
            return ""
        else:
            text = node.symbol.text
            if text == "c":
                # This is a tuple.
                return "tuple"
            else:
                return text

    def terminal_node_name(self, node):
        """
        Converts a terminal node into a rule name
        """
        return str(type(node.parentCtx)).split('.')[-1].strip("]['><").replace("Context", "")

    def visitTerminal(self, node):
        """
        event
        """
        # node: ['symbol', 'parentCtx']
        # node.symbol: ['source', 'type', 'channel', 'start', 'stop', 'tokenIndex', 'line', 'column', '_text']
        # help(node.parentCtx)
        full_text = node.parentCtx.getText().replace("\n", " EOL ")
        text = node.symbol.text.replace("\n", " EOL ")
        stype = self.terminal_node_name(node)
        text = "{0} [{1} - {2}] {3}".format("    " *
                                            self.level, text, stype, full_text)
        self.buffer.append(text)
        self.add_code(node)

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
        return self.get_python() + "\n----\n" + "\n".join(self.buffer)
