"""
@file
@brief Convert R into Python
"""
import sys
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
        mes = "Unable to convert\n'{0}'\n{1}\n{2}\nPARENT\n'{3}'\n{4}\n---SOFAR---\n{5}\n---SOSTACK---\n{6}\n---END---".format(
            text, type(node), node, ("" if isinstance(
                node, str) else node.parentCtx),
            (str if isinstance(node, str) else type(node.parentCtx)), sofar, sostack)
        mes += "\n------------\nMESSAGE=\n" + str(message)
        Exception.__init__(self, mes)


def r2python(code: str, pep8=False, fLOG=None) -> str:
    """
    Converts a R script into Python.

    @param      code        R string
    @param      pep8        modify the output to be compliant with pep8
    @param      fLOG        logging function
    @return                 Python string

    .. _code-r2python:

    The function uses a customized R grammar implemented with Antlr4.
    Formula becomes strings. They should be handled with
    `patsy <http://patsy.readthedocs.io/en/latest/>`_.

    .. exref::
        :title: Convert R into Python

        .. runpython::
            :showcode:

            rscript = '''
                nb=function(y=1930){
                debut=1816
                MatDFemale=matrix(D$Female,nrow=111)
                colnames(MatDFemale)=(debut+0):198
                cly=(y-debut+1):111
                deces=diag(MatDFemale[:,cly[cly%in%1:199]])
                return(c(B$Female[B$Year==y],deces))}
                '''

            from pyensae.languages import r2python
            print(r2python(rscript, pep8=True))

    Some patterns are not well migrated such expression ``a:b`` into ``range(a,b)``.
    The grammar could be improved to detect the beginning of the expression but
    for now, if the function fails to do the conversion, ``a:b`` must be written
    into ``(a):b``. The same trick is sometimes needed for other patterns
    such as the operator ``%in%`` which is converted into an intersection
    of two sets.

    Kwonws bugs:

    * ``} else {`` needs to be replaced by ``} EOL else {``
    * comment added at the end of line must be followed by an empty line
    * ``m[,1]`` must be replaced by ``M[:,1]``
    * formula ``~.`` is not translated
    * ``%<%`` cannot be followed by an empty line
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
        self.indent_level = {}
        self.add_lambda = False

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
            elif name_parent == "Functioncall":
                if text == "system.time":
                    self.add_lambda = True
                else:
                    self.add_lambda = False
                self.stack.append(("Functioncall", ""))
            if text == "list":
                self.imports.add("from python2r_helper import list_or_dict")
                self.stack.append((name, "list_or_dict"))
            elif text == "is":
                self.imports.add("from python2r_helper import is_")
                self.stack.append((name, "is_"))
            elif text == "(" and self.add_lambda:
                self.stack.append((name, "lambda: "))
                self.stack.append((name, node))
            else:
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
        elif name in ("Functiondef", "Functiondefargs", "Functiondefbody"):
            if text == "{":
                self.empty_stack()
                if len(self.block) == 0:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.block[-1] = True
                return self.add_code_final()
            elif text == "}":
                self.empty_stack()
                if len(self.block) == 0:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                self.block.pop()
                self.indent -= 1
                self.fLOG(
                    "[TreeStringListener.add_code*] indent -= 1", "--", self.indent)
                return self.add_code_final()
            elif text == '\n':
                return self.add_code_final()
            elif text in ('(', ')', 'function'):
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Functiondefargslambda":
            if text == "(":
                return self.add_code_final()
            elif text == ")":
                self.stack.append((name, ":"))
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
                self.stack.append(("Not!", node))
                return self.add_code_final()
            if text == "%*%":
                if sys.version_info[:2] >= (3, 6):
                    self.stack.append((name, "@"))
                else:
                    self.stack.append((name, "*"))
                return self.add_code_final()
            if text in ("%>%", "%<%", "%+%", "%-%", "%/%"):
                self.stack.append((name, text.replace("%", "")))
                return self.add_code_final()
            if text == "\n":
                self.empty_stack()
                if len(self.elements) > 0 and self.elements[-1] != '\n':
                    self.elements.append("\n")
                return self.add_code_final()
            if text == "break":
                self.stack.append((name, node))
                return self.add_code_final()
            if text == "{":
                self.empty_stack()
                if len(self.block) == 0:
                    # We are in an expression.
                    self.stack.append((name, "("))
                    return self.add_code_final()
                else:
                    self.block[-1] = True
                    return self.add_code_final()
            if text == "}":
                # We are in an expression.
                self.empty_stack()
                if len(self.block) == 0:
                    self.stack.append((name, ")"))
                    return self.add_code_final()
                else:
                    self.block.pop()
                    self.indent -= 1
                    self.fLOG(
                        "[TreeStringListener.add_code] indent -= 1", "--", self.indent)
                    return self.add_code_final()
        elif name == "Form":
            if text == "...":
                self.stack.append((None, "*args"))
                return self.add_code_final()
            else:
                self.stack.append((None, node))
                return self.add_code_final()
        elif name == "Argumentname":
            self.stack.append((name, node))
            return self.add_code_final()
        elif name == "Formlist":
            self.stack.append((None, node))
            return self.add_code_final()
        elif name == "Functioncall":
            if text == ')':
                self.stack.append((name, node))
                return self.add_code_final()
            if text == '(':
                self.stack.append((name, node))
                if self.add_lambda:
                    self.stack.append((name, "lambda: "))
                return self.add_code_final()
            if text == '\n':
                return self.add_code_final()
        elif name == "Affectation":
            if text == '\n':
                return self.add_code_final()
        elif name in ("Sub", "Subnobracket"):
            if text == '=':
                # Named parameter.
                self.stack.append((name, node))
                return self.add_code_final()
            if text == ':':
                self.stack.append((name, node))
                return self.add_code_final()
            if text == '...':
                self.stack.append((name, "*args"))
                return self.add_code_final()
        elif name == "Sublist":
            if text == ",":
                self.stack.append((name, node))
                return self.add_code_final()
            if text == '\n':
                return self.add_code_final()
        elif name in ("Exprlist", "Rightexpr"):
            if text.startswith("#"):
                # Comment
                self.empty_stack()
                self.elements.append("  ")
                self.elements.append(text.strip("\n"))
                self.elements.append("\n")
                return self.add_code_final()
            if text in (";", "\n"):
                if self.search_parents(node, "Inlinefunction"):
                    self.empty_stack()
                    self.stack.append(("Inlinefunction", text))
                    return self.add_code_final()
                else:
                    self.empty_stack()
                    if len(self.elements) > 0 and self.elements[-1] != '\n':
                        self.elements.append("\n")
                    return self.add_code_final()
        elif name == "Elseif":
            if text == "if":
                if id(node.parentCtx.parentCtx) not in self.indent_level:
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
                else:
                    if self.indent_level[id(node.parentCtx.parentCtx)] != self.indent:
                        raise R2PyConversionError(node, name, "".join(
                            self.elements), "\n".join(str(_) for _ in self.stack))
                self.stack.append((name, "elif"))
                return self.add_code_final()
            elif text == "else":
                # We do nothing. If follows.
                return self.add_code_final()
            else:
                # There should be nothing else.
                pass
        elif name == "Ifelseexpr" or name == "Ifexpr":
            if self.search_parents(node, "Sublist") or self.search_parents(node, "Affectation", 2):
                if text == "if":
                    self.stack.append((name, node))
                    return self.add_code_final()
                elif text == "else":
                    self.stack.append((name, node))
                    return self.add_code_final()
                elif text in ("(", ")"):
                    self.stack.append((name, node))
                    return self.add_code_final()
                elif text == "\n":
                    raise R2PyConversionError(node, name, "".join(
                        self.elements), "\n".join(str(_) for _ in self.stack))
            else:

                if text == "if":
                    self.indent_level[id(node.parentCtx)] = self.indent
                    self.stack.append((name, node))
                    return self.add_code_final()
                elif text == "else":
                    if id(node.parentCtx) not in self.indent_level:
                        raise R2PyConversionError(node, name, "".join(
                            self.elements), "\n".join(str(_) for _ in self.stack))
                    else:
                        if self.indent_level[id(node.parentCtx)] != self.indent:
                            raise R2PyConversionError(node, name, "".join(
                                self.elements), "\n".join(str(_) for _ in self.stack))
                    if len(self.stack):
                        # It does follow }
                        self.empty_stack()
                    if len(self.elements) > 0 and self.elements[-1] != '\n':
                        self.elements.append("\n")

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
        elif name == "Whileexpr":
            if text == "while":
                self.stack.append((name, node))
                return self.add_code_final()
            elif text in ('(', ')'):
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
            elif text in ("(",):
                self.stack.append((name, node))
                return self.add_code_final()
            elif text == "{":
                return self.add_code_final()
            elif text == "}":
                return self.add_code_final()
            elif text == ",":
                self.stack.append((name, node))
                self.stack.append(("Formop", '"'))
                return self.add_code_final()
            elif text == ";":
                self.stack.append(("Formop", '"'))
                self.stack.append((name, ","))
                self.stack.append(("Formop", '"'))
                return self.add_code_final()
            elif text == ")":
                self.stack.append(("Formop", '"'))
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Operator":
            if text == "%%":
                self.stack.append((name, "%"))
                return self.add_code_final()
            elif text == "^":
                self.stack.append((name, "**"))
                return self.add_code_final()
            else:
                self.stack.append((name, node))
                return self.add_code_final()
        elif name in ("Range_simple", "Range_complexe"):
            if text == ":":
                self.stack.append((name, ","))
                return self.add_code_final()
            else:
                self.stack.append((name, node))
                return self.add_code_final()
        elif name in ("Intersection_simple", "Intersection_complexe"):
            if text == "%in%":
                self.stack.append((name, node))
                return self.add_code_final()
            else:
                self.stack.append((name, node))
                return self.add_code_final()
        elif name == "Implicit_column_name":
            if text == ".":
                self.imports.add("from python2r_helper import ImplicitColumn")
                self.stack.append(("Identifier", "ImplicitColumn"))
                self.stack.append((name, node))
                return self.add_code_final()
            elif text in ("(", ")"):
                return self.add_code_final()
        elif name == "Inlinefunction":
            if text == "{":
                self.inlinefunction = []
                self.stack.append((name, "compile_inline_function('''\n"))
                return self.add_code_final()
            elif text in ("\n", ";"):
                if hasattr(self, "inlinefunction") and len(self.inlinefunction) > 0:
                    self.stack.append((name, text))
                return self.add_code_final()
            elif text == "}":
                self.stack.append((name, "''')"))
                self.inlinefunction = []
                return self.add_code_final()
            else:
                self.inlinefunction.append((name, node))
                return self.add_code_final()

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
        Empty the stack.
        """
        if len(self.stack) > 0 and len(self.block) > 0 and not self.block[-1]:
            self.indent -= 1
            self.fLOG("[TreeStringListener.empty_stack] indent -= 1",
                      "--", self.indent)
            self.block.pop()

        is_function_def = False
        is_for = False
        as_namespace = False
        for ipos, (name, node) in enumerate(self.stack):
            if name == "Functiondef" and not self.search_parents(node, "Functiondefargslambda", 3):
                is_function_def = True
                break
            elif name == "Forexpr":
                is_for = True
                break
            elif name == "Whileexpr":
                is_for = True
                break
            elif name == "Identifier":
                text = node if isinstance(node, str) else node.symbol.text
                if text == "asNamespace":
                    as_namespace = True
                    break

        if self.indent > 0:
            self.elements.append("    " * self.indent)

        if is_function_def:
            self.elements.append("\n")
            function_name = self.stack[0][1] if isinstance(
                self.stack[0][1], str) else self.stack[0][1].symbol.text
            self.fLOG(
                "[TreeStringListener.empty_stack] add function '{0}'".format(function_name))
            self.elements.append("    " * self.indent)
            self.elements.append("def")
            self.elements.append(" ")
            function_name = function_name.strip(
                '"').replace('.', "_").replace("-", "_")
            self.elements.append(function_name)
            self.stack = self.stack[3:]
            last = self.stack[-1][1].symbol.text
            if last != ")":
                raise R2PyConversionError(self.stack[-1][1], last, "".join(
                    self.elements), "\n".join(str(_) for _ in self.stack))

        # We store some end character we need to add.
        closure = {}

        for ipos, (name, node) in enumerate(self.stack):

            if name == "Functioncall" and node == "":
                # Silent addition.
                continue

            self.fLOG(
                "    cl={0} n={1} - {2}".format(len(closure), name, node))

            if len(closure) > 0 and not isinstance(node, str):
                rem = []
                for k, (leave_node, symbol) in closure.items():
                    b = self.has_parent(node, leave_node)
                    if not b:
                        rem.append(k)
                        args = [symbol, self.terminal_node_name(leave_node),
                                self.terminal_node_name(node), node.symbol.text]
                        self.fLOG(
                            "      closure '{0}' - L-{1} C-{2} ({3})".format(*args))
                        self.elements.append(symbol)
                for r in rem:
                    del closure[r]

            converted = self.to_python(name, node)

            if name == "Identifier":
                converted = converted.replace(".", "_")
            elif name in ("Ifexpr", "Ifelseexpr"):
                if node.symbol.text in ("(", ")") and (self.search_parents(node, "Sublist") or
                                                       self.search_parents(node, "Affectation", 2)):
                    self.fLOG(
                        "      inlineif {0} - '{1}'".format(name, node.symbol.text))
                    if node.symbol.text == "(":
                        converted = "("
                    else:
                        # We need to add ) when leaving this node.
                        converted = ","
                        closure[id(node.parentCtx)] = (node.parentCtx, ")")
            elif name == "Affectop" and self.stack[0][0] in ("Functioncall", "Inlinefunction") and \
                    self.stack[0][1] == "":
                # How to deal with syntax names(df) = something.
                # We add set add a bracket at the end.
                converted = ".set("
                closure[id(node.parentCtx.parentCtx)] = (
                    node.parentCtx.parentCtx, ")")
            elif name == "Formula_simple_C":
                if converted == "(":
                    self.elements.append('"')
                    closure[id(node.parentCtx)] = (node.parentCtx, '"')

            if as_namespace and converted == "=":
                converted = "."

            if self.indent > 0 and converted and self.elements[-1] == "\n":
                self.elements.append("    " * self.indent)

            self.elements.append(converted)
            self.elements.append(" ")
            if is_for and len(self.memo) > 0 and converted == "in":
                self.elements.append(self.memo[-1])
                self.elements.append('(')
            if name == ":EOL":
                self.elements.append(":")
                self.elements.append("\n")
                self.indent += 1
                self.fLOG(
                    "[TreeStringListener.empty_stack-1] indent += 1", "--", self.indent)
                self.block.append(False)

        if len(closure) > 0:
            for k, (leave_node, symbol) in closure.items():
                self.elements.append(symbol)
            # closure = {}

        if is_function_def or is_for:
            if is_for and len(self.memo) > 0:
                self.elements.append(")")
            self.elements.append(":")
            self.elements.append("\n")
            self.indent += 1
            self.fLOG(
                "[TreeStringListener.empty_stack-2] indent += 1", "--", self.indent)
            self.block.append(False)

        self.stack.clear()
        self.memo.clear()

    def search_parents(self, node, substring, max_depth=None):
        """
        Search for a substring in parents' node name.

        @param      node        current node
        @param      substring   substring to search
        @param      max_depth   number of parents to look at
        @return                 boolean
        """
        if isinstance(node, str):
            return False
        depth = max_depth if max_depth else 0
        n = node.parentCtx
        while (max_depth is None or depth > 0) and n is not None:
            na = self.terminal_node_name(n)
            if substring in na:
                return True
            n = n.parentCtx
            depth -= 1
        return False

    def has_parent(self, current, parent, depth=None):
        """
        Tell if *parent* is one of the parents of *current*.

        @param      current     current node
        @param      parent      parent to look for
        @return                 boolean
        """
        if isinstance(current, str):
            raise NotImplementedError()
        if depth is None:
            ide = 0
        else:
            ide = depth
        n = current
        while (depth is None or ide > 0) and n is not None:
            if id(n) == id(parent):
                return True
            n = n.parentCtx
            ide -= 1
        return False

    def to_python(self, name, node):
        """
        Convert a couple (name, node) into Python.
        """
        if name == "Affectop":
            return "="
        elif name == "Not":
            return " not "
        elif name == "Not!":
            return " ~ "
        elif name == "Boolean":
            text = node.symbol.text
            return text[0] + text[1:].lower()
        elif name == "Dotop":
            return "."
        elif name == "Dotop_static":
            return ".static."
        elif name == "Constant":
            text = node.symbol.text
            if text.startswith("`") and text.endswith("`") and len(text) > 1:
                return 'RCOL("{0}")'.format(text[1:-1])
            if text == "NULL":
                return "None"
            if text.endswith("L"):
                # Integer
                return text[:-1]
            is_formula = self.search_parents(node, "Formula")
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
        elif name in ("Ifexpr", "Ifelseexpr"):
            text = node if isinstance(node, str) else node.symbol.text
            if text in ("if", "else") and (self.search_parents(node, "Sublist") or
                                           self.search_parents(node, "Affectation", 2)):
                if text == "if":
                    self.imports.add("from python2r_helper import inlineif")
                    return "inlineif"
                else:
                    return ","
            else:
                return text
        elif name in ("Intersection_simple", "Intersection_complexe"):
            text = node.symbol.text
            if text == "%in%":
                return ") & set("
            else:
                return text
        elif isinstance(node, str):
            return node
        elif node is None:
            return ""
        elif name == "Functiondef":
            if self.search_parents(node, "Functiondeflambda", 2):
                return "lambda"
            else:
                return node.symbol.text
        elif name == "Argumentname":
            text = node.symbol.text
            if text == "lambda":
                return "lambda_"
            else:
                return text.replace(".", "_")
        elif name == "Identifier":
            text = node.symbol.text
            if text == "c":
                # This is a tuple.
                self.imports.add("from python2r_helper import make_tuple")
                return "make_tuple"
            elif text == "class":
                parent_name = self.terminal_node_name(node.parentCtx)
                if parent_name in ("Functioncall", "Subnobracket"):
                    self.imports.add("from python2r_helper import make_class")
                    return "make_class"
                else:
                    return text.replace(".", "_")
            elif text == "finally":
                self.imports.add("from python2r_helper import finallyR")
                return "finallyR"
            elif text == "lambda":
                return "lambda_"
            elif text in ("bquote", "ImplicitColumn"):
                self.imports.add(
                    "from python2r_helper import {0}".format(text))
                return text
            elif text == "try":
                parent_name = self.terminal_node_name(node.parentCtx)
                if parent_name == "Functioncall":
                    self.imports.add("from python2r_helper import dotry")
                    return "dotry"
                else:
                    return text.replace(".", "_")
            else:
                return text.replace(".", "_")
        else:
            text = node.symbol.text
            if text == "c":
                # This is a tuple.
                self.imports.add("from python2r_helper import make_tuple")
                return "make_tuple"
            elif text == "&&":
                return "and"
            elif text == "||":
                return "or"
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

    def enterRanges(self, ctx: RParser.RangesContext):
        self.fLOG("    add 'range('")
        self.stack.append(("Ranges", "range("))

    def exitRanges(self, ctx: RParser.RangesContext):
        self.fLOG("    add ') # range'")
        self.stack.append(("Ranges", ")"))

    def enterIntersections(self, ctx: RParser.RangesContext):
        self.fLOG("    add 'set('")
        self.stack.append(("Intersections", "set("))

    def exitIntersections(self, ctx: RParser.RangesContext):
        self.fLOG("    add ') # set'")
        self.stack.append(("Intersections", ")"))
