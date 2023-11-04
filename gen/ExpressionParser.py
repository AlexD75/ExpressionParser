# Generated from C:/Users/aledi/source/TlTSqlParser/ExpressionParser.g4 by ANTLR 4.13.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,12,147,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,1,1,3,1,23,8,1,1,1,4,1,26,8,1,11,1,
        12,1,27,1,1,1,1,1,2,4,2,33,8,2,11,2,12,2,34,1,2,1,2,1,3,1,3,4,3,
        41,8,3,11,3,12,3,42,1,3,1,3,3,3,47,8,3,1,3,3,3,50,8,3,1,3,3,3,53,
        8,3,4,3,55,8,3,11,3,12,3,56,1,3,4,3,60,8,3,11,3,12,3,61,1,3,3,3,
        65,8,3,1,3,3,3,68,8,3,1,3,3,3,71,8,3,4,3,73,8,3,11,3,12,3,74,1,3,
        4,3,78,8,3,11,3,12,3,79,1,3,3,3,83,8,3,3,3,85,8,3,1,4,1,4,4,4,89,
        8,4,11,4,12,4,90,1,4,1,4,1,4,1,4,4,4,97,8,4,11,4,12,4,98,1,4,1,4,
        3,4,103,8,4,1,4,3,4,106,8,4,1,4,3,4,109,8,4,1,4,4,4,112,8,4,11,4,
        12,4,113,3,4,116,8,4,1,5,1,5,1,5,3,5,121,8,5,1,5,3,5,124,8,5,1,6,
        1,6,3,6,128,8,6,1,6,3,6,131,8,6,1,7,4,7,134,8,7,11,7,12,7,135,1,
        8,4,8,139,8,8,11,8,12,8,140,1,8,1,8,3,8,145,8,8,1,8,0,0,9,0,2,4,
        6,8,10,12,14,16,0,0,169,0,18,1,0,0,0,2,22,1,0,0,0,4,32,1,0,0,0,6,
        84,1,0,0,0,8,115,1,0,0,0,10,123,1,0,0,0,12,127,1,0,0,0,14,133,1,
        0,0,0,16,144,1,0,0,0,18,19,3,4,2,0,19,20,3,2,1,0,20,1,1,0,0,0,21,
        23,5,1,0,0,22,21,1,0,0,0,22,23,1,0,0,0,23,25,1,0,0,0,24,26,3,6,3,
        0,25,24,1,0,0,0,26,27,1,0,0,0,27,25,1,0,0,0,27,28,1,0,0,0,28,29,
        1,0,0,0,29,30,5,0,0,1,30,3,1,0,0,0,31,33,3,6,3,0,32,31,1,0,0,0,33,
        34,1,0,0,0,34,32,1,0,0,0,34,35,1,0,0,0,35,36,1,0,0,0,36,37,5,5,0,
        0,37,5,1,0,0,0,38,40,5,6,0,0,39,41,3,8,4,0,40,39,1,0,0,0,41,42,1,
        0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,46,5,7,0,0,45,
        47,5,1,0,0,46,45,1,0,0,0,46,47,1,0,0,0,47,49,1,0,0,0,48,50,5,4,0,
        0,49,48,1,0,0,0,49,50,1,0,0,0,50,52,1,0,0,0,51,53,5,1,0,0,52,51,
        1,0,0,0,52,53,1,0,0,0,53,55,1,0,0,0,54,38,1,0,0,0,55,56,1,0,0,0,
        56,54,1,0,0,0,56,57,1,0,0,0,57,85,1,0,0,0,58,60,3,8,4,0,59,58,1,
        0,0,0,60,61,1,0,0,0,61,59,1,0,0,0,61,62,1,0,0,0,62,64,1,0,0,0,63,
        65,5,1,0,0,64,63,1,0,0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,68,5,4,0,
        0,67,66,1,0,0,0,67,68,1,0,0,0,68,70,1,0,0,0,69,71,5,1,0,0,70,69,
        1,0,0,0,70,71,1,0,0,0,71,73,1,0,0,0,72,59,1,0,0,0,73,74,1,0,0,0,
        74,72,1,0,0,0,74,75,1,0,0,0,75,85,1,0,0,0,76,78,3,10,5,0,77,76,1,
        0,0,0,78,79,1,0,0,0,79,77,1,0,0,0,79,80,1,0,0,0,80,82,1,0,0,0,81,
        83,5,1,0,0,82,81,1,0,0,0,82,83,1,0,0,0,83,85,1,0,0,0,84,54,1,0,0,
        0,84,72,1,0,0,0,84,77,1,0,0,0,85,7,1,0,0,0,86,88,5,6,0,0,87,89,3,
        10,5,0,88,87,1,0,0,0,89,90,1,0,0,0,90,88,1,0,0,0,90,91,1,0,0,0,91,
        92,1,0,0,0,92,93,5,7,0,0,93,116,1,0,0,0,94,96,5,6,0,0,95,97,3,10,
        5,0,96,95,1,0,0,0,97,98,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,100,
        1,0,0,0,100,102,5,7,0,0,101,103,5,1,0,0,102,101,1,0,0,0,102,103,
        1,0,0,0,103,105,1,0,0,0,104,106,5,4,0,0,105,104,1,0,0,0,105,106,
        1,0,0,0,106,108,1,0,0,0,107,109,5,1,0,0,108,107,1,0,0,0,108,109,
        1,0,0,0,109,116,1,0,0,0,110,112,3,10,5,0,111,110,1,0,0,0,112,113,
        1,0,0,0,113,111,1,0,0,0,113,114,1,0,0,0,114,116,1,0,0,0,115,86,1,
        0,0,0,115,94,1,0,0,0,115,111,1,0,0,0,116,9,1,0,0,0,117,118,3,12,
        6,0,118,120,5,4,0,0,119,121,5,1,0,0,120,119,1,0,0,0,120,121,1,0,
        0,0,121,124,1,0,0,0,122,124,3,12,6,0,123,117,1,0,0,0,123,122,1,0,
        0,0,124,11,1,0,0,0,125,128,3,16,8,0,126,128,3,14,7,0,127,125,1,0,
        0,0,127,126,1,0,0,0,128,130,1,0,0,0,129,131,5,1,0,0,130,129,1,0,
        0,0,130,131,1,0,0,0,131,13,1,0,0,0,132,134,5,2,0,0,133,132,1,0,0,
        0,134,135,1,0,0,0,135,133,1,0,0,0,135,136,1,0,0,0,136,15,1,0,0,0,
        137,139,5,2,0,0,138,137,1,0,0,0,139,140,1,0,0,0,140,138,1,0,0,0,
        140,141,1,0,0,0,141,142,1,0,0,0,142,145,5,3,0,0,143,145,5,3,0,0,
        144,138,1,0,0,0,144,143,1,0,0,0,145,17,1,0,0,0,30,22,27,34,42,46,
        49,52,56,61,64,67,70,74,79,82,84,90,98,102,105,108,113,115,120,123,
        127,130,135,140,144
    ]

