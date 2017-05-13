/*
 [The "BSD licence"]
 Copyright (c) 2013 Terence Parr
 All rights reserved.

 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. The name of the author may not be used to endorse or promote products
    derived from this software without specific prior written permission.

 THIS SOFTWARE IS PROVIDED BY THE AUTHOR ``AS IS'' AND ANY EXPRESS OR
 IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES
 OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
 IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR ANY DIRECT, INDIRECT,
 INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
 DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
 THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
 (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF
 THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
*/

/**
derived from http://svn.r-project.org/R/trunk/src/main/gram.y
http://cran.r-project.org/doc/manuals/R-lang.html#Parser

I'm no R genius but this seems to work.

Requires RFilter.g4 to strip away NL that are really whitespace,
not end-of-command. See TestR.java

Usage:

$ antlr4 R.g4 RFilter.g4
$ javac *.java
$ java TestR sample.R
... prints parse tree ...
*/
grammar R;

parse
    : ( expr (';'| NL ) | NL )* EOF
    ;

expr
    : expr '[[' sublist ']' ']'  // '[[' follows R's yacc grammar
    | expr '[' sublist ']'
    | expr dotop expr
    | ('-'|'+') expr
    | expr affectation
    | expr rangeopexpr
    | <assoc=right> expr USER_OP expr // anything wrappedin %: '%' .* '%'
    | <assoc=right> expr operator expr
    | <assoc=right> expr comparison expr
    | '!' expr
    | expr ('&'|'&&') expr
    | expr ('|'|'||') expr
    | formula_simple
    | functiondef '(' NL* formlist? NL* ')' expr // define function
    | functioncall
    | NL* '{' NL* exprlist NL* '}' NL*  // compound statement
    | returnexpr
    | ifelseexpr
    | ifexpr
    | forexpr
    | whileexpr
    | repeatexpr
    | '?' expr // get help on expr, usually string or ID
    | nextexpr
    | 'break'
    | ('(' expr ')')
    | constant
    | identifier
    ;

affectation
    : affectop NL? expr
    ;

rangeopexpr
    : rangeop expr
    ;

exprlist
    : (expr ((';'|NL) expr?)*)
    |
    ;
    
formlist
    : form ( NL? ',' NL* form)*
    ;

form:   ID
    |   ID '=' expr
    |   '...'
    ;

sublist
    : sub ( NL* ',' NL* sub NL* )* ;

sublistadd
    : identifier ( NL? '+' NL? identifier NL? )* ;

sub
    : identifier '=' range_simple
    | identifier '=' expr
    | STRING '='
    | STRING '=' expr
    | 'NULL' '='
    | 'NULL' '=' expr
    | '...'
    | ':'
    | expr
    ;

range_simple
    : (identifier | INT ) ':' (identifier | INT )
    ;
    
//////    
// NEW
//////

constant
    : STRING
    | HEX
    | INT
    | FLOAT
    | COMPLEX
    | 'NULL'
    | 'NA'
    | 'Inf'
    | 'NaN'
    | boolean
    ;

boolean
    : 'TRUE'
    | 'FALSE'
    ;

nextexpr
    : 'next'
    ;

repeatexpr
    : 'repeat' expr
    ;

whileexpr
    : 'while' '(' expr ')' expr
    ;

forexpr
    : 'for' '(' identifier 'in' expr ')' expr
    ;

ifexpr
    : 'if' '(' expr ')' NL*  expr
    ;
    
ifelseexpr
    : 'if' '(' expr ')' NL*  expr NL* 'else' NL* expr
    ;

returnexpr
    : 'return' '(' expr ')'
    ;

functioncall
    : identifier (('(' ')') | ('(' NL* sublist NL* ')'))
    ;

formula_simple
    : formula_simple_B
    | formula_simple_A
    | formula_simple_C
    ;

formula_simple_A
    : identifier formop ( sublistadd | '.' )
    ;

formula_simple_B
    : 'within' '(' identifier ',' (
           ('{' expr (';' expr)* '}' ) |
           ( identifier affectop expr )
           ) ')'
    ;

formula_simple_C
    : '(' expr ')' formop ( sublistadd | '.' )
    ;

affectop
    : '<-'
    | '<<-'
    | '='
    | '->'
    | '->>'
    | ':='
    ;

functiondef
    : 'function'
    ;
    
identifier
    : ID
    ;

formop
    : '~'
    ;

rangeop
    : ':'
    | '::'
    | ':::'
    ;

dotop
    : '$'
    | '@'
    ;

operator
    : '-'
    | '+'
    | '*'
    | '/'
    | '%'
    | '^'
    | '%%'
    ;

comparison
    : '>'
    | '>='
    | '<'
    | '<='
    | '=='
    | '!='
    ;
    
//////
// END
//////

HEX :   '0' ('x'|'X') HEXDIGIT+ [Ll]? ;

INT :   DIGIT+ [Ll]? ;

fragment
HEXDIGIT : ('0'..'9'|'a'..'f'|'A'..'F') ;

FLOAT:  DIGIT+ '.' DIGIT* EXP? [Ll]?
    |   DIGIT+ EXP? [Ll]?
    |   '.' DIGIT+ EXP? [Ll]?
    ;
fragment
DIGIT:  '0'..'9' ; 
fragment
EXP :   ('E' | 'e') ('+' | '-')? INT ;

COMPLEX
    :   INT 'i'
    |   FLOAT 'i'
    ;

STRING
    :   '"' ( ESC | ~[\\"] )*? '"'
    |   '\'' ( ESC | ~[\\'] )*? '\''
    |   '`' ( ESC | ~[\\'] )*? '`'
    ;

fragment
ESC :   '\\' [abtnfrv"'\\]
    |   UNICODE_ESCAPE
    |   HEX_ESCAPE
    |   OCTAL_ESCAPE
    ;

fragment
UNICODE_ESCAPE
    :   '\\' 'u' HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT
    |   '\\' 'u' '{' HEXDIGIT HEXDIGIT HEXDIGIT HEXDIGIT '}'
    ;

fragment
OCTAL_ESCAPE
    :   '\\' [0-3] [0-7] [0-7]
    |   '\\' [0-7] [0-7]
    |   '\\' [0-7]
    ;

fragment
HEX_ESCAPE
    :   '\\' HEXDIGIT HEXDIGIT?
    ;

ID  :   '.' (LETTER|'_'|'.') (LETTER|DIGIT|'_'|'.')*
    |   LETTER (LETTER|DIGIT|'_'|'.')*
    ;
    
fragment LETTER  : [a-zA-Z] ;

USER_OP :   '%' .*? '%' ;

COMMENT :   '#' .*? '\r'? '\n' -> type(NL) ;

// Match both UNIX and Windows newlines
NL      :   '\r'? '\n' ;

WS      :   [ \t\u000C]+ -> skip ;
