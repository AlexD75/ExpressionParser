# Generated from C:/Users/aledi/source/ExpressionParser/TestParser.g4 by ANTLR 4.13.1
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
        4,1,13,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,1,0,3,0,12,8,0,
        1,0,1,0,4,0,16,8,0,11,0,12,0,17,1,0,1,0,1,0,3,0,23,8,0,1,0,1,0,1,
        0,1,0,4,0,29,8,0,11,0,12,0,30,1,0,1,0,1,0,3,0,36,8,0,1,0,1,0,1,0,
        4,0,41,8,0,11,0,12,0,42,1,0,1,0,3,0,47,8,0,1,1,3,1,50,8,1,1,1,1,
        1,3,1,54,8,1,1,1,1,1,3,1,58,8,1,1,2,1,2,1,3,1,3,1,4,1,4,4,4,66,8,
        4,11,4,12,4,67,1,4,4,4,71,8,4,11,4,12,4,72,3,4,75,8,4,1,4,0,0,5,
        0,2,4,6,8,0,0,85,0,46,1,0,0,0,2,49,1,0,0,0,4,59,1,0,0,0,6,61,1,0,
        0,0,8,74,1,0,0,0,10,12,5,4,0,0,11,10,1,0,0,0,11,12,1,0,0,0,12,13,
        1,0,0,0,13,15,5,6,0,0,14,16,3,2,1,0,15,14,1,0,0,0,16,17,1,0,0,0,
        17,15,1,0,0,0,17,18,1,0,0,0,18,19,1,0,0,0,19,22,5,7,0,0,20,21,5,
        13,0,0,21,23,3,4,2,0,22,20,1,0,0,0,22,23,1,0,0,0,23,24,1,0,0,0,24,
        25,5,0,0,1,25,47,1,0,0,0,26,28,5,6,0,0,27,29,3,2,1,0,28,27,1,0,0,
        0,29,30,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,32,1,0,0,0,32,35,
        5,7,0,0,33,34,5,13,0,0,34,36,3,4,2,0,35,33,1,0,0,0,35,36,1,0,0,0,
        36,37,1,0,0,0,37,38,5,0,0,1,38,47,1,0,0,0,39,41,3,2,1,0,40,39,1,
        0,0,0,41,42,1,0,0,0,42,40,1,0,0,0,42,43,1,0,0,0,43,44,1,0,0,0,44,
        45,5,0,0,1,45,47,1,0,0,0,46,11,1,0,0,0,46,26,1,0,0,0,46,40,1,0,0,
        0,47,1,1,0,0,0,48,50,5,4,0,0,49,48,1,0,0,0,49,50,1,0,0,0,50,53,1,
        0,0,0,51,54,3,8,4,0,52,54,3,6,3,0,53,51,1,0,0,0,53,52,1,0,0,0,54,
        57,1,0,0,0,55,56,5,13,0,0,56,58,3,4,2,0,57,55,1,0,0,0,57,58,1,0,
        0,0,58,3,1,0,0,0,59,60,3,8,4,0,60,5,1,0,0,0,61,62,5,2,0,0,62,7,1,
        0,0,0,63,65,5,2,0,0,64,66,5,3,0,0,65,64,1,0,0,0,66,67,1,0,0,0,67,
        65,1,0,0,0,67,68,1,0,0,0,68,75,1,0,0,0,69,71,5,3,0,0,70,69,1,0,0,
        0,71,72,1,0,0,0,72,70,1,0,0,0,72,73,1,0,0,0,73,75,1,0,0,0,74,63,
        1,0,0,0,74,70,1,0,0,0,75,9,1,0,0,0,13,11,17,22,30,35,42,46,49,53,
        57,67,72,74
    ]