class ExpressionParser ( Parser ):

    grammarFileName = "ExpressionParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "'('", "')'", "','", "'*'", "'/'", 
                     "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", 
                      "EQUAL", "LR_BRACKET", "RR_BRACKET", "COMMA", "STAR", 
                      "DIVIDE", "PLUS", "MINUS" ]

    RULE_equation = 0
    RULE_right_equation = 1
    RULE_left_equation = 2
    RULE_large_expression = 3
    RULE_polynomial = 4
    RULE_element = 5
    RULE_monomial = 6
    RULE_known_value = 7
    RULE_incognita = 8

    ruleNames =  [ "equation", "right_equation", "left_equation", "large_expression", 
                   "polynomial", "element", "monomial", "known_value", "incognita" ]

    EOF = Token.EOF
    SPACE=1
    DECIMAL=2
    VARIABLE=3
    OPERATOR=4
    EQUAL=5
    LR_BRACKET=6
    RR_BRACKET=7
    COMMA=8
    STAR=9
    DIVIDE=10
    PLUS=11
    MINUS=12

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class EquationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def left_equation(self):
            return self.getTypedRuleContext(ExpressionParser.Left_equationContext,0)


        def right_equation(self):
            return self.getTypedRuleContext(ExpressionParser.Right_equationContext,0)


        def getRuleIndex(self):
            return ExpressionParser.RULE_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEquation" ):
                listener.enterEquation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEquation" ):
                listener.exitEquation(self)




    def equation(self):

        localctx = ExpressionParser.EquationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_equation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 18
            self.left_equation()
            self.state = 19
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(ExpressionParser.EOF, 0)

        def SPACE(self):
            return self.getToken(ExpressionParser.SPACE, 0)

        def large_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.Large_expressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.Large_expressionContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_right_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRight_equation" ):
                listener.enterRight_equation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRight_equation" ):
                listener.exitRight_equation(self)




    def right_equation(self):

        localctx = ExpressionParser.Right_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_right_equation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==1:
                self.state = 21
                self.match(ExpressionParser.SPACE)


            self.state = 25 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 24
                self.large_expression()
                self.state = 27 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 76) != 0)):
                    break

            self.state = 29
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EQUAL(self):
            return self.getToken(ExpressionParser.EQUAL, 0)

        def large_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.Large_expressionContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.Large_expressionContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_left_equation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLeft_equation" ):
                listener.enterLeft_equation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLeft_equation" ):
                listener.exitLeft_equation(self)




    def left_equation(self):

        localctx = ExpressionParser.Left_equationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_left_equation)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 31
                self.large_expression()
                self.state = 34 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 76) != 0)):
                    break

            self.state = 36
            self.match(ExpressionParser.EQUAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Large_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.LR_BRACKET)
            else:
                return self.getToken(ExpressionParser.LR_BRACKET, i)

        def RR_BRACKET(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.RR_BRACKET)
            else:
                return self.getToken(ExpressionParser.RR_BRACKET, i)

        def polynomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.PolynomialContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.PolynomialContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.SPACE)
            else:
                return self.getToken(ExpressionParser.SPACE, i)

        def OPERATOR(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.OPERATOR)
            else:
                return self.getToken(ExpressionParser.OPERATOR, i)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.ElementContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.ElementContext,i)


        def getRuleIndex(self):
            return ExpressionParser.RULE_large_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLarge_expression" ):
                listener.enterLarge_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLarge_expression" ):
                listener.exitLarge_expression(self)




    def large_expression(self):

        localctx = ExpressionParser.Large_expressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_large_expression)
        self._la = 0 # Token type
        try:
            self.state = 84
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 38
                        self.match(ExpressionParser.LR_BRACKET)
                        self.state = 40 
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        while True:
                            self.state = 39
                            self.polynomial()
                            self.state = 42 
                            self._errHandler.sync(self)
                            _la = self._input.LA(1)
                            if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 76) != 0)):
                                break

                        self.state = 44
                        self.match(ExpressionParser.RR_BRACKET)
                        self.state = 46
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                        if la_ == 1:
                            self.state = 45
                            self.match(ExpressionParser.SPACE)


                        self.state = 49
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==4:
                            self.state = 48
                            self.match(ExpressionParser.OPERATOR)


                        self.state = 52
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==1:
                            self.state = 51
                            self.match(ExpressionParser.SPACE)



                    else:
                        raise NoViableAltException(self)
                    self.state = 56 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 72 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 59 
                        self._errHandler.sync(self)
                        _alt = 1
                        while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                            if _alt == 1:
                                self.state = 58
                                self.polynomial()

                            else:
                                raise NoViableAltException(self)
                            self.state = 61 
                            self._errHandler.sync(self)
                            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

                        self.state = 64
                        self._errHandler.sync(self)
                        la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                        if la_ == 1:
                            self.state = 63
                            self.match(ExpressionParser.SPACE)


                        self.state = 67
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==4:
                            self.state = 66
                            self.match(ExpressionParser.OPERATOR)


                        self.state = 70
                        self._errHandler.sync(self)
                        _la = self._input.LA(1)
                        if _la==1:
                            self.state = 69
                            self.match(ExpressionParser.SPACE)



                    else:
                        raise NoViableAltException(self)
                    self.state = 74 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 77 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 76
                        self.element()

                    else:
                        raise NoViableAltException(self)
                    self.state = 79 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==1:
                    self.state = 81
                    self.match(ExpressionParser.SPACE)


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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self):
            return self.getToken(ExpressionParser.LR_BRACKET, 0)

        def RR_BRACKET(self):
            return self.getToken(ExpressionParser.RR_BRACKET, 0)

        def element(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(ExpressionParser.ElementContext)
            else:
                return self.getTypedRuleContext(ExpressionParser.ElementContext,i)


        def SPACE(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.SPACE)
            else:
                return self.getToken(ExpressionParser.SPACE, i)

        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_polynomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolynomial" ):
                listener.enterPolynomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolynomial" ):
                listener.exitPolynomial(self)




    def polynomial(self):

        localctx = ExpressionParser.PolynomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_polynomial)
        self._la = 0 # Token type
        try:
            self.state = 115
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 86
                self.match(ExpressionParser.LR_BRACKET)
                self.state = 88 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 87
                    self.element()
                    self.state = 90 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2 or _la==3):
                        break

                self.state = 92
                self.match(ExpressionParser.RR_BRACKET)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 94
                self.match(ExpressionParser.LR_BRACKET)
                self.state = 96 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 95
                    self.element()
                    self.state = 98 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2 or _la==3):
                        break

                self.state = 100
                self.match(ExpressionParser.RR_BRACKET)
                self.state = 102
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 101
                    self.match(ExpressionParser.SPACE)


                self.state = 105
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 104
                    self.match(ExpressionParser.OPERATOR)


                self.state = 108
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
                if la_ == 1:
                    self.state = 107
                    self.match(ExpressionParser.SPACE)


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 111 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 110
                        self.element()

                    else:
                        raise NoViableAltException(self)
                    self.state = 113 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,21,self._ctx)

                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def monomial(self):
            return self.getTypedRuleContext(ExpressionParser.MonomialContext,0)


        def OPERATOR(self):
            return self.getToken(ExpressionParser.OPERATOR, 0)

        def SPACE(self):
            return self.getToken(ExpressionParser.SPACE, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_element

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElement" ):
                listener.enterElement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElement" ):
                listener.exitElement(self)




    def element(self):

        localctx = ExpressionParser.ElementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_element)
        try:
            self.state = 123
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,24,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 117
                self.monomial()
                self.state = 118
                self.match(ExpressionParser.OPERATOR)
                self.state = 120
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,23,self._ctx)
                if la_ == 1:
                    self.state = 119
                    self.match(ExpressionParser.SPACE)


                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 122
                self.monomial()
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def incognita(self):
            return self.getTypedRuleContext(ExpressionParser.IncognitaContext,0)


        def known_value(self):
            return self.getTypedRuleContext(ExpressionParser.Known_valueContext,0)


        def SPACE(self):
            return self.getToken(ExpressionParser.SPACE, 0)

        def getRuleIndex(self):
            return ExpressionParser.RULE_monomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonomial" ):
                listener.enterMonomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonomial" ):
                listener.exitMonomial(self)




    def monomial(self):

        localctx = ExpressionParser.MonomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_monomial)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 127
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,25,self._ctx)
            if la_ == 1:
                self.state = 125
                self.incognita()
                pass

            elif la_ == 2:
                self.state = 126
                self.known_value()
                pass


            self.state = 130
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,26,self._ctx)
            if la_ == 1:
                self.state = 129
                self.match(ExpressionParser.SPACE)


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Known_valueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def DECIMAL(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.DECIMAL)
            else:
                return self.getToken(ExpressionParser.DECIMAL, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_known_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnown_value" ):
                listener.enterKnown_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnown_value" ):
                listener.exitKnown_value(self)




    def known_value(self):

        localctx = ExpressionParser.Known_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_known_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 133 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 132
                    self.match(ExpressionParser.DECIMAL)

                else:
                    raise NoViableAltException(self)
                self.state = 135 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,27,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IncognitaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VARIABLE(self):
            return self.getToken(ExpressionParser.VARIABLE, 0)

        def DECIMAL(self, i:int=None):
            if i is None:
                return self.getTokens(ExpressionParser.DECIMAL)
            else:
                return self.getToken(ExpressionParser.DECIMAL, i)

        def getRuleIndex(self):
            return ExpressionParser.RULE_incognita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncognita" ):
                listener.enterIncognita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncognita" ):
                listener.exitIncognita(self)




    def incognita(self):

        localctx = ExpressionParser.IncognitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_incognita)
        self._la = 0 # Token type
        try:
            self.state = 144
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 138 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 137
                    self.match(ExpressionParser.DECIMAL)
                    self.state = 140 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==2):
                        break

                self.state = 142
                self.match(ExpressionParser.VARIABLE)
                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 143
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





