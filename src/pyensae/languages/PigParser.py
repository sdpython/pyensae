# Generated from java-escape by ANTLR 4.4
from antlr4 import *
from io import StringIO
package = globals().get("__package__", None)
ischild = len(package)>0 if package is not None else False
if ischild:
    from .PigListener import PigListener
else:
    from PigListener import PigListener
def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3f")
        buf.write("\u0202\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36")
        buf.write("\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t")
        buf.write("&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.\t.\4")
        buf.write("/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\3\2\3\2\3")
        buf.write("\2\3\3\3\3\7\3l\n\3\f\3\16\3o\13\3\3\3\3\3\5\3s\n\3\3")
        buf.write("\3\3\3\7\3w\n\3\f\3\16\3z\13\3\3\4\3\4\3\4\5\4\177\n\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\5\4\u0087\n\4\3\4\3\4\5\4\u008b")
        buf.write("\n\4\3\5\3\5\3\6\3\6\3\6\3\6\5\6\u0093\n\6\3\7\3\7\3\7")
        buf.write("\3\7\5\7\u0099\n\7\3\7\5\7\u009c\n\7\3\b\3\b\3\t\3\t\3")
        buf.write("\t\3\n\3\n\3\n\3\n\7\n\u00a7\n\n\f\n\16\n\u00aa\13\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\6\n\u00b1\n\n\r\n\16\n\u00b2\5\n\u00b5")
        buf.write("\n\n\3\13\3\13\3\13\5\13\u00ba\n\13\3\13\3\13\3\13\3\13")
        buf.write("\5\13\u00c0\n\13\5\13\u00c2\n\13\3\f\3\f\3\f\3\f\5\f\u00c8")
        buf.write("\n\f\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\17\3\20\3\20\3")
        buf.write("\20\3\20\3\21\3\21\3\21\5\21\u00d9\n\21\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\5\21\u00e1\n\21\5\21\u00e3\n\21\3\22\3")
        buf.write("\22\3\22\7\22\u00e8\n\22\f\22\16\22\u00eb\13\22\3\22\6")
        buf.write("\22\u00ee\n\22\r\22\16\22\u00ef\5\22\u00f2\n\22\3\23\3")
        buf.write("\23\3\23\7\23\u00f7\n\23\f\23\16\23\u00fa\13\23\3\23\6")
        buf.write("\23\u00fd\n\23\r\23\16\23\u00fe\5\23\u0101\n\23\3\24\3")
        buf.write("\24\3\24\3\24\3\24\3\24\5\24\u0109\n\24\3\25\3\25\3\25")
        buf.write("\3\25\3\25\3\26\3\26\3\27\3\27\3\27\7\27\u0115\n\27\f")
        buf.write("\27\16\27\u0118\13\27\3\30\3\30\3\30\7\30\u011d\n\30\f")
        buf.write("\30\16\30\u0120\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\5\31\u012d\n\31\3\32\3\32\3\32")
        buf.write("\3\33\3\33\3\33\5\33\u0135\n\33\3\33\3\33\3\34\3\34\3")
        buf.write("\35\3\35\3\35\7\35\u013e\n\35\f\35\16\35\u0141\13\35\3")
        buf.write("\36\3\36\3\36\7\36\u0146\n\36\f\36\16\36\u0149\13\36\3")
        buf.write("\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37\3\37")
        buf.write("\3\37\5\37\u0157\n\37\3 \3 \3 \3 \3 \3 \5 \u015f\n \3")
        buf.write("!\3!\5!\u0163\n!\3\"\3\"\3\"\7\"\u0168\n\"\f\"\16\"\u016b")
        buf.write("\13\"\3#\3#\3#\5#\u0170\n#\3$\3$\3$\3$\3$\3$\7$\u0178")
        buf.write("\n$\f$\16$\u017b\13$\3$\3$\5$\u017f\n$\3$\3$\3$\6$\u0184")
        buf.write("\n$\r$\16$\u0185\5$\u0188\n$\3%\3%\3%\3&\3&\3&\3&\3&\3")
        buf.write("&\3&\3&\3&\3&\3&\3&\3&\3&\5&\u019b\n&\3\'\3\'\3\'\3(\3")
        buf.write("(\3(\3)\3)\5)\u01a5\n)\3*\3*\3+\3+\3+\3,\3,\3-\3-\3-\3")
        buf.write("-\5-\u01b2\n-\3.\3.\3/\3/\3/\3/\7/\u01ba\n/\f/\16/\u01bd")
        buf.write("\13/\5/\u01bf\n/\3/\3/\3/\3/\6/\u01c5\n/\r/\16/\u01c6")
        buf.write("\5/\u01c9\n/\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3\60\3")
        buf.write("\60\5\60\u01d4\n\60\3\61\3\61\3\62\3\62\3\62\3\62\7\62")
        buf.write("\u01dc\n\62\f\62\16\62\u01df\13\62\5\62\u01e1\n\62\3\62")
        buf.write("\3\62\3\62\3\62\6\62\u01e7\n\62\r\62\16\62\u01e8\5\62")
        buf.write("\u01eb\n\62\3\63\3\63\3\63\3\63\7\63\u01f1\n\63\f\63\16")
        buf.write("\63\u01f4\13\63\5\63\u01f6\n\63\3\63\3\63\3\63\3\63\6")
        buf.write("\63\u01fc\n\63\r\63\16\63\u01fd\5\63\u0200\n\63\3\63\2")
        buf.write("\3\4\64\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*")
        buf.write(",.\60\62\64\668:<>@BDFHJLNPRTVXZ\\^`bd\2\b\3\2%*\3\2Z")
        buf.write("[\4\2XY^^\4\2//EE\4\2\34\34@@\6\2//AACEaa\u0215\2f\3\2")
        buf.write("\2\2\4r\3\2\2\2\6\u008a\3\2\2\2\b\u008c\3\2\2\2\n\u0092")
        buf.write("\3\2\2\2\f\u0094\3\2\2\2\16\u009d\3\2\2\2\20\u009f\3\2")
        buf.write("\2\2\22\u00b4\3\2\2\2\24\u00c1\3\2\2\2\26\u00c7\3\2\2")
        buf.write("\2\30\u00c9\3\2\2\2\32\u00cb\3\2\2\2\34\u00ce\3\2\2\2")
        buf.write("\36\u00d1\3\2\2\2 \u00e2\3\2\2\2\"\u00f1\3\2\2\2$\u0100")
        buf.write("\3\2\2\2&\u0102\3\2\2\2(\u010a\3\2\2\2*\u010f\3\2\2\2")
        buf.write(",\u0111\3\2\2\2.\u0119\3\2\2\2\60\u012c\3\2\2\2\62\u012e")
        buf.write("\3\2\2\2\64\u0131\3\2\2\2\66\u0138\3\2\2\28\u013a\3\2")
        buf.write("\2\2:\u0142\3\2\2\2<\u0156\3\2\2\2>\u015e\3\2\2\2@\u0162")
        buf.write("\3\2\2\2B\u0164\3\2\2\2D\u016f\3\2\2\2F\u0187\3\2\2\2")
        buf.write("H\u0189\3\2\2\2J\u019a\3\2\2\2L\u019c\3\2\2\2N\u019f\3")
        buf.write("\2\2\2P\u01a4\3\2\2\2R\u01a6\3\2\2\2T\u01a8\3\2\2\2V\u01ab")
        buf.write("\3\2\2\2X\u01b1\3\2\2\2Z\u01b3\3\2\2\2\\\u01c8\3\2\2\2")
        buf.write("^\u01d3\3\2\2\2`\u01d5\3\2\2\2b\u01ea\3\2\2\2d\u01ff\3")
        buf.write("\2\2\2fg\5\4\3\2gh\7\2\2\3h\3\3\2\2\2im\b\3\1\2jl\5\6")
        buf.write("\4\2kj\3\2\2\2lo\3\2\2\2mk\3\2\2\2mn\3\2\2\2ns\3\2\2\2")
        buf.write("om\3\2\2\2pq\7\37\2\2qs\5\6\4\2ri\3\2\2\2rp\3\2\2\2sx")
        buf.write("\3\2\2\2tu\f\3\2\2uw\5\6\4\2vt\3\2\2\2wz\3\2\2\2xv\3\2")
        buf.write("\2\2xy\3\2\2\2y\5\3\2\2\2zx\3\2\2\2{|\5\b\5\2|}\7U\2\2")
        buf.write("}\177\3\2\2\2~{\3\2\2\2~\177\3\2\2\2\177\u0080\3\2\2\2")
        buf.write("\u0080\u0081\5\n\6\2\u0081\u0082\7M\2\2\u0082\u008b\3")
        buf.write("\2\2\2\u0083\u0084\7\37\2\2\u0084\u0086\5\6\4\2\u0085")
        buf.write("\u0087\5\b\5\2\u0086\u0085\3\2\2\2\u0086\u0087\3\2\2\2")
        buf.write("\u0087\u0088\3\2\2\2\u0088\u0089\5\n\6\2\u0089\u008b\3")
        buf.write("\2\2\2\u008a~\3\2\2\2\u008a\u0083\3\2\2\2\u008b\7\3\2")
        buf.write("\2\2\u008c\u008d\7@\2\2\u008d\t\3\2\2\2\u008e\u0093\5")
        buf.write("\f\7\2\u008f\u0093\5&\24\2\u0090\u0093\5(\25\2\u0091\u0093")
        buf.write("\5N(\2\u0092\u008e\3\2\2\2\u0092\u008f\3\2\2\2\u0092\u0090")
        buf.write("\3\2\2\2\u0092\u0091\3\2\2\2\u0093\13\3\2\2\2\u0094\u0095")
        buf.write("\7\4\2\2\u0095\u0098\5\16\b\2\u0096\u0097\7\25\2\2\u0097")
        buf.write("\u0099\5 \21\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009b\3\2\2\2\u009a\u009c\5\20\t\2\u009b\u009a")
        buf.write("\3\2\2\2\u009b\u009c\3\2\2\2\u009c\r\3\2\2\2\u009d\u009e")
        buf.write("\7E\2\2\u009e\17\3\2\2\2\u009f\u00a0\7\23\2\2\u00a0\u00a1")
        buf.write("\5\22\n\2\u00a1\21\3\2\2\2\u00a2\u00a3\7N\2\2\u00a3\u00a8")
        buf.write("\5\24\13\2\u00a4\u00a5\7V\2\2\u00a5\u00a7\5\24\13\2\u00a6")
        buf.write("\u00a4\3\2\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00a6\3\2\2\2")
        buf.write("\u00a8\u00a9\3\2\2\2\u00a9\u00ab\3\2\2\2\u00aa\u00a8\3")
        buf.write("\2\2\2\u00ab\u00ac\7O\2\2\u00ac\u00b5\3\2\2\2\u00ad\u00ae")
        buf.write("\7\37\2\2\u00ae\u00b0\5\22\n\2\u00af\u00b1\5\24\13\2\u00b0")
        buf.write("\u00af\3\2\2\2\u00b1\u00b2\3\2\2\2\u00b2\u00b0\3\2\2\2")
        buf.write("\u00b2\u00b3\3\2\2\2\u00b3\u00b5\3\2\2\2\u00b4\u00a2\3")
        buf.write("\2\2\2\u00b4\u00ad\3\2\2\2\u00b5\23\3\2\2\2\u00b6\u00b9")
        buf.write("\7@\2\2\u00b7\u00b8\7L\2\2\u00b8\u00ba\5\26\f\2\u00b9")
        buf.write("\u00b7\3\2\2\2\u00b9\u00ba\3\2\2\2\u00ba\u00c2\3\2\2\2")
        buf.write("\u00bb\u00bc\7\37\2\2\u00bc\u00bd\5\24\13\2\u00bd\u00bf")
        buf.write("\7@\2\2\u00be\u00c0\5\26\f\2\u00bf\u00be\3\2\2\2\u00bf")
        buf.write("\u00c0\3\2\2\2\u00c0\u00c2\3\2\2\2\u00c1\u00b6\3\2\2\2")
        buf.write("\u00c1\u00bb\3\2\2\2\u00c2\25\3\2\2\2\u00c3\u00c8\5\30")
        buf.write("\r\2\u00c4\u00c8\5\32\16\2\u00c5\u00c8\5\34\17\2\u00c6")
        buf.write("\u00c8\5\36\20\2\u00c7\u00c3\3\2\2\2\u00c7\u00c4\3\2\2")
        buf.write("\2\u00c7\u00c5\3\2\2\2\u00c7\u00c6\3\2\2\2\u00c8\27\3")
        buf.write("\2\2\2\u00c9\u00ca\t\2\2\2\u00ca\31\3\2\2\2\u00cb\u00cc")
        buf.write("\5d\63\2\u00cc\u00cd\5\22\n\2\u00cd\33\3\2\2\2\u00ce\u00cf")
        buf.write("\7+\2\2\u00cf\u00d0\5\22\n\2\u00d0\35\3\2\2\2\u00d1\u00d2")
        buf.write("\7-\2\2\u00d2\u00d3\7R\2\2\u00d3\u00d4\7S\2\2\u00d4\37")
        buf.write("\3\2\2\2\u00d5\u00d6\5\"\22\2\u00d6\u00d8\7N\2\2\u00d7")
        buf.write("\u00d9\5$\23\2\u00d8\u00d7\3\2\2\2\u00d8\u00d9\3\2\2\2")
        buf.write("\u00d9\u00da\3\2\2\2\u00da\u00db\7O\2\2\u00db\u00e3\3")
        buf.write("\2\2\2\u00dc\u00dd\7\37\2\2\u00dd\u00de\7]\2\2\u00de\u00e0")
        buf.write("\5\"\22\2\u00df\u00e1\5$\23\2\u00e0\u00df\3\2\2\2\u00e0")
        buf.write("\u00e1\3\2\2\2\u00e1\u00e3\3\2\2\2\u00e2\u00d5\3\2\2\2")
        buf.write("\u00e2\u00dc\3\2\2\2\u00e3!\3\2\2\2\u00e4\u00e9\7@\2\2")
        buf.write("\u00e5\u00e6\7W\2\2\u00e6\u00e8\7@\2\2\u00e7\u00e5\3\2")
        buf.write("\2\2\u00e8\u00eb\3\2\2\2\u00e9\u00e7\3\2\2\2\u00e9\u00ea")
        buf.write("\3\2\2\2\u00ea\u00f2\3\2\2\2\u00eb\u00e9\3\2\2\2\u00ec")
        buf.write("\u00ee\7@\2\2\u00ed\u00ec\3\2\2\2\u00ee\u00ef\3\2\2\2")
        buf.write("\u00ef\u00ed\3\2\2\2\u00ef\u00f0\3\2\2\2\u00f0\u00f2\3")
        buf.write("\2\2\2\u00f1\u00e4\3\2\2\2\u00f1\u00ed\3\2\2\2\u00f2#")
        buf.write("\3\2\2\2\u00f3\u00f8\7E\2\2\u00f4\u00f5\7V\2\2\u00f5\u00f7")
        buf.write("\7E\2\2\u00f6\u00f4\3\2\2\2\u00f7\u00fa\3\2\2\2\u00f8")
        buf.write("\u00f6\3\2\2\2\u00f8\u00f9\3\2\2\2\u00f9\u0101\3\2\2\2")
        buf.write("\u00fa\u00f8\3\2\2\2\u00fb\u00fd\7E\2\2\u00fc\u00fb\3")
        buf.write("\2\2\2\u00fd\u00fe\3\2\2\2\u00fe\u00fc\3\2\2\2\u00fe\u00ff")
        buf.write("\3\2\2\2\u00ff\u0101\3\2\2\2\u0100\u00f3\3\2\2\2\u0100")
        buf.write("\u00fc\3\2\2\2\u0101%\3\2\2\2\u0102\u0103\7\62\2\2\u0103")
        buf.write("\u0104\5\b\5\2\u0104\u0105\7\17\2\2\u0105\u0108\5\16\b")
        buf.write("\2\u0106\u0107\7\25\2\2\u0107\u0109\5 \21\2\u0108\u0106")
        buf.write("\3\2\2\2\u0108\u0109\3\2\2\2\u0109\'\3\2\2\2\u010a\u010b")
        buf.write("\7\5\2\2\u010b\u010c\5\b\5\2\u010c\u010d\7\24\2\2\u010d")
        buf.write("\u010e\5*\26\2\u010e)\3\2\2\2\u010f\u0110\5,\27\2\u0110")
        buf.write("+\3\2\2\2\u0111\u0116\5.\30\2\u0112\u0113\7\36\2\2\u0113")
        buf.write("\u0115\5.\30\2\u0114\u0112\3\2\2\2\u0115\u0118\3\2\2\2")
        buf.write("\u0116\u0114\3\2\2\2\u0116\u0117\3\2\2\2\u0117-\3\2\2")
        buf.write("\2\u0118\u0116\3\2\2\2\u0119\u011e\5\60\31\2\u011a\u011b")
        buf.write("\7\35\2\2\u011b\u011d\5\60\31\2\u011c\u011a\3\2\2\2\u011d")
        buf.write("\u0120\3\2\2\2\u011e\u011c\3\2\2\2\u011e\u011f\3\2\2\2")
        buf.write("\u011f/\3\2\2\2\u0120\u011e\3\2\2\2\u0121\u0122\7N\2\2")
        buf.write("\u0122\u0123\5*\26\2\u0123\u0124\7O\2\2\u0124\u012d\3")
        buf.write("\2\2\2\u0125\u0126\5\66\34\2\u0126\u0127\7K\2\2\u0127")
        buf.write("\u0128\5\66\34\2\u0128\u012d\3\2\2\2\u0129\u012d\5 \21")
        buf.write("\2\u012a\u012d\5\64\33\2\u012b\u012d\5\62\32\2\u012c\u0121")
        buf.write("\3\2\2\2\u012c\u0125\3\2\2\2\u012c\u0129\3\2\2\2\u012c")
        buf.write("\u012a\3\2\2\2\u012c\u012b\3\2\2\2\u012d\61\3\2\2\2\u012e")
        buf.write("\u012f\7\37\2\2\u012f\u0130\5\60\31\2\u0130\63\3\2\2\2")
        buf.write("\u0131\u0132\5\66\34\2\u0132\u0134\7.\2\2\u0133\u0135")
        buf.write("\7\37\2\2\u0134\u0133\3\2\2\2\u0134\u0135\3\2\2\2\u0135")
        buf.write("\u0136\3\2\2\2\u0136\u0137\7/\2\2\u0137\65\3\2\2\2\u0138")
        buf.write("\u0139\58\35\2\u0139\67\3\2\2\2\u013a\u013f\5:\36\2\u013b")
        buf.write("\u013c\t\3\2\2\u013c\u013e\5:\36\2\u013d\u013b\3\2\2\2")
        buf.write("\u013e\u0141\3\2\2\2\u013f\u013d\3\2\2\2\u013f\u0140\3")
        buf.write("\2\2\2\u01409\3\2\2\2\u0141\u013f\3\2\2\2\u0142\u0147")
        buf.write("\5<\37\2\u0143\u0144\t\4\2\2\u0144\u0146\5<\37\2\u0145")
        buf.write("\u0143\3\2\2\2\u0146\u0149\3\2\2\2\u0147\u0145\3\2\2\2")
        buf.write("\u0147\u0148\3\2\2\2\u0148;\3\2\2\2\u0149\u0147\3\2\2")
        buf.write("\2\u014a\u014b\7N\2\2\u014b\u014c\5\26\f\2\u014c\u014d")
        buf.write("\7O\2\2\u014d\u014e\3\2\2\2\u014e\u014f\5> \2\u014f\u0157")
        buf.write("\3\2\2\2\u0150\u0151\7\37\2\2\u0151\u0152\7_\2\2\u0152")
        buf.write("\u0153\5\26\f\2\u0153\u0154\5> \2\u0154\u0157\3\2\2\2")
        buf.write("\u0155\u0157\5> \2\u0156\u014a\3\2\2\2\u0156\u0150\3\2")
        buf.write("\2\2\u0156\u0155\3\2\2\2\u0157=\3\2\2\2\u0158\u015f\5")
        buf.write("@!\2\u0159\u015a\7N\2\2\u015a\u015b\5V,\2\u015b\u015c")
        buf.write("\7O\2\2\u015c\u015f\3\2\2\2\u015d\u015f\5L\'\2\u015e\u0158")
        buf.write("\3\2\2\2\u015e\u0159\3\2\2\2\u015e\u015d\3\2\2\2\u015f")
        buf.write("?\3\2\2\2\u0160\u0163\5X-\2\u0161\u0163\5B\"\2\u0162\u0160")
        buf.write("\3\2\2\2\u0162\u0161\3\2\2\2\u0163A\3\2\2\2\u0164\u0169")
        buf.write("\5D#\2\u0165\u0168\5F$\2\u0166\u0168\5H%\2\u0167\u0165")
        buf.write("\3\2\2\2\u0167\u0166\3\2\2\2\u0168\u016b\3\2\2\2\u0169")
        buf.write("\u0167\3\2\2\2\u0169\u016a\3\2\2\2\u016aC\3\2\2\2\u016b")
        buf.write("\u0169\3\2\2\2\u016c\u0170\5 \21\2\u016d\u0170\5P)\2\u016e")
        buf.write("\u0170\5J&\2\u016f\u016c\3\2\2\2\u016f\u016d\3\2\2\2\u016f")
        buf.write("\u016e\3\2\2\2\u0170E\3\2\2\2\u0171\u017e\7W\2\2\u0172")
        buf.write("\u017f\5P)\2\u0173\u0174\7N\2\2\u0174\u0179\5P)\2\u0175")
        buf.write("\u0176\7V\2\2\u0176\u0178\5P)\2\u0177\u0175\3\2\2\2\u0178")
        buf.write("\u017b\3\2\2\2\u0179\u0177\3\2\2\2\u0179\u017a\3\2\2\2")
        buf.write("\u017a\u017c\3\2\2\2\u017b\u0179\3\2\2\2\u017c\u017d\7")
        buf.write("O\2\2\u017d\u017f\3\2\2\2\u017e\u0172\3\2\2\2\u017e\u0173")
        buf.write("\3\2\2\2\u017f\u0188\3\2\2\2\u0180\u0181\7\37\2\2\u0181")
        buf.write("\u0183\7W\2\2\u0182\u0184\5P)\2\u0183\u0182\3\2\2\2\u0184")
        buf.write("\u0185\3\2\2\2\u0185\u0183\3\2\2\2\u0185\u0186\3\2\2\2")
        buf.write("\u0186\u0188\3\2\2\2\u0187\u0171\3\2\2\2\u0187\u0180\3")
        buf.write("\2\2\2\u0188G\3\2\2\2\u0189\u018a\7T\2\2\u018a\u018b\t")
        buf.write("\5\2\2\u018bI\3\2\2\2\u018c\u018d\7N\2\2\u018d\u018e\5")
        buf.write("*\26\2\u018e\u018f\7\\\2\2\u018f\u0190\5V,\2\u0190\u0191")
        buf.write("\7L\2\2\u0191\u0192\5V,\2\u0192\u0193\7O\2\2\u0193\u019b")
        buf.write("\3\2\2\2\u0194\u0195\7\37\2\2\u0195\u0196\7`\2\2\u0196")
        buf.write("\u0197\5*\26\2\u0197\u0198\5V,\2\u0198\u0199\5V,\2\u0199")
        buf.write("\u019b\3\2\2\2\u019a\u018c\3\2\2\2\u019a\u0194\3\2\2\2")
        buf.write("\u019bK\3\2\2\2\u019c\u019d\7[\2\2\u019d\u019e\5<\37\2")
        buf.write("\u019eM\3\2\2\2\u019f\u01a0\7\t\2\2\u01a0\u01a1\5\b\5")
        buf.write("\2\u01a1O\3\2\2\2\u01a2\u01a5\5R*\2\u01a3\u01a5\5T+\2")
        buf.write("\u01a4\u01a2\3\2\2\2\u01a4\u01a3\3\2\2\2\u01a5Q\3\2\2")
        buf.write("\2\u01a6\u01a7\t\6\2\2\u01a7S\3\2\2\2\u01a8\u01a9\7G\2")
        buf.write("\2\u01a9\u01aa\7A\2\2\u01aaU\3\2\2\2\u01ab\u01ac\58\35")
        buf.write("\2\u01acW\3\2\2\2\u01ad\u01b2\5Z.\2\u01ae\u01b2\5\\/\2")
        buf.write("\u01af\u01b2\5b\62\2\u01b0\u01b2\5d\63\2\u01b1\u01ad\3")
        buf.write("\2\2\2\u01b1\u01ae\3\2\2\2\u01b1\u01af\3\2\2\2\u01b1\u01b0")
        buf.write("\3\2\2\2\u01b2Y\3\2\2\2\u01b3\u01b4\t\7\2\2\u01b4[\3\2")
        buf.write("\2\2\u01b5\u01be\7R\2\2\u01b6\u01bb\5^\60\2\u01b7\u01b8")
        buf.write("\7V\2\2\u01b8\u01ba\5^\60\2\u01b9\u01b7\3\2\2\2\u01ba")
        buf.write("\u01bd\3\2\2\2\u01bb\u01b9\3\2\2\2\u01bb\u01bc\3\2\2\2")
        buf.write("\u01bc\u01bf\3\2\2\2\u01bd\u01bb\3\2\2\2\u01be\u01b6\3")
        buf.write("\2\2\2\u01be\u01bf\3\2\2\2\u01bf\u01c0\3\2\2\2\u01c0\u01c9")
        buf.write("\7S\2\2\u01c1\u01c2\7\37\2\2\u01c2\u01c4\7b\2\2\u01c3")
        buf.write("\u01c5\5^\60\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2")
        buf.write("\u01c6\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c9\3")
        buf.write("\2\2\2\u01c8\u01b5\3\2\2\2\u01c8\u01c1\3\2\2\2\u01c9]")
        buf.write("\3\2\2\2\u01ca\u01cb\5`\61\2\u01cb\u01cc\7T\2\2\u01cc")
        buf.write("\u01cd\5X-\2\u01cd\u01d4\3\2\2\2\u01ce\u01cf\7\37\2\2")
        buf.write("\u01cf\u01d0\7c\2\2\u01d0\u01d1\5`\61\2\u01d1\u01d2\5")
        buf.write("X-\2\u01d2\u01d4\3\2\2\2\u01d3\u01ca\3\2\2\2\u01d3\u01ce")
        buf.write("\3\2\2\2\u01d4_\3\2\2\2\u01d5\u01d6\t\5\2\2\u01d6a\3\2")
        buf.write("\2\2\u01d7\u01e0\7d\2\2\u01d8\u01dd\5d\63\2\u01d9\u01da")
        buf.write("\7V\2\2\u01da\u01dc\5d\63\2\u01db\u01d9\3\2\2\2\u01dc")
        buf.write("\u01df\3\2\2\2\u01dd\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01e1\3\2\2\2\u01df\u01dd\3\2\2\2\u01e0\u01d8\3")
        buf.write("\2\2\2\u01e0\u01e1\3\2\2\2\u01e1\u01e2\3\2\2\2\u01e2\u01eb")
        buf.write("\7e\2\2\u01e3\u01e4\7\37\2\2\u01e4\u01e6\7f\2\2\u01e5")
        buf.write("\u01e7\5d\63\2\u01e6\u01e5\3\2\2\2\u01e7\u01e8\3\2\2\2")
        buf.write("\u01e8\u01e6\3\2\2\2\u01e8\u01e9\3\2\2\2\u01e9\u01eb\3")
        buf.write("\2\2\2\u01ea\u01d7\3\2\2\2\u01ea\u01e3\3\2\2\2\u01ebc")
        buf.write("\3\2\2\2\u01ec\u01f5\7N\2\2\u01ed\u01f2\5X-\2\u01ee\u01ef")
        buf.write("\7V\2\2\u01ef\u01f1\5X-\2\u01f0\u01ee\3\2\2\2\u01f1\u01f4")
        buf.write("\3\2\2\2\u01f2\u01f0\3\2\2\2\u01f2\u01f3\3\2\2\2\u01f3")
        buf.write("\u01f6\3\2\2\2\u01f4\u01f2\3\2\2\2\u01f5\u01ed\3\2\2\2")
        buf.write("\u01f5\u01f6\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7\u0200\7")
        buf.write("O\2\2\u01f8\u01f9\7\37\2\2\u01f9\u01fb\5d\63\2\u01fa\u01fc")
        buf.write("\5X-\2\u01fb\u01fa\3\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01fb")
        buf.write("\3\2\2\2\u01fd\u01fe\3\2\2\2\u01fe\u0200\3\2\2\2\u01ff")
        buf.write("\u01ec\3\2\2\2\u01ff\u01f8\3\2\2\2\u0200e\3\2\2\2<mrx")
        buf.write("~\u0086\u008a\u0092\u0098\u009b\u00a8\u00b2\u00b4\u00b9")
        buf.write("\u00bf\u00c1\u00c7\u00d8\u00e0\u00e2\u00e9\u00ef\u00f1")
        buf.write("\u00f8\u00fe\u0100\u0108\u0116\u011e\u012c\u0134\u013f")
        buf.write("\u0147\u0156\u015e\u0162\u0167\u0169\u016f\u0179\u017e")
        buf.write("\u0185\u0187\u019a\u01a4\u01b1\u01bb\u01be\u01c6\u01c8")
        buf.write("\u01d3\u01dd\u01e0\u01e8\u01ea\u01f2\u01f5\u01fd\u01ff")
        return buf.getvalue()
		

