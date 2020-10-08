grammar BKIT;

@lexer::header {
from lexererr import *
}

@lexer::members {
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
}

options{
	language=Python3;
}

program  : VAR COLON ID SEMI EOF ;

/// Identifiers
ID: [a-z][a-zA-Z0-9]*;

/// Comment
COMMENT: ('**' .*? '**') -> skip;

/*--------------------Keywords--------------------------*/

VAR: 'Var';
/// Function
FUNCTION:  'Function';
PARAMETER: 'Parameter';
RETURN: 'Return';
/// Scope
BODY: 'Body';
ENDBODY: 'EndBody';
/// If
IF: 'If';
THEN: 'Then';
ELSE: 'Else';
ELSE_IF: 'ElseIf';
END_IF: 'EndIf';
/// Loop
FOR: 'For';
END_FOR: 'EndFor';
WHILE: 'While';
END_WHITE: 'EndWhile';
BREAK: 'Break';
CONTINUTE: 'Continue'; 
DO: 'Do';
END_DO: 'EndDo';
/// Boolean value 
TRUE: 'True';
FALSE: 'False';
/*-------------------------------------------------------*/

/*--------------------Operators--------------------------*/

/// Arithmetic operators
ADD: '+';
SUB: '−';
MUL: '*';
DIV: '\\';
MOD: '%';
ADD_FLOAT: '+.'; 
SUB_FLOAT: '−.';
MUL_FLOAT: '*.';
DIV_FLOAT: '\\.';
/// Logical operators
NOT: '!';
AND: '&&';
OR: '||';
/// Equality operators
EQUAL: '==';
EQUAL_FLOAT: '=/=';
NOT_EQUAL: '!=';
/// Relational operators
LESS_THAN: '<';
MORE_THAN: '>';
LESS_THAN_EQUAL: '<=';
MORE_THAN_EQUAL: '>=';
LESS_THAN_FLOAT: '<.';
MORE_THAN_FLOAT: '>.';
LESS_THAN_EQUAL_FLOAT: '<=.';
MORE_THAN_EQUAL_FLOAT: '>=.';
/*-------------------------------------------------------*/

/*--------------------Separators-------------------------*/
DOT: '.';
COLON: ':';
SEMI: ';';
LPAREN: '('; // Parenthesis
RPAREN: ')';
LSQUARE: '['; // Square Bracket
RSQUARE: ']';
LCURLY: '{'; // Curly Bracket
RCURLY: '}';
/*-------------------------------------------------------*/

/*---------------------Literals--------------------------*/
/// Integer
INT_LITERAL
    : '0'
    | DEC
    | '0'[xX]HEX
    | '0'[oO]OCT
    ;
fragment DEC: NON_ZERO [0-9]*;
fragment HEX: NON_ZERO [0-9A-F]*;
fragment OCT: NON_ZERO [0-7]*;
fragment NON_ZERO: [1-9];

/// Float
FLOAT_LITERAL
    :   INT_PART DECIMAL_PART EXPONENT_PART
    |   INT_PART EXPONENT_PART
    |   INT_PART DECIMAL_PART
    ;
fragment INT_PART: NON_ZERO DIGIT*; 
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXPONENT_PART: [eE] SIGN? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];

/// Boolean
BOOLEAN: TRUE | FALSE;

/// String
STRING: '"' STRING_CHAR* '"' {
    self.text = (self.text)[1:-1] #To split string
};
fragment STRING_CHAR: ESCAPE_CHAR | ~[\n'"\\] | '\'' '"';
fragment ESCAPE_CHAR
    : '\\b'
	| '\\f'
	| '\\r'
	| '\\n'
	| '\\t'
	| '\\\''
	| '\\\\'
    ;

/// Array

/*-------------------------------------------------------*/


WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines
/*--------------------Lexical errors---------------------*/
ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CHAR* ( '\n' | EOF ) {
    self.text = (self.text)[1:]
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_CHAR {
    self.text = (self.text)[1:]
};
ILLEGAL_CHAR: '\\' ~[bfrnt'\\] | ~'\\';
UNTERMINATED_COMMENT: '**' .*?;
/*-------------------------------------------------------*/