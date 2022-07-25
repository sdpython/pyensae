# Generated from \DOT.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 24, 129, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13, 7, 13,
        1, 0, 3, 0, 30, 8, 0, 1, 0, 1, 0, 3, 0, 34, 8, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 3,
        1, 43, 8, 1, 5, 1, 45, 8, 1, 10, 1, 12, 1, 48, 9, 1, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2,
        1, 2, 3, 2, 58, 8, 2, 1, 3, 1, 3, 1, 3, 1, 4, 1, 4, 3, 4, 65, 8, 4, 1, 4, 4, 4, 68, 8, 4, 11,
        4, 12, 4, 69, 1, 5, 1, 5, 1, 5, 3, 5, 75, 8, 5, 1, 5, 3, 5, 78, 8, 5, 4, 5, 80, 8, 5, 11, 5,
        12, 5, 81, 1, 6, 1, 6, 3, 6, 86, 8, 6, 1, 6, 1, 6, 3, 6, 90, 8, 6, 1, 7, 1, 7, 1, 7, 3, 7, 95,
        8, 7, 4, 7, 97, 8, 7, 11, 7, 12, 7, 98, 1, 8, 1, 8, 1, 9, 1, 9, 3, 9, 105, 8, 9, 1, 10, 1, 10,
        3, 10, 109, 8, 10, 1, 11, 1, 11, 1, 11, 1, 11, 3, 11, 115, 8, 11, 1, 12, 1, 12, 3, 12, 119,
        8, 12, 3, 12, 121, 8, 12, 1, 12, 1, 12, 1, 12, 1, 12, 1, 13, 1, 13, 1, 13, 0, 0, 14, 0, 2,
        4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 0, 4, 1, 0, 12, 13, 2, 0, 12, 12, 14, 15, 1,
        0, 8, 9, 1, 0, 17, 20, 136, 0, 29, 1, 0, 0, 0, 2, 46, 1, 0, 0, 0, 4, 57, 1, 0, 0, 0, 6, 59,
        1, 0, 0, 0, 8, 67, 1, 0, 0, 0, 10, 79, 1, 0, 0, 0, 12, 85, 1, 0, 0, 0, 14, 96, 1, 0, 0, 0, 16,
        100, 1, 0, 0, 0, 18, 102, 1, 0, 0, 0, 20, 106, 1, 0, 0, 0, 22, 110, 1, 0, 0, 0, 24, 120,
        1, 0, 0, 0, 26, 126, 1, 0, 0, 0, 28, 30, 5, 11, 0, 0, 29, 28, 1, 0, 0, 0, 29, 30, 1, 0, 0,
        0, 30, 31, 1, 0, 0, 0, 31, 33, 7, 0, 0, 0, 32, 34, 3, 26, 13, 0, 33, 32, 1, 0, 0, 0, 33, 34,
        1, 0, 0, 0, 34, 35, 1, 0, 0, 0, 35, 36, 5, 1, 0, 0, 36, 37, 3, 2, 1, 0, 37, 38, 5, 2, 0, 0,
        38, 39, 5, 0, 0, 1, 39, 1, 1, 0, 0, 0, 40, 42, 3, 4, 2, 0, 41, 43, 5, 3, 0, 0, 42, 41, 1, 0,
        0, 0, 42, 43, 1, 0, 0, 0, 43, 45, 1, 0, 0, 0, 44, 40, 1, 0, 0, 0, 45, 48, 1, 0, 0, 0, 46, 44,
        1, 0, 0, 0, 46, 47, 1, 0, 0, 0, 47, 3, 1, 0, 0, 0, 48, 46, 1, 0, 0, 0, 49, 58, 3, 18, 9, 0,
        50, 58, 3, 12, 6, 0, 51, 58, 3, 6, 3, 0, 52, 53, 3, 26, 13, 0, 53, 54, 5, 4, 0, 0, 54, 55,
        3, 26, 13, 0, 55, 58, 1, 0, 0, 0, 56, 58, 3, 24, 12, 0, 57, 49, 1, 0, 0, 0, 57, 50, 1, 0,
        0, 0, 57, 51, 1, 0, 0, 0, 57, 52, 1, 0, 0, 0, 57, 56, 1, 0, 0, 0, 58, 5, 1, 0, 0, 0, 59, 60,
        7, 1, 0, 0, 60, 61, 3, 8, 4, 0, 61, 7, 1, 0, 0, 0, 62, 64, 5, 5, 0, 0, 63, 65, 3, 10, 5, 0,
        64, 63, 1, 0, 0, 0, 64, 65, 1, 0, 0, 0, 65, 66, 1, 0, 0, 0, 66, 68, 5, 6, 0, 0, 67, 62, 1,
        0, 0, 0, 68, 69, 1, 0, 0, 0, 69, 67, 1, 0, 0, 0, 69, 70, 1, 0, 0, 0, 70, 9, 1, 0, 0, 0, 71,
        74, 3, 26, 13, 0, 72, 73, 5, 4, 0, 0, 73, 75, 3, 26, 13, 0, 74, 72, 1, 0, 0, 0, 74, 75, 1,
        0, 0, 0, 75, 77, 1, 0, 0, 0, 76, 78, 5, 7, 0, 0, 77, 76, 1, 0, 0, 0, 77, 78, 1, 0, 0, 0, 78,
        80, 1, 0, 0, 0, 79, 71, 1, 0, 0, 0, 80, 81, 1, 0, 0, 0, 81, 79, 1, 0, 0, 0, 81, 82, 1, 0, 0,
        0, 82, 11, 1, 0, 0, 0, 83, 86, 3, 20, 10, 0, 84, 86, 3, 24, 12, 0, 85, 83, 1, 0, 0, 0, 85,
        84, 1, 0, 0, 0, 86, 87, 1, 0, 0, 0, 87, 89, 3, 14, 7, 0, 88, 90, 3, 8, 4, 0, 89, 88, 1, 0,
        0, 0, 89, 90, 1, 0, 0, 0, 90, 13, 1, 0, 0, 0, 91, 94, 3, 16, 8, 0, 92, 95, 3, 20, 10, 0, 93,
        95, 3, 24, 12, 0, 94, 92, 1, 0, 0, 0, 94, 93, 1, 0, 0, 0, 95, 97, 1, 0, 0, 0, 96, 91, 1, 0,
        0, 0, 97, 98, 1, 0, 0, 0, 98, 96, 1, 0, 0, 0, 98, 99, 1, 0, 0, 0, 99, 15, 1, 0, 0, 0, 100,
        101, 7, 2, 0, 0, 101, 17, 1, 0, 0, 0, 102, 104, 3, 20, 10, 0, 103, 105, 3, 8, 4, 0, 104,
        103, 1, 0, 0, 0, 104, 105, 1, 0, 0, 0, 105, 19, 1, 0, 0, 0, 106, 108, 3, 26, 13, 0, 107,
        109, 3, 22, 11, 0, 108, 107, 1, 0, 0, 0, 108, 109, 1, 0, 0, 0, 109, 21, 1, 0, 0, 0, 110,
        111, 5, 10, 0, 0, 111, 114, 3, 26, 13, 0, 112, 113, 5, 10, 0, 0, 113, 115, 3, 26, 13,
        0, 114, 112, 1, 0, 0, 0, 114, 115, 1, 0, 0, 0, 115, 23, 1, 0, 0, 0, 116, 118, 5, 16, 0,
        0, 117, 119, 3, 26, 13, 0, 118, 117, 1, 0, 0, 0, 118, 119, 1, 0, 0, 0, 119, 121, 1, 0,
        0, 0, 120, 116, 1, 0, 0, 0, 120, 121, 1, 0, 0, 0, 121, 122, 1, 0, 0, 0, 122, 123, 5, 1,
        0, 0, 123, 124, 3, 2, 1, 0, 124, 125, 5, 2, 0, 0, 125, 25, 1, 0, 0, 0, 126, 127, 7, 3, 0,
        0, 127, 27, 1, 0, 0, 0, 19, 29, 33, 42, 46, 57, 64, 69, 74, 77, 81, 85, 89, 94, 98, 104,
        108, 114, 118, 120
    ]


