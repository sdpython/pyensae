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
    : 'set' variable_name '=' constant
    ;
    
variable_name
    : Identifier
    ;

/////
// for
/////

for_stmt
    : 'for' '(' loop_variable 'in' range_function ')' '{' final_stmt+ '}' 
    ;
    
range_function
    : evaluation_function '(' data_or_module_output_constant? (',' data_or_module_output_constant)* ')'
    ;
    
loop_variable
    : Identifier
    ;
    
/////
// if
/////

if_stmt
    : 'if' '(' condition ')' '{' final_stmt+ '}' ('else' '{' final_stmt+ '}')?
    ;
    
condition
    : evaluation_function '(' data_or_module_output_constant? (',' data_or_module_output_constant)* ')'
    ;
    
evaluation_function
    : Identifier 
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
    
data_or_module_output_constant
    : data_or_module_output
    | constant 
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
    : param_name '=' constant
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
