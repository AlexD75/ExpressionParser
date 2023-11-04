parser grammar ExpressionParser;

options { tokenVocab=ExpressionLexer; }

equation
    : left_equation right_equation
    ;

right_equation
    : SPACE? large_expression+ EOF
    ;

left_equation
    : large_expression+ EQUAL
    ;

large_expression
    : (LR_BRACKET polynomial+ RR_BRACKET SPACE? OPERATOR? SPACE?)+
    | (polynomial+ SPACE? OPERATOR? SPACE?)+
    | element+ SPACE?
    ;

polynomial
    : LR_BRACKET element+ RR_BRACKET
    | LR_BRACKET element+ RR_BRACKET SPACE? OPERATOR? SPACE?
    | element+
    ;

element
    : monomial OPERATOR SPACE?
    | monomial
    ;

monomial
    : (incognita | known_value) SPACE?
    ;

known_value
    : DECIMAL+
    ;

incognita
    : DECIMAL+ VARIABLE | VARIABLE
    ;
