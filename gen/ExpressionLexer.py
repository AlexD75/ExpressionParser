# Generated from C:/Users/aledi/source/ExpressionParser/ExpressionLexer.g4 by ANTLR 4.13.1
import sys

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 0, 12, 69, 6, -1, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2,
        6, 7, 6, 2, 7, 7, 7, 2, 8, 7, 8, 2, 9, 7, 9, 2, 10, 7, 10, 2, 11, 7, 11, 2, 12, 7, 12, 2, 13,
        7, 13, 1, 0, 4, 0, 31, 8, 0, 11, 0, 12, 0, 32, 1, 0, 1, 0, 1, 1, 4, 1, 38, 8, 1, 11, 1, 12,
        1, 39, 1, 2, 1, 2, 1, 3, 1, 3, 1, 3, 1, 3, 3, 3, 48, 8, 3, 1, 4, 1, 4, 1, 5, 1, 5, 1, 6, 1, 6,
        1, 7, 1, 7, 1, 8, 1, 8, 1, 9, 1, 9, 1, 10, 1, 10, 1, 11, 1, 11, 1, 12, 1, 12, 1, 13, 1, 13,
        0, 0, 14, 1, 1, 3, 2, 5, 3, 7, 4, 9, 5, 11, 6, 13, 7, 15, 8, 17, 9, 19, 10, 21, 11, 23, 12,
        25, 0, 27, 0, 1, 0, 3, 1, 0, 32, 32, 2, 0, 65, 90, 97, 122, 1, 0, 48, 57, 71, 0, 1, 1, 0,
        0, 0, 0, 3, 1, 0, 0, 0, 0, 5, 1, 0, 0, 0, 0, 7, 1, 0, 0, 0, 0, 9, 1, 0, 0, 0, 0, 11, 1, 0, 0, 0,
        0, 13, 1, 0, 0, 0, 0, 15, 1, 0, 0, 0, 0, 17, 1, 0, 0, 0, 0, 19, 1, 0, 0, 0, 0, 21, 1, 0, 0, 0,
        0, 23, 1, 0, 0, 0, 1, 30, 1, 0, 0, 0, 3, 37, 1, 0, 0, 0, 5, 41, 1, 0, 0, 0, 7, 47, 1, 0, 0, 0,
        9, 49, 1, 0, 0, 0, 11, 51, 1, 0, 0, 0, 13, 53, 1, 0, 0, 0, 15, 55, 1, 0, 0, 0, 17, 57, 1, 0,
        0, 0, 19, 59, 1, 0, 0, 0, 21, 61, 1, 0, 0, 0, 23, 63, 1, 0, 0, 0, 25, 65, 1, 0, 0, 0, 27, 67,
        1, 0, 0, 0, 29, 31, 7, 0, 0, 0, 30, 29, 1, 0, 0, 0, 31, 32, 1, 0, 0, 0, 32, 30, 1, 0, 0, 0,
        32, 33, 1, 0, 0, 0, 33, 34, 1, 0, 0, 0, 34, 35, 6, 0, 0, 0, 35, 2, 1, 0, 0, 0, 36, 38, 3, 27,
        13, 0, 37, 36, 1, 0, 0, 0, 38, 39, 1, 0, 0, 0, 39, 37, 1, 0, 0, 0, 39, 40, 1, 0, 0, 0, 40,
        4, 1, 0, 0, 0, 41, 42, 3, 25, 12, 0, 42, 6, 1, 0, 0, 0, 43, 48, 3, 17, 8, 0, 44, 48, 3, 19,
        9, 0, 45, 48, 3, 21, 10, 0, 46, 48, 3, 23, 11, 0, 47, 43, 1, 0, 0, 0, 47, 44, 1, 0, 0, 0,
        47, 45, 1, 0, 0, 0, 47, 46, 1, 0, 0, 0, 48, 8, 1, 0, 0, 0, 49, 50, 5, 61, 0, 0, 50, 10, 1,
        0, 0, 0, 51, 52, 5, 40, 0, 0, 52, 12, 1, 0, 0, 0, 53, 54, 5, 41, 0, 0, 54, 14, 1, 0, 0, 0,
        55, 56, 5, 44, 0, 0, 56, 16, 1, 0, 0, 0, 57, 58, 5, 42, 0, 0, 58, 18, 1, 0, 0, 0, 59, 60,
        5, 47, 0, 0, 60, 20, 1, 0, 0, 0, 61, 62, 5, 43, 0, 0, 62, 22, 1, 0, 0, 0, 63, 64, 5, 45, 0,
        0, 64, 24, 1, 0, 0, 0, 65, 66, 7, 1, 0, 0, 66, 26, 1, 0, 0, 0, 67, 68, 7, 2, 0, 0, 68, 28,
        1, 0, 0, 0, 4, 0, 32, 39, 47, 1, 6, 0, 0
    ]


class ExpressionLexer(Lexer):
    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

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

    channelNames = [u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN"]

    modeNames = ["DEFAULT_MODE"]

    literalNames = ["<INVALID>",
                    "'='", "'('", "')'", "','", "'*'", "'/'", "'+'", "'-'"]

    symbolicNames = ["<INVALID>",
                     "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET",
                     "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS"]

    ruleNames = ["SPACE", "DECIMAL", "VARIABLE", "OPERATOR", "EQUAL", "LR_BRACKET",
                 "RR_BRACKET", "COMMA", "STAR", "DIVIDE", "PLUS", "MINUS",
                 "LETTER", "DEC_DIGIT"]

    grammarFileName = "ExpressionLexer.g4"

    def __init__(self, input=None, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None
