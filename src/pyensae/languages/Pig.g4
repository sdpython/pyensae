/*
http://wiki.apache.org/pig/PigLexer
http://wiki.apache.org/pig/PigParser

A few types were replaced by <type_>.
*/

grammar Pig;

parse
    : query EOF
    ;

query 
    : statement* 
    | NOT statement
    | query statement
    ;

statement 
    : ( alias EQUAL ) ? op_clause SEMI_COLON 
    | NOT ( statement alias? op_clause )
    ;

alias 
    : IDENTIFIER
    ;

op_clause 
    : load_clause 
    | store_clause 
    | filter_clause 
    | distinct_clause
    ;

load_clause 
    : LOAD filename ( USING func_clause )? as_clause?
    ;

filename 
    : QUOTEDSTRING
    ;

as_clause
    : AS tuple_def
    ;

tuple_def 
    : LEFT_PAREN field ( COMMA field )* RIGHT_PAREN
    | NOT ( tuple_def field+ )
    ;

field 
    : IDENTIFIER ( COLON type_ )?
    | NOT ( field IDENTIFIER type_? )
    ;

type_ 
    : simple_type 
    | tuple_type 
    | bag_type 
    | map_type
    ;

simple_type 
    : INT 
    | LONG 
    | FLOAT 
    | DOUBLE 
    | CHARARRAY 
    | BYTEARRAY
    ;

tuple_type 
    : tuple_ tuple_def
    ;

bag_type 
    : BAG tuple_def
    ;

map_type 
    : MAP LEFT_BRACKET RIGHT_BRACKET
    ;

func_clause 
    : func_name LEFT_PAREN func_args? RIGHT_PAREN
    | NOT ( FUNC func_name func_args? )
    ;

func_name 
    : IDENTIFIER ( PERIOD IDENTIFIER )*
    | IDENTIFIER+
    ;

func_args 
    : QUOTEDSTRING ( COMMA QUOTEDSTRING )*
    | QUOTEDSTRING+
    ;

store_clause 
    : STORE alias INTO filename ( USING func_clause ) ?
    ;

filter_clause 
    : FILTER alias BY cond
    ;

cond 
    : or_cond
    ;

or_cond 
    : and_cond  ( OR and_cond )*
    ;

and_cond 
    : unary_cond ( AND unary_cond )*
    ;

unary_cond 
    : LEFT_PAREN cond RIGHT_PAREN
    | expr FILTEROP expr
    | func_clause
    | null_check_cond
    | not_cond
    ;

not_cond 
    : NOT unary_cond
    ;

null_check_cond 
    : expr IS NOT? NULL
    ;

expr 
    : add_expr
    ;

add_expr 
    : multi_expr ( ( PLUS | MINUS ) multi_expr )*
    ;

multi_expr 
    : cast_expr ( ( START | DIV | PERCENT ) cast_expr )*
    ;

cast_expr 
    : ( LEFT_PAREN type_ RIGHT_PAREN ) unary_expr
    | NOT ( CAST_EXPR type_ unary_expr )
    | unary_expr
    ;

unary_expr 
    : eval_expr 
    | ( LEFT_PAREN infix_expr RIGHT_PAREN )  
    | neg_expr
    ;

eval_expr 
    : const_expr 
    | var_expr
    ;

var_expr 
    : projectable_expr ( dot_proj | pound_proj )*
    ;

projectable_expr
    : func_clause 
    | col_ref 
    | bin_expr
    ;

dot_proj 
    : PERIOD ( col_ref | ( LEFT_PAREN col_ref ( COMMA col_ref )* RIGHT_PAREN ) )
    | NOT ( PERIOD col_ref+ )
    ;

pound_proj 
    : POUND ( QUOTEDSTRING | NULL )
    ;

bin_expr 
    : LEFT_PAREN cond QMARK infix_expr COLON infix_expr RIGHT_PAREN
    | NOT ( BIN_EXPR cond infix_expr infix_expr )
    ;

neg_expr 
    : MINUS cast_expr
    ;

distinct_clause 
    : DISTINCT alias
    ;

col_ref 
    : alias_col_ref 
    | dollar_col_ref
    ;

alias_col_ref 
    : GROUP 
    | IDENTIFIER
    ;

dollar_col_ref 
    : DOLLAR INTEGER
    ;

infix_expr 
    : add_expr
    ;

const_expr 
    : scalar 
    | map_ 
    | bag 
    | tuple_
    ;

scalar 
    : INTEGER 
    | LONGINEGER 
    | FLOATNUMBER 
    | DOUBLENUMBER 
    | QUOTEDSTRING 
    | NULL
    ;

map_ 
    : LEFT_BRACKET ( keyvalue ( COMMA keyvalue )* )? RIGHT_BRACKET
    | NOT ( MAP_VAL keyvalue+ )
    ;

keyvalue 
    : string_val POUND const_expr
    | NOT ( KEY_VAL_PAIR string_val const_expr )
    ;

string_val 
    : QUOTEDSTRING 
    | NULL
    ;

bag 
    : LEFT_CURLY ( tuple_ ( COMMA tuple_ )* )? RIGHT_CURLY
    | NOT ( BAG_VAL tuple_+ )
    ;

tuple_ 
    : LEFT_PAREN ( const_expr ( COMMA const_expr )* )? RIGHT_PAREN
    | NOT ( tuple_ const_expr+ )
    ;


