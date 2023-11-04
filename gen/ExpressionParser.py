# Generated from C:/Users/aledi/source/ExpressionParser/ExpressionParser.g4 by ANTLR 4.13.1
# encoding: utf-8
import sys

from antlr4 import *

if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4, 1, 12, 114, 2, 0, 7, 0, 2, 1, 7, 1, 2, 2, 7, 2, 2, 3, 7, 3, 2, 4, 7, 4, 2, 5, 7, 5, 2, 6, 7,
        6, 2, 7, 7, 7, 1, 0, 1, 0, 1, 0, 1, 1, 4, 1, 21, 8, 1, 11, 1, 12, 1, 22, 1, 1, 1, 1, 1, 2, 4,
        2, 28, 8, 2, 11, 2, 12, 2, 29, 1, 2, 1, 2, 1, 3, 3, 3, 35, 8, 3, 1, 3, 1, 3, 4, 3, 39, 8, 3,
        11, 3, 12, 3, 40, 1, 3, 1, 3, 4, 3, 45, 8, 3, 11, 3, 12, 3, 46, 1, 3, 3, 3, 50, 8, 3, 1, 3,
        4, 3, 53, 8, 3, 11, 3, 12, 3, 54, 4, 3, 57, 8, 3, 11, 3, 12, 3, 58, 3, 3, 61, 8, 3, 1, 4, 3,
        4, 64, 8, 4, 1, 4, 1, 4, 4, 4, 68, 8, 4, 11, 4, 12, 4, 69, 1, 4, 1, 4, 1, 4, 1, 4, 4, 4, 76,
        8, 4, 11, 4, 12, 4, 77, 1, 4, 1, 4, 1, 4, 4, 4, 83, 8, 4, 11, 4, 12, 4, 84, 3, 4, 87, 8, 4,
        1, 5, 1, 5, 1, 5, 3, 5, 92, 8, 5, 1, 5, 1, 5, 3, 5, 96, 8, 5, 3, 5, 98, 8, 5, 1, 6, 4, 6, 101,
        8, 6, 11, 6, 12, 6, 102, 1, 7, 4, 7, 106, 8, 7, 11, 7, 12, 7, 107, 1, 7, 1, 7, 3, 7, 112,
        8, 7, 1, 7, 0, 0, 8, 0, 2, 4, 6, 8, 10, 12, 14, 0, 0, 126, 0, 16, 1, 0, 0, 0, 2, 20, 1, 0, 0,
        0, 4, 27, 1, 0, 0, 0, 6, 60, 1, 0, 0, 0, 8, 86, 1, 0, 0, 0, 10, 97, 1, 0, 0, 0, 12, 100, 1,
        0, 0, 0, 14, 111, 1, 0, 0, 0, 16, 17, 3, 4, 2, 0, 17, 18, 3, 2, 1, 0, 18, 1, 1, 0, 0, 0, 19,
        21, 3, 6, 3, 0, 20, 19, 1, 0, 0, 0, 21, 22, 1, 0, 0, 0, 22, 20, 1, 0, 0, 0, 22, 23, 1, 0, 0,
        0, 23, 24, 1, 0, 0, 0, 24, 25, 5, 0, 0, 1, 25, 3, 1, 0, 0, 0, 26, 28, 3, 6, 3, 0, 27, 26, 1,
        0, 0, 0, 28, 29, 1, 0, 0, 0, 29, 27, 1, 0, 0, 0, 29, 30, 1, 0, 0, 0, 30, 31, 1, 0, 0, 0, 31,
        32, 5, 5, 0, 0, 32, 5, 1, 0, 0, 0, 33, 35, 5, 4, 0, 0, 34, 33, 1, 0, 0, 0, 34, 35, 1, 0, 0,
        0, 35, 36, 1, 0, 0, 0, 36, 38, 5, 6, 0, 0, 37, 39, 3, 8, 4, 0, 38, 37, 1, 0, 0, 0, 39, 40,
        1, 0, 0, 0, 40, 38, 1, 0, 0, 0, 40, 41, 1, 0, 0, 0, 41, 42, 1, 0, 0, 0, 42, 43, 5, 7, 0, 0,
        43, 45, 1, 0, 0, 0, 44, 34, 1, 0, 0, 0, 45, 46, 1, 0, 0, 0, 46, 44, 1, 0, 0, 0, 46, 47, 1,
        0, 0, 0, 47, 61, 1, 0, 0, 0, 48, 50, 5, 4, 0, 0, 49, 48, 1, 0, 0, 0, 49, 50, 1, 0, 0, 0, 50,
        52, 1, 0, 0, 0, 51, 53, 3, 8, 4, 0, 52, 51, 1, 0, 0, 0, 53, 54, 1, 0, 0, 0, 54, 52, 1, 0, 0,
        0, 54, 55, 1, 0, 0, 0, 55, 57, 1, 0, 0, 0, 56, 49, 1, 0, 0, 0, 57, 58, 1, 0, 0, 0, 58, 56,
        1, 0, 0, 0, 58, 59, 1, 0, 0, 0, 59, 61, 1, 0, 0, 0, 60, 44, 1, 0, 0, 0, 60, 56, 1, 0, 0, 0,
        61, 7, 1, 0, 0, 0, 62, 64, 5, 4, 0, 0, 63, 62, 1, 0, 0, 0, 63, 64, 1, 0, 0, 0, 64, 65, 1, 0,
        0, 0, 65, 67, 5, 6, 0, 0, 66, 68, 3, 10, 5, 0, 67, 66, 1, 0, 0, 0, 68, 69, 1, 0, 0, 0, 69,
        67, 1, 0, 0, 0, 69, 70, 1, 0, 0, 0, 70, 71, 1, 0, 0, 0, 71, 72, 5, 7, 0, 0, 72, 87, 1, 0, 0,
        0, 73, 75, 5, 6, 0, 0, 74, 76, 3, 10, 5, 0, 75, 74, 1, 0, 0, 0, 76, 77, 1, 0, 0, 0, 77, 75,
        1, 0, 0, 0, 77, 78, 1, 0, 0, 0, 78, 79, 1, 0, 0, 0, 79, 80, 5, 7, 0, 0, 80, 87, 1, 0, 0, 0,
        81, 83, 3, 10, 5, 0, 82, 81, 1, 0, 0, 0, 83, 84, 1, 0, 0, 0, 84, 82, 1, 0, 0, 0, 84, 85, 1,
        0, 0, 0, 85, 87, 1, 0, 0, 0, 86, 63, 1, 0, 0, 0, 86, 73, 1, 0, 0, 0, 86, 82, 1, 0, 0, 0, 87,
        9, 1, 0, 0, 0, 88, 91, 5, 4, 0, 0, 89, 92, 3, 14, 7, 0, 90, 92, 3, 12, 6, 0, 91, 89, 1, 0,
        0, 0, 91, 90, 1, 0, 0, 0, 92, 98, 1, 0, 0, 0, 93, 96, 3, 14, 7, 0, 94, 96, 3, 12, 6, 0, 95,
        93, 1, 0, 0, 0, 95, 94, 1, 0, 0, 0, 96, 98, 1, 0, 0, 0, 97, 88, 1, 0, 0, 0, 97, 95, 1, 0, 0,
        0, 98, 11, 1, 0, 0, 0, 99, 101, 5, 2, 0, 0, 100, 99, 1, 0, 0, 0, 101, 102, 1, 0, 0, 0, 102,
        100, 1, 0, 0, 0, 102, 103, 1, 0, 0, 0, 103, 13, 1, 0, 0, 0, 104, 106, 5, 2, 0, 0, 105, 104,
        1, 0, 0, 0, 106, 107, 1, 0, 0, 0, 107, 105, 1, 0, 0, 0, 107, 108, 1, 0, 0, 0, 108, 109,
        1, 0, 0, 0, 109, 112, 5, 3, 0, 0, 110, 112, 5, 3, 0, 0, 111, 105, 1, 0, 0, 0, 111, 110,
        1, 0, 0, 0, 112, 15, 1, 0, 0, 0, 20, 22, 29, 34, 40, 46, 49, 54, 58, 60, 63, 69, 77, 84,
        86, 91, 95, 97, 102, 107, 111
    ]


