parser grammar TestParser;

options { tokenVocab=ExpressionLexer; }

file
    : line+ EOF
    ;

line
    : equation NEWLINE?
    ;

equation
    : left_equation right_equation
    ;

right_equation
    : polynomial+ (NEWLINE? | EOF)
    | monomial+ (NEWLINE? | EOF)
    | nested_polynomial+ (NEWLINE? | EOF)
    ;

left_equation
    : monomial+ EQUAL
    | polynomial+ EQUAL
    | nested_polynomial+ EQUAL
    ;

nested_polynomial
    : (OPERATOR? LR_BRACKET polynomial+ RR_BRACKET)+ (POWER exponent)?
    | (OPERATOR? polynomial+)+
    ;

polynomial
    : OPERATOR? LR_BRACKET monomial+ RR_BRACKET (POWER exponent)?
    | LR_BRACKET monomial+ RR_BRACKET (POWER exponent)?
    | monomial+
    ;

monomial
    : OPERATOR? (incognita | known_value) (POWER exponent)?
    ;

exponent
    : incognita
    | known_value
    ;

known_value
    : DECIMAL
    ;

incognita
    : DECIMAL VARIABLE+ | VARIABLE+
    ;
