# -*- coding: utf-8 -*-
"""
@file
@brief Parses :epkg:`C# `.
"""
from antlr4.tree.Tree import TerminalNodeImpl
from antlr4 import ParseTreeWalker
from ..languages.antlr_grammar_use import get_parser_lexer, parse_code
from ..languages.CSharpParserListener import CSharpParserListener


class CSharpElement:
    """
    Base class of a :epkg:`C#` element.    
    """
    
    _kinds = {'class', 'method', 'domain', 'type'}
    _privates = {'public', 'private', 'protected'}    
    
    def __init__(self, domain, name, doc=None, source=None, code=None, **kwargs):
        """
        @param  domain      domain
        @param  name        name
        @param  doc         documentation
        @param  source      source file
        @param  code        code
        """
        self.name = name
        self.doc = doc
        self.domain = domain
        self.source = source
        self.code = code
        self.options = kwargs
        
    def __str__(self):
        """
        usual
        """
        return f"{self.name}"
        

class CSharpDomain(CSharpElement):
    """
    Base class of a :epkg:`C#` domaon.    
    """
    
    def __init__(self, domain, name, doc=None, source=None, code=None, **kwargs):
        """
        @param  domain      domain
        @param  name        name
        @param  doc         documentation
        @param  source      source file
        @param  code        code
        """
        if "{" in domain or "{" in name:            
            raise ValueError("Issue with domain name\ndomain={0}\nname={1}".format(domain, name))
        CSharpElement.__init__(self, domain, name, doc, source, code, **kwargs)
        
    def __str__(self):
        """
        usual
        """
        return f"namespace {self.name}"


class CSharpVariable(CSharpElement):
    """
    :epkg:`C#` variables
    """
    def __init__(self, domain, name, typ, value=None, doc=None, source=None, code=None, **kwargs):
        """
        @param      domain      domain
        @param      name        name
        @param      typ         type
        @param      value       default value if it exists
        @param      doc         documentation
        @param  source      source file
        @param  code        code
        """
        CSharpElement.__init__(self, domain, name, doc=doc, source=source, code=code, **kwargs)
        if not isinstance(typ, CSharpType):
            raise TypeError("typ must be of type CSharpType")
        self.type = typ
        self.value = value
        
    def __str__(self):
        """
        usual
        """
        if isinstance(self.value, str):
            v = self.value.replace('"', '\\"')
            value = f'"{v}"'
        else:
            value = self.value
        return f"{self.type} {self.name} = {value}"
        
    
class CSharpType(CSharpVariable):
    """
    :epkg:`C#` type
    """
    def __init__(self, domain, name, typ, doc=None, source=None, code=None, **kwargs):
        """
        @param      domain      domain
        @param      name        name
        @param      typ         type
        @param      source      source file
        @param      code        code
        """
        CSharpVariable.__init__(self, domain, name, typ=typ, doc=doc, source=source, code=code, **kwargs)
        
    def __str__(self):
        """
        usual
        """
        return f"{self.name}"


class CSharpMethod(CSharpElement):
    """
    :epkg:`C#` function.
    """
    def __init__(self, domain, name, rtype, params=None, private='public',
                 static=False, doc=None, source=None, code=None, **kwargs):
        """
        @param      domain          domain
        @param      name            name
        @param      rtype           return type
        @param      private         private, public or protected
        @param      static          static or not
        @param      parameters      parameters
        @param      doc             documentation   
        @param      code            code
        """
        CSharpElement.__init__(self, domain, name, doc=doc, source=source, code=code, **kwargs)
        if private not in CSharpElement._privates:
            raise ValueError(f"Unable to find '{private}' in {CSharpElement._privates}.")
        self.params = params
        self.source = source
        self.static = static
        self.private = private
        self.rtype = rtype
        
    def __str__(self):
        """
        usual
        """
        pars = ", ".join(str(p) for p in self.params)        
        return f"{self.domain}.{self.name} ({self.kind})"
    
    
