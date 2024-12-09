grammar python;

tokens { INDENT, DEDENT }

@lexer::header{
from Denter import DenterHelper
from pythonParser import pythonParser
}
@lexer::members {
"""
NOTE:
This Dynamic indent and dedent token support for the lexer is from the DenterHelper library.
To avoid having to pip download DenterHelper, I just downloaded the DenterHelper locally (Denter.py)
https://github.com/yshavit/antlr-denter/tree/main
"""
class pythonDenter(DenterHelper):
    def __init__(self, lexer, nl_token, indent_token, dedent_token, ignore_eof):
        super().__init__(nl_token, indent_token, dedent_token, ignore_eof)
        self.lexer: pythonLexer = lexer

    def pull_token(self):
        return super(pythonLexer, self.lexer).nextToken()

denter = None

def nextToken(self):
    if not self.denter:
        self.denter = self.pythonDenter(self, self.NL, pythonParser.INDENT, pythonParser.DEDENT, False)
    return self.denter.next_token()

}

COMMENT_SINGLELINE: '#' ~[\r\n]* -> skip;
COMMENT_TRIPLE_QUOTE: '"""' .*? '"""' -> skip;
COMMENT_SINGLE_TRIPLE_QUOTE: '\'\'\'' .*? '\'\'\'' -> skip;

// operands
ADD: '+' ;
SUB: '-';                         
MUL: '*';                         
DIV: '/';                         
MOD: '%';                         

// assignments
ASSIGN: '=';                        
ADD_ASSIGN: '+=';
SUB_ASSIGN: '-=';
MUL_ASSIGN: '*=';
DIV_ASSIGN: '/=';

// control statements
IF: 'if' ;
ELIF: 'elif' ;
ELSE: 'else' ;
WHILE: 'while';
FOR: 'for';

// comparison
LT: '<' ;
LTE: '<=' ;
GT: '>' ;
GTE: '>=' ;
EQL: '==' ; 
NEQL: '!=' ;

AND: 'and' ;
OR: 'or' ;
NOT: 'not' ;

LBRACKET: '['; 
RBRACKET: ']' ;
LPAREN: '(';
RPAREN: ')';
COMMA: ','; 
COLON: ':' ;
RANGE: 'range' ;
IN: 'in';

VARIABLE: [a-zA-Z_][a-zA-Z0-9_]*; 
STRING: ('"' (~["\\] | '\\' ["\\])* '"' | '\'' (~['\\] | '\\' ['\\])* '\''); 
NUMBER: [0-9]+('.'[0-9]+)?;         
NL: ('\r'? '\n' '\t'*); 
WS: [ \t]+ -> skip;                 





// Parser rules
program
    : (statement NL?)+ EOF
    ;

body
    : (block NL|NL|block)+ ;    //there is one body for every statement that requires indent/dedent.

block
    : statement                 //the body can then branch off into multiple "blocks" which comprise of a single statement.
    ;

statement
    : assignment
    | expression
    | if_statement
    | while_loop
    | for_loop
    ;     

assignment
    : VARIABLE ASSIGN expression
    | VARIABLE ADD_ASSIGN expression
    | VARIABLE SUB_ASSIGN expression
    | VARIABLE MUL_ASSIGN expression
    | VARIABLE DIV_ASSIGN expression
    ;

expression
    : SUB expression                   // unary minus
    | expression ADD expression
    | expression SUB expression
    | expression MUL expression
    | expression DIV expression
    | expression MOD expression
    | LPAREN expression RPAREN
    | array
    | STRING
    | NUMBER
    | VARIABLE
    ;

if_statement
    : IF condition COLON INDENT body DEDENT (elif_statement)* (else_statement)?
    ;

elif_statement
    : ELIF condition COLON INDENT body DEDENT
    ;

else_statement
    : ELSE COLON INDENT body DEDENT
    ;

while_loop
    : WHILE condition COLON INDENT body DEDENT
    ;

for_loop
    : FOR VARIABLE IN iterable COLON INDENT body DEDENT
    ;

iterable
    : RANGE LPAREN expression (',' expression)? (',' expression)? RPAREN
    | array
    | VARIABLE
    ;

condition
    : LPAREN condition RPAREN
    | expression comparison expression
    | NOT expression
    | NOT condition
    | condition AND condition
    | condition OR condition
    | expression
    ;

comparison
    : LT
    | LTE
    | GT
    | GTE
    | EQL
    | NEQL
    ;

term
    : factor ((MUL | DIV | MOD) factor)*
    ;

factor
    : NUMBER
    | VARIABLE
    | STRING
    | array
    ;

array
    : LBRACKET (expression (COMMA expression)*)? RBRACKET
    ;
