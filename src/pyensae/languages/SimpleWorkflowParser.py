# Generated from java-escape by ANTLR 4.5
# encoding: utf-8
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package) > 0 if package is not None else False
if ischild:
    from .SimpleWorkflowListener import SimpleWorkflowListener
else:
    from SimpleWorkflowListener import SimpleWorkflowListener


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3\35")
        buf.write("\u010e\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \3\2\7\2B\n\2\f\2\16\2E\13\2\3\2\3\2\3")
        buf.write("\3\3\3\3\3\3\3\5\3M\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\6\7a\n\7\r")
        buf.write("\7\16\7b\3\7\3\7\3\b\3\b\3\b\5\bj\n\b\3\b\3\b\7\bn\n\b")
        buf.write("\f\b\16\bq\13\b\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3")
        buf.write("\n\6\n}\n\n\r\n\16\n~\3\n\3\n\3\n\3\n\6\n\u0085\n\n\r")
        buf.write("\n\16\n\u0086\3\n\3\n\5\n\u008b\n\n\3\13\3\13\3\13\5\13")
        buf.write("\u0090\n\13\3\13\3\13\7\13\u0094\n\13\f\13\16\13\u0097")
        buf.write("\13\13\3\13\3\13\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\5")
        buf.write("\16\u00a3\n\16\3\17\3\17\3\17\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\17\3\17\5\17\u00b1\n\17\3\20\3\20\5\20\u00b5")
        buf.write("\n\20\3\21\3\21\3\21\5\21\u00ba\n\21\3\22\3\22\3\22\5")
        buf.write("\22\u00bf\n\22\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24")
        buf.write("\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\27\5\27\u00d1\n")
        buf.write("\27\3\27\3\27\7\27\u00d5\n\27\f\27\16\27\u00d8\13\27\3")
        buf.write("\30\3\30\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\33")
        buf.write("\3\33\3\34\3\34\3\34\3\34\3\35\3\35\3\35\5\35\u00ed\n")
        buf.write("\35\3\36\3\36\3\37\5\37\u00f2\n\37\3\37\3\37\3 \5 \u00f7")
        buf.write("\n \3 \3 \3 \3 \3 \5 \u00fe\n \3 \5 \u0101\n \3 \5 \u0104")
        buf.write("\n \3 \3 \3 \5 \u0109\n \3 \5 \u010c\n \3 \2\2!\2\4\6")
        buf.write("\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\66")
        buf.write("8:<>\2\4\3\2\20\21\4\2\27\27\31\31\u010b\2C\3\2\2\2\4")
        buf.write("L\3\2\2\2\6N\3\2\2\2\bQ\3\2\2\2\nV\3\2\2\2\fX\3\2\2\2")
        buf.write("\16f\3\2\2\2\20t\3\2\2\2\22v\3\2\2\2\24\u008c\3\2\2\2")
        buf.write("\26\u009a\3\2\2\2\30\u009c\3\2\2\2\32\u00a2\3\2\2\2\34")
        buf.write("\u00b0\3\2\2\2\36\u00b4\3\2\2\2 \u00b6\3\2\2\2\"\u00bb")
        buf.write("\3\2\2\2$\u00c0\3\2\2\2&\u00c4\3\2\2\2(\u00c8\3\2\2\2")
        buf.write("*\u00cd\3\2\2\2,\u00d0\3\2\2\2.\u00d9\3\2\2\2\60\u00dd")
        buf.write("\3\2\2\2\62\u00df\3\2\2\2\64\u00e1\3\2\2\2\66\u00e5\3")
        buf.write("\2\2\28\u00ec\3\2\2\2:\u00ee\3\2\2\2<\u00f1\3\2\2\2>\u010b")
        buf.write("\3\2\2\2@B\5\4\3\2A@\3\2\2\2BE\3\2\2\2CA\3\2\2\2CD\3\2")
        buf.write("\2\2DF\3\2\2\2EC\3\2\2\2FG\7\2\2\3G\3\3\2\2\2HM\5\22\n")
        buf.write("\2IM\5\f\7\2JM\5\6\4\2KM\5\30\r\2LH\3\2\2\2LI\3\2\2\2")
        buf.write("LJ\3\2\2\2LK\3\2\2\2M\5\3\2\2\2NO\5\b\5\2OP\7\3\2\2P\7")
        buf.write("\3\2\2\2QR\7\4\2\2RS\5\n\6\2ST\7\5\2\2TU\58\35\2U\t\3")
        buf.write("\2\2\2VW\7\27\2\2W\13\3\2\2\2XY\7\6\2\2YZ\7\7\2\2Z[\5")
        buf.write("\20\t\2[\\\7\b\2\2\\]\5\16\b\2]^\7\t\2\2^`\7\n\2\2_a\5")
        buf.write("\4\3\2`_\3\2\2\2ab\3\2\2\2b`\3\2\2\2bc\3\2\2\2cd\3\2\2")
        buf.write("\2de\7\13\2\2e\r\3\2\2\2fg\5\26\f\2gi\7\7\2\2hj\5\36\20")
        buf.write("\2ih\3\2\2\2ij\3\2\2\2jo\3\2\2\2kl\7\f\2\2ln\5\36\20\2")
        buf.write("mk\3\2\2\2nq\3\2\2\2om\3\2\2\2op\3\2\2\2pr\3\2\2\2qo\3")
        buf.write("\2\2\2rs\7\t\2\2s\17\3\2\2\2tu\7\27\2\2u\21\3\2\2\2vw")
        buf.write("\7\r\2\2wx\7\7\2\2xy\5\24\13\2yz\7\t\2\2z|\7\n\2\2{}\5")
        buf.write("\4\3\2|{\3\2\2\2}~\3\2\2\2~|\3\2\2\2~\177\3\2\2\2\177")
        buf.write("\u0080\3\2\2\2\u0080\u008a\7\13\2\2\u0081\u0082\7\16\2")
        buf.write("\2\u0082\u0084\7\n\2\2\u0083\u0085\5\4\3\2\u0084\u0083")
        buf.write("\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0084\3\2\2\2\u0086")
        buf.write("\u0087\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7\13\2")
        buf.write("\2\u0089\u008b\3\2\2\2\u008a\u0081\3\2\2\2\u008a\u008b")
        buf.write("\3\2\2\2\u008b\23\3\2\2\2\u008c\u008d\5\26\f\2\u008d\u008f")
        buf.write("\7\7\2\2\u008e\u0090\5\36\20\2\u008f\u008e\3\2\2\2\u008f")
        buf.write("\u0090\3\2\2\2\u0090\u0095\3\2\2\2\u0091\u0092\7\f\2\2")
        buf.write("\u0092\u0094\5\36\20\2\u0093\u0091\3\2\2\2\u0094\u0097")
        buf.write("\3\2\2\2\u0095\u0093\3\2\2\2\u0095\u0096\3\2\2\2\u0096")
        buf.write("\u0098\3\2\2\2\u0097\u0095\3\2\2\2\u0098\u0099\7\t\2\2")
        buf.write("\u0099\25\3\2\2\2\u009a\u009b\7\27\2\2\u009b\27\3\2\2")
        buf.write("\2\u009c\u009d\5\32\16\2\u009d\u009e\7\3\2\2\u009e\31")
        buf.write("\3\2\2\2\u009f\u00a3\5\34\17\2\u00a0\u00a3\5$\23\2\u00a1")
        buf.write("\u00a3\5&\24\2\u00a2\u009f\3\2\2\2\u00a2\u00a0\3\2\2\2")
        buf.write("\u00a2\u00a1\3\2\2\2\u00a3\33\3\2\2\2\u00a4\u00a5\7\17")
        buf.write("\2\2\u00a5\u00a6\5 \21\2\u00a6\u00a7\t\2\2\2\u00a7\u00a8")
        buf.write("\5\"\22\2\u00a8\u00b1\3\2\2\2\u00a9\u00aa\7\17\2\2\u00aa")
        buf.write("\u00ab\7\7\2\2\u00ab\u00ac\5 \21\2\u00ac\u00ad\7\f\2\2")
        buf.write("\u00ad\u00ae\5\"\22\2\u00ae\u00af\7\t\2\2\u00af\u00b1")
        buf.write("\3\2\2\2\u00b0\u00a4\3\2\2\2\u00b0\u00a9\3\2\2\2\u00b1")
        buf.write("\35\3\2\2\2\u00b2\u00b5\5 \21\2\u00b3\u00b5\58\35\2\u00b4")
        buf.write("\u00b2\3\2\2\2\u00b4\u00b3\3\2\2\2\u00b5\37\3\2\2\2\u00b6")
        buf.write("\u00b9\5*\26\2\u00b7\u00b8\7\22\2\2\u00b8\u00ba\5\62\32")
        buf.write("\2\u00b9\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba!\3\2")
        buf.write("\2\2\u00bb\u00be\5*\26\2\u00bc\u00bd\7\22\2\2\u00bd\u00bf")
        buf.write("\5\62\32\2\u00be\u00bc\3\2\2\2\u00be\u00bf\3\2\2\2\u00bf")
        buf.write("#\3\2\2\2\u00c0\u00c1\5*\26\2\u00c1\u00c2\7\5\2\2\u00c2")
        buf.write("\u00c3\5\66\34\2\u00c3%\3\2\2\2\u00c4\u00c5\5*\26\2\u00c5")
        buf.write("\u00c6\7\5\2\2\u00c6\u00c7\5(\25\2\u00c7\'\3\2\2\2\u00c8")
        buf.write("\u00c9\5\64\33\2\u00c9\u00ca\7\7\2\2\u00ca\u00cb\5,\27")
        buf.write("\2\u00cb\u00cc\7\t\2\2\u00cc)\3\2\2\2\u00cd\u00ce\7\27")
        buf.write("\2\2\u00ce+\3\2\2\2\u00cf\u00d1\5.\30\2\u00d0\u00cf\3")
        buf.write("\2\2\2\u00d0\u00d1\3\2\2\2\u00d1\u00d6\3\2\2\2\u00d2\u00d3")
        buf.write("\7\f\2\2\u00d3\u00d5\5.\30\2\u00d4\u00d2\3\2\2\2\u00d5")
        buf.write("\u00d8\3\2\2\2\u00d6\u00d4\3\2\2\2\u00d6\u00d7\3\2\2\2")
        buf.write("\u00d7-\3\2\2\2\u00d8\u00d6\3\2\2\2\u00d9\u00da\5\60\31")
        buf.write("\2\u00da\u00db\7\5\2\2\u00db\u00dc\58\35\2\u00dc/\3\2")
        buf.write("\2\2\u00dd\u00de\7\27\2\2\u00de\61\3\2\2\2\u00df\u00e0")
        buf.write("\7\27\2\2\u00e0\63\3\2\2\2\u00e1\u00e2\7\23\2\2\u00e2")
        buf.write("\u00e3\7\22\2\2\u00e3\u00e4\t\3\2\2\u00e4\65\3\2\2\2\u00e5")
        buf.write("\u00e6\7\24\2\2\u00e6\u00e7\7\22\2\2\u00e7\u00e8\t\3\2")
        buf.write("\2\u00e8\67\3\2\2\2\u00e9\u00ed\5<\37\2\u00ea\u00ed\5")
        buf.write("> \2\u00eb\u00ed\5:\36\2\u00ec\u00e9\3\2\2\2\u00ec\u00ea")
        buf.write("\3\2\2\2\u00ec\u00eb\3\2\2\2\u00ed9\3\2\2\2\u00ee\u00ef")
        buf.write("\7\31\2\2\u00ef;\3\2\2\2\u00f0\u00f2\7\30\2\2\u00f1\u00f0")
        buf.write("\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f3\3\2\2\2\u00f3")
        buf.write("\u00f4\7\26\2\2\u00f4=\3\2\2\2\u00f5\u00f7\7\30\2\2\u00f6")
        buf.write("\u00f5\3\2\2\2\u00f6\u00f7\3\2\2\2\u00f7\u00f8\3\2\2\2")
        buf.write("\u00f8\u00f9\7\26\2\2\u00f9\u00fa\7\22\2\2\u00fa\u0100")
        buf.write("\7\26\2\2\u00fb\u00fd\7\25\2\2\u00fc\u00fe\7\30\2\2\u00fd")
        buf.write("\u00fc\3\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00ff\3\2\2\2")
        buf.write("\u00ff\u0101\7\26\2\2\u0100\u00fb\3\2\2\2\u0100\u0101")
        buf.write("\3\2\2\2\u0101\u010c\3\2\2\2\u0102\u0104\7\30\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0103\u0104\3\2\2\2\u0104\u0105\3\2\2\2")
        buf.write("\u0105\u0106\7\26\2\2\u0106\u0108\7\25\2\2\u0107\u0109")
        buf.write("\7\30\2\2\u0108\u0107\3\2\2\2\u0108\u0109\3\2\2\2\u0109")
        buf.write("\u010a\3\2\2\2\u010a\u010c\7\26\2\2\u010b\u00f6\3\2\2")
        buf.write("\2\u010b\u0103\3\2\2\2\u010c?\3\2\2\2\33CLbio~\u0086\u008a")
        buf.write("\u008f\u0095\u00a2\u00b0\u00b4\u00b9\u00be\u00d0\u00d6")
        buf.write("\u00ec\u00f1\u00f6\u00fd\u0100\u0103\u0108\u010b")
        return buf.getvalue()


