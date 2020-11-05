/* Student_id: 1811389 */
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
program  : (global_var_declare)* function_declare* EOF;
/// **Global variable declaration part** ///
global_var_declare: VAR COLON var_list SEMI;
var_list: var_def (COMMA var_def)*;
var_def: variable (ASSIGN init_value)?; // variable = initial-value
variable: (scalar_var | composite_var); // 2 type scalar and composite
scalar_var: ID;
composite_var: ID dimension+;
dimension: (LSQUARE INT_LIT RSQUARE);
init_value: literal;

literal // literal type
    : INT_LIT 
    | FLOAT_LIT 
    | STRING_LIT 
    | bool_literal
    | array_literal
    ;
// Array literal
array_literal: LCURLY array_element_list? RCURLY;
array_element_list
    : array_element (COMMA array_element)*
    ;
array_element: literal;
bool_literal: TRUE | FALSE;
/// **Function declaration part** ///
function_declare: FUNCTION COLON ID (PARAMETER COLON parameter_list)? BODY COLON statement_list END_BODY DOT;
parameter_list: parameter (COMMA parameter)*;
parameter: variable; // 'variable' in Global variable declaration part
statement_list
    : local_var_declare* 
        ( assignment_statement
        | if_statement 
        | for_statement 
        | while_statement
        | do_while_statement
        | break_statement
        | continue_statement
        | call_statement
        | return_statement
        )*
    ;
// *Statements*
local_var_declare: global_var_declare;
assignment_statement: (scalar_var index_operator?) ASSIGN expression SEMI;
if_statement
    :
        IF expression THEN statement_list
        (ELSE_IF expression THEN statement_list)*
        (ELSE statement_list)?
        END_IF DOT
    ;
for_statement
    :
        FOR LPAREN scalar_var ASSIGN initExpr COMMA conditionExpr COMMA updateExpr RPAREN DO
            statement_list
        END_FOR DOT
    ;
initExpr: expression;
conditionExpr: expression;
updateExpr: expression;
while_statement: WHILE expression DO statement_list END_WHITE DOT;
do_while_statement: DO statement_list WHILE expression END_DO DOT;
break_statement: BREAK SEMI;
continue_statement: CONTINUTE SEMI;
call_statement: function_call SEMI;
return_statement: RETURN expression? SEMI;
// Expression: operators and operands
expression //lowest
    : exp1 relational_operator exp1 
    | exp1
    ;
exp1
    : exp1 (AND | OR) exp2 
    | exp2
    ;
exp2
    : exp2 adding exp3 
    | exp3
    ;
exp3
    : exp3 multiplying exp4 
    | exp4
    ;
exp4
    : NOT exp4 
    | exp5
    ;
exp5
    : sign exp5
    | exp6
    ;
exp6
    : exp6 index_operator
    | exp7
    ;
exp7
    : function_call
    | exp8
    ;
exp8
    : LPAREN expression RPAREN
    | operand
    ;
operand
    : literal
    | ID
    ;
// Operators
adding
    : ADD
    | SUB
    | ADD_FLOAT
    | SUB_FLOAT
    ;
multiplying
    : MUL
    | DIV
    | MOD
    | MUL_FLOAT
    | DIV_FLOAT
    ;
relational_operator
    : EQUAL
    | NOT_EQUAL
    | LESS_THAN
    | MORE_THAN
    | LESS_THAN_EQUAL
    | MORE_THAN_EQUAL
    | NOT_EQUAL_FLOAT
    | LESS_THAN_FLOAT
    | MORE_THAN_FLOAT
    | LESS_THAN_EQUAL_FLOAT
    | MORE_THAN_EQUAL_FLOAT
    ;
sign
    : SUB 
    | SUB_FLOAT
    ;
index_operator //6.4 Index operators
    : (LSQUARE expression RSQUARE)+
    ; 
function_call // 6.5 Function call
    : ID LPAREN argument_list RPAREN
    ;
argument_list: expression? (COMMA expression)*;
/* ===================LEXER=RULES=======================*/

/*--------------------Identifiers-----------------------*/
ID: [a-z][a-zA-Z0-9_]*;
/*------------------------------------------------------*/

/*--------------------Keywords--------------------------*/
/// Function
VAR: 'Var';
FUNCTION:  'Function';
PARAMETER: 'Parameter';
RETURN: 'Return';
/// Scope
BODY: 'Body';
END_BODY: 'EndBody';
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
SUB: '-';
MUL: '*';
DIV: '\\';
MOD: '%';
ADD_FLOAT: '+.'; 
SUB_FLOAT: '-.';
MUL_FLOAT: '*.';
DIV_FLOAT: '\\.';
/// Logical operators
NOT: '!';
AND: '&&';
OR: '||';
/// Equality operators
ASSIGN: '=';
EQUAL: '==';
NOT_EQUAL: '!=';
NOT_EQUAL_FLOAT: '=/=';
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
fragment DEC: [1-9] [0-9]*;
fragment HEX: [1-9A-F] [0-9A-F]*;
fragment OCT: [1-7] [0-7]*;

/// Float
FLOAT_LIT
    :   INT_PART DECIMAL_PART EXPONENT_PART
    |   INT_PART EXPONENT_PART
    |   INT_PART DECIMAL_PART
    ;
fragment INT_PART: [0-9]+; 
fragment DECIMAL_PART: '.' DIGIT*;
fragment EXPONENT_PART: [eE] SIGN? DIGIT+;
fragment DIGIT: [0-9];
fragment SIGN: [+-];

/// Boolean -> parser


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

/// Array -> parser
// ARRAY_LIT: LCURLY (WS_A* LITERAL WS_A* (COMMA WS_A* LITERAL WS_A*)*)? RCURLY;
// LITERAL
//     : INT_LIT
//     | FLOAT_LIT
//     | STRING_LIT
//     | BOOLEAN_LIT
//     | ARRAY_LIT
//     ;
// fragment WS_A: ' ';

/*-------------------------------------------------------*/

COMMENT: ('**' .*? '**') -> skip; // skip comment
WS : [ \t\r\n\f]+ -> skip ; // skip spaces, tabs, newlines

/*--------------------Lexical errors---------------------*/
ERROR_CHAR: .;
UNCLOSE_STRING: '"' STRING_CHAR* ( '\n' | EOF ) {
    self.text = (self.text)[1:]
    #newline on windowOs: \r\n, linuxOs: \n, macOs > 9: \r
};
ILLEGAL_ESCAPE: '"' STRING_CHAR* ILLEGAL_CHAR {
    self.text = (self.text)[1:]
};
fragment ILLEGAL_CHAR: ('\\' ~[bfrnt'\\]) | '\'' ~'"';
UNTERMINATED_COMMENT: '**' .*?;
/*-------------------------------------------------------*/