grammar SimpleWorkflow;

parse
    : final_stmt*  EOF 
    ;
    
final_stmt
    : if_stmt
    | for_stmt
    | affectation_stmt_comma
    | stmt_comma 
    ;
    
/////
// variable
/////

affectation_stmt_comma
    : affectation_stmt ';'
    ;

affectation_stmt
    : 'set' variable_name '=' expression
    ;
    
/////
// for
/////

for_stmt
    : 'for' '(' variable_name 'in' function_call ')' '{' final_stmt+ '}' 
    ;
    
/////
// if
/////

if_stmt
    : 'if' '(' expression ')' '{' final_stmt+ '}' ('else' '{' final_stmt+ '}')?
    ;
    
evaluation_function
    : Identifier 
    ;
    
/////////////
// expression
/////////////


expression
    : expression_no_binary
    | (expression_no_binary binary_operator expression )
    ;

expression_no_binary
    : constant 
    | variable_name
    | data_or_module_output
    | ('(' expression ')')
    | (unary_operator expression_no_binary )
    | function_call
    ;

function_call
    : evaluation_function '(' expression? (',' expression)* ')'
    ;
    
variable_name
    : Identifier
    ;
    
binary_operator
    : '+' | '-' | '*' | '/' | '%' | '&&' | '||' | '==' | '!=' | '<=' | '>=' | '>' | '<'
    ;

unary_operator
    : '-' | '+' | '!'
    ;

////////
// stmt
////////

stmt_comma 
    : stmt ';'
    ;
    
stmt
    : connect_stmt
    | data_stmt
    | module_stmt
    ;


connect_stmt
    : ('connect' data_or_module_output ('to' | '->') module_input )
    | ('connect' '(' data_or_module_output ',' module_input ')' )
    ;
    
data_or_module_output
    : element_name ('.' inout_name)?
    ;

module_input
    : element_name ('.' inout_name)?
    ;

data_stmt
    : element_name '=' data_name
    ;

module_stmt
    : element_name '=' module_call 
    ;

////////
// rules
////////

module_call
    : module_name '(' list_param_affectation ')' ;
    
element_name
    : Identifier 
    ;
    
list_param_affectation    
    : param_affectation? (',' param_affectation)*
    ;
    
param_affectation
    : param_name '=' expression
    ;
    
param_name
    : Identifier
    ;

inout_name
    : Identifier
    ;

module_name
    : 'flowmodule' '.' ( Identifier | STRING ) // for autocompletion
    ;

data_name
    : 'flowdata' '.' (Identifier | STRING ) // for autocompletion
    ;

constant
    : integer_number
    | real_number
    | string_literal
    ;

string_literal
    : STRING
    ;

integer_number
    : Sign? Digits
    ;
    
real_number
    : (Sign? Digits '.' Digits ('e' Sign? Digits)?)
    | (Sign? Digits 'e' Sign? Digits)
    ;
    

/////////
// tokens
/////////

Digits
    : DIGIT+
    ;

Identifier
    : LETTER LETTER_DIGIT*
    ;
    
Sign
    : '+' | '-'
    ;
    
STRING
    : STRING_DOUBLE_QUOTE
    | STRING_QUOTE
    ;
    
STRING_DOUBLE_QUOTE
    : '"' (NO_DOUBLE_QUOTE | '\\"')* '"'
    ;
    
STRING_QUOTE
    : '\'' (NO_QUOTE | '\\\'')* '\''
    ;
    
fragment NO_QUOTE
    : ~[']
    ;

fragment NO_DOUBLE_QUOTE
    : ~["]
    ;

fragment LETTER_DIGIT
    : LETTER | DIGIT
    ;
    
fragment DIGIT
    : [0-9]
    ;

fragment LETTER      
    : [a-zA-Z\u0080-\u00FF_] 
    ;

LINE_COMMENT:   '#' .*? '\r'? '\n' {skip();} ;

WS          :   [ \t\r\n] -> skip ;
