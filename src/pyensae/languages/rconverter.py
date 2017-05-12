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


def r2python(code: str, pep8=False) -> str:
    """
    Converts a R script into Python.

    @param      code        R string
    @param      pep8        modify the output to be compliant with pep8
    @return                 Python string
    """
    parser = parse_code(code, RParser, RLexer)
    parsed = parser.parse()
    listen = TreeStringListener(parsed)
    walker = ParseTreeWalker()
    walker.walk(listen, parsed)
    code = listen.get_python()
    if pep8:
        code = remove_extra_spaces_and_pep8(code, aggressive=True)
    return code


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
        self.stack = []
        self.elements = []
        self.indent = 0
        self.block = []
        self.memo = []

    def get_python(self):
        """
        Get the Python code for the R code.

        @return     Python code
        """
        return "".join(self.elements)

    def add_code(self, node):
        """
        Converts one node into python.
        """
        name = self.terminal_node_name(node)
        text = node.symbol.text
        if name == "Parse":
            if text.startswith("#"):
                # Comment
                self.elements.append(text.strip("\n"))
                self.elements.append("\n")
                return
            elif text in (";", "\n"):
                # End of an instruction
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return
            elif text == "<EOF>":
                return
            elif len(text.strip()) == 0:
                return
        elif name == "Identifier":
            self.stack.append((name, node))
            return
        elif name in ("Affectop", "Comparison"):
            self.stack.append((name, node))
            return
        elif name == "Constant":
            self.stack.append((name, node))
            return
        elif name == "Boolean":
            self.stack.append((name, node))
            return
        elif name == "Functiondef":
            self.stack.append((name, node))
            return
        elif name == "Expr":
            if text.startswith("#"):
                # Comment
                self.elements.append("    " * self.indent)
                self.elements.append(text.strip("\n"))
                self.elements.append("\n")
                return
            if text in ('(', ')', '[', ']', "+", "-"):
                self.stack.append((None, node))
                return
            if text == "\n":
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return
            if text == "{":
                self.empty_stack()
                if len(self.block) == 0:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.block[-1] = True
                return
            if text == "}":
                self.empty_stack()
                self.block.pop()
                self.indent -= 1
                return
        elif name == "Form":
            self.stack.append((None, node))
            return
        elif name == "Formlist":
            self.stack.append((None, node))
            return
        elif name == "Functioncall":
            if text in ('(', ')'):
                self.stack.append((name, node))
                return
            if text == '\n':
                return
        elif name == "Sublist":
            if text == ",":
                self.stack.append((name, node))
                return
            if text == '\n':
                return
        elif name == "Exprlist":
            if text in (";", "\n"):
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return
        elif name == "Ifelseexpr":
            if text == "if":
                self.stack.append((name, node))
                return
            elif text == "else":
                self.stack.append((name, node))
                return
            elif text in ('(', ')'):
                return
        elif name == "Forexpr":
            if text == "for":
                self.stack.append((name, node))
                return
            elif text in ('(', ')'):
                return
            elif text == "in":
                self.stack.append((name, node))
                return
        elif name == "Rangeop":
            if text == ":":
                self.memo.append("range")
                self.stack.append((name, node))
                return
        elif name == "Returnexpr":
            if text == "return":
                self.stack.append((name, node))
                return
            if text in ('(', ')'):
                return

        if text.startswith("#"):
            # Comment
            self.elements.append("    " * self.indent)
            self.elements.append(text.strip("\n"))
            self.elements.append("\n")
            return

        raise R2PyConversionError(node, name, "".join(
            self.elements), "\n".join(str(_) for _ in self.stack))

    def empty_stack(self):
        """
        Empty the stack. We assume it contains one instruction.
        """
        if len(self.stack) > 0 and len(self.block) > 0 and not self.block[-1]:
            self.indent -= 1
            self.block.pop()

        is_function_def = False
        is_for = False
        is_if = False
        as_namespace = False
        for name, node in self.stack:
            if name == "Functiondef":
                is_function_def = True
                break
            elif name == "Forexpr":
                is_for = True
                break
            elif name == "Ifelseexpr" or name == "Ifexpr":
                is_if = True
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
            if as_namespace and converted == "=":
                converted = "."
            self.elements.append(converted)
            self.elements.append(" ")
            if is_for and len(self.memo) > 0 and converted == "in":
                self.elements.append(self.memo[-1])
                self.elements.append('(')

        if is_function_def or is_for or is_if:
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
        elif name == "Boolean":
            text = node.symbol.text
            return text[0] + text[1:].lower()
        elif name == "Rangeop":
            text = node.symbol.text
            if text == ":":
                return ","
            else:
                return text
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
