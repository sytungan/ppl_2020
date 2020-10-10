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
        buf.write("B\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\3\2\6\2\22\n\2\r\2\16\2\23\3\2\3\2\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\4\3\4\3\4\5\4 \n\4\3\5\3\5\5\5$\n\5\3\5\3\5\3")
        buf.write("\5\5\5)\n\5\7\5+\n\5\f\5\16\5.\13\5\3\6\3\6\3\7\3\7\3")
        buf.write("\7\3\7\6\7\66\n\7\r\7\16\7\67\3\b\3\b\3\b\7\b=\n\b\f\b")
        buf.write("\16\b@\13\b\3\b\2\2\t\2\4\6\b\n\f\16\2\3\4\2\4\4??\2A")
        buf.write("\2\21\3\2\2\2\4\27\3\2\2\2\6\34\3\2\2\2\b#\3\2\2\2\n/")
        buf.write("\3\2\2\2\f\61\3\2\2\2\169\3\2\2\2\20\22\5\4\3\2\21\20")
        buf.write("\3\2\2\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24")
        buf.write("\25\3\2\2\2\25\26\7\2\2\3\26\3\3\2\2\2\27\30\7\3\2\2\30")
        buf.write("\31\7\63\2\2\31\32\5\6\4\2\32\33\7\64\2\2\33\5\3\2\2\2")
        buf.write("\34\37\5\b\5\2\35\36\7%\2\2\36 \5\16\b\2\37\35\3\2\2\2")
        buf.write("\37 \3\2\2\2 \7\3\2\2\2!$\5\n\6\2\"$\5\f\7\2#!\3\2\2\2")
        buf.write("#\"\3\2\2\2$,\3\2\2\2%(\7\61\2\2&)\5\n\6\2\')\5\f\7\2")
        buf.write("(&\3\2\2\2(\'\3\2\2\2)+\3\2\2\2*%\3\2\2\2+.\3\2\2\2,*")
        buf.write("\3\2\2\2,-\3\2\2\2-\t\3\2\2\2.,\3\2\2\2/\60\7\4\2\2\60")
        buf.write("\13\3\2\2\2\61\65\7\4\2\2\62\63\7\67\2\2\63\64\7;\2\2")
        buf.write("\64\66\78\2\2\65\62\3\2\2\2\66\67\3\2\2\2\67\65\3\2\2")
        buf.write("\2\678\3\2\2\28\r\3\2\2\29>\t\2\2\2:;\7\61\2\2;=\t\2\2")
        buf.write("\2<:\3\2\2\2=@\3\2\2\2><\3\2\2\2>?\3\2\2\2?\17\3\2\2\2")
        buf.write("@>\3\2\2\2\t\23\37#(,\67>")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'Var'", "<INVALID>", "'Function'", "'Parameter'", 
                     "'Return'", "'Body'", "'EndBody'", "'If'", "'Then'", 
                     "'Else'", "'ElseIf'", "'EndIf'", "'For'", "'EndFor'", 
                     "'While'", "'EndWhile'", "'Break'", "'Continue'", "'Do'", 
                     "'EndDo'", "'True'", "'False'", "'+'", "'\u00E2\u02C6\u2019'", 
                     "'*'", "'\\'", "'%'", "'+.'", "'\u00E2\u02C6\u2019.'", 
                     "'*.'", "'\\.'", "'!'", "'&&'", "'||'", "'='", "'=='", 
                     "'=/='", "'!='", "'<'", "'>'", "'<='", "'>='", "'<.'", 
                     "'>.'", "'<=.'", "'>=.'", "','", "'.'", "':'", "';'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "VAR", "ID", "FUNCTION", "PARAMETER", 
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
                      "STRING_LIT", "LITERAL", "ARRAY_LIT", "COMMENT", "WS", 
                      "ERROR_CHAR", "UNCLOSE_STRING", "ILLEGAL_ESCAPE", 
                      "UNTERMINATED_COMMENT" ]

    RULE_program = 0
    RULE_global_var_declare = 1
    RULE_var_list = 2
    RULE_variable_name = 3
    RULE_scalar_var = 4
    RULE_composite_var = 5
    RULE_init_value = 6

    ruleNames =  [ "program", "global_var_declare", "var_list", "variable_name", 
                   "scalar_var", "composite_var", "init_value" ]

    EOF = Token.EOF
    VAR=1
    ID=2
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
    LITERAL=61
    ARRAY_LIT=62
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
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 14
                self.global_var_declare()
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==BKITParser.VAR):
                    break

            self.state = 19
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
            self.state = 21
            self.match(BKITParser.VAR)
            self.state = 22
            self.match(BKITParser.COLON)
            self.state = 23
            self.var_list()
            self.state = 24
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

        def variable_name(self):
            return self.getTypedRuleContext(BKITParser.Variable_nameContext,0)


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
            self.state = 26
            self.variable_name()
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==BKITParser.ASSIGN:
                self.state = 27
                self.match(BKITParser.ASSIGN)
                self.state = 28
                self.init_value()


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

        def scalar_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Scalar_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Scalar_varContext,i)


        def composite_var(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(BKITParser.Composite_varContext)
            else:
                return self.getTypedRuleContext(BKITParser.Composite_varContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_variable_name




    def variable_name(self):

        localctx = BKITParser.Variable_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_variable_name)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 31
                self.scalar_var()
                pass

            elif la_ == 2:
                self.state = 32
                self.composite_var()
                pass


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 35
                self.match(BKITParser.COMMA)
                self.state = 38
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                if la_ == 1:
                    self.state = 36
                    self.scalar_var()
                    pass

                elif la_ == 2:
                    self.state = 37
                    self.composite_var()
                    pass


                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 8, self.RULE_scalar_var)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
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
        self.enterRule(localctx, 10, self.RULE_composite_var)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(BKITParser.ID)
            self.state = 51 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.match(BKITParser.LSQUARE)
                self.state = 49
                self.match(BKITParser.INT_LIT)
                self.state = 50
                self.match(BKITParser.RSQUARE)
                self.state = 53 
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

        def LITERAL(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.LITERAL)
            else:
                return self.getToken(BKITParser.LITERAL, i)

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.ID)
            else:
                return self.getToken(BKITParser.ID, i)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(BKITParser.COMMA)
            else:
                return self.getToken(BKITParser.COMMA, i)

        def getRuleIndex(self):
            return BKITParser.RULE_init_value




    def init_value(self):

        localctx = BKITParser.Init_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_init_value)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            _la = self._input.LA(1)
            if not(_la==BKITParser.ID or _la==BKITParser.LITERAL):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 60
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==BKITParser.COMMA:
                self.state = 56
                self.match(BKITParser.COMMA)
                self.state = 57
                _la = self._input.LA(1)
                if not(_la==BKITParser.ID or _la==BKITParser.LITERAL):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 62
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





