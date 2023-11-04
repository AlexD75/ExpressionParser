# Generated from C:/Users/aledi/source/TlTSqlParser/ExpressionLexer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,12,70,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,
        7,13,1,0,5,0,31,8,0,10,0,12,0,34,9,0,1,0,1,0,1,1,4,1,39,8,1,11,1,
        12,1,40,1,2,1,2,1,3,1,3,1,3,1,3,3,3,49,8,3,1,4,1,4,1,5,1,5,1,6,1,
        6,1,7,1,7,1,8,1,8,1,9,1,9,1,10,1,10,1,11,1,11,1,12,1,12,1,13,1,13,
        0,0,14,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,8,17,9,19,10,21,11,23,12,
        25,0,27,0,1,0,3,1,0,32,32,2,0,65,90,97,122,1,0,48,57,72,0,1,1,0,
        0,0,0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,
        0,13,1,0,0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,0,21,1,0,0,0,
        0,23,1,0,0,0,1,32,1,0,0,0,3,38,1,0,0,0,5,42,1,0,0,0,7,48,1,0,0,0,
        9,50,1,0,0,0,11,52,1,0,0,0,13,54,1,0,0,0,15,56,1,0,0,0,17,58,1,0,
        0,0,19,60,1,0,0,0,21,62,1,0,0,0,23,64,1,0,0,0,25,66,1,0,0,0,27,68,
        1,0,0,0,29,31,7,0,0,0,30,29,1,0,0,0,31,34,1,0,0,0,32,30,1,0,0,0,
        32,33,1,0,0,0,33,35,1,0,0,0,34,32,1,0,0,0,35,36,6,0,0,0,36,2,1,0,
        0,0,37,39,3,27,13,0,38,37,1,0,0,0,39,40,1,0,0,0,40,38,1,0,0,0,40,
        41,1,0,0,0,41,4,1,0,0,0,42,43,3,25,12,0,43,6,1,0,0,0,44,49,3,17,
        8,0,45,49,3,19,9,0,46,49,3,21,10,0,47,49,3,23,11,0,48,44,1,0,0,0,
        48,45,1,0,0,0,48,46,1,0,0,0,48,47,1,0,0,0,49,8,1,0,0,0,50,51,5,61,
        0,0,51,10,1,0,0,0,52,53,5,40,0,0,53,12,1,0,0,0,54,55,5,41,0,0,55,
        14,1,0,0,0,56,57,5,44,0,0,57,16,1,0,0,0,58,59,5,42,0,0,59,18,1,0,
        0,0,60,61,5,47,0,0,61,20,1,0,0,0,62,63,5,43,0,0,63,22,1,0,0,0,64,
        65,5,45,0,0,65,24,1,0,0,0,66,67,7,1,0,0,67,26,1,0,0,0,68,69,7,2,
        0,0,69,28,1,0,0,0,4,0,32,40,48,1,6,0,0
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

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'('", "')'", "','", "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>",
            "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET", 
            "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS" ]

    ruleNames = [ "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET", 
                  "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS", 
                  "LETTER", "DEC_DIGIT" ]

    grammarFileName = "ExpressionLexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


