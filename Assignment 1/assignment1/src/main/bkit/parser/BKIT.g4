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

/* ==================PARSER=RULES====================== */
/// BKIT program
program  : (global_var_declare)+ EOF;
/// Global variable declaration part
global_var_declare: VAR COLON var_list SEMI;
var_list: variable (ASSIGN init_value)?;
variable: variable_name (COMMA variable_name)*;
variable_name: (scalar_var | composite_var);
scalar_var: ID;
composite_var: ID (LSQUARE INT_LIT RSQUARE)+;
init_value: (literal | scalar_var) (COMMA (LITERAL | scalar_var))*;
literal: INT_LIT | ARRAY_LIT | STRING_LIT | FLOAT_LIT | BOOLEAN_LIT;
/* ===================LEXER=RULES=======================*/

/*--------------------Identifiers-----------------------*/
ID: [a-z][a-zA-Z0-9]*;
/*------------------------------------------------------*/

/*--------------------Keywords--------------------------*/
/// Function
VAR: 'Var';
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
ASSIGN: '=';
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
COMMA: ',';
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
INT_LIT
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
FLOAT_LIT
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
BOOLEAN_LIT: TRUE | FALSE;

/// String
STRING_LIT: '"' STRING_CHAR* '"' {
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
ARRAY_LIT: LCURLY (WS_A* (LITERAL)? WS_A* COMMA WS_A* LITERAL WS_A*)* RCURLY;
fragment WS_A: ' ';
LITERAL: INT_LIT | FLOAT_LIT | STRING_LIT | ARRAY_LIT | BOOLEAN_LIT;
/*-------------------------------------------------------*/

COMMENT: ('**' .*? '**') -> skip; // skip comment
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

/*--------------------Lexical errors---------------------*/
ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CHAR* ( '\n' | EOF ) {
    self.text = (self.text)[1:]
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_CHAR {
    self.text = (self.text)[1:]
};
fragment ILLEGAL_CHAR: '\\' ~[bfrnt'\\] | ~'\\';
UNTERMINATED_COMMENT: '**' .*?;
/*-------------------------------------------------------*/