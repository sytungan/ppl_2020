# Generated from d:\Works\HK5\PPL\Assignment 1\initial\initial\src\main\bkit\parser\BKIT.g4 by ANTLR 4.8
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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3B")
        buf.write("\13\4\2\t\2\3\2\3\2\3\2\3\2\3\2\3\2\3\2\2\2\3\2\2\2\2")
        buf.write("\t\2\4\3\2\2\2\4\5\7\5\2\2\5\6\7\62\2\2\6\7\7\3\2\2\7")
        buf.write("\b\7\63\2\2\b\t\7\2\2\3\t\3\3\2\2\2\2")
        return buf.getvalue()


class BKITParser ( Parser ):

    grammarFileName = "BKIT.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "'Var'", "'Function'", 
                     "'Parameter'", "'Return'", "'Body'", "'EndBody'", "'If'", 
                     "'Then'", "'Else'", "'ElseIf'", "'EndIf'", "'For'", 
                     "'EndFor'", "'While'", "'EndWhile'", "'Break'", "'Continue'", 
                     "'Do'", "'EndDo'", "'True'", "'False'", "'+'", "'\u00E2\u02C6\u2019'", 
                     "'\u00E2\u02C6\u2014'", "'\\'", "'%'", "'+.'", "'\u00E2\u02C6\u2019.'", 
                     "'\u00E2\u02C6\u2014.'", "'\\.'", "'!'", "'&&'", "'||'", 
                     "'=='", "'=/='", "'!='", "'<'", "'>'", "'<='", "'>='", 
                     "'<.'", "'>.'", "'<=.'", "'>=.'", "'.'", "':'", "';'", 
                     "'('", "')'", "'['", "']'", "'{'", "'}'" ]

    symbolicNames = [ "<INVALID>", "ID", "COMMENT", "VAR", "FUNCTION", "PARAMETER", 
                      "RETURN", "BODY", "ENDBODY", "IF", "THEN", "ELSE", 
                      "ELSE_IF", "END_IF", "FOR", "END_FOR", "WHILE", "END_WHITE", 
                      "BREAK", "CONTINUTE", "DO", "END_DO", "TRUE", "FALSE", 
                      "ADD", "SUB", "MUL", "DIV", "MOD", "ADD_FLOAT", "SUB_FLOAT", 
                      "MUL_FLOAT", "DIV_FLOAT", "NOT", "AND", "OR", "EQUAL", 
                      "EQUAL_FLOAT", "NOT_EQUAL", "LESS_THAN", "MORE_THAN", 
                      "LESS_THAN_EQUAL", "MORE_THAN_EQUAL", "LESS_THAN_FLOAT", 
                      "MORE_THAN_FLOAT", "LESS_THAN_EQUAL_FLOAT", "MORE_THAN_EQUAL_FLOAT", 
                      "DOT", "COLON", "SEMI", "LPAREN", "RPAREN", "LSQUARE", 
                      "RSQUARE", "LCURLY", "RCURLY", "INT_LITERAL", "FLOAT_LITERAL", 
                      "BOOLEAN", "STRING", "WS", "ERROR_CHAR", "UNCLOSE_STRING", 
                      "ILLEGAL_ESCAPE", "UNTERMINATED_COMMENT" ]

    RULE_program = 0

    ruleNames =  [ "program" ]

    EOF = Token.EOF
    ID=1
    COMMENT=2
    VAR=3
    FUNCTION=4
    PARAMETER=5
    RETURN=6
    BODY=7
    ENDBODY=8
    IF=9
    THEN=10
    ELSE=11
    ELSE_IF=12
    END_IF=13
    FOR=14
    END_FOR=15
    WHILE=16
    END_WHITE=17
    BREAK=18
    CONTINUTE=19
    DO=20
    END_DO=21
    TRUE=22
    FALSE=23
    ADD=24
    SUB=25
    MUL=26
    DIV=27
    MOD=28
    ADD_FLOAT=29
    SUB_FLOAT=30
    MUL_FLOAT=31
    DIV_FLOAT=32
    NOT=33
    AND=34
    OR=35
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
    DOT=47
    COLON=48
    SEMI=49
    LPAREN=50
    RPAREN=51
    LSQUARE=52
    RSQUARE=53
    LCURLY=54
    RCURLY=55
    INT_LITERAL=56
    FLOAT_LITERAL=57
    BOOLEAN=58
    STRING=59
    WS=60
    ERROR_CHAR=61
    UNCLOSE_STRING=62
    ILLEGAL_ESCAPE=63
    UNTERMINATED_COMMENT=64

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.8")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(BKITParser.VAR, 0)

        def COLON(self):
            return self.getToken(BKITParser.COLON, 0)

        def ID(self):
            return self.getToken(BKITParser.ID, 0)

        def SEMI(self):
            return self.getToken(BKITParser.SEMI, 0)

        def EOF(self):
            return self.getToken(BKITParser.EOF, 0)

        def getRuleIndex(self):
            return BKITParser.RULE_program




    def program(self):

        localctx = BKITParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 2
            self.match(BKITParser.VAR)
            self.state = 3
            self.match(BKITParser.COLON)
            self.state = 4
            self.match(BKITParser.ID)
            self.state = 5
            self.match(BKITParser.SEMI)
            self.state = 6
            self.match(BKITParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