class DOTParser (Parser):

    grammarFileName = "DOT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "'{'", "'}'", "';'", "'='", "'['", "']'",
                    "','", "'->'", "'--'", "':'"]

    symbolicNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                     "<INVALID>", "<INVALID>", "<INVALID>", "STRICT", "GRAPH",
                     "DIGRAPH", "NODE", "EDGE", "SUBGRAPH", "NUMBER", "STRING",
                     "ID", "HTML_STRING", "COMMENT", "LINE_COMMENT", "PREPROC",
                     "WS"]

    RULE_graph = 0
    RULE_stmt_list = 1
    RULE_stmt = 2
    RULE_attr_stmt = 3
    RULE_attr_list = 4
    RULE_a_list = 5
    RULE_edge_stmt = 6
    RULE_edgeRHS = 7
    RULE_edgeop = 8
    RULE_node_stmt = 9
    RULE_node_id = 10
    RULE_port = 11
    RULE_subgraph = 12
    RULE_id_ = 13

    ruleNames = ["graph", "stmt_list", "stmt", "attr_stmt", "attr_list",
                 "a_list", "edge_stmt", "edgeRHS", "edgeop", "node_stmt",
                 "node_id", "port", "subgraph", "id_"]

    EOF = Token.EOF
    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    STRICT = 11
    GRAPH = 12
    DIGRAPH = 13
    NODE = 14
    EDGE = 15
    SUBGRAPH = 16
    NUMBER = 17
    STRING = 18
    ID = 19
    HTML_STRING = 20
    COMMENT = 21
    LINE_COMMENT = 22
    PREPROC = 23
    WS = 24

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class GraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(DOTParser.Stmt_listContext, 0)

        def EOF(self):
            return self.getToken(DOTParser.EOF, 0)

        def GRAPH(self):
            return self.getToken(DOTParser.GRAPH, 0)

        def DIGRAPH(self):
            return self.getToken(DOTParser.DIGRAPH, 0)

        def STRICT(self):
            return self.getToken(DOTParser.STRICT, 0)

        def id_(self):
            return self.getTypedRuleContext(DOTParser.Id_Context, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_graph

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterGraph"):
                listener.enterGraph(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitGraph"):
                listener.exitGraph(self)

    def graph(self):

        localctx = DOTParser.GraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_graph)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.STRICT:
                self.state = 28
                self.match(DOTParser.STRICT)

            self.state = 31
            _la = self._input.LA(1)
            if not(_la == DOTParser.GRAPH or _la == DOTParser.DIGRAPH):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0):
                self.state = 32
                self.id_()

            self.state = 35
            self.match(DOTParser.T__0)
            self.state = 36
            self.stmt_list()
            self.state = 37
            self.match(DOTParser.T__1)
            self.state = 38
            self.match(DOTParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stmt_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.StmtContext)
            else:
                return self.getTypedRuleContext(DOTParser.StmtContext, i)

        def getRuleIndex(self):
            return DOTParser.RULE_stmt_list

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt_list"):
                listener.enterStmt_list(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt_list"):
                listener.exitStmt_list(self)

    def stmt_list(self):

        localctx = DOTParser.Stmt_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stmt_list)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.T__0) | (1 << DOTParser.GRAPH) | (1 << DOTParser.NODE) | (1 << DOTParser.EDGE) | (1 << DOTParser.SUBGRAPH) | (1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0):
                self.state = 40
                self.stmt()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == DOTParser.T__2:
                    self.state = 41
                    self.match(DOTParser.T__2)

                self.state = 48
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_stmt(self):
            return self.getTypedRuleContext(DOTParser.Node_stmtContext, 0)

        def edge_stmt(self):
            return self.getTypedRuleContext(DOTParser.Edge_stmtContext, 0)

        def attr_stmt(self):
            return self.getTypedRuleContext(DOTParser.Attr_stmtContext, 0)

        def id_(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.Id_Context)
            else:
                return self.getTypedRuleContext(DOTParser.Id_Context, i)

        def subgraph(self):
            return self.getTypedRuleContext(DOTParser.SubgraphContext, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterStmt"):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitStmt"):
                listener.exitStmt(self)

    def stmt(self):

        localctx = DOTParser.StmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_stmt)
        try:
            self.state = 57
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 4, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.node_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.edge_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 51
                self.attr_stmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 52
                self.id_()
                self.state = 53
                self.match(DOTParser.T__3)
                self.state = 54
                self.id_()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.subgraph()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def attr_list(self):
            return self.getTypedRuleContext(DOTParser.Attr_listContext, 0)

        def GRAPH(self):
            return self.getToken(DOTParser.GRAPH, 0)

        def NODE(self):
            return self.getToken(DOTParser.NODE, 0)

        def EDGE(self):
            return self.getToken(DOTParser.EDGE, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_attr_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAttr_stmt"):
                listener.enterAttr_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAttr_stmt"):
                listener.exitAttr_stmt(self)

    def attr_stmt(self):

        localctx = DOTParser.Attr_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_attr_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.GRAPH) | (1 << DOTParser.NODE) | (1 << DOTParser.EDGE))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self.attr_list()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Attr_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def a_list(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.A_listContext)
            else:
                return self.getTypedRuleContext(DOTParser.A_listContext, i)

        def getRuleIndex(self):
            return DOTParser.RULE_attr_list

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterAttr_list"):
                listener.enterAttr_list(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitAttr_list"):
                listener.exitAttr_list(self)

    def attr_list(self):

        localctx = DOTParser.Attr_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_attr_list)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 62
                self.match(DOTParser.T__4)
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0):
                    self.state = 63
                    self.a_list()

                self.state = 66
                self.match(DOTParser.T__5)
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == DOTParser.T__4):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class A_listContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.Id_Context)
            else:
                return self.getTypedRuleContext(DOTParser.Id_Context, i)

        def getRuleIndex(self):
            return DOTParser.RULE_a_list

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterA_list"):
                listener.enterA_list(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitA_list"):
                listener.exitA_list(self)

    def a_list(self):

        localctx = DOTParser.A_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_a_list)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 71
                self.id_()
                self.state = 74
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == DOTParser.T__3:
                    self.state = 72
                    self.match(DOTParser.T__3)
                    self.state = 73
                    self.id_()

                self.state = 77
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == DOTParser.T__6:
                    self.state = 76
                    self.match(DOTParser.T__6)

                self.state = 81
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Edge_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgeRHS(self):
            return self.getTypedRuleContext(DOTParser.EdgeRHSContext, 0)

        def node_id(self):
            return self.getTypedRuleContext(DOTParser.Node_idContext, 0)

        def subgraph(self):
            return self.getTypedRuleContext(DOTParser.SubgraphContext, 0)

        def attr_list(self):
            return self.getTypedRuleContext(DOTParser.Attr_listContext, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_edge_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdge_stmt"):
                listener.enterEdge_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdge_stmt"):
                listener.exitEdge_stmt(self)

    def edge_stmt(self):

        localctx = DOTParser.Edge_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_edge_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [DOTParser.NUMBER, DOTParser.STRING, DOTParser.ID, DOTParser.HTML_STRING]:
                self.state = 83
                self.node_id()
                pass
            elif token in [DOTParser.T__0, DOTParser.SUBGRAPH]:
                self.state = 84
                self.subgraph()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 87
            self.edgeRHS()
            self.state = 89
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.T__4:
                self.state = 88
                self.attr_list()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdgeRHSContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def edgeop(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.EdgeopContext)
            else:
                return self.getTypedRuleContext(DOTParser.EdgeopContext, i)

        def node_id(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.Node_idContext)
            else:
                return self.getTypedRuleContext(DOTParser.Node_idContext, i)

        def subgraph(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.SubgraphContext)
            else:
                return self.getTypedRuleContext(DOTParser.SubgraphContext, i)

        def getRuleIndex(self):
            return DOTParser.RULE_edgeRHS

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdgeRHS"):
                listener.enterEdgeRHS(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdgeRHS"):
                listener.exitEdgeRHS(self)

    def edgeRHS(self):

        localctx = DOTParser.EdgeRHSContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_edgeRHS)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 91
                self.edgeop()
                self.state = 94
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [DOTParser.NUMBER, DOTParser.STRING, DOTParser.ID, DOTParser.HTML_STRING]:
                    self.state = 92
                    self.node_id()
                    pass
                elif token in [DOTParser.T__0, DOTParser.SUBGRAPH]:
                    self.state = 93
                    self.subgraph()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la == DOTParser.T__7 or _la == DOTParser.T__8):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class EdgeopContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def getRuleIndex(self):
            return DOTParser.RULE_edgeop

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEdgeop"):
                listener.enterEdgeop(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEdgeop"):
                listener.exitEdgeop(self)

    def edgeop(self):

        localctx = DOTParser.EdgeopContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_edgeop)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            _la = self._input.LA(1)
            if not(_la == DOTParser.T__7 or _la == DOTParser.T__8):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_stmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def node_id(self):
            return self.getTypedRuleContext(DOTParser.Node_idContext, 0)

        def attr_list(self):
            return self.getTypedRuleContext(DOTParser.Attr_listContext, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_node_stmt

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNode_stmt"):
                listener.enterNode_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNode_stmt"):
                listener.exitNode_stmt(self)

    def node_stmt(self):

        localctx = DOTParser.Node_stmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_node_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.node_id()
            self.state = 104
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.T__4:
                self.state = 103
                self.attr_list()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Node_idContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self):
            return self.getTypedRuleContext(DOTParser.Id_Context, 0)

        def port(self):
            return self.getTypedRuleContext(DOTParser.PortContext, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_node_id

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNode_id"):
                listener.enterNode_id(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNode_id"):
                listener.exitNode_id(self)

    def node_id(self):

        localctx = DOTParser.Node_idContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_node_id)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 106
            self.id_()
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.T__9:
                self.state = 107
                self.port()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PortContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def id_(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(DOTParser.Id_Context)
            else:
                return self.getTypedRuleContext(DOTParser.Id_Context, i)

        def getRuleIndex(self):
            return DOTParser.RULE_port

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPort"):
                listener.enterPort(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPort"):
                listener.exitPort(self)

    def port(self):

        localctx = DOTParser.PortContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_port)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(DOTParser.T__9)
            self.state = 111
            self.id_()
            self.state = 114
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.T__9:
                self.state = 112
                self.match(DOTParser.T__9)
                self.state = 113
                self.id_()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SubgraphContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt_list(self):
            return self.getTypedRuleContext(DOTParser.Stmt_listContext, 0)

        def SUBGRAPH(self):
            return self.getToken(DOTParser.SUBGRAPH, 0)

        def id_(self):
            return self.getTypedRuleContext(DOTParser.Id_Context, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_subgraph

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterSubgraph"):
                listener.enterSubgraph(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitSubgraph"):
                listener.exitSubgraph(self)

    def subgraph(self):

        localctx = DOTParser.SubgraphContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_subgraph)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la == DOTParser.SUBGRAPH:
                self.state = 116
                self.match(DOTParser.SUBGRAPH)
                self.state = 118
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0):
                    self.state = 117
                    self.id_()

            self.state = 122
            self.match(DOTParser.T__0)
            self.state = 123
            self.stmt_list()
            self.state = 124
            self.match(DOTParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Id_Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(DOTParser.ID, 0)

        def STRING(self):
            return self.getToken(DOTParser.STRING, 0)

        def HTML_STRING(self):
            return self.getToken(DOTParser.HTML_STRING, 0)

        def NUMBER(self):
            return self.getToken(DOTParser.NUMBER, 0)

        def getRuleIndex(self):
            return DOTParser.RULE_id_

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterId_"):
                listener.enterId_(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitId_"):
                listener.exitId_(self)

    def id_(self):

        localctx = DOTParser.Id_Context(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_id_)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << DOTParser.NUMBER) | (1 << DOTParser.STRING) | (1 << DOTParser.ID) | (1 << DOTParser.HTML_STRING))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
