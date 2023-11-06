# Generated from C:/Users/aledi/source/ExpressionParser/TestParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete listener for a parse tree produced by TestParser.
class TestParserListener(ParseTreeListener):

    # Enter a parse tree produced by TestParser#polynomial.
    def enterPolynomial(self, ctx:TestParser.PolynomialContext):
        pass

    # Exit a parse tree produced by TestParser#polynomial.
    def exitPolynomial(self, ctx:TestParser.PolynomialContext):
        pass


    # Enter a parse tree produced by TestParser#monomial.
    def enterMonomial(self, ctx:TestParser.MonomialContext):
        pass

    # Exit a parse tree produced by TestParser#monomial.
    def exitMonomial(self, ctx:TestParser.MonomialContext):
        pass


    # Enter a parse tree produced by TestParser#exponent.
    def enterExponent(self, ctx:TestParser.ExponentContext):
        pass

    # Exit a parse tree produced by TestParser#exponent.
    def exitExponent(self, ctx:TestParser.ExponentContext):
        pass


    # Enter a parse tree produced by TestParser#known_value.
    def enterKnown_value(self, ctx:TestParser.Known_valueContext):
        pass

    # Exit a parse tree produced by TestParser#known_value.
    def exitKnown_value(self, ctx:TestParser.Known_valueContext):
        pass


    # Enter a parse tree produced by TestParser#incognita.
    def enterIncognita(self, ctx:TestParser.IncognitaContext):
        pass

    # Exit a parse tree produced by TestParser#incognita.
    def exitIncognita(self, ctx:TestParser.IncognitaContext):
        pass



del TestParser