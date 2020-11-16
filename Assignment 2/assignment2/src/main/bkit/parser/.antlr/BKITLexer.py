# Generated from d:\Works\HK5\PPL\Assignment 2\assignment2\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2C")
        buf.write("\u021a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\3\2\3\2\7\2\u009e\n\2\f\2\16\2\u00a1\13\2\3\3")
        buf.write("\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3")
        buf.write("\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r")
        buf.write("\3\r\3\r\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\21\3\21\3\21\3\21\3\21\3\22\3\22\3\22\3\22\3\22")
        buf.write("\3\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31")
        buf.write("\3\31\3\32\3\32\3\33\3\33\3\34\3\34\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3!\3!\3\"\3\"\3\"\3")
        buf.write("#\3#\3#\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3\'\3\'\3(\3(")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3+\3,\3,\3,\3-\3-\3-\3.\3.\3.\3")
        buf.write(".\3/\3/\3/\3/\3\60\3\60\3\61\3\61\3\62\3\62\3\63\3\63")
        buf.write("\3\64\3\64\3\65\3\65\3\66\3\66\3\67\3\67\38\38\39\39\3")
        buf.write(":\3:\3:\3:\3:\3:\3:\3:\5:\u0183\n:\3;\3;\7;\u0187\n;\f")
        buf.write(";\16;\u018a\13;\3<\3<\7<\u018e\n<\f<\16<\u0191\13<\3=")
        buf.write("\3=\7=\u0195\n=\f=\16=\u0198\13=\3>\3>\3>\3>\3>\3>\3>")
        buf.write("\3>\3>\3>\5>\u01a4\n>\3?\6?\u01a7\n?\r?\16?\u01a8\3@\3")
        buf.write("@\7@\u01ad\n@\f@\16@\u01b0\13@\3A\3A\5A\u01b4\nA\3A\6")
        buf.write("A\u01b7\nA\rA\16A\u01b8\3B\3B\3C\3C\3D\3D\7D\u01c1\nD")
        buf.write("\fD\16D\u01c4\13D\3D\3D\3D\3E\3E\3E\3E\5E\u01cd\nE\3F")
        buf.write("\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\3F\5F\u01dd\nF\3")
        buf.write("G\3G\3G\3G\7G\u01e3\nG\fG\16G\u01e6\13G\3G\3G\3G\3G\3")
        buf.write("G\3H\6H\u01ee\nH\rH\16H\u01ef\3H\3H\3I\3I\3J\3J\7J\u01f8")
        buf.write("\nJ\fJ\16J\u01fb\13J\3J\5J\u01fe\nJ\3J\3J\3K\3K\7K\u0204")
        buf.write("\nK\fK\16K\u0207\13K\3K\3K\3K\3L\3L\3L\3L\5L\u0210\nL")
        buf.write("\3M\3M\3M\3M\7M\u0216\nM\fM\16M\u0219\13M\4\u01e4\u0217")
        buf.write("\2N\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'")
        buf.write("M(O)Q*S+U,W-Y.[/]\60_\61a\62c\63e\64g\65i\66k\67m8o9q")
        buf.write(":s;u\2w\2y\2{<}\2\177\2\u0081\2\u0083\2\u0085\2\u0087")
        buf.write("=\u0089\2\u008b\2\u008d>\u008f?\u0091@\u0093A\u0095B\u0097")
        buf.write("\2\u0099C\3\2\23\3\2c|\6\2\62;C\\aac|\4\2ZZzz\4\2QQqq")
        buf.write("\3\2\63;\3\2\62;\4\2\63;CH\4\2\62;CH\3\2\639\3\2\629\4")
        buf.write("\2GGgg\4\2--//\6\2\f\f$$))^^\5\2\13\f\16\17\"\"\3\3\f")
        buf.write("\f\t\2))^^ddhhppttvv\3\2$$\2\u022a\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\2[\3\2\2\2\2]\3\2\2\2\2_\3\2\2\2\2a")
        buf.write("\3\2\2\2\2c\3\2\2\2\2e\3\2\2\2\2g\3\2\2\2\2i\3\2\2\2\2")
        buf.write("k\3\2\2\2\2m\3\2\2\2\2o\3\2\2\2\2q\3\2\2\2\2s\3\2\2\2")
        buf.write("\2{\3\2\2\2\2\u0087\3\2\2\2\2\u008d\3\2\2\2\2\u008f\3")
        buf.write("\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095\3\2\2\2")
        buf.write("\2\u0099\3\2\2\2\3\u009b\3\2\2\2\5\u00a2\3\2\2\2\7\u00a6")
        buf.write("\3\2\2\2\t\u00af\3\2\2\2\13\u00b9\3\2\2\2\r\u00c0\3\2")
        buf.write("\2\2\17\u00c5\3\2\2\2\21\u00cd\3\2\2\2\23\u00d0\3\2\2")
        buf.write("\2\25\u00d5\3\2\2\2\27\u00da\3\2\2\2\31\u00e1\3\2\2\2")
        buf.write("\33\u00e7\3\2\2\2\35\u00eb\3\2\2\2\37\u00f2\3\2\2\2!\u00f8")
        buf.write("\3\2\2\2#\u0101\3\2\2\2%\u0107\3\2\2\2\'\u0110\3\2\2\2")
        buf.write(")\u0113\3\2\2\2+\u0119\3\2\2\2-\u011e\3\2\2\2/\u0124\3")
        buf.write("\2\2\2\61\u0126\3\2\2\2\63\u0128\3\2\2\2\65\u012a\3\2")
        buf.write("\2\2\67\u012c\3\2\2\29\u012e\3\2\2\2;\u0131\3\2\2\2=\u0134")
        buf.write("\3\2\2\2?\u0137\3\2\2\2A\u013a\3\2\2\2C\u013c\3\2\2\2")
        buf.write("E\u013f\3\2\2\2G\u0142\3\2\2\2I\u0144\3\2\2\2K\u0147\3")
        buf.write("\2\2\2M\u014a\3\2\2\2O\u014e\3\2\2\2Q\u0150\3\2\2\2S\u0152")
        buf.write("\3\2\2\2U\u0155\3\2\2\2W\u0158\3\2\2\2Y\u015b\3\2\2\2")
        buf.write("[\u015e\3\2\2\2]\u0162\3\2\2\2_\u0166\3\2\2\2a\u0168\3")
        buf.write("\2\2\2c\u016a\3\2\2\2e\u016c\3\2\2\2g\u016e\3\2\2\2i\u0170")
        buf.write("\3\2\2\2k\u0172\3\2\2\2m\u0174\3\2\2\2o\u0176\3\2\2\2")
        buf.write("q\u0178\3\2\2\2s\u0182\3\2\2\2u\u0184\3\2\2\2w\u018b\3")
        buf.write("\2\2\2y\u0192\3\2\2\2{\u01a3\3\2\2\2}\u01a6\3\2\2\2\177")
        buf.write("\u01aa\3\2\2\2\u0081\u01b1\3\2\2\2\u0083\u01ba\3\2\2\2")
        buf.write("\u0085\u01bc\3\2\2\2\u0087\u01be\3\2\2\2\u0089\u01cc\3")
        buf.write("\2\2\2\u008b\u01dc\3\2\2\2\u008d\u01de\3\2\2\2\u008f\u01ed")
        buf.write("\3\2\2\2\u0091\u01f3\3\2\2\2\u0093\u01f5\3\2\2\2\u0095")
        buf.write("\u0201\3\2\2\2\u0097\u020f\3\2\2\2\u0099\u0211\3\2\2\2")
        buf.write("\u009b\u009f\t\2\2\2\u009c\u009e\t\3\2\2\u009d\u009c\3")
        buf.write("\2\2\2\u009e\u00a1\3\2\2\2\u009f\u009d\3\2\2\2\u009f\u00a0")
        buf.write("\3\2\2\2\u00a0\4\3\2\2\2\u00a1\u009f\3\2\2\2\u00a2\u00a3")
        buf.write("\7X\2\2\u00a3\u00a4\7c\2\2\u00a4\u00a5\7t\2\2\u00a5\6")
        buf.write("\3\2\2\2\u00a6\u00a7\7H\2\2\u00a7\u00a8\7w\2\2\u00a8\u00a9")
        buf.write("\7p\2\2\u00a9\u00aa\7e\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7k\2\2\u00ac\u00ad\7q\2\2\u00ad\u00ae\7p\2\2\u00ae\b")
        buf.write("\3\2\2\2\u00af\u00b0\7R\2\2\u00b0\u00b1\7c\2\2\u00b1\u00b2")
        buf.write("\7t\2\2\u00b2\u00b3\7c\2\2\u00b3\u00b4\7o\2\2\u00b4\u00b5")
        buf.write("\7g\2\2\u00b5\u00b6\7v\2\2\u00b6\u00b7\7g\2\2\u00b7\u00b8")
        buf.write("\7t\2\2\u00b8\n\3\2\2\2\u00b9\u00ba\7T\2\2\u00ba\u00bb")
        buf.write("\7g\2\2\u00bb\u00bc\7v\2\2\u00bc\u00bd\7w\2\2\u00bd\u00be")
        buf.write("\7t\2\2\u00be\u00bf\7p\2\2\u00bf\f\3\2\2\2\u00c0\u00c1")
        buf.write("\7D\2\2\u00c1\u00c2\7q\2\2\u00c2\u00c3\7f\2\2\u00c3\u00c4")
        buf.write("\7{\2\2\u00c4\16\3\2\2\2\u00c5\u00c6\7G\2\2\u00c6\u00c7")
        buf.write("\7p\2\2\u00c7\u00c8\7f\2\2\u00c8\u00c9\7D\2\2\u00c9\u00ca")
        buf.write("\7q\2\2\u00ca\u00cb\7f\2\2\u00cb\u00cc\7{\2\2\u00cc\20")
        buf.write("\3\2\2\2\u00cd\u00ce\7K\2\2\u00ce\u00cf\7h\2\2\u00cf\22")
        buf.write("\3\2\2\2\u00d0\u00d1\7V\2\2\u00d1\u00d2\7j\2\2\u00d2\u00d3")
        buf.write("\7g\2\2\u00d3\u00d4\7p\2\2\u00d4\24\3\2\2\2\u00d5\u00d6")
        buf.write("\7G\2\2\u00d6\u00d7\7n\2\2\u00d7\u00d8\7u\2\2\u00d8\u00d9")
        buf.write("\7g\2\2\u00d9\26\3\2\2\2\u00da\u00db\7G\2\2\u00db\u00dc")
        buf.write("\7n\2\2\u00dc\u00dd\7u\2\2\u00dd\u00de\7g\2\2\u00de\u00df")
        buf.write("\7K\2\2\u00df\u00e0\7h\2\2\u00e0\30\3\2\2\2\u00e1\u00e2")
        buf.write("\7G\2\2\u00e2\u00e3\7p\2\2\u00e3\u00e4\7f\2\2\u00e4\u00e5")
        buf.write("\7K\2\2\u00e5\u00e6\7h\2\2\u00e6\32\3\2\2\2\u00e7\u00e8")
        buf.write("\7H\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea\7t\2\2\u00ea\34")
        buf.write("\3\2\2\2\u00eb\u00ec\7G\2\2\u00ec\u00ed\7p\2\2\u00ed\u00ee")
        buf.write("\7f\2\2\u00ee\u00ef\7H\2\2\u00ef\u00f0\7q\2\2\u00f0\u00f1")
        buf.write("\7t\2\2\u00f1\36\3\2\2\2\u00f2\u00f3\7Y\2\2\u00f3\u00f4")
        buf.write("\7j\2\2\u00f4\u00f5\7k\2\2\u00f5\u00f6\7n\2\2\u00f6\u00f7")
        buf.write("\7g\2\2\u00f7 \3\2\2\2\u00f8\u00f9\7G\2\2\u00f9\u00fa")
        buf.write("\7p\2\2\u00fa\u00fb\7f\2\2\u00fb\u00fc\7Y\2\2\u00fc\u00fd")
        buf.write("\7j\2\2\u00fd\u00fe\7k\2\2\u00fe\u00ff\7n\2\2\u00ff\u0100")
        buf.write("\7g\2\2\u0100\"\3\2\2\2\u0101\u0102\7D\2\2\u0102\u0103")
        buf.write("\7t\2\2\u0103\u0104\7g\2\2\u0104\u0105\7c\2\2\u0105\u0106")
        buf.write("\7m\2\2\u0106$\3\2\2\2\u0107\u0108\7E\2\2\u0108\u0109")
        buf.write("\7q\2\2\u0109\u010a\7p\2\2\u010a\u010b\7v\2\2\u010b\u010c")
        buf.write("\7k\2\2\u010c\u010d\7p\2\2\u010d\u010e\7w\2\2\u010e\u010f")
        buf.write("\7g\2\2\u010f&\3\2\2\2\u0110\u0111\7F\2\2\u0111\u0112")
        buf.write("\7q\2\2\u0112(\3\2\2\2\u0113\u0114\7G\2\2\u0114\u0115")
        buf.write("\7p\2\2\u0115\u0116\7f\2\2\u0116\u0117\7F\2\2\u0117\u0118")
        buf.write("\7q\2\2\u0118*\3\2\2\2\u0119\u011a\7V\2\2\u011a\u011b")
        buf.write("\7t\2\2\u011b\u011c\7w\2\2\u011c\u011d\7g\2\2\u011d,\3")
        buf.write("\2\2\2\u011e\u011f\7H\2\2\u011f\u0120\7c\2\2\u0120\u0121")
        buf.write("\7n\2\2\u0121\u0122\7u\2\2\u0122\u0123\7g\2\2\u0123.\3")
        buf.write("\2\2\2\u0124\u0125\7-\2\2\u0125\60\3\2\2\2\u0126\u0127")
        buf.write("\7/\2\2\u0127\62\3\2\2\2\u0128\u0129\7,\2\2\u0129\64\3")
        buf.write("\2\2\2\u012a\u012b\7^\2\2\u012b\66\3\2\2\2\u012c\u012d")
        buf.write("\7\'\2\2\u012d8\3\2\2\2\u012e\u012f\7-\2\2\u012f\u0130")
        buf.write("\7\60\2\2\u0130:\3\2\2\2\u0131\u0132\7/\2\2\u0132\u0133")
        buf.write("\7\60\2\2\u0133<\3\2\2\2\u0134\u0135\7,\2\2\u0135\u0136")
        buf.write("\7\60\2\2\u0136>\3\2\2\2\u0137\u0138\7^\2\2\u0138\u0139")
        buf.write("\7\60\2\2\u0139@\3\2\2\2\u013a\u013b\7#\2\2\u013bB\3\2")
        buf.write("\2\2\u013c\u013d\7(\2\2\u013d\u013e\7(\2\2\u013eD\3\2")
        buf.write("\2\2\u013f\u0140\7~\2\2\u0140\u0141\7~\2\2\u0141F\3\2")
        buf.write("\2\2\u0142\u0143\7?\2\2\u0143H\3\2\2\2\u0144\u0145\7?")
        buf.write("\2\2\u0145\u0146\7?\2\2\u0146J\3\2\2\2\u0147\u0148\7#")
        buf.write("\2\2\u0148\u0149\7?\2\2\u0149L\3\2\2\2\u014a\u014b\7?")
        buf.write("\2\2\u014b\u014c\7\61\2\2\u014c\u014d\7?\2\2\u014dN\3")
        buf.write("\2\2\2\u014e\u014f\7>\2\2\u014fP\3\2\2\2\u0150\u0151\7")
        buf.write("@\2\2\u0151R\3\2\2\2\u0152\u0153\7>\2\2\u0153\u0154\7")
        buf.write("?\2\2\u0154T\3\2\2\2\u0155\u0156\7@\2\2\u0156\u0157\7")
        buf.write("?\2\2\u0157V\3\2\2\2\u0158\u0159\7>\2\2\u0159\u015a\7")
        buf.write("\60\2\2\u015aX\3\2\2\2\u015b\u015c\7@\2\2\u015c\u015d")
        buf.write("\7\60\2\2\u015dZ\3\2\2\2\u015e\u015f\7>\2\2\u015f\u0160")
        buf.write("\7?\2\2\u0160\u0161\7\60\2\2\u0161\\\3\2\2\2\u0162\u0163")
        buf.write("\7@\2\2\u0163\u0164\7?\2\2\u0164\u0165\7\60\2\2\u0165")
        buf.write("^\3\2\2\2\u0166\u0167\7.\2\2\u0167`\3\2\2\2\u0168\u0169")
        buf.write("\7\60\2\2\u0169b\3\2\2\2\u016a\u016b\7<\2\2\u016bd\3\2")
        buf.write("\2\2\u016c\u016d\7=\2\2\u016df\3\2\2\2\u016e\u016f\7*")
        buf.write("\2\2\u016fh\3\2\2\2\u0170\u0171\7+\2\2\u0171j\3\2\2\2")
        buf.write("\u0172\u0173\7]\2\2\u0173l\3\2\2\2\u0174\u0175\7_\2\2")
        buf.write("\u0175n\3\2\2\2\u0176\u0177\7}\2\2\u0177p\3\2\2\2\u0178")
        buf.write("\u0179\7\177\2\2\u0179r\3\2\2\2\u017a\u0183\7\62\2\2\u017b")
        buf.write("\u0183\5u;\2\u017c\u017d\7\62\2\2\u017d\u017e\t\4\2\2")
        buf.write("\u017e\u0183\5w<\2\u017f\u0180\7\62\2\2\u0180\u0181\t")
        buf.write("\5\2\2\u0181\u0183\5y=\2\u0182\u017a\3\2\2\2\u0182\u017b")
        buf.write("\3\2\2\2\u0182\u017c\3\2\2\2\u0182\u017f\3\2\2\2\u0183")
        buf.write("t\3\2\2\2\u0184\u0188\t\6\2\2\u0185\u0187\t\7\2\2\u0186")
        buf.write("\u0185\3\2\2\2\u0187\u018a\3\2\2\2\u0188\u0186\3\2\2\2")
        buf.write("\u0188\u0189\3\2\2\2\u0189v\3\2\2\2\u018a\u0188\3\2\2")
        buf.write("\2\u018b\u018f\t\b\2\2\u018c\u018e\t\t\2\2\u018d\u018c")
        buf.write("\3\2\2\2\u018e\u0191\3\2\2\2\u018f\u018d\3\2\2\2\u018f")
        buf.write("\u0190\3\2\2\2\u0190x\3\2\2\2\u0191\u018f\3\2\2\2\u0192")
        buf.write("\u0196\t\n\2\2\u0193\u0195\t\13\2\2\u0194\u0193\3\2\2")
        buf.write("\2\u0195\u0198\3\2\2\2\u0196\u0194\3\2\2\2\u0196\u0197")
        buf.write("\3\2\2\2\u0197z\3\2\2\2\u0198\u0196\3\2\2\2\u0199\u019a")
        buf.write("\5}?\2\u019a\u019b\5\177@\2\u019b\u019c\5\u0081A\2\u019c")
        buf.write("\u01a4\3\2\2\2\u019d\u019e\5}?\2\u019e\u019f\5\u0081A")
        buf.write("\2\u019f\u01a4\3\2\2\2\u01a0\u01a1\5}?\2\u01a1\u01a2\5")
        buf.write("\177@\2\u01a2\u01a4\3\2\2\2\u01a3\u0199\3\2\2\2\u01a3")
        buf.write("\u019d\3\2\2\2\u01a3\u01a0\3\2\2\2\u01a4|\3\2\2\2\u01a5")
        buf.write("\u01a7\t\7\2\2\u01a6\u01a5\3\2\2\2\u01a7\u01a8\3\2\2\2")
        buf.write("\u01a8\u01a6\3\2\2\2\u01a8\u01a9\3\2\2\2\u01a9~\3\2\2")
        buf.write("\2\u01aa\u01ae\7\60\2\2\u01ab\u01ad\5\u0083B\2\u01ac\u01ab")
        buf.write("\3\2\2\2\u01ad\u01b0\3\2\2\2\u01ae\u01ac\3\2\2\2\u01ae")
        buf.write("\u01af\3\2\2\2\u01af\u0080\3\2\2\2\u01b0\u01ae\3\2\2\2")
        buf.write("\u01b1\u01b3\t\f\2\2\u01b2\u01b4\5\u0085C\2\u01b3\u01b2")
        buf.write("\3\2\2\2\u01b3\u01b4\3\2\2\2\u01b4\u01b6\3\2\2\2\u01b5")
        buf.write("\u01b7\5\u0083B\2\u01b6\u01b5\3\2\2\2\u01b7\u01b8\3\2")
        buf.write("\2\2\u01b8\u01b6\3\2\2\2\u01b8\u01b9\3\2\2\2\u01b9\u0082")
        buf.write("\3\2\2\2\u01ba\u01bb\t\7\2\2\u01bb\u0084\3\2\2\2\u01bc")
        buf.write("\u01bd\t\r\2\2\u01bd\u0086\3\2\2\2\u01be\u01c2\7$\2\2")
        buf.write("\u01bf\u01c1\5\u0089E\2\u01c0\u01bf\3\2\2\2\u01c1\u01c4")
        buf.write("\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c2\u01c3\3\2\2\2\u01c3")
        buf.write("\u01c5\3\2\2\2\u01c4\u01c2\3\2\2\2\u01c5\u01c6\7$\2\2")
        buf.write("\u01c6\u01c7\bD\2\2\u01c7\u0088\3\2\2\2\u01c8\u01cd\5")
        buf.write("\u008bF\2\u01c9\u01cd\n\16\2\2\u01ca\u01cb\7)\2\2\u01cb")
        buf.write("\u01cd\7$\2\2\u01cc\u01c8\3\2\2\2\u01cc\u01c9\3\2\2\2")
        buf.write("\u01cc\u01ca\3\2\2\2\u01cd\u008a\3\2\2\2\u01ce\u01cf\7")
        buf.write("^\2\2\u01cf\u01dd\7d\2\2\u01d0\u01d1\7^\2\2\u01d1\u01dd")
        buf.write("\7h\2\2\u01d2\u01d3\7^\2\2\u01d3\u01dd\7t\2\2\u01d4\u01d5")
        buf.write("\7^\2\2\u01d5\u01dd\7p\2\2\u01d6\u01d7\7^\2\2\u01d7\u01dd")
        buf.write("\7v\2\2\u01d8\u01d9\7^\2\2\u01d9\u01dd\7)\2\2\u01da\u01db")
        buf.write("\7^\2\2\u01db\u01dd\7^\2\2\u01dc\u01ce\3\2\2\2\u01dc\u01d0")
        buf.write("\3\2\2\2\u01dc\u01d2\3\2\2\2\u01dc\u01d4\3\2\2\2\u01dc")
        buf.write("\u01d6\3\2\2\2\u01dc\u01d8\3\2\2\2\u01dc\u01da\3\2\2\2")
        buf.write("\u01dd\u008c\3\2\2\2\u01de\u01df\7,\2\2\u01df\u01e0\7")
        buf.write(",\2\2\u01e0\u01e4\3\2\2\2\u01e1\u01e3\13\2\2\2\u01e2\u01e1")
        buf.write("\3\2\2\2\u01e3\u01e6\3\2\2\2\u01e4\u01e5\3\2\2\2\u01e4")
        buf.write("\u01e2\3\2\2\2\u01e5\u01e7\3\2\2\2\u01e6\u01e4\3\2\2\2")
        buf.write("\u01e7\u01e8\7,\2\2\u01e8\u01e9\7,\2\2\u01e9\u01ea\3\2")
        buf.write("\2\2\u01ea\u01eb\bG\3\2\u01eb\u008e\3\2\2\2\u01ec\u01ee")
        buf.write("\t\17\2\2\u01ed\u01ec\3\2\2\2\u01ee\u01ef\3\2\2\2\u01ef")
        buf.write("\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2\u01f0\u01f1\3\2\2\2")
        buf.write("\u01f1\u01f2\bH\3\2\u01f2\u0090\3\2\2\2\u01f3\u01f4\13")
        buf.write("\2\2\2\u01f4\u0092\3\2\2\2\u01f5\u01f9\7$\2\2\u01f6\u01f8")
        buf.write("\5\u0089E\2\u01f7\u01f6\3\2\2\2\u01f8\u01fb\3\2\2\2\u01f9")
        buf.write("\u01f7\3\2\2\2\u01f9\u01fa\3\2\2\2\u01fa\u01fd\3\2\2\2")
        buf.write("\u01fb\u01f9\3\2\2\2\u01fc\u01fe\t\20\2\2\u01fd\u01fc")
        buf.write("\3\2\2\2\u01fe\u01ff\3\2\2\2\u01ff\u0200\bJ\4\2\u0200")
        buf.write("\u0094\3\2\2\2\u0201\u0205\7$\2\2\u0202\u0204\5\u0089")
        buf.write("E\2\u0203\u0202\3\2\2\2\u0204\u0207\3\2\2\2\u0205\u0203")
        buf.write("\3\2\2\2\u0205\u0206\3\2\2\2\u0206\u0208\3\2\2\2\u0207")
        buf.write("\u0205\3\2\2\2\u0208\u0209\5\u0097L\2\u0209\u020a\bK\5")
        buf.write("\2\u020a\u0096\3\2\2\2\u020b\u020c\7^\2\2\u020c\u0210")
        buf.write("\n\21\2\2\u020d\u020e\7)\2\2\u020e\u0210\n\22\2\2\u020f")
        buf.write("\u020b\3\2\2\2\u020f\u020d\3\2\2\2\u0210\u0098\3\2\2\2")
        buf.write("\u0211\u0212\7,\2\2\u0212\u0213\7,\2\2\u0213\u0217\3\2")
        buf.write("\2\2\u0214\u0216\13\2\2\2\u0215\u0214\3\2\2\2\u0216\u0219")
        buf.write("\3\2\2\2\u0217\u0218\3\2\2\2\u0217\u0215\3\2\2\2\u0218")
        buf.write("\u009a\3\2\2\2\u0219\u0217\3\2\2\2\27\2\u009f\u0182\u0188")
        buf.write("\u018f\u0196\u01a3\u01a8\u01ae\u01b3\u01b8\u01c2\u01cc")
        buf.write("\u01dc\u01e4\u01ef\u01f9\u01fd\u0205\u020f\u0217\6\3D")
        buf.write("\2\b\2\2\3J\3\3K\4")
        return buf.getvalue()


class BKITLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    ID = 1
    VAR = 2
    FUNCTION = 3
    PARAMETER = 4
    RETURN = 5
    BODY = 6
    END_BODY = 7
    IF = 8
    THEN = 9
    ELSE = 10
    ELSE_IF = 11
    END_IF = 12
    FOR = 13
    END_FOR = 14
    WHILE = 15
    END_WHITE = 16
    BREAK = 17
    CONTINUTE = 18
    DO = 19
    END_DO = 20
    TRUE = 21
    FALSE = 22
    ADD = 23
    SUB = 24
    MUL = 25
    DIV = 26
    MOD = 27
    ADD_FLOAT = 28
    SUB_FLOAT = 29
    MUL_FLOAT = 30
    DIV_FLOAT = 31
    NOT = 32
    AND = 33
    OR = 34
    ASSIGN = 35
    EQUAL = 36
    NOT_EQUAL = 37
    NOT_EQUAL_FLOAT = 38
    LESS_THAN = 39
    MORE_THAN = 40
    LESS_THAN_EQUAL = 41
    MORE_THAN_EQUAL = 42
    LESS_THAN_FLOAT = 43
    MORE_THAN_FLOAT = 44
    LESS_THAN_EQUAL_FLOAT = 45
    MORE_THAN_EQUAL_FLOAT = 46
    COMMA = 47
    DOT = 48
    COLON = 49
    SEMI = 50
    LPAREN = 51
    RPAREN = 52
    LSQUARE = 53
    RSQUARE = 54
    LCURLY = 55
    RCURLY = 56
    INT_LIT = 57
    FLOAT_LIT = 58
    STRING_LIT = 59
    COMMENT = 60
    WS = 61
    ERROR_CHAR = 62
    UNCLOSE_STRING = 63
    ILLEGAL_ESCAPE = 64
    UNTERMINATED_COMMENT = 65

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'Var'", "'Function'", "'Parameter'", "'Return'", "'Body'", 
            "'EndBody'", "'If'", "'Then'", "'Else'", "'ElseIf'", "'EndIf'", 
            "'For'", "'EndFor'", "'While'", "'EndWhile'", "'Break'", "'Continue'", 
            "'Do'", "'EndDo'", "'True'", "'False'", "'+'", "'-'", "'*'", 
            "'\\'", "'%'", "'+.'", "'-.'", "'*.'", "'\\.'", "'!'", "'&&'", 
            "'||'", "'='", "'=='", "'!='", "'=/='", "'<'", "'>'", "'<='", 
            "'>='", "'<.'", "'>.'", "'<=.'", "'>=.'", "','", "'.'", "':'", 
            "';'", "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>",
            "ID", "VAR", "FUNCTION", "PARAMETER", "RETURN", "BODY", "END_BODY", 
            "IF", "THEN", "ELSE", "ELSE_IF", "END_IF", "FOR", "END_FOR", 
            "WHILE", "END_WHITE", "BREAK", "CONTINUTE", "DO", "END_DO", 
            "TRUE", "FALSE", "ADD", "SUB", "MUL", "DIV", "MOD", "ADD_FLOAT", 
            "SUB_FLOAT", "MUL_FLOAT", "DIV_FLOAT", "NOT", "AND", "OR", "ASSIGN", 
            "EQUAL", "NOT_EQUAL", "NOT_EQUAL_FLOAT", "LESS_THAN", "MORE_THAN", 
            "LESS_THAN_EQUAL", "MORE_THAN_EQUAL", "LESS_THAN_FLOAT", "MORE_THAN_FLOAT", 
            "LESS_THAN_EQUAL_FLOAT", "MORE_THAN_EQUAL_FLOAT", "COMMA", "DOT", 
            "COLON", "SEMI", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "LCURLY", 
            "RCURLY", "INT_LIT", "FLOAT_LIT", "STRING_LIT", "COMMENT", "WS", 
            "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    ruleNames = [ "ID", "VAR", "FUNCTION", "PARAMETER", "RETURN", "BODY", 
                  "END_BODY", "IF", "THEN", "ELSE", "ELSE_IF", "END_IF", 
                  "FOR", "END_FOR", "WHILE", "END_WHITE", "BREAK", "CONTINUTE", 
                  "DO", "END_DO", "TRUE", "FALSE", "ADD", "SUB", "MUL", 
                  "DIV", "MOD", "ADD_FLOAT", "SUB_FLOAT", "MUL_FLOAT", "DIV_FLOAT", 
                  "NOT", "AND", "OR", "ASSIGN", "EQUAL", "NOT_EQUAL", "NOT_EQUAL_FLOAT", 
                  "LESS_THAN", "MORE_THAN", "LESS_THAN_EQUAL", "MORE_THAN_EQUAL", 
                  "LESS_THAN_FLOAT", "MORE_THAN_FLOAT", "LESS_THAN_EQUAL_FLOAT", 
                  "MORE_THAN_EQUAL_FLOAT", "COMMA", "DOT", "COLON", "SEMI", 
                  "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", "LCURLY", "RCURLY", 
                  "INT_LIT", "DEC", "HEX", "OCT", "FLOAT_LIT", "INT_PART", 
                  "DECIMAL_PART", "EXPONENT_PART", "DIGIT", "SIGN", "STRING_LIT", 
                  "STRING_CHAR", "ESCAPE_CHAR", "COMMENT", "WS", "ERROR_CHAR", 
                  "UNCLOSE_STRING", "ILLEGAL_ESCAPE", "ILLEGAL_CHAR", "UNTERMINATED_COMMENT" ]

    grammarFileName = "BKIT.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


    def emit(self):
        tk = self.type
        result = super().emit()
        if tk == self.UNCLOSE_STRING:       
            raise UncloseString(result.text)
        elif tk == self.ILLEGAL_ESCAPE:
            raise IllegalEscape(result.text)
        elif tk == self.ERROR_CHAR:
            raise ErrorToken(result.text)
        elif tk == self.UNTERMINATED_COMMENT:
            raise UnterminatedComment()
        else:
            return result;


    def action(self, localctx:RuleContext, ruleIndex:int, actionIndex:int):
        if self._actions is None:
            actions = dict()
            actions[66] = self.STRING_LIT_action 
            actions[72] = self.UNCLOSE_STRING_action 
            actions[73] = self.ILLEGAL_ESCAPE_action 
            self._actions = actions
        action = self._actions.get(ruleIndex, None)
        if action is not None:
            action(localctx, actionIndex)
        else:
            raise Exception("No registered action for:" + str(ruleIndex))


    def STRING_LIT_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 0:

                self.text = (self.text)[1:-1] #To split string

     

    def UNCLOSE_STRING_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 1:

                self.text = (self.text)[1:]
                if len(self.text) > 0:
                    if self.text[-1] == '\n':
                        self.text = (self.text)[:-1]

     

    def ILLEGAL_ESCAPE_action(self, localctx:RuleContext , actionIndex:int):
        if actionIndex == 2:

                self.text = (self.text)[1:]

     