class TestParser ( Parser ):

    grammarFileName = "TestParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'='", "<INVALID>", "<INVALID>", "','", 
                     "'*'", "'/'", "'+'", "'-'", "'^'" ]

    symbolicNames = [ "<INVALID>", "SPACE", "DECIMAL", "VARIABLE", "OPERATOR", 
                      "EQUAL", "LR_BRACKET", "RR_BRACKET", "COMMA", "STAR", 
                      "DIVIDE", "PLUS", "MINUS", "POWER" ]

    RULE_polynomial = 0
    RULE_monomial = 1
    RULE_exponent = 2
    RULE_known_value = 3
    RULE_incognita = 4

    ruleNames =  [ "polynomial", "monomial", "exponent", "known_value", 
                   "incognita" ]

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
    POWER=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class PolynomialContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LR_BRACKET(self):
            return self.getToken(TestParser.LR_BRACKET, 0)

        def RR_BRACKET(self):
            return self.getToken(TestParser.RR_BRACKET, 0)

        def EOF(self):
            return self.getToken(TestParser.EOF, 0)

        def OPERATOR(self):
            return self.getToken(TestParser.OPERATOR, 0)

        def monomial(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(TestParser.MonomialContext)
            else:
                return self.getTypedRuleContext(TestParser.MonomialContext,i)


        def POWER(self):
            return self.getToken(TestParser.POWER, 0)

        def exponent(self):
            return self.getTypedRuleContext(TestParser.ExponentContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_polynomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPolynomial" ):
                listener.enterPolynomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPolynomial" ):
                listener.exitPolynomial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPolynomial" ):
                return visitor.visitPolynomial(self)
            else:
                return visitor.visitChildren(self)




    def polynomial(self):

        localctx = TestParser.PolynomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_polynomial)
        self._la = 0 # Token type
        try:
            self.state = 46
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==4:
                    self.state = 10
                    self.match(TestParser.OPERATOR)


                self.state = 13
                self.match(TestParser.LR_BRACKET)
                self.state = 15 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 14
                    self.monomial()
                    self.state = 17 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 19
                self.match(TestParser.RR_BRACKET)
                self.state = 22
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 20
                    self.match(TestParser.POWER)
                    self.state = 21
                    self.exponent()


                self.state = 24
                self.match(TestParser.EOF)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 26
                self.match(TestParser.LR_BRACKET)
                self.state = 28 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 27
                    self.monomial()
                    self.state = 30 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 32
                self.match(TestParser.RR_BRACKET)
                self.state = 35
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==13:
                    self.state = 33
                    self.match(TestParser.POWER)
                    self.state = 34
                    self.exponent()


                self.state = 37
                self.match(TestParser.EOF)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 40 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 39
                    self.monomial()
                    self.state = 42 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & 28) != 0)):
                        break

                self.state = 44
                self.match(TestParser.EOF)
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
            return self.getTypedRuleContext(TestParser.IncognitaContext,0)


        def known_value(self):
            return self.getTypedRuleContext(TestParser.Known_valueContext,0)


        def OPERATOR(self):
            return self.getToken(TestParser.OPERATOR, 0)

        def POWER(self):
            return self.getToken(TestParser.POWER, 0)

        def exponent(self):
            return self.getTypedRuleContext(TestParser.ExponentContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_monomial

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMonomial" ):
                listener.enterMonomial(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMonomial" ):
                listener.exitMonomial(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMonomial" ):
                return visitor.visitMonomial(self)
            else:
                return visitor.visitChildren(self)




    def monomial(self):

        localctx = TestParser.MonomialContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_monomial)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 49
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==4:
                self.state = 48
                self.match(TestParser.OPERATOR)


            self.state = 53
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 51
                self.incognita()
                pass

            elif la_ == 2:
                self.state = 52
                self.known_value()
                pass


            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==13:
                self.state = 55
                self.match(TestParser.POWER)
                self.state = 56
                self.exponent()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExponentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def incognita(self):
            return self.getTypedRuleContext(TestParser.IncognitaContext,0)


        def getRuleIndex(self):
            return TestParser.RULE_exponent

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExponent" ):
                listener.enterExponent(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExponent" ):
                listener.exitExponent(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExponent" ):
                return visitor.visitExponent(self)
            else:
                return visitor.visitChildren(self)




    def exponent(self):

        localctx = TestParser.ExponentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_exponent)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 59
            self.incognita()
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

        def DECIMAL(self):
            return self.getToken(TestParser.DECIMAL, 0)

        def getRuleIndex(self):
            return TestParser.RULE_known_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterKnown_value" ):
                listener.enterKnown_value(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitKnown_value" ):
                listener.exitKnown_value(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitKnown_value" ):
                return visitor.visitKnown_value(self)
            else:
                return visitor.visitChildren(self)




    def known_value(self):

        localctx = TestParser.Known_valueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_known_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(TestParser.DECIMAL)
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

        def DECIMAL(self):
            return self.getToken(TestParser.DECIMAL, 0)

        def VARIABLE(self, i:int=None):
            if i is None:
                return self.getTokens(TestParser.VARIABLE)
            else:
                return self.getToken(TestParser.VARIABLE, i)

        def getRuleIndex(self):
            return TestParser.RULE_incognita

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIncognita" ):
                listener.enterIncognita(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIncognita" ):
                listener.exitIncognita(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIncognita" ):
                return visitor.visitIncognita(self)
            else:
                return visitor.visitChildren(self)




    def incognita(self):

        localctx = TestParser.IncognitaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_incognita)
        try:
            self.state = 74
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.match(TestParser.DECIMAL)
                self.state = 65 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 64
                        self.match(TestParser.VARIABLE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 67 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

                pass
            elif token in [3]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70 
                self._errHandler.sync(self)
                _alt = 1
                while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                    if _alt == 1:
                        self.state = 69
                        self.match(TestParser.VARIABLE)

                    else:
                        raise NoViableAltException(self)
                    self.state = 72 
                    self._errHandler.sync(self)
                    _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

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