class ExpressionParser(Parser):
    grammarFileName = "ExpressionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [DFA(ds, i) for i, ds in enumerate(atn.decisionToState)]

    sharedContextCache = PredictionContextCache()

    literalNames = ["<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>",
                    "<INVALID>", "'='", "'('", "')'", "','", "'*'", "'/'",
                    "'+'", "'-'"]

    symbolicNames = ["<INVALID>", "SPACE", "DECIMAL", "VARIABLE", "OPERATOR",
                     "EQUAL", "LR_BRACKET", "RR_BRACKET", "COMMA", "STAR",
                     "DIVIDE", "PLUS", "MINUS"]

    RULE_equation = 0
    RULE_right_equation = 1
    RULE_left_equation = 2
    RULE_nested_polynomial = 3
    RULE_polynomial = 4
    RULE_monomial = 5
    RULE_known_value = 6
    RULE_incognita = 7

    ruleNames = ["equation", "right_equation", "left_equation", "nested_polynomial",
                 "polynomial", "monomial", "known_value", "incognita"]

    EOF = Token.EOF
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

    def __init__(self, input: TokenStream, output: TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None

    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_equation(self):
            return self.getTypedRuleContext(ExpressionParser.Left_equationContext, 0)

        def right_equation(self):
            return self.getTypedRuleContext(ExpressionParser.Right_equationContext, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_equation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterEquation"):
                listener.enterEquation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitEquation"):
                listener.exitEquation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitEquation"):
                return visitor.visitEquation(self)
            else:
                return visitor.visitChildren(self)

    def equation(self):

        localctx = ExpressionParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.left_equation()
            self.state = 17
            self.right_equation()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Right_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExpressionParser.EOF, 0)

        def nested_polynomial(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.Nested_polynomialContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.Nested_polynomialContext, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_right_equation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterRight_equation"):
                listener.enterRight_equation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitRight_equation"):
                listener.exitRight_equation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitRight_equation"):
                return visitor.visitRight_equation(self)
            else:
                return visitor.visitChildren(self)

    def right_equation(self):

        localctx = ExpressionParser.Right_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_right_equation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 20
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 19
                self.nested_polynomial()
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 92) != 0)):
                    break

            self.state = 24
            self.match(ExpressionParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Left_equationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ExpressionParser.EQUAL, 0)

        def nested_polynomial(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.Nested_polynomialContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.Nested_polynomialContext, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_left_equation

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterLeft_equation"):
                listener.enterLeft_equation(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitLeft_equation"):
                listener.exitLeft_equation(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitLeft_equation"):
                return visitor.visitLeft_equation(self)
            else:
                return visitor.visitChildren(self)

    def left_equation(self):

        localctx = ExpressionParser.Left_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_left_equation)
        self._la = 0  # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.nested_polynomial()
                self.state = 29
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 92) != 0)):
                    break

            self.state = 31
            self.match(ExpressionParser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Nested_polynomialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self, i: int = None):
            if i is None:
                return self.getTokens(ExpressionParser.LR_BRACKET)
            else:
                return self.getToken(ExpressionParser.LR_BRACKET, i)

        def RR_BRACKET(self, i: int = None):
            if i is None:
                return self.getTokens(ExpressionParser.RR_BRACKET)
            else:
                return self.getToken(ExpressionParser.RR_BRACKET, i)

        def OPERATOR(self, i: int = None):
            if i is None:
                return self.getTokens(ExpressionParser.OPERATOR)
            else:
                return self.getToken(ExpressionParser.OPERATOR, i)

        def polynomial(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.PolynomialContext, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_nested_polynomial

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterNested_polynomial"):
                listener.enterNested_polynomial(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitNested_polynomial"):
                listener.exitNested_polynomial(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitNested_polynomial"):
                return visitor.visitNested_polynomial(self)
            else:
                return visitor.visitChildren(self)

    def nested_polynomial(self):

        localctx = ExpressionParser.Nested_polynomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_nested_polynomial)
        self._la = 0  # Token type
        try:
            self.state = 60
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 8, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 44
                self._errHandler.sync(self)
                _alt = 1
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 34
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la == 4:
                            self.state = 33
                            self.match(ExpressionParser.OPERATOR)

                        self.state = 36
                        self.match(ExpressionParser.LR_BRACKET)
                        self.state = 38
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 37
                            self.polynomial()
                            self.state = 40
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 92) != 0)):
                                break

                        self.state = 42
                        self.match(ExpressionParser.RR_BRACKET)

                    else:
                        raise NoViableAltException(self)
                    self.state = 46
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 4, self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 56
                self._errHandler.sync(self)
                _alt = 1
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 49
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input, 5, self._ctx)
                        if la_ == 1:
                            self.state = 48
                            self.match(ExpressionParser.OPERATOR)

                        self.state = 52
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 51
                                self.polynomial()

                            else:
                                raise NoViableAltException(self)
                            self.state = 54
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input, 6, self._ctx)


                    else:
                        raise NoViableAltException(self)
                    self.state = 58
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 7, self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class PolynomialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self):
            return self.getToken(ExpressionParser.LR_BRACKET, 0)

        def RR_BRACKET(self):
            return self.getToken(ExpressionParser.RR_BRACKET, 0)

        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def monomial(self, i: int = None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.MonomialContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.MonomialContext, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_polynomial

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterPolynomial"):
                listener.enterPolynomial(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitPolynomial"):
                listener.exitPolynomial(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitPolynomial"):
                return visitor.visitPolynomial(self)
            else:
                return visitor.visitChildren(self)

    def polynomial(self):

        localctx = ExpressionParser.PolynomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_polynomial)
        self._la = 0  # Token type
        try:
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input, 13, self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la == 4:
                    self.state = 62
                    self.match(ExpressionParser.OPERATOR)

                self.state = 65
                self.match(ExpressionParser.LR_BRACKET)
                self.state = 67
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 66
                    self.monomial()
                    self.state = 69
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 71
                self.match(ExpressionParser.RR_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 73
                self.match(ExpressionParser.LR_BRACKET)
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 74
                    self.monomial()
                    self.state = 77
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 79
                self.match(ExpressionParser.RR_BRACKET)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 82
                self._errHandler.sync(self)
                _alt = 1
                while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 81
                        self.monomial()

                    else:
                        raise NoViableAltException(self)
                    self.state = 84
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input, 12, self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class MonomialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def incognita(self):
            return self.getTypedRuleContext(ExpressionParser.IncognitaContext, 0)

        def known_value(self):
            return self.getTypedRuleContext(ExpressionParser.Known_valueContext, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_monomial

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterMonomial"):
                listener.enterMonomial(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitMonomial"):
                listener.exitMonomial(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitMonomial"):
                return visitor.visitMonomial(self)
            else:
                return visitor.visitChildren(self)

    def monomial(self):

        localctx = ExpressionParser.MonomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_monomial)
        try:
            self.state = 97
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 88
                self.match(ExpressionParser.OPERATOR)
                self.state = 91
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 14, self._ctx)
                if la_ == 1:
                    self.state = 89
                    self.incognita()
                    pass

                elif la_ == 2:
                    self.state = 90
                    self.known_value()
                    pass

                pass
            elif token in [2, 3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 95
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input, 15, self._ctx)
                if la_ == 1:
                    self.state = 93
                    self.incognita()
                    pass

                elif la_ == 2:
                    self.state = 94
                    self.known_value()
                    pass

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Known_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self, i: int = None):
            if i is None:
                return self.getTokens(ExpressionParser.DECIMAL)
            else:
                return self.getToken(ExpressionParser.DECIMAL, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_known_value

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterKnown_value"):
                listener.enterKnown_value(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitKnown_value"):
                listener.exitKnown_value(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitKnown_value"):
                return visitor.visitKnown_value(self)
            else:
                return visitor.visitChildren(self)

    def known_value(self):

        localctx = ExpressionParser.Known_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_known_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self._errHandler.sync(self)
            _alt = 1
            while _alt != 2 and _alt != ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 99
                    self.match(ExpressionParser.DECIMAL)

                else:
                    raise NoViableAltException(self)
                self.state = 102
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input, 17, self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class IncognitaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent: ParserRuleContext = None, invokingState: int = -1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExpressionParser.VARIABLE, 0)

        def DECIMAL(self, i: int = None):
            if i is None:
                return self.getTokens(ExpressionParser.DECIMAL)
            else:
                return self.getToken(ExpressionParser.DECIMAL, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_incognita

        def enterRule(self, listener: ParseTreeListener):
            if hasattr(listener, "enterIncognita"):
                listener.enterIncognita(self)

        def exitRule(self, listener: ParseTreeListener):
            if hasattr(listener, "exitIncognita"):
                listener.exitIncognita(self)

        def accept(self, visitor: ParseTreeVisitor):
            if hasattr(visitor, "visitIncognita"):
                return visitor.visitIncognita(self)
            else:
                return visitor.visitChildren(self)

    def incognita(self):

        localctx = ExpressionParser.IncognitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_incognita)
        self._la = 0  # Token type
        try:
            self.state = 111
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 105
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 104
                    self.match(ExpressionParser.DECIMAL)
                    self.state = 107
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la == 2):
                        break

                self.state = 109
                self.match(ExpressionParser.VARIABLE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 110
                self.match(ExpressionParser.VARIABLE)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx
