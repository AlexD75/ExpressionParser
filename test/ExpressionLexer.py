# Generated from C:/Users/aledi/source/ExpressionParser/ExpressionLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,14,84,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,2,14,7,14,2,15,7,15,1,0,4,0,35,8,0,11,0,12,0,36,1,0,1,0,1,1,
        4,1,42,8,1,11,1,12,1,43,1,2,1,2,1,3,1,3,1,3,1,3,3,3,52,8,3,1,4,1,
        4,1,5,1,5,1,6,1,6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,
        12,1,12,1,13,3,13,73,8,13,1,13,1,13,4,13,77,8,13,11,13,12,13,78,
        1,14,1,14,1,15,1,15,0,0,16,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,
        9,19,10,21,11,23,12,25,13,27,14,29,0,31,0,1,0,5,1,0,32,32,3,0,40,
        40,91,91,123,123,3,0,41,41,93,93,125,125,2,0,65,90,97,122,1,0,48,
        57,89,0,1,1,0,0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,
        0,0,11,1,0,0,0,0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,
        0,0,21,1,0,0,0,0,23,1,0,0,0,0,25,1,0,0,0,0,27,1,0,0,0,1,34,1,0,0,
        0,3,41,1,0,0,0,5,45,1,0,0,0,7,51,1,0,0,0,9,53,1,0,0,0,11,55,1,0,
        0,0,13,57,1,0,0,0,15,59,1,0,0,0,17,61,1,0,0,0,19,63,1,0,0,0,21,65,
        1,0,0,0,23,67,1,0,0,0,25,69,1,0,0,0,27,76,1,0,0,0,29,80,1,0,0,0,
        31,82,1,0,0,0,33,35,7,0,0,0,34,33,1,0,0,0,35,36,1,0,0,0,36,34,1,
        0,0,0,36,37,1,0,0,0,37,38,1,0,0,0,38,39,6,0,0,0,39,2,1,0,0,0,40,
        42,3,31,15,0,41,40,1,0,0,0,42,43,1,0,0,0,43,41,1,0,0,0,43,44,1,0,
        0,0,44,4,1,0,0,0,45,46,3,29,14,0,46,6,1,0,0,0,47,52,3,17,8,0,48,
        52,3,19,9,0,49,52,3,21,10,0,50,52,3,23,11,0,51,47,1,0,0,0,51,48,
        1,0,0,0,51,49,1,0,0,0,51,50,1,0,0,0,52,8,1,0,0,0,53,54,5,61,0,0,
        54,10,1,0,0,0,55,56,7,1,0,0,56,12,1,0,0,0,57,58,7,2,0,0,58,14,1,
        0,0,0,59,60,5,44,0,0,60,16,1,0,0,0,61,62,5,42,0,0,62,18,1,0,0,0,
        63,64,5,47,0,0,64,20,1,0,0,0,65,66,5,43,0,0,66,22,1,0,0,0,67,68,
        5,45,0,0,68,24,1,0,0,0,69,70,5,94,0,0,70,26,1,0,0,0,71,73,5,13,0,
        0,72,71,1,0,0,0,72,73,1,0,0,0,73,74,1,0,0,0,74,77,5,10,0,0,75,77,
        5,13,0,0,76,72,1,0,0,0,76,75,1,0,0,0,77,78,1,0,0,0,78,76,1,0,0,0,
        78,79,1,0,0,0,79,28,1,0,0,0,80,81,7,3,0,0,81,30,1,0,0,0,82,83,7,
        4,0,0,83,32,1,0,0,0,7,0,36,43,51,72,76,78,1,6,0,0
    ]

class ExpressionLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SPACE = 1
    DECIMAL = 2
    VARIABLE = 3
    OPERATOR = 4
    EQUAL = 5
    LR_BRACKET = 6
    RR_BRACKET = 7
    COMMA = 8
    STAR = 9
    DIVIDE = 10
    PLUS = 11
    MINUS = 12
    POWER = 13
    NEWLINE = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "','", "'*'", "'/'", "'+'", "'-'", "'^'" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET", 
            "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS", "POWER", 
            "NEWLINE" ]

    ruleNames = [ "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET", 
                  "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS", 
                  "POWER", "NEWLINE", "LETTER", "DEC_DIGIT" ]

    grammarFileName = "ExpressionLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


