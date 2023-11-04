lexer grammar ExpressionLexer;

options { caseInsensitive = true; }

//SPACE:              [ \t\r\n]+    -> skip;
SPACE:               [ ]+ -> skip;
//SQUARE_BRACKET_ID:  '[' (~']' | ']' ']')* ']';
//CURLY_BRACKET_ID:   '{' (~'}' | '}' '}')* '}';
DECIMAL:             DEC_DIGIT+;
VARIABLE:            LETTER;
//FLOAT:               DEC_DOT_DEC;
//REAL:                (DECIMAL | DEC_DOT_DEC) ('E' [+-]? DEC_DIGIT+);
OPERATOR:            STAR | DIVIDE | PLUS | MINUS;

EQUAL:               '=';

//LR_BRACKET:          '(';
//RR_BRACKET:          ')';
LR_BRACKET:          [([{];
RR_BRACKET:          [)\]}];
COMMA:               ',';
STAR:                '*';
DIVIDE:              '/';
PLUS:                '+';
MINUS:               '-';
POWER:               '^';

fragment LETTER:       [A-Z];
//fragment DEC_DOT_DEC:  (DEC_DIGIT+ '.' DEC_DIGIT+ |  DEC_DIGIT+ '.' | '.' DEC_DIGIT+);
fragment DEC_DIGIT:    [0-9];