class SimpleWorkflowParser (Parser):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = [u"<INVALID>", u"';'", u"'set'", u"'='", u"'for'", u"'('",
                    u"'in'", u"')'", u"'{'", u"'}'", u"','", u"'if'", u"'else'",
                    u"'connect'", u"'to'", u"'->'", u"'.'", u"'flowmodule'",
                    u"'flowdata'", u"'e'"]

    symbolicNames = [u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>",
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>",
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>",
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>",
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>",
                     u"Digits", u"Identifier", u"Sign", u"STRING", u"STRING_DOUBLE_QUOTE",
                     u"STRING_QUOTE", u"LINE_COMMENT", u"WS"]

    RULE_parse = 0
    RULE_final_stmt = 1
    RULE_affectation_stmt_comma = 2
    RULE_affectation_stmt = 3
    RULE_variable_name = 4
    RULE_for_stmt = 5
    RULE_range_function = 6
    RULE_loop_variable = 7
    RULE_if_stmt = 8
    RULE_condition = 9
    RULE_evaluation_function = 10
    RULE_stmt_comma = 11
    RULE_stmt = 12
    RULE_connect_stmt = 13
    RULE_data_or_module_output_constant = 14
    RULE_data_or_module_output = 15
    RULE_module_input = 16
    RULE_data_stmt = 17
    RULE_module_stmt = 18
    RULE_module_call = 19
    RULE_element_name = 20
    RULE_list_param_affectation = 21
    RULE_param_affectation = 22
    RULE_param_name = 23
    RULE_inout_name = 24
    RULE_module_name = 25
    RULE_data_name = 26
    RULE_constant = 27
    RULE_string_literal = 28
    RULE_integer_number = 29
    RULE_real_number = 30

    ruleNames = ["parse", "final_stmt", "affectation_stmt_comma", "affectation_stmt",
                 "variable_name", "for_stmt", "range_function", "loop_variable",
                 "if_stmt", "condition", "evaluation_function", "stmt_comma",
                 "stmt", "connect_stmt", "data_or_module_output_constant",
                 "data_or_module_output", "module_input", "data_stmt",
                 "module_stmt", "module_call", "element_name", "list_param_affectation",
                 "param_affectation", "param_name", "inout_name", "module_name",
                 "data_name", "constant", "string_literal", "integer_number",
                 "real_number"]

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
    T__10 = 11
    T__11 = 12
    T__12 = 13
    T__13 = 14
    T__14 = 15
    T__15 = 16
    T__16 = 17
    T__17 = 18
    T__18 = 19
    Digits = 20
    Identifier = 21
    Sign = 22
    STRING = 23
    STRING_DOUBLE_QUOTE = 24
    STRING_QUOTE = 25
    LINE_COMMENT = 26
    WS = 27

    def __init__(self, input: TokenStream):
        super().__init__(input)
        self.checkVersion("4.5")
        self._interp = ParserATNSimulator(
            self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SimpleWorkflowParser.EOF, 0)

        def final_stmt(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_parse

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterParse(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitParse(self)

    def parse(self):

        localctx = SimpleWorkflowParser.ParseContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 65
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__10) | (1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.Identifier))) != 0):
                self.state = 62
                self.final_stmt()
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 68
            self.match(SimpleWorkflowParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Final_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def if_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.If_stmtContext, 0)

        def for_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.For_stmtContext, 0)

        def affectation_stmt_comma(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Affectation_stmt_commaContext, 0)

        def stmt_comma(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Stmt_commaContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_final_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterFinal_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitFinal_stmt(self)

    def final_stmt(self):

        localctx = SimpleWorkflowParser.Final_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_final_stmt)
        try:
            self.state = 74
            token = self._input.LA(1)
            if token in [SimpleWorkflowParser.T__10]:
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.if_stmt()

            elif token in [SimpleWorkflowParser.T__3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.for_stmt()

            elif token in [SimpleWorkflowParser.T__1]:
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.affectation_stmt_comma()

            elif token in [SimpleWorkflowParser.T__12, SimpleWorkflowParser.Identifier]:
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.stmt_comma()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Affectation_stmt_commaContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def affectation_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Affectation_stmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_affectation_stmt_comma

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterAffectation_stmt_comma(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitAffectation_stmt_comma(self)

    def affectation_stmt_comma(self):

        localctx = SimpleWorkflowParser.Affectation_stmt_commaContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_affectation_stmt_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.affectation_stmt()
            self.state = 77
            self.match(SimpleWorkflowParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Affectation_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Variable_nameContext, 0)

        def constant(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ConstantContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_affectation_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterAffectation_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitAffectation_stmt(self)

    def affectation_stmt(self):

        localctx = SimpleWorkflowParser.Affectation_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_affectation_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self.match(SimpleWorkflowParser.T__1)
            self.state = 80
            self.variable_name()
            self.state = 81
            self.match(SimpleWorkflowParser.T__2)
            self.state = 82
            self.constant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_variable_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterVariable_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitVariable_name(self)

    def variable_name(self):

        localctx = SimpleWorkflowParser.Variable_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class For_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def loop_variable(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Loop_variableContext, 0)

        def range_function(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Range_functionContext, 0)

        def final_stmt(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_for_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterFor_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitFor_stmt(self)

    def for_stmt(self):

        localctx = SimpleWorkflowParser.For_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_for_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(SimpleWorkflowParser.T__3)
            self.state = 87
            self.match(SimpleWorkflowParser.T__4)
            self.state = 88
            self.loop_variable()
            self.state = 89
            self.match(SimpleWorkflowParser.T__5)
            self.state = 90
            self.range_function()
            self.state = 91
            self.match(SimpleWorkflowParser.T__6)
            self.state = 92
            self.match(SimpleWorkflowParser.T__7)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 93
                self.final_stmt()
                self.state = 96
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__10) | (1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                    break

            self.state = 98
            self.match(SimpleWorkflowParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Range_functionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evaluation_function(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Evaluation_functionContext, 0)

        def data_or_module_output_constant(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Data_or_module_output_constantContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_output_constantContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_range_function

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterRange_function(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitRange_function(self)

    def range_function(self):

        localctx = SimpleWorkflowParser.Range_functionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_range_function)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.evaluation_function()
            self.state = 101
            self.match(SimpleWorkflowParser.T__4)
            self.state = 103
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.Digits) | (1 << SimpleWorkflowParser.Identifier) | (1 << SimpleWorkflowParser.Sign) | (1 << SimpleWorkflowParser.STRING))) != 0):
                self.state = 102
                self.data_or_module_output_constant()

            self.state = 109
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SimpleWorkflowParser.T__9:
                self.state = 105
                self.match(SimpleWorkflowParser.T__9)
                self.state = 106
                self.data_or_module_output_constant()
                self.state = 111
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 112
            self.match(SimpleWorkflowParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Loop_variableContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_loop_variable

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterLoop_variable(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitLoop_variable(self)

    def loop_variable(self):

        localctx = SimpleWorkflowParser.Loop_variableContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_loop_variable)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 114
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class If_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def condition(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ConditionContext, 0)

        def final_stmt(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Final_stmtContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Final_stmtContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_if_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterIf_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitIf_stmt(self)

    def if_stmt(self):

        localctx = SimpleWorkflowParser.If_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_if_stmt)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 116
            self.match(SimpleWorkflowParser.T__10)
            self.state = 117
            self.match(SimpleWorkflowParser.T__4)
            self.state = 118
            self.condition()
            self.state = 119
            self.match(SimpleWorkflowParser.T__6)
            self.state = 120
            self.match(SimpleWorkflowParser.T__7)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 121
                self.final_stmt()
                self.state = 124
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__10) | (1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                    break

            self.state = 126
            self.match(SimpleWorkflowParser.T__8)
            self.state = 136
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__11:
                self.state = 127
                self.match(SimpleWorkflowParser.T__11)
                self.state = 128
                self.match(SimpleWorkflowParser.T__7)
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 129
                    self.final_stmt()
                    self.state = 132
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.T__1) | (1 << SimpleWorkflowParser.T__3) | (1 << SimpleWorkflowParser.T__10) | (1 << SimpleWorkflowParser.T__12) | (1 << SimpleWorkflowParser.Identifier))) != 0)):
                        break

                self.state = 134
                self.match(SimpleWorkflowParser.T__8)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConditionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def evaluation_function(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Evaluation_functionContext, 0)

        def data_or_module_output_constant(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Data_or_module_output_constantContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_output_constantContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_condition

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterCondition(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitCondition(self)

    def condition(self):

        localctx = SimpleWorkflowParser.ConditionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_condition)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.evaluation_function()
            self.state = 139
            self.match(SimpleWorkflowParser.T__4)
            self.state = 141
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SimpleWorkflowParser.Digits) | (1 << SimpleWorkflowParser.Identifier) | (1 << SimpleWorkflowParser.Sign) | (1 << SimpleWorkflowParser.STRING))) != 0):
                self.state = 140
                self.data_or_module_output_constant()

            self.state = 147
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SimpleWorkflowParser.T__9:
                self.state = 143
                self.match(SimpleWorkflowParser.T__9)
                self.state = 144
                self.data_or_module_output_constant()
                self.state = 149
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 150
            self.match(SimpleWorkflowParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Evaluation_functionContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_evaluation_function

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterEvaluation_function(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitEvaluation_function(self)

    def evaluation_function(self):

        localctx = SimpleWorkflowParser.Evaluation_functionContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_evaluation_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 152
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Stmt_commaContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.StmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_stmt_comma

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterStmt_comma(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitStmt_comma(self)

    def stmt_comma(self):

        localctx = SimpleWorkflowParser.Stmt_commaContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_stmt_comma)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 154
            self.stmt()
            self.state = 155
            self.match(SimpleWorkflowParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def connect_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Connect_stmtContext, 0)

        def data_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_stmtContext, 0)

        def module_stmt(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_stmtContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterStmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitStmt(self)

    def stmt(self):

        localctx = SimpleWorkflowParser.StmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_stmt)
        try:
            self.state = 160
            la_ = self._interp.adaptivePredict(self._input, 10, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 157
                self.connect_stmt()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 158
                self.data_stmt()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 159
                self.module_stmt()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Connect_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_or_module_output(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_outputContext, 0)

        def module_input(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_inputContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_connect_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterConnect_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitConnect_stmt(self)

    def connect_stmt(self):

        localctx = SimpleWorkflowParser.Connect_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_connect_stmt)
        self._la = 0  # Token type
        try:
            self.state = 174
            la_ = self._interp.adaptivePredict(self._input, 11, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(SimpleWorkflowParser.T__12)
                self.state = 163
                self.data_or_module_output()
                self.state = 164
                _la = self._input.LA(1)
                if not(_la == SimpleWorkflowParser.T__13 or _la == SimpleWorkflowParser.T__14):
                    self._errHandler.recoverInline(self)
                else:
                    self.consume()
                self.state = 165
                self.module_input()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 167
                self.match(SimpleWorkflowParser.T__12)
                self.state = 168
                self.match(SimpleWorkflowParser.T__4)
                self.state = 169
                self.data_or_module_output()
                self.state = 170
                self.match(SimpleWorkflowParser.T__9)
                self.state = 171
                self.module_input()
                self.state = 172
                self.match(SimpleWorkflowParser.T__6)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_or_module_output_constantContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def data_or_module_output(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_or_module_outputContext, 0)

        def constant(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ConstantContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_or_module_output_constant

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterData_or_module_output_constant(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitData_or_module_output_constant(self)

    def data_or_module_output_constant(self):

        localctx = SimpleWorkflowParser.Data_or_module_output_constantContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_data_or_module_output_constant)
        try:
            self.state = 178
            token = self._input.LA(1)
            if token in [SimpleWorkflowParser.Identifier]:
                self.enterOuterAlt(localctx, 1)
                self.state = 176
                self.data_or_module_output()

            elif token in [SimpleWorkflowParser.Digits, SimpleWorkflowParser.Sign, SimpleWorkflowParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 177
                self.constant()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_or_module_outputContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def inout_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Inout_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_or_module_output

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterData_or_module_output(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitData_or_module_output(self)

    def data_or_module_output(self):

        localctx = SimpleWorkflowParser.Data_or_module_outputContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_data_or_module_output)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
            self.element_name()
            self.state = 183
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__15:
                self.state = 181
                self.match(SimpleWorkflowParser.T__15)
                self.state = 182
                self.inout_name()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_inputContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def inout_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Inout_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_input

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterModule_input(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitModule_input(self)

    def module_input(self):

        localctx = SimpleWorkflowParser.Module_inputContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_module_input)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 185
            self.element_name()
            self.state = 188
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.T__15:
                self.state = 186
                self.match(SimpleWorkflowParser.T__15)
                self.state = 187
                self.inout_name()

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def data_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Data_nameContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterData_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitData_stmt(self)

    def data_stmt(self):

        localctx = SimpleWorkflowParser.Data_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_data_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 190
            self.element_name()
            self.state = 191
            self.match(SimpleWorkflowParser.T__2)
            self.state = 192
            self.data_name()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_stmtContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def element_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Element_nameContext, 0)

        def module_call(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_callContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_stmt

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterModule_stmt(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitModule_stmt(self)

    def module_stmt(self):

        localctx = SimpleWorkflowParser.Module_stmtContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_module_stmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 194
            self.element_name()
            self.state = 195
            self.match(SimpleWorkflowParser.T__2)
            self.state = 196
            self.module_call()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_callContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def module_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Module_nameContext, 0)

        def list_param_affectation(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.List_param_affectationContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_call

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterModule_call(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitModule_call(self)

    def module_call(self):

        localctx = SimpleWorkflowParser.Module_callContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_module_call)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.module_name()
            self.state = 199
            self.match(SimpleWorkflowParser.T__4)
            self.state = 200
            self.list_param_affectation()
            self.state = 201
            self.match(SimpleWorkflowParser.T__6)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Element_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_element_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterElement_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitElement_name(self)

    def element_name(self):

        localctx = SimpleWorkflowParser.Element_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_element_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 203
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class List_param_affectationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_affectation(self, i: int=None):
            if i is None:
                return self.getTypedRuleContexts(SimpleWorkflowParser.Param_affectationContext)
            else:
                return self.getTypedRuleContext(SimpleWorkflowParser.Param_affectationContext, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_list_param_affectation

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterList_param_affectation(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitList_param_affectation(self)

    def list_param_affectation(self):

        localctx = SimpleWorkflowParser.List_param_affectationContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_list_param_affectation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.Identifier:
                self.state = 205
                self.param_affectation()

            self.state = 212
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la == SimpleWorkflowParser.T__9:
                self.state = 208
                self.match(SimpleWorkflowParser.T__9)
                self.state = 209
                self.param_affectation()
                self.state = 214
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_affectationContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param_name(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Param_nameContext, 0)

        def constant(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.ConstantContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_param_affectation

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterParam_affectation(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitParam_affectation(self)

    def param_affectation(self):

        localctx = SimpleWorkflowParser.Param_affectationContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_param_affectation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 215
            self.param_name()
            self.state = 216
            self.match(SimpleWorkflowParser.T__2)
            self.state = 217
            self.constant()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Param_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_param_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterParam_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitParam_name(self)

    def param_name(self):

        localctx = SimpleWorkflowParser.Param_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_param_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 219
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Inout_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_inout_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterInout_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitInout_name(self)

    def inout_name(self):

        localctx = SimpleWorkflowParser.Inout_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_inout_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 221
            self.match(SimpleWorkflowParser.Identifier)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Module_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_module_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterModule_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitModule_name(self)

    def module_name(self):

        localctx = SimpleWorkflowParser.Module_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_module_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 223
            self.match(SimpleWorkflowParser.T__16)
            self.state = 224
            self.match(SimpleWorkflowParser.T__15)
            self.state = 225
            _la = self._input.LA(1)
            if not(_la == SimpleWorkflowParser.Identifier or _la == SimpleWorkflowParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_nameContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Identifier(self):
            return self.getToken(SimpleWorkflowParser.Identifier, 0)

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_data_name

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterData_name(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitData_name(self)

    def data_name(self):

        localctx = SimpleWorkflowParser.Data_nameContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_data_name)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 227
            self.match(SimpleWorkflowParser.T__17)
            self.state = 228
            self.match(SimpleWorkflowParser.T__15)
            self.state = 229
            _la = self._input.LA(1)
            if not(_la == SimpleWorkflowParser.Identifier or _la == SimpleWorkflowParser.STRING):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ConstantContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def integer_number(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Integer_numberContext, 0)

        def real_number(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.Real_numberContext, 0)

        def string_literal(self):
            return self.getTypedRuleContext(SimpleWorkflowParser.String_literalContext, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_constant

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterConstant(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitConstant(self)

    def constant(self):

        localctx = SimpleWorkflowParser.ConstantContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_constant)
        try:
            self.state = 234
            la_ = self._interp.adaptivePredict(self._input, 17, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 231
                self.integer_number()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 232
                self.real_number()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 233
                self.string_literal()
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_literalContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STRING(self):
            return self.getToken(SimpleWorkflowParser.STRING, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_string_literal

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterString_literal(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitString_literal(self)

    def string_literal(self):

        localctx = SimpleWorkflowParser.String_literalContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_string_literal)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 236
            self.match(SimpleWorkflowParser.STRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Integer_numberContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self):
            return self.getToken(SimpleWorkflowParser.Digits, 0)

        def Sign(self):
            return self.getToken(SimpleWorkflowParser.Sign, 0)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_integer_number

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterInteger_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitInteger_number(self)

    def integer_number(self):

        localctx = SimpleWorkflowParser.Integer_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_integer_number)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 239
            _la = self._input.LA(1)
            if _la == SimpleWorkflowParser.Sign:
                self.state = 238
                self.match(SimpleWorkflowParser.Sign)

            self.state = 241
            self.match(SimpleWorkflowParser.Digits)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Real_numberContext(ParserRuleContext):

        def __init__(self, parser, parent: ParserRuleContext=None, invokingState: int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def Digits(self, i: int=None):
            if i is None:
                return self.getTokens(SimpleWorkflowParser.Digits)
            else:
                return self.getToken(SimpleWorkflowParser.Digits, i)

        def Sign(self, i: int=None):
            if i is None:
                return self.getTokens(SimpleWorkflowParser.Sign)
            else:
                return self.getToken(SimpleWorkflowParser.Sign, i)

        def getRuleIndex(self):
            return SimpleWorkflowParser.RULE_real_number

        def enterRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.enterReal_number(self)

        def exitRule(self, listener: ParseTreeListener):
            if isinstance(listener, SimpleWorkflowListener):
                listener.exitReal_number(self)

    def real_number(self):

        localctx = SimpleWorkflowParser.Real_numberContext(
            self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_real_number)
        self._la = 0  # Token type
        try:
            self.state = 265
            la_ = self._interp.adaptivePredict(self._input, 24, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 244
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 243
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 246
                self.match(SimpleWorkflowParser.Digits)
                self.state = 247
                self.match(SimpleWorkflowParser.T__15)
                self.state = 248
                self.match(SimpleWorkflowParser.Digits)
                self.state = 254
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.T__18:
                    self.state = 249
                    self.match(SimpleWorkflowParser.T__18)
                    self.state = 251
                    _la = self._input.LA(1)
                    if _la == SimpleWorkflowParser.Sign:
                        self.state = 250
                        self.match(SimpleWorkflowParser.Sign)

                    self.state = 253
                    self.match(SimpleWorkflowParser.Digits)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 257
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 256
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 259
                self.match(SimpleWorkflowParser.Digits)
                self.state = 260
                self.match(SimpleWorkflowParser.T__18)
                self.state = 262
                _la = self._input.LA(1)
                if _la == SimpleWorkflowParser.Sign:
                    self.state = 261
                    self.match(SimpleWorkflowParser.Sign)

                self.state = 264
                self.match(SimpleWorkflowParser.Digits)
                pass

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
