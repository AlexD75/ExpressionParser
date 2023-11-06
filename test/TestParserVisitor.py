# Generated from C:/Users/aledi/source/ExpressionParser/TestParser.g4 by ANTLR 4.13.1
from antlr4 import *
if "." in __name__:
    from .TestParser import TestParser
else:
    from TestParser import TestParser

# This class defines a complete generic visitor for a parse tree produced by TestParser.

class TestParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by TestParser#polynomial.
    def visitPolynomial(self, ctx:TestParser.PolynomialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#monomial.
    def visitMonomial(self, ctx:TestParser.MonomialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#exponent.
    def visitExponent(self, ctx:TestParser.ExponentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#known_value.
    def visitKnown_value(self, ctx:TestParser.Known_valueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by TestParser#incognita.
    def visitIncognita(self, ctx:TestParser.IncognitaContext):
        return self.visitChildren(ctx)



del TestParser