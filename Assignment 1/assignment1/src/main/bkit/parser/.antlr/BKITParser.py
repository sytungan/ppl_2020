# Generated from d:\Works\HK5\PPL\Assignment 1\assignment1\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3F")
        buf.write("L\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\6\2\26\n\2\r\2\16\2\27\3\2\3")
        buf.write("\2\3\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\5\4$\n\4\3\5\3\5\3")
        buf.write("\5\7\5)\n\5\f\5\16\5,\13\5\3\6\3\6\5\6\60\n\6\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\6\b8\n\b\r\b\16\b9\3\t\3\t\5\t>\n\t\3")
        buf.write("\t\3\t\3\t\5\tC\n\t\7\tE\n\t\f\t\16\tH\13\t\3\n\3\n\3")
        buf.write("\n\2\2\13\2\4\6\b\n\f\16\20\22\2\3\3\2;?\2J\2\25\3\2\2")
        buf.write("\2\4\33\3\2\2\2\6 \3\2\2\2\b%\3\2\2\2\n/\3\2\2\2\f\61")
        buf.write("\3\2\2\2\16\63\3\2\2\2\20=\3\2\2\2\22I\3\2\2\2\24\26\5")
        buf.write("\4\3\2\25\24\3\2\2\2\26\27\3\2\2\2\27\25\3\2\2\2\27\30")
        buf.write("\3\2\2\2\30\31\3\2\2\2\31\32\7\2\2\3\32\3\3\2\2\2\33\34")
        buf.write("\7\4\2\2\34\35\7\63\2\2\35\36\5\6\4\2\36\37\7\64\2\2\37")
        buf.write("\5\3\2\2\2 #\5\b\5\2!\"\7%\2\2\"$\5\20\t\2#!\3\2\2\2#")
        buf.write("$\3\2\2\2$\7\3\2\2\2%*\5\n\6\2&\'\7\61\2\2\')\5\n\6\2")
        buf.write("(&\3\2\2\2),\3\2\2\2*(\3\2\2\2*+\3\2\2\2+\t\3\2\2\2,*")
        buf.write("\3\2\2\2-\60\5\f\7\2.\60\5\16\b\2/-\3\2\2\2/.\3\2\2\2")
        buf.write("\60\13\3\2\2\2\61\62\7\3\2\2\62\r\3\2\2\2\63\67\7\3\2")
        buf.write("\2\64\65\7\67\2\2\65\66\7;\2\2\668\78\2\2\67\64\3\2\2")
        buf.write("\289\3\2\2\29\67\3\2\2\29:\3\2\2\2:\17\3\2\2\2;>\5\22")
        buf.write("\n\2<>\5\f\7\2=;\3\2\2\2=<\3\2\2\2>F\3\2\2\2?B\7\61\2")
        buf.write("\2@C\7@\2\2AC\5\f\7\2B@\3\2\2\2BA\3\2\2\2CE\3\2\2\2D?")
        buf.write("\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2G\21\3\2\2\2HF\3")
        buf.write("\2\2\2IJ\t\2\2\2J\23\3\2\2\2\n\27#*/9=BF")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "'Var'", "'Function'", "'Parameter'", 
                     "'Return'", "'Body'", "'EndBody'", "'If'", "'Then'", 
                     "'Else'", "'ElseIf'", "'EndIf'", "'For'", "'EndFor'", 
                     "'While'", "'EndWhile'", "'Break'", "'Continue'", "'Do'", 
                     "'EndDo'", "'True'", "'False'", "'+'", "'\u00E2\u02C6\u2019'", 
                     "'*'", "'\\'", "'%'", "'+.'", "'\u00E2\u02C6\u2019.'", 
                     "'*.'", "'\\.'", "'!'", "'&&'", "'||'", "'='", "'=='", 
                     "'=/='", "'!='", "'<'", "'>'", "'<='", "'>='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "','", "'.'", "':'", "';'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "VAR", "FUNCTION", "PARAMETER", 
                      "RETURN", "BODY", "ENDBODY", "IF", "THEN", "ELSE", 
                      "ELSE_IF", "END_IF", "FOR", "END_FOR", "WHILE", "END_WHITE", 
                      "BREAK", "CONTINUTE", "DO", "END_DO", "TRUE", "FALSE", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "ADD_FLOAT", "SUB_FLOAT", 
                      "MUL_FLOAT", "DIV_FLOAT", "NOT", "AND", "OR", "ASSIGN", 
                      "EQUAL", "EQUAL_FLOAT", "NOT_EQUAL", "LESS_THAN", 
                      "MORE_THAN", "LESS_THAN_EQUAL", "MORE_THAN_EQUAL", 
                      "LESS_THAN_FLOAT", "MORE_THAN_FLOAT", "LESS_THAN_EQUAL_FLOAT", 
                      "MORE_THAN_EQUAL_FLOAT", "COMMA", "DOT", "COLON", 
                      "SEMI", "LPAREN", "RPAREN", "LSQUARE", "RSQUARE", 
                      "LCURLY", "RCURLY", "INT_LIT", "FLOAT_LIT", "BOOLEAN_LIT", 
                      "STRING_LIT", "ARRAY_LIT", "LITERAL", "COMMENT", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_global_var_declare = 1
    RULE_var_list = 2
    RULE_variable = 3
    RULE_variable_name = 4
    RULE_scalar_var = 5
    RULE_composite_var = 6
    RULE_init_value = 7
    RULE_literal = 8

    ruleNames =  [ "program", "global_var_declare", "var_list", "variable", 
                   "variable_name", "scalar_var", "composite_var", "init_value", 
                   "literal" ]

    EOF = Token.EOF
    ID=1
    VAR=2
    FUNCTION=3
    PARAMETER=4
    RETURN=5
    BODY=6
    ENDBODY=7
    IF=8
    THEN=9
    ELSE=10
    ELSE_IF=11
    END_IF=12
    FOR=13
    END_FOR=14
    WHILE=15
    END_WHITE=16
    BREAK=17
    CONTINUTE=18
    DO=19
    END_DO=20
    TRUE=21
    FALSE=22
    ADD=23
    SUB=24
    MUL=25
    DIV=26
    MOD=27
    ADD_FLOAT=28
    SUB_FLOAT=29
    MUL_FLOAT=30
    DIV_FLOAT=31
    NOT=32
    AND=33
    OR=34
    ASSIGN=35
    EQUAL=36
    EQUAL_FLOAT=37
    NOT_EQUAL=38
    LESS_THAN=39
    MORE_THAN=40
    LESS_THAN_EQUAL=41
    MORE_THAN_EQUAL=42
    LESS_THAN_FLOAT=43
    MORE_THAN_FLOAT=44
    LESS_THAN_EQUAL_FLOAT=45
    MORE_THAN_EQUAL_FLOAT=46
    COMMA=47
    DOT=48
    COLON=49
    SEMI=50
    LPAREN=51
    RPAREN=52
    LSQUARE=53
    RSQUARE=54
    LCURLY=55
    RCURLY=56
    INT_LIT=57
    FLOAT_LIT=58
    BOOLEAN_LIT=59
    STRING_LIT=60
    ARRAY_LIT=61
    LITERAL=62
    COMMENT=63
    WS=64
    ERROR_CHAR=65
    UNCLOSE_STRING=66
    ILLEGAL_ESCAPE=67
    UNTERMINATED_COMMENT=68

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def global_var_declare(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Global_var_declareContext)
            else:
                return self.getTypedRuleContext(BKITParser.Global_var_declareContext,i)


        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 18
                self.global_var_declare()
                self.state = 21 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.VAR):
                    break

            self.state = 23
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_var_declareContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def var_list(self):
            return self.getTypedRuleContext(BKITParser.Var_listContext,0)


        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_global_var_declare




    def global_var_declare(self):

        localctx = BKITParser.Global_var_declareContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_global_var_declare)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.match(BKITParser.VAR)
            self.state = 26
            self.match(BKITParser.COLON)
            self.state = 27
            self.var_list()
            self.state = 28
            self.match(BKITParser.SEMI)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_listContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable(self):
            return self.getTypedRuleContext(BKITParser.VariableContext,0)


        def ASSIGN(self):
            return self.getToken(BKITParser.ASSIGN, 0)

        def init_value(self):
            return self.getTypedRuleContext(BKITParser.Init_valueContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_var_list




    def var_list(self):

        localctx = BKITParser.Var_listContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_list)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.variable()
            self.state = 33
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 31
                self.match(BKITParser.ASSIGN)
                self.state = 32
                self.init_value()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VariableContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def variable_name(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Variable_nameContext)
            else:
                return self.getTypedRuleContext(BKITParser.Variable_nameContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable




    def variable(self):

        localctx = BKITParser.VariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.variable_name()
            self.state = 40
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 36
                self.match(BKITParser.COMMA)
                self.state = 37
                self.variable_name()
                self.state = 42
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Variable_nameContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def scalar_var(self):
            return self.getTypedRuleContext(BKITParser.Scalar_varContext,0)


        def composite_var(self):
            return self.getTypedRuleContext(BKITParser.Composite_varContext,0)


        def getRuleIndex(self):
            return BKITParser.RULE_variable_name




    def variable_name(self):

        localctx = BKITParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_variable_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 43
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 44
                self.composite_var()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Scalar_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_scalar_var




    def scalar_var(self):

        localctx = BKITParser.Scalar_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKITParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Composite_varContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def LSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LSQUARE)
            else:
                return self.getToken(BKITParser.LSQUARE, i)

        def INT_LIT(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.INT_LIT)
            else:
                return self.getToken(BKITParser.INT_LIT, i)

        def RSQUARE(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.RSQUARE)
            else:
                return self.getToken(BKITParser.RSQUARE, i)

        def getRuleIndex(self):
            return BKITParser.RULE_composite_var




    def composite_var(self):

        localctx = BKITParser.Composite_varContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self.match(BKITParser.ID)
            self.state = 53 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 50
                self.match(BKITParser.LSQUARE)
                self.state = 51
                self.match(BKITParser.INT_LIT)
                self.state = 52
                self.match(BKITParser.RSQUARE)
                self.state = 55 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.LSQUARE):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Init_valueContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def literal(self):
            return self.getTypedRuleContext(BKITParser.LiteralContext,0)


        def scalar_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_varContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LITERAL)
            else:
                return self.getToken(BKITParser.LITERAL, i)

        def getRuleIndex(self):
            return BKITParser.RULE_init_value




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_init_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [BKITParser.INT_LIT, BKITParser.FLOAT_LIT, BKITParser.BOOLEAN_LIT, BKITParser.STRING_LIT, BKITParser.ARRAY_LIT]:
                self.state = 57
                self.literal()
                pass
            elif token in [BKITParser.ID]:
                self.state = 58
                self.scalar_var()
                pass
            else:
                raise NoViableAltException(self)

            self.state = 68
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 61
                self.match(BKITParser.COMMA)
                self.state = 64
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [BKITParser.LITERAL]:
                    self.state = 62
                    self.match(BKITParser.LITERAL)
                    pass
                elif token in [BKITParser.ID]:
                    self.state = 63
                    self.scalar_var()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 70
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LiteralContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT_LIT(self):
            return self.getToken(BKITParser.INT_LIT, 0)

        def ARRAY_LIT(self):
            return self.getToken(BKITParser.ARRAY_LIT, 0)

        def STRING_LIT(self):
            return self.getToken(BKITParser.STRING_LIT, 0)

        def FLOAT_LIT(self):
            return self.getToken(BKITParser.FLOAT_LIT, 0)

        def BOOLEAN_LIT(self):
            return self.getToken(BKITParser.BOOLEAN_LIT, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_literal




    def literal(self):

        localctx = BKITParser.LiteralContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_literal)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << BKITParser.INT_LIT) | (1 << BKITParser.FLOAT_LIT) | (1 << BKITParser.BOOLEAN_LIT) | (1 << BKITParser.STRING_LIT) | (1 << BKITParser.ARRAY_LIT))) != 0)):
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





