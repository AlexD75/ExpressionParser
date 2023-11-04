parser grammar ExpressionParser;

options { tokenVocab=ExpressionLexer; }

equation
    : left_equation right_equation
    ;

right_equation
    : nested_polynomial+ EOF
    ;

left_equation
    : nested_polynomial+ EQUAL
    ;

nested_polynomial
    : (OPERATOR? LR_BRACKET polynomial+ RR_BRACKET)+ (POWER known_value)?
    | (OPERATOR? polynomial+)+
    ;

polynomial
    : OPERATOR? LR_BRACKET monomial+ RR_BRACKET (POWER known_value)?
    | LR_BRACKET monomial+ RR_BRACKET (POWER known_value)?
    | monomial+
    ;

monomial
    : OPERATOR (incognita | known_value) (POWER known_value)?
    | (incognita | known_value) (POWER known_value)?
    ;

known_value
    : DECIMAL+
    ;

incognita
    : DECIMAL+ VARIABLE | VARIABLE
    ;