class PigParser ( Parser ):

    grammarFileName = "java-escape"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    EOF = Token.EOF
    DEFINE=1
    LOAD=2
    FILTER=3
    FOREACH=4
    ORDER=5
    ARRANGE=6
    DISTINCT=7
    COGROUP=8
    JOIN=9
    CROSS=10
    UNION=11
    SPLIT=12
    INTO=13
    IF=14
    ALL=15
    ANY=16
    AS=17
    BY=18
    USING=19
    INNER=20
    OUTER=21
    ONSCHEMA=22
    STAR=23
    PARALLEL=24
    PARTITION=25
    GROUP=26
    AND=27
    OR=28
    NOT=29
    GENERATE=30
    FLATTEN=31
    EVAL=32
    ASC=33
    DESC=34
    INT=35
    LONG=36
    FLOAT=37
    DOUBLE=38
    CHARARRAY=39
    BYTEARRAY=40
    BAG=41
    TUPLE=42
    MAP=43
    IS=44
    NULL=45
    STREAM=46
    THROUGH=47
    STORE=48
    MAPREDUCE=49
    SHIP=50
    CACHE=51
    INPUT=52
    OUTPUT=53
    ERROR=54
    STDIN=55
    STDOUT=56
    LIMIT=57
    SAMPLE=58
    LEFT=59
    RIGHT=60
    FULL=61
    IDENTIFIER=62
    INTEGER=63
    LONGINTEGER=64
    DOUBLENUMBER=65
    FLOATNUMBER=66
    QUOTEDSTRING=67
    EXECCOMMAND=68
    DOLLAR=69
    WS=70
    SL_COMMENT=71
    ML_COMMENT=72
    FILTEROP=73
    COLON=74
    SEMI_COLON=75
    LEFT_PAREN=76
    RIGHT_PAREN=77
    LEFT_CURLYP=78
    RIGHT_CURLYP=79
    LEFT_BRACKET=80
    RIGHT_BRACKET=81
    POUND=82
    EQUAL=83
    COMMA=84
    PERIOD=85
    DIV=86
    PERCENT=87
    PLUS=88
    MINUS=89
    QMARK=90
    FUNC=91
    START=92
    CAST_EXPR=93
    BIN_EXPR=94
    LONGINEGER=95
    MAP_VAL=96
    KEY_VAL_PAIR=97
    LEFT_CURLY=98
    RIGHT_CURLY=99
    BAG_VAL=100

    tokenNames = [ "<INVALID>", "'define'", "'load'", "'filter'", "'foreach'",
                   "'order'", "'arrange'", "'distinct'", "'cogroup'", "'join'",
                   "'cross'", "'union'", "'split'", "'into'", "'if'", "'all'",
                   "'any'", "'as'", "'by'", "'using'", "'inner'", "'outer'",
                   "'ONSCHEMA'", "'*'", "'parallel'", "'partition'", "'group'",
                   "'and'", "'or'", "'not'", "'generate'", "'flatten'",
                   "'eval'", "'asc'", "'desc'", "'int'", "'long'", "'float'",
                   "'double'", "'chararray'", "'bytearray'", "'bag'", "'tuple'",
                   "'map'", "'is'", "'null'", "'stream'", "'through'", "'store'",
                   "'mapreduce'", "'ship'", "'cache'", "'input'", "'output'",
                   "'stderr'", "'stdin'", "'stdout'", "'limit'", "'sample'",
                   "'left'", "'right'", "'full'", "IDENTIFIER", "INTEGER",
                   "LONGINTEGER", "DOUBLENUMBER", "FLOATNUMBER", "QUOTEDSTRING",
                   "EXECCOMMAND", "'$'", "WS", "SL_COMMENT", "ML_COMMENT",
                   "FILTEROP", "':'", "';'", "'('", "')'", "'{'", "'}'",
                   "'['", "']'", "'#'", "'='", "','", "'.'", "'/'", "'%'",
                   "'+'", "'-'", "'?'", "FUNC", "START", "CAST_EXPR", "BIN_EXPR",
                   "LONGINEGER", "MAP_VAL", "KEY_VAL_PAIR", "LEFT_CURLY",
                   "RIGHT_CURLY", "BAG_VAL" ]

    RULE_parse = 0
    RULE_query = 1
    RULE_statement = 2
    RULE_alias = 3
    RULE_op_clause = 4
    RULE_load_clause = 5
    RULE_filename = 6
    RULE_as_clause = 7
    RULE_tuple_def = 8
    RULE_field = 9
    RULE_type = 10
    RULE_simple_type = 11
    RULE_tuple_type = 12
    RULE_bag_type = 13
    RULE_map_type = 14
    RULE_func_clause = 15
    RULE_func_name = 16
    RULE_func_args = 17
    RULE_store_clause = 18
    RULE_filter_clause = 19
    RULE_cond = 20
    RULE_or_cond = 21
    RULE_and_cond = 22
    RULE_unary_cond = 23
    RULE_not_cond = 24
    RULE_null_check_cond = 25
    RULE_expr = 26
    RULE_add_expr = 27
    RULE_multi_expr = 28
    RULE_cast_expr = 29
    RULE_unary_expr = 30
    RULE_eval_expr = 31
    RULE_var_expr = 32
    RULE_projectable_expr = 33
    RULE_dot_proj = 34
    RULE_pound_proj = 35
    RULE_bin_expr = 36
    RULE_neg_expr = 37
    RULE_distinct_clause = 38
    RULE_col_ref = 39
    RULE_alias_col_ref = 40
    RULE_dollar_col_ref = 41
    RULE_infix_expr = 42
    RULE_const_expr = 43
    RULE_scalar = 44
    RULE_map = 45
    RULE_keyvalue = 46
    RULE_string_val = 47
    RULE_bag = 48
    RULE_tuple = 49

    ruleNames =  [ "parse", "query", "statement", "alias", "op_clause",
                   "load_clause", "filename", "as_clause", "tuple_def",
                   "field", "type", "simple_type", "tuple_type", "bag_type",
                   "map_type", "func_clause", "func_name", "func_args",
                   "store_clause", "filter_clause", "cond", "or_cond", "and_cond",
                   "unary_cond", "not_cond", "null_check_cond", "expr",
                   "add_expr", "multi_expr", "cast_expr", "unary_expr",
                   "eval_expr", "var_expr", "projectable_expr", "dot_proj",
                   "pound_proj", "bin_expr", "neg_expr", "distinct_clause",
                   "col_ref", "alias_col_ref", "dollar_col_ref", "infix_expr",
                   "const_expr", "scalar", "map", "keyvalue", "string_val",
                   "bag", "tuple" ]

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.4")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ParseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(PigParser.EOF, 0)

        def query(self):
            return self.getTypedRuleContext(PigParser.QueryContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_parse

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterParse(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitParse(self)




    def parse(self):

        localctx = PigParser.ParseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_parse)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.query(0)
            self.state = 101
            self.match(self.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class QueryContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def query(self):
            return self.getTypedRuleContext(PigParser.QueryContext,0)


        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.StatementContext)
            else:
                return self.getTypedRuleContext(PigParser.StatementContext,i)


        def getRuleIndex(self):
            return PigParser.RULE_query

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterQuery(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitQuery(self)



    def query(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = PigParser.QueryContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_query, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.state = 107
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,0,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 104
                        self.statement()
                    self.state = 109
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,0,self._ctx)

                pass

            elif la_ == 2:
                self.state = 110
                self.match(self.NOT)
                self.state = 111
                self.statement()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 118
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    localctx = PigParser.QueryContext(self, _parentctx, _parentState)
                    self.pushNewRecursionContext(localctx, _startState, self.RULE_query)
                    self.state = 114
                    if not self.precpred(self._ctx, 1):
                        raise FailedPredicateException(self, "self.precpred(self._ctx, 1)")
                    self.state = 115
                    self.statement()
                self.state = 120
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(PigParser.StatementContext,0)


        def SEMI_COLON(self):
            return self.getToken(PigParser.SEMI_COLON, 0)

        def op_clause(self):
            return self.getTypedRuleContext(PigParser.Op_clauseContext,0)


        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def EQUAL(self):
            return self.getToken(PigParser.EQUAL, 0)

        def alias(self):
            return self.getTypedRuleContext(PigParser.AliasContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitStatement(self)




    def statement(self):

        localctx = PigParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        self._la = 0 # Token type
        try:
            self.state = 136
            token = self._input.LA(1)
            if token in [self.LOAD, self.FILTER, self.DISTINCT, self.STORE, self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 124
                _la = self._input.LA(1)
                if _la==PigParser.IDENTIFIER:
                    self.state = 121
                    self.alias()
                    self.state = 122
                    self.match(self.EQUAL)


                self.state = 126
                self.op_clause()
                self.state = 127
                self.match(self.SEMI_COLON)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 129
                self.match(self.NOT)

                self.state = 130
                self.statement()
                self.state = 132
                _la = self._input.LA(1)
                if _la==PigParser.IDENTIFIER:
                    self.state = 131
                    self.alias()


                self.state = 134
                self.op_clause()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AliasContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PigParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return PigParser.RULE_alias

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterAlias(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitAlias(self)




    def alias(self):

        localctx = PigParser.AliasContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_alias)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 138
            self.match(self.IDENTIFIER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Op_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def load_clause(self):
            return self.getTypedRuleContext(PigParser.Load_clauseContext,0)


        def store_clause(self):
            return self.getTypedRuleContext(PigParser.Store_clauseContext,0)


        def distinct_clause(self):
            return self.getTypedRuleContext(PigParser.Distinct_clauseContext,0)


        def filter_clause(self):
            return self.getTypedRuleContext(PigParser.Filter_clauseContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_op_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterOp_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitOp_clause(self)




    def op_clause(self):

        localctx = PigParser.Op_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_op_clause)
        try:
            self.state = 144
            token = self._input.LA(1)
            if token in [self.LOAD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.load_clause()

            elif token in [self.STORE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.store_clause()

            elif token in [self.FILTER]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.filter_clause()

            elif token in [self.DISTINCT]:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.distinct_clause()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Load_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def USING(self):
            return self.getToken(PigParser.USING, 0)

        def func_clause(self):
            return self.getTypedRuleContext(PigParser.Func_clauseContext,0)


        def LOAD(self):
            return self.getToken(PigParser.LOAD, 0)

        def as_clause(self):
            return self.getTypedRuleContext(PigParser.As_clauseContext,0)


        def filename(self):
            return self.getTypedRuleContext(PigParser.FilenameContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_load_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterLoad_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitLoad_clause(self)




    def load_clause(self):

        localctx = PigParser.Load_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_load_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 146
            self.match(self.LOAD)
            self.state = 147
            self.filename()
            self.state = 150
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 148
                self.match(self.USING)
                self.state = 149
                self.func_clause()


            self.state = 153
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 152
                self.as_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FilenameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self):
            return self.getToken(PigParser.QUOTEDSTRING, 0)

        def getRuleIndex(self):
            return PigParser.RULE_filename

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterFilename(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitFilename(self)




    def filename(self):

        localctx = PigParser.FilenameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_filename)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
            self.match(self.QUOTEDSTRING)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class As_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AS(self):
            return self.getToken(PigParser.AS, 0)

        def tuple_def(self):
            return self.getTypedRuleContext(PigParser.Tuple_defContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_as_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterAs_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitAs_clause(self)




    def as_clause(self):

        localctx = PigParser.As_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_as_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.match(self.AS)
            self.state = 158
            self.tuple_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_def(self):
            return self.getTypedRuleContext(PigParser.Tuple_defContext,0)


        def field(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.FieldContext)
            else:
                return self.getTypedRuleContext(PigParser.FieldContext,i)


        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def getRuleIndex(self):
            return PigParser.RULE_tuple_def

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterTuple_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitTuple_def(self)




    def tuple_def(self):

        localctx = PigParser.Tuple_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_tuple_def)
        self._la = 0 # Token type
        try:
            self.state = 178
            token = self._input.LA(1)
            if token in [self.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 160
                self.match(self.LEFT_PAREN)
                self.state = 161
                self.field()
                self.state = 166
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==PigParser.COMMA:
                    self.state = 162
                    self.match(self.COMMA)
                    self.state = 163
                    self.field()
                    self.state = 168
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 169
                self.match(self.RIGHT_PAREN)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 171
                self.match(self.NOT)

                self.state = 172
                self.tuple_def()
                self.state = 174
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 173
                        self.field()

                    else:
                        raise NoViableAltException(self)
                    self.state = 176
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FieldContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PigParser.IDENTIFIER, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def field(self):
            return self.getTypedRuleContext(PigParser.FieldContext,0)


        def type(self):
            return self.getTypedRuleContext(PigParser.TypeContext,0)


        def COLON(self):
            return self.getToken(PigParser.COLON, 0)

        def getRuleIndex(self):
            return PigParser.RULE_field

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterField(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitField(self)




    def field(self):

        localctx = PigParser.FieldContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_field)
        try:
            self.state = 191
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 180
                self.match(self.IDENTIFIER)
                self.state = 183
                la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                if la_ == 1:
                    self.state = 181
                    self.match(self.COLON)
                    self.state = 182
                    self.type()



            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 185
                self.match(self.NOT)

                self.state = 186
                self.field()
                self.state = 187
                self.match(self.IDENTIFIER)
                self.state = 189
                la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                if la_ == 1:
                    self.state = 188
                    self.type()



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TypeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple_type(self):
            return self.getTypedRuleContext(PigParser.Tuple_typeContext,0)


        def map_type(self):
            return self.getTypedRuleContext(PigParser.Map_typeContext,0)


        def simple_type(self):
            return self.getTypedRuleContext(PigParser.Simple_typeContext,0)


        def bag_type(self):
            return self.getTypedRuleContext(PigParser.Bag_typeContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterType(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitType(self)




    def type(self):

        localctx = PigParser.TypeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_type)
        try:
            self.state = 197
            token = self._input.LA(1)
            if token in [self.INT, self.LONG, self.FLOAT, self.DOUBLE, self.CHARARRAY, self.BYTEARRAY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 193
                self.simple_type()

            elif token in [self.NOT, self.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 194
                self.tuple_type()

            elif token in [self.BAG]:
                self.enterOuterAlt(localctx, 3)
                self.state = 195
                self.bag_type()

            elif token in [self.MAP]:
                self.enterOuterAlt(localctx, 4)
                self.state = 196
                self.map_type()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Simple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BYTEARRAY(self):
            return self.getToken(PigParser.BYTEARRAY, 0)

        def FLOAT(self):
            return self.getToken(PigParser.FLOAT, 0)

        def INT(self):
            return self.getToken(PigParser.INT, 0)

        def LONG(self):
            return self.getToken(PigParser.LONG, 0)

        def DOUBLE(self):
            return self.getToken(PigParser.DOUBLE, 0)

        def CHARARRAY(self):
            return self.getToken(PigParser.CHARARRAY, 0)

        def getRuleIndex(self):
            return PigParser.RULE_simple_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterSimple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitSimple_type(self)




    def simple_type(self):

        localctx = PigParser.Simple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_simple_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 199
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.INT) | (1 << self.LONG) | (1 << self.FLOAT) | (1 << self.DOUBLE) | (1 << self.CHARARRAY) | (1 << self.BYTEARRAY))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Tuple_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple(self):
            return self.getTypedRuleContext(PigParser.TupleContext,0)


        def tuple_def(self):
            return self.getTypedRuleContext(PigParser.Tuple_defContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_tuple_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterTuple_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitTuple_type(self)




    def tuple_type(self):

        localctx = PigParser.Tuple_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_tuple_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 201
            self.tuple()
            self.state = 202
            self.tuple_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bag_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAG(self):
            return self.getToken(PigParser.BAG, 0)

        def tuple_def(self):
            return self.getTypedRuleContext(PigParser.Tuple_defContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_bag_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterBag_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitBag_type(self)




    def bag_type(self):

        localctx = PigParser.Bag_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_bag_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 204
            self.match(self.BAG)
            self.state = 205
            self.tuple_def()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Map_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MAP(self):
            return self.getToken(PigParser.MAP, 0)

        def LEFT_BRACKET(self):
            return self.getToken(PigParser.LEFT_BRACKET, 0)

        def RIGHT_BRACKET(self):
            return self.getToken(PigParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return PigParser.RULE_map_type

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterMap_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitMap_type(self)




    def map_type(self):

        localctx = PigParser.Map_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_map_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 207
            self.match(self.MAP)
            self.state = 208
            self.match(self.LEFT_BRACKET)
            self.state = 209
            self.match(self.RIGHT_BRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def func_name(self):
            return self.getTypedRuleContext(PigParser.Func_nameContext,0)


        def FUNC(self):
            return self.getToken(PigParser.FUNC, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def func_args(self):
            return self.getTypedRuleContext(PigParser.Func_argsContext,0)


        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def getRuleIndex(self):
            return PigParser.RULE_func_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterFunc_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitFunc_clause(self)




    def func_clause(self):

        localctx = PigParser.Func_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_func_clause)
        self._la = 0 # Token type
        try:
            self.state = 224
            token = self._input.LA(1)
            if token in [self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 211
                self.func_name()
                self.state = 212
                self.match(self.LEFT_PAREN)
                self.state = 214
                _la = self._input.LA(1)
                if _la==PigParser.QUOTEDSTRING:
                    self.state = 213
                    self.func_args()


                self.state = 216
                self.match(self.RIGHT_PAREN)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 218
                self.match(self.NOT)

                self.state = 219
                self.match(self.FUNC)
                self.state = 220
                self.func_name()
                self.state = 222
                la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                if la_ == 1:
                    self.state = 221
                    self.func_args()



            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.IDENTIFIER)
            else:
                return self.getToken(PigParser.IDENTIFIER, i)

        def PERIOD(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.PERIOD)
            else:
                return self.getToken(PigParser.PERIOD, i)

        def getRuleIndex(self):
            return PigParser.RULE_func_name

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterFunc_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitFunc_name(self)




    def func_name(self):

        localctx = PigParser.Func_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_func_name)
        try:
            self.state = 239
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 226
                self.match(self.IDENTIFIER)
                self.state = 231
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,19,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 227
                        self.match(self.PERIOD)
                        self.state = 228
                        self.match(self.IDENTIFIER)
                    self.state = 233
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,19,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 235
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 234
                        self.match(self.IDENTIFIER)

                    else:
                        raise NoViableAltException(self)
                    self.state = 237
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,20,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Func_argsContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.QUOTEDSTRING)
            else:
                return self.getToken(PigParser.QUOTEDSTRING, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def getRuleIndex(self):
            return PigParser.RULE_func_args

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterFunc_args(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitFunc_args(self)




    def func_args(self):

        localctx = PigParser.Func_argsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_func_args)
        try:
            self.state = 254
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 241
                self.match(self.QUOTEDSTRING)
                self.state = 246
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,22,self._ctx)
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt==1:
                        self.state = 242
                        self.match(self.COMMA)
                        self.state = 243
                        self.match(self.QUOTEDSTRING)
                    self.state = 248
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,22,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 250
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 249
                        self.match(self.QUOTEDSTRING)

                    else:
                        raise NoViableAltException(self)
                    self.state = 252
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,23,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Store_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTO(self):
            return self.getToken(PigParser.INTO, 0)

        def USING(self):
            return self.getToken(PigParser.USING, 0)

        def func_clause(self):
            return self.getTypedRuleContext(PigParser.Func_clauseContext,0)


        def filename(self):
            return self.getTypedRuleContext(PigParser.FilenameContext,0)


        def STORE(self):
            return self.getToken(PigParser.STORE, 0)

        def alias(self):
            return self.getTypedRuleContext(PigParser.AliasContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_store_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterStore_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitStore_clause(self)




    def store_clause(self):

        localctx = PigParser.Store_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_store_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 256
            self.match(self.STORE)
            self.state = 257
            self.alias()
            self.state = 258
            self.match(self.INTO)
            self.state = 259
            self.filename()
            self.state = 262
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 260
                self.match(self.USING)
                self.state = 261
                self.func_clause()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Filter_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BY(self):
            return self.getToken(PigParser.BY, 0)

        def FILTER(self):
            return self.getToken(PigParser.FILTER, 0)

        def cond(self):
            return self.getTypedRuleContext(PigParser.CondContext,0)


        def alias(self):
            return self.getTypedRuleContext(PigParser.AliasContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_filter_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterFilter_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitFilter_clause(self)




    def filter_clause(self):

        localctx = PigParser.Filter_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_filter_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 264
            self.match(self.FILTER)
            self.state = 265
            self.alias()
            self.state = 266
            self.match(self.BY)
            self.state = 267
            self.cond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class CondContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def or_cond(self):
            return self.getTypedRuleContext(PigParser.Or_condContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterCond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitCond(self)




    def cond(self):

        localctx = PigParser.CondContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 269
            self.or_cond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Or_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OR(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.OR)
            else:
                return self.getToken(PigParser.OR, i)

        def and_cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.And_condContext)
            else:
                return self.getTypedRuleContext(PigParser.And_condContext,i)


        def getRuleIndex(self):
            return PigParser.RULE_or_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterOr_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitOr_cond(self)




    def or_cond(self):

        localctx = PigParser.Or_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_or_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.and_cond()
            self.state = 276
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,26,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 272
                    self.match(self.OR)
                    self.state = 273
                    self.and_cond()
                self.state = 278
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,26,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class And_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_cond(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Unary_condContext)
            else:
                return self.getTypedRuleContext(PigParser.Unary_condContext,i)


        def AND(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.AND)
            else:
                return self.getToken(PigParser.AND, i)

        def getRuleIndex(self):
            return PigParser.RULE_and_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterAnd_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitAnd_cond(self)




    def and_cond(self):

        localctx = PigParser.And_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_and_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 279
            self.unary_cond()
            self.state = 284
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,27,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 280
                    self.match(self.AND)
                    self.state = 281
                    self.unary_cond()
                self.state = 286
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.ExprContext)
            else:
                return self.getTypedRuleContext(PigParser.ExprContext,i)


        def not_cond(self):
            return self.getTypedRuleContext(PigParser.Not_condContext,0)


        def func_clause(self):
            return self.getTypedRuleContext(PigParser.Func_clauseContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def cond(self):
            return self.getTypedRuleContext(PigParser.CondContext,0)


        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def FILTEROP(self):
            return self.getToken(PigParser.FILTEROP, 0)

        def null_check_cond(self):
            return self.getTypedRuleContext(PigParser.Null_check_condContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_unary_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterUnary_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitUnary_cond(self)




    def unary_cond(self):

        localctx = PigParser.Unary_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_unary_cond)
        try:
            self.state = 298
            la_ = self._interp.adaptivePredict(self._input,28,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 287
                self.match(self.LEFT_PAREN)
                self.state = 288
                self.cond()
                self.state = 289
                self.match(self.RIGHT_PAREN)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 291
                self.expr()
                self.state = 292
                self.match(self.FILTEROP)
                self.state = 293
                self.expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 295
                self.func_clause()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 296
                self.null_check_cond()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 297
                self.not_cond()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Not_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def unary_cond(self):
            return self.getTypedRuleContext(PigParser.Unary_condContext,0)


        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def getRuleIndex(self):
            return PigParser.RULE_not_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterNot_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitNot_cond(self)




    def not_cond(self):

        localctx = PigParser.Not_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_not_cond)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 300
            self.match(self.NOT)
            self.state = 301
            self.unary_cond()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Null_check_condContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(PigParser.ExprContext,0)


        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def IS(self):
            return self.getToken(PigParser.IS, 0)

        def NULL(self):
            return self.getToken(PigParser.NULL, 0)

        def getRuleIndex(self):
            return PigParser.RULE_null_check_cond

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterNull_check_cond(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitNull_check_cond(self)




    def null_check_cond(self):

        localctx = PigParser.Null_check_condContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_null_check_cond)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 303
            self.expr()
            self.state = 304
            self.match(self.IS)
            self.state = 306
            _la = self._input.LA(1)
            if _la==PigParser.NOT:
                self.state = 305
                self.match(self.NOT)


            self.state = 308
            self.match(self.NULL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(PigParser.Add_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitExpr(self)




    def expr(self):

        localctx = PigParser.ExprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 310
            self.add_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Add_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.MINUS)
            else:
                return self.getToken(PigParser.MINUS, i)

        def multi_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Multi_exprContext)
            else:
                return self.getTypedRuleContext(PigParser.Multi_exprContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.PLUS)
            else:
                return self.getToken(PigParser.PLUS, i)

        def getRuleIndex(self):
            return PigParser.RULE_add_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterAdd_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitAdd_expr(self)




    def add_expr(self):

        localctx = PigParser.Add_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_add_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.multi_expr()
            self.state = 317
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,30,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 313
                    _la = self._input.LA(1)
                    if not(_la==PigParser.PLUS or _la==PigParser.MINUS):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 314
                    self.multi_expr()
                self.state = 319
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,30,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Multi_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def cast_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Cast_exprContext)
            else:
                return self.getTypedRuleContext(PigParser.Cast_exprContext,i)


        def PERCENT(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.PERCENT)
            else:
                return self.getToken(PigParser.PERCENT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.DIV)
            else:
                return self.getToken(PigParser.DIV, i)

        def START(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.START)
            else:
                return self.getToken(PigParser.START, i)

        def getRuleIndex(self):
            return PigParser.RULE_multi_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterMulti_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitMulti_expr(self)




    def multi_expr(self):

        localctx = PigParser.Multi_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_multi_expr)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.cast_expr()
            self.state = 325
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,31,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 321
                    _la = self._input.LA(1)
                    if not(((((_la - 86)) & ~0x3f) == 0 and ((1 << (_la - 86)) & ((1 << (self.DIV - 86)) | (1 << (self.PERCENT - 86)) | (1 << (self.START - 86)))) != 0)):
                        self._errHandler.recoverInline(self)
                    self.consume()
                    self.state = 322
                    self.cast_expr()
                self.state = 327
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,31,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Cast_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CAST_EXPR(self):
            return self.getToken(PigParser.CAST_EXPR, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def type(self):
            return self.getTypedRuleContext(PigParser.TypeContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def unary_expr(self):
            return self.getTypedRuleContext(PigParser.Unary_exprContext,0)


        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def getRuleIndex(self):
            return PigParser.RULE_cast_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterCast_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitCast_expr(self)




    def cast_expr(self):

        localctx = PigParser.Cast_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_cast_expr)
        try:
            self.state = 340
            la_ = self._interp.adaptivePredict(self._input,32,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 328
                self.match(self.LEFT_PAREN)
                self.state = 329
                self.type()
                self.state = 330
                self.match(self.RIGHT_PAREN)
                self.state = 332
                self.unary_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 334
                self.match(self.NOT)

                self.state = 335
                self.match(self.CAST_EXPR)
                self.state = 336
                self.type()
                self.state = 337
                self.unary_expr()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 339
                self.unary_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Unary_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def infix_expr(self):
            return self.getTypedRuleContext(PigParser.Infix_exprContext,0)


        def eval_expr(self):
            return self.getTypedRuleContext(PigParser.Eval_exprContext,0)


        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def neg_expr(self):
            return self.getTypedRuleContext(PigParser.Neg_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_unary_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterUnary_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitUnary_expr(self)




    def unary_expr(self):

        localctx = PigParser.Unary_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_unary_expr)
        try:
            self.state = 348
            la_ = self._interp.adaptivePredict(self._input,33,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 342
                self.eval_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 343
                self.match(self.LEFT_PAREN)
                self.state = 344
                self.infix_expr()
                self.state = 345
                self.match(self.RIGHT_PAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 347
                self.neg_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Eval_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_expr(self):
            return self.getTypedRuleContext(PigParser.Const_exprContext,0)


        def var_expr(self):
            return self.getTypedRuleContext(PigParser.Var_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_eval_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterEval_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitEval_expr(self)




    def eval_expr(self):

        localctx = PigParser.Eval_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 62, self.RULE_eval_expr)
        try:
            self.state = 352
            la_ = self._interp.adaptivePredict(self._input,34,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 350
                self.const_expr()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 351
                self.var_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def projectable_expr(self):
            return self.getTypedRuleContext(PigParser.Projectable_exprContext,0)


        def pound_proj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Pound_projContext)
            else:
                return self.getTypedRuleContext(PigParser.Pound_projContext,i)


        def dot_proj(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Dot_projContext)
            else:
                return self.getTypedRuleContext(PigParser.Dot_projContext,i)


        def getRuleIndex(self):
            return PigParser.RULE_var_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterVar_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitVar_expr(self)




    def var_expr(self):

        localctx = PigParser.Var_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 64, self.RULE_var_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 354
            self.projectable_expr()
            self.state = 359
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,36,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 357
                    token = self._input.LA(1)
                    if token in [self.NOT, self.PERIOD]:
                        self.state = 355
                        self.dot_proj()

                    elif token in [self.POUND]:
                        self.state = 356
                        self.pound_proj()

                    else:
                        raise NoViableAltException(self)

                self.state = 361
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,36,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Projectable_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def col_ref(self):
            return self.getTypedRuleContext(PigParser.Col_refContext,0)


        def func_clause(self):
            return self.getTypedRuleContext(PigParser.Func_clauseContext,0)


        def bin_expr(self):
            return self.getTypedRuleContext(PigParser.Bin_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_projectable_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterProjectable_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitProjectable_expr(self)




    def projectable_expr(self):

        localctx = PigParser.Projectable_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 66, self.RULE_projectable_expr)
        try:
            self.state = 365
            la_ = self._interp.adaptivePredict(self._input,37,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 362
                self.func_clause()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 363
                self.col_ref()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 364
                self.bin_expr()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dot_projContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def col_ref(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Col_refContext)
            else:
                return self.getTypedRuleContext(PigParser.Col_refContext,i)


        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def PERIOD(self):
            return self.getToken(PigParser.PERIOD, 0)

        def getRuleIndex(self):
            return PigParser.RULE_dot_proj

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterDot_proj(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitDot_proj(self)




    def dot_proj(self):

        localctx = PigParser.Dot_projContext(self, self._ctx, self.state)
        self.enterRule(localctx, 68, self.RULE_dot_proj)
        self._la = 0 # Token type
        try:
            self.state = 389
            token = self._input.LA(1)
            if token in [self.PERIOD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 367
                self.match(self.PERIOD)
                self.state = 380
                token = self._input.LA(1)
                if token in [self.GROUP, self.IDENTIFIER, self.DOLLAR]:
                    self.state = 368
                    self.col_ref()

                elif token in [self.LEFT_PAREN]:
                    self.state = 369
                    self.match(self.LEFT_PAREN)
                    self.state = 370
                    self.col_ref()
                    self.state = 375
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PigParser.COMMA:
                        self.state = 371
                        self.match(self.COMMA)
                        self.state = 372
                        self.col_ref()
                        self.state = 377
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)

                    self.state = 378
                    self.match(self.RIGHT_PAREN)

                else:
                    raise NoViableAltException(self)


            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 382
                self.match(self.NOT)

                self.state = 383
                self.match(self.PERIOD)
                self.state = 385
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 384
                        self.col_ref()

                    else:
                        raise NoViableAltException(self)
                    self.state = 387
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,40,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Pound_projContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self):
            return self.getToken(PigParser.QUOTEDSTRING, 0)

        def POUND(self):
            return self.getToken(PigParser.POUND, 0)

        def NULL(self):
            return self.getToken(PigParser.NULL, 0)

        def getRuleIndex(self):
            return PigParser.RULE_pound_proj

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterPound_proj(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitPound_proj(self)




    def pound_proj(self):

        localctx = PigParser.Pound_projContext(self, self._ctx, self.state)
        self.enterRule(localctx, 70, self.RULE_pound_proj)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 391
            self.match(self.POUND)
            self.state = 392
            _la = self._input.LA(1)
            if not(_la==PigParser.NULL or _la==PigParser.QUOTEDSTRING):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Bin_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BIN_EXPR(self):
            return self.getToken(PigParser.BIN_EXPR, 0)

        def infix_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Infix_exprContext)
            else:
                return self.getTypedRuleContext(PigParser.Infix_exprContext,i)


        def QMARK(self):
            return self.getToken(PigParser.QMARK, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def cond(self):
            return self.getTypedRuleContext(PigParser.CondContext,0)


        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def COLON(self):
            return self.getToken(PigParser.COLON, 0)

        def getRuleIndex(self):
            return PigParser.RULE_bin_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterBin_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitBin_expr(self)




    def bin_expr(self):

        localctx = PigParser.Bin_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 72, self.RULE_bin_expr)
        try:
            self.state = 408
            token = self._input.LA(1)
            if token in [self.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 394
                self.match(self.LEFT_PAREN)
                self.state = 395
                self.cond()
                self.state = 396
                self.match(self.QMARK)
                self.state = 397
                self.infix_expr()
                self.state = 398
                self.match(self.COLON)
                self.state = 399
                self.infix_expr()
                self.state = 400
                self.match(self.RIGHT_PAREN)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 402
                self.match(self.NOT)

                self.state = 403
                self.match(self.BIN_EXPR)
                self.state = 404
                self.cond()
                self.state = 405
                self.infix_expr()
                self.state = 406
                self.infix_expr()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Neg_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def MINUS(self):
            return self.getToken(PigParser.MINUS, 0)

        def cast_expr(self):
            return self.getTypedRuleContext(PigParser.Cast_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_neg_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterNeg_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitNeg_expr(self)




    def neg_expr(self):

        localctx = PigParser.Neg_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 74, self.RULE_neg_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 410
            self.match(self.MINUS)
            self.state = 411
            self.cast_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Distinct_clauseContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DISTINCT(self):
            return self.getToken(PigParser.DISTINCT, 0)

        def alias(self):
            return self.getTypedRuleContext(PigParser.AliasContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_distinct_clause

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterDistinct_clause(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitDistinct_clause(self)




    def distinct_clause(self):

        localctx = PigParser.Distinct_clauseContext(self, self._ctx, self.state)
        self.enterRule(localctx, 76, self.RULE_distinct_clause)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 413
            self.match(self.DISTINCT)
            self.state = 414
            self.alias()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Col_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def dollar_col_ref(self):
            return self.getTypedRuleContext(PigParser.Dollar_col_refContext,0)


        def alias_col_ref(self):
            return self.getTypedRuleContext(PigParser.Alias_col_refContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_col_ref

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterCol_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitCol_ref(self)




    def col_ref(self):

        localctx = PigParser.Col_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 78, self.RULE_col_ref)
        try:
            self.state = 418
            token = self._input.LA(1)
            if token in [self.GROUP, self.IDENTIFIER]:
                self.enterOuterAlt(localctx, 1)
                self.state = 416
                self.alias_col_ref()

            elif token in [self.DOLLAR]:
                self.enterOuterAlt(localctx, 2)
                self.state = 417
                self.dollar_col_ref()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Alias_col_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(PigParser.IDENTIFIER, 0)

        def GROUP(self):
            return self.getToken(PigParser.GROUP, 0)

        def getRuleIndex(self):
            return PigParser.RULE_alias_col_ref

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterAlias_col_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitAlias_col_ref(self)




    def alias_col_ref(self):

        localctx = PigParser.Alias_col_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 80, self.RULE_alias_col_ref)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 420
            _la = self._input.LA(1)
            if not(_la==PigParser.GROUP or _la==PigParser.IDENTIFIER):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Dollar_col_refContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DOLLAR(self):
            return self.getToken(PigParser.DOLLAR, 0)

        def INTEGER(self):
            return self.getToken(PigParser.INTEGER, 0)

        def getRuleIndex(self):
            return PigParser.RULE_dollar_col_ref

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterDollar_col_ref(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitDollar_col_ref(self)




    def dollar_col_ref(self):

        localctx = PigParser.Dollar_col_refContext(self, self._ctx, self.state)
        self.enterRule(localctx, 82, self.RULE_dollar_col_ref)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 422
            self.match(self.DOLLAR)
            self.state = 423
            self.match(self.INTEGER)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Infix_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def add_expr(self):
            return self.getTypedRuleContext(PigParser.Add_exprContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_infix_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterInfix_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitInfix_expr(self)




    def infix_expr(self):

        localctx = PigParser.Infix_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 84, self.RULE_infix_expr)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 425
            self.add_expr()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Const_exprContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple(self):
            return self.getTypedRuleContext(PigParser.TupleContext,0)


        def bag(self):
            return self.getTypedRuleContext(PigParser.BagContext,0)


        def map(self):
            return self.getTypedRuleContext(PigParser.MapContext,0)


        def scalar(self):
            return self.getTypedRuleContext(PigParser.ScalarContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_const_expr

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterConst_expr(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitConst_expr(self)




    def const_expr(self):

        localctx = PigParser.Const_exprContext(self, self._ctx, self.state)
        self.enterRule(localctx, 86, self.RULE_const_expr)
        try:
            self.state = 431
            la_ = self._interp.adaptivePredict(self._input,44,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 427
                self.scalar()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 428
                self.map()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 429
                self.bag()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 430
                self.tuple()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ScalarContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self):
            return self.getToken(PigParser.QUOTEDSTRING, 0)

        def LONGINEGER(self):
            return self.getToken(PigParser.LONGINEGER, 0)

        def FLOATNUMBER(self):
            return self.getToken(PigParser.FLOATNUMBER, 0)

        def DOUBLENUMBER(self):
            return self.getToken(PigParser.DOUBLENUMBER, 0)

        def NULL(self):
            return self.getToken(PigParser.NULL, 0)

        def INTEGER(self):
            return self.getToken(PigParser.INTEGER, 0)

        def getRuleIndex(self):
            return PigParser.RULE_scalar

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterScalar(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitScalar(self)




    def scalar(self):

        localctx = PigParser.ScalarContext(self, self._ctx, self.state)
        self.enterRule(localctx, 88, self.RULE_scalar)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 433
            _la = self._input.LA(1)
            if not(((((_la - 45)) & ~0x3f) == 0 and ((1 << (_la - 45)) & ((1 << (self.NULL - 45)) | (1 << (self.INTEGER - 45)) | (1 << (self.DOUBLENUMBER - 45)) | (1 << (self.FLOATNUMBER - 45)) | (1 << (self.QUOTEDSTRING - 45)) | (1 << (self.LONGINEGER - 45)))) != 0)):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MapContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def keyvalue(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.KeyvalueContext)
            else:
                return self.getTypedRuleContext(PigParser.KeyvalueContext,i)


        def MAP_VAL(self):
            return self.getToken(PigParser.MAP_VAL, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def LEFT_BRACKET(self):
            return self.getToken(PigParser.LEFT_BRACKET, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def RIGHT_BRACKET(self):
            return self.getToken(PigParser.RIGHT_BRACKET, 0)

        def getRuleIndex(self):
            return PigParser.RULE_map

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterMap(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitMap(self)




    def map(self):

        localctx = PigParser.MapContext(self, self._ctx, self.state)
        self.enterRule(localctx, 90, self.RULE_map)
        self._la = 0 # Token type
        try:
            self.state = 454
            token = self._input.LA(1)
            if token in [self.LEFT_BRACKET]:
                self.enterOuterAlt(localctx, 1)
                self.state = 435
                self.match(self.LEFT_BRACKET)
                self.state = 444
                _la = self._input.LA(1)
                if ((((_la - 29)) & ~0x3f) == 0 and ((1 << (_la - 29)) & ((1 << (self.NOT - 29)) | (1 << (self.NULL - 29)) | (1 << (self.QUOTEDSTRING - 29)))) != 0):
                    self.state = 436
                    self.keyvalue()
                    self.state = 441
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PigParser.COMMA:
                        self.state = 437
                        self.match(self.COMMA)
                        self.state = 438
                        self.keyvalue()
                        self.state = 443
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 446
                self.match(self.RIGHT_BRACKET)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 447
                self.match(self.NOT)

                self.state = 448
                self.match(self.MAP_VAL)
                self.state = 450
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 449
                        self.keyvalue()

                    else:
                        raise NoViableAltException(self)
                    self.state = 452
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,47,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class KeyvalueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def const_expr(self):
            return self.getTypedRuleContext(PigParser.Const_exprContext,0)


        def KEY_VAL_PAIR(self):
            return self.getToken(PigParser.KEY_VAL_PAIR, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def POUND(self):
            return self.getToken(PigParser.POUND, 0)

        def string_val(self):
            return self.getTypedRuleContext(PigParser.String_valContext,0)


        def getRuleIndex(self):
            return PigParser.RULE_keyvalue

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterKeyvalue(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitKeyvalue(self)




    def keyvalue(self):

        localctx = PigParser.KeyvalueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 92, self.RULE_keyvalue)
        try:
            self.state = 465
            token = self._input.LA(1)
            if token in [self.NULL, self.QUOTEDSTRING]:
                self.enterOuterAlt(localctx, 1)
                self.state = 456
                self.string_val()
                self.state = 457
                self.match(self.POUND)
                self.state = 458
                self.const_expr()

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 460
                self.match(self.NOT)

                self.state = 461
                self.match(self.KEY_VAL_PAIR)
                self.state = 462
                self.string_val()
                self.state = 463
                self.const_expr()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class String_valContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def QUOTEDSTRING(self):
            return self.getToken(PigParser.QUOTEDSTRING, 0)

        def NULL(self):
            return self.getToken(PigParser.NULL, 0)

        def getRuleIndex(self):
            return PigParser.RULE_string_val

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterString_val(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitString_val(self)




    def string_val(self):

        localctx = PigParser.String_valContext(self, self._ctx, self.state)
        self.enterRule(localctx, 94, self.RULE_string_val)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 467
            _la = self._input.LA(1)
            if not(_la==PigParser.NULL or _la==PigParser.QUOTEDSTRING):
                self._errHandler.recoverInline(self)
            self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BagContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BAG_VAL(self):
            return self.getToken(PigParser.BAG_VAL, 0)

        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def tuple(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.TupleContext)
            else:
                return self.getTypedRuleContext(PigParser.TupleContext,i)


        def LEFT_CURLY(self):
            return self.getToken(PigParser.LEFT_CURLY, 0)

        def RIGHT_CURLY(self):
            return self.getToken(PigParser.RIGHT_CURLY, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def getRuleIndex(self):
            return PigParser.RULE_bag

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterBag(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitBag(self)




    def bag(self):

        localctx = PigParser.BagContext(self, self._ctx, self.state)
        self.enterRule(localctx, 96, self.RULE_bag)
        self._la = 0 # Token type
        try:
            self.state = 488
            token = self._input.LA(1)
            if token in [self.LEFT_CURLY]:
                self.enterOuterAlt(localctx, 1)
                self.state = 469
                self.match(self.LEFT_CURLY)
                self.state = 478
                _la = self._input.LA(1)
                if _la==PigParser.NOT or _la==PigParser.LEFT_PAREN:
                    self.state = 470
                    self.tuple()
                    self.state = 475
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PigParser.COMMA:
                        self.state = 471
                        self.match(self.COMMA)
                        self.state = 472
                        self.tuple()
                        self.state = 477
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 480
                self.match(self.RIGHT_CURLY)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 481
                self.match(self.NOT)

                self.state = 482
                self.match(self.BAG_VAL)
                self.state = 484
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 483
                        self.tuple()

                    else:
                        raise NoViableAltException(self)
                    self.state = 486
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,52,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class TupleContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def tuple(self):
            return self.getTypedRuleContext(PigParser.TupleContext,0)


        def const_expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(PigParser.Const_exprContext)
            else:
                return self.getTypedRuleContext(PigParser.Const_exprContext,i)


        def NOT(self):
            return self.getToken(PigParser.NOT, 0)

        def RIGHT_PAREN(self):
            return self.getToken(PigParser.RIGHT_PAREN, 0)

        def LEFT_PAREN(self):
            return self.getToken(PigParser.LEFT_PAREN, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(PigParser.COMMA)
            else:
                return self.getToken(PigParser.COMMA, i)

        def getRuleIndex(self):
            return PigParser.RULE_tuple

        def enterRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.enterTuple(self)

        def exitRule(self, listener:ParseTreeListener):
            if isinstance( listener, PigListener ):
                listener.exitTuple(self)




    def tuple(self):

        localctx = PigParser.TupleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 98, self.RULE_tuple)
        self._la = 0 # Token type
        try:
            self.state = 509
            token = self._input.LA(1)
            if token in [self.LEFT_PAREN]:
                self.enterOuterAlt(localctx, 1)
                self.state = 490
                self.match(self.LEFT_PAREN)
                self.state = 499
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << self.NOT) | (1 << self.NULL) | (1 << self.INTEGER))) != 0) or ((((_la - 65)) & ~0x3f) == 0 and ((1 << (_la - 65)) & ((1 << (self.DOUBLENUMBER - 65)) | (1 << (self.FLOATNUMBER - 65)) | (1 << (self.QUOTEDSTRING - 65)) | (1 << (self.LEFT_PAREN - 65)) | (1 << (self.LEFT_BRACKET - 65)) | (1 << (self.LONGINEGER - 65)) | (1 << (self.LEFT_CURLY - 65)))) != 0):
                    self.state = 491
                    self.const_expr()
                    self.state = 496
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    while _la==PigParser.COMMA:
                        self.state = 492
                        self.match(self.COMMA)
                        self.state = 493
                        self.const_expr()
                        self.state = 498
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)



                self.state = 501
                self.match(self.RIGHT_PAREN)

            elif token in [self.NOT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 502
                self.match(self.NOT)

                self.state = 503
                self.tuple()
                self.state = 505
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 504
                        self.const_expr()

                    else:
                        raise NoViableAltException(self)
                    self.state = 507
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,56,self._ctx)


            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[1] = self.query_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def query_sempred(self, localctx:QueryContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 1)