class CSharpClass(CSharpElement):
    """
    :epkg:`C#` class.
    """
    def __init__(self, domain, name, methods=None, constants=None, 
                 params=None, private='public', static=False,
                 doc=None, source=None, code=None, **kwargs):
        """
        @param      domain          domain
        @param      name            name
        @param      methods         methods
        @param      constants       constants
        @param      private         private, public or protected
        @param      static          static or not
        @param      doc             documentation 
        @param      source          source file
        @param      code            code
        """
        CSharpElement.__init__(self, domain, name, doc=doc, source=source, code=code, **kwargs)
        if private not in CSharpElement._privates:
            raise ValueError(f"Unable to find '{private}' in {CSharpElement._privates}.")
        self.source = source
        self.static = static
        self.private = private
        self.methods = methods
        self.contansts = constants
        
    def __str__(self):
        """
        usual
        """
        return f"class {self.domain}.{self.name}"
    


class CSharpParserListenerSignatures(CSharpParserListener):
    """
    :epkg:`C#` Listener
    """
    
    def __init__(self, parser, source):
        """
        constructor

        @param      parser      parser used to parse the code
        """
        CSharpParserListener.__init__(self)
        self.buffer = []
        self.parser = parser
        self._elements = []
        self._context = []
        self._obj = None
        self._source = source
        
    def stack_element(self, el):
        """
        Adds an element.
        """
        self._obj = el

    def enter_body(self):
        """
        Adds an element.
        """
        if self._obj is None:
            raise RuntimeError("self._obj cannot be None")
        self._context.append(self._obj)

    def exit_body(self):
        """
        Adds an element.
        """
        el = self._context.pop()
        if el is None:
            raise RuntimeError("el cannot be None")
        self._elements.append(el)

    # def enterEveryRule(self, ctx):
    #    pass
    
    # def leaveEveryRule(self, ctx):
    #    pass
        
    def get_code(self, ctx):
        line, col = ctx.start.line, ctx.start.column
        class_name = ctx.__class__.__name__
        return class_name, line, col   

    def enumerate_all_children(self, ctx):
        """
        Enumerate all children.

        @param      ctx     context
        @return             iterator
        """

        def roll(ctx):
            if not isinstance(ctx, TerminalNodeImpl):
                yield ctx
                for ch in ctx.getChildren():
                    for r in roll(ch):
                        yield r
        for r in roll(ctx):
            yield r
            
    ############
    ## namespace
    ############
            
    def enterNamespace_declaration(self, ctx):
        self._namespace_code = ctx.getText()

    def enterNamespace_body(self, ctx):
        pass
        
    def enterNamespace_or_type_name(self, ctx):
        code = getattr(self, '_namespace_code', None)
        if code:
            self._namespace_code = None
            name = ctx.getText()
            children = list(self.enumerate_all_children(ctx))
            line1 = ctx.start.line
            line2 = ctx.stop.line
            self.stack_element(CSharpDomain(name, name, code=code, source=self._source, lines=[line1, line2]))
            self.enter_body()
        
    def exitNamespace_or_type_name(self, ctx):
        pass
        
    def exitNamespace_body(self, ctx):
        self.exit_body()

    def exitNamespace_declaration(self, ctx):
        pass
        


class CSharpParser:
    """
    Parses :epkg:`C#`.
    """
    
    def __init__(self):
        """
        """
        clparser, cllexer = get_parser_lexer("C#")
        self._parser = clparser
        self._lexer = cllexer
        
    def parse(self, code, source=None):
        """
        Returns all elements of codes inside a string.
        
        @param      code        string
        @param      source      source
        @return                 list of @see cl CSharpElement
        """
        self._source = source
        parser = parse_code(code, self._parser, self._lexer)
        tree = parser.parse()
        walker = ParseTreeWalker()
        listen = CSharpParserListenerSignatures(parser, source)
        walker.walk(listen, tree)
        return listen._elements
    