DEFINE 
    : 'define'
    ;

LOAD   
    : 'load'
    ;

FILTER 
    : 'filter'
    ;

FOREACH 
    : 'foreach'
    ;

ORDER   
    :  'order'
    ;

ARRANGE 
    : 'arrange'
    ;

DISTINCT 
    : 'distinct'
    ;

COGROUP 
    : 'cogroup'
    ;

JOIN 
    : 'join'
    ;

CROSS 
    : 'cross'
    ;

UNION 
    : 'union'
    ;

SPLIT 
    : 'split'
    ;

INTO 
    : 'into'
    ;

IF 
    : 'if'
    ;

ALL 
    : 'all'
    ;

ANY 
    : 'any'
    ;

AS 
    : 'as'
    ;

BY  
    : 'by'
    ;

USING 
    : 'using'
    ;

INNER 
    : 'inner'
    ;

OUTER 
    : 'outer'
    ;

ONSCHEMA 
    : 'ONSCHEMA'
    ;

STAR : '*'
;

PARALLEL : 'parallel'
;

PARTITION : 'partition'
;

GROUP : 'group'
;

AND : 'and'
;

OR : 'or'
;

NOT : 'not'
;

GENERATE : 'generate'
;

FLATTEN : 'flatten'
;

EVAL : 'eval'
;

ASC : 'asc'
;

DESC : 'desc'
;

INT : 'int'
;

LONG : 'long'
;

FLOAT : 'float'
;

DOUBLE : 'double'
;

CHARARRAY : 'chararray'
;

BYTEARRAY : 'bytearray'
;

BAG 
    : 'bag'
    ;

TUPLE 
    : 'tuple'
    ;

MAP 
    : 'map'
    ;

IS 
    : 'is'
    ;

NULL 
    : 'null'
    ;

STREAM 
    : 'stream'
    ;

THROUGH 
    : 'through'
    ;

STORE 
    : 'store'
    ;

MAPREDUCE 
    : 'mapreduce'
    ;

SHIP 
    : 'ship'
    ;

CACHE 
    : 'cache'
    ;

INPUT 
    : 'input'
    ;

OUTPUT 
    : 'output'
    ;

ERROR 
    : 'stderr'
    ;

STDIN 
    : 'stdin'
    ;

STDOUT 
    : 'stdout'
    ;

LIMIT 
    : 'limit'
    ;

SAMPLE 
    : 'sample'
    ;

LEFT 
    : 'left'
    ;

RIGHT 
    : 'right'
    ;

FULL 
    : 'full'
    ;

fragment DIGIT 
    : '0'..'9'
    ;

fragment LETTER 
    : 'a'..'z' | 'A'..'Z'
    ;
    
fragment SPECIALCHAR 
    : '_'
    ;
   
fragment FSSPECIALCHAR 
    : '-' | ':' | '/'
    ;

IDENTIFIER: LETTER ( DIGIT | LETTER | SPECIALCHAR | '::' )*
;

fragment FLOATINGPOINT : INTEGER ( '.' INTEGER )? | '.' INTEGER 
;
    
INTEGER: ( DIGIT )+
;

LONGINTEGER: INTEGER ( 'l' | 'L' )?
;
    
DOUBLENUMBER : FLOATINGPOINT ( ('e' | 'E') ( '-' | '+' )? FLOATINGPOINT )?
;
    
FLOATNUMBER : DOUBLENUMBER ('f' | 'F')?
;

QUOTEDSTRING :  '\'' (   (~('\'' | '\\' | '\n' | '\r'))
  | ('\\'
      ( ('n' | 't' | 'b' | 'r' | 'f' | '\\' | '\'') )
    )
  | ('\\u'
        ('0'..'9' | 'A'..'F' | 'a'..'f')
        ('0'..'9' | 'A'..'F' | 'a'..'f')
        ('0'..'9' | 'A'..'F' | 'a'..'f')
        ('0'..'9' | 'A'..'F' | 'a'..'f')
    ) )*
'\''
;

EXECCOMMAND : '`' (~('`'))* '`'
;
    
DOLLAR : '$'
;
            
WS  :  ( ' ' | '\r' | '\t' | '\u000C' | '\n' ) 
;
    
SL_COMMENT 
    : '--' (~('\r' | '\n'))*? 
    ;

ML_COMMENT 
    : '/*' .*? '*/' 
    ;

fragment STRFILTEROP : 'eq' | 'gt' | 'lt' | 'gte' | 'lte' | 'neq' | 'matches'
;
    
fragment NUMFILTEROP : '==' | '<' | '<=' | '>' | '>=' | '!='
;
    
FILTEROP : STRFILTEROP | NUMFILTEROP
;

COLON
    : ':'
    ;
    
SEMI_COLON 
    : ';'
    ;
    
LEFT_PAREN 
    : '('
    ;
    
RIGHT_PAREN 
    : ')'
    ;

LEFT_CURLYP 
    : '{'
    ;

RIGHT_CURLYP 
    : '}'
    ;

LEFT_BRACKET : '['
;
    
RIGHT_BRACKET : ']'
;

POUND : '#'
;

EQUAL : '='
;

COMMA : ','
;

PERIOD : '.'
;

DIV : '/'
;

PERCENT : '%'
;

PLUS : '+'
;

MINUS : '-'
;

QMARK : '?'
;