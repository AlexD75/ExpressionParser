# Generated from C:/Users/aledi/source/ExpressionParser/ExpressionParser.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser


# This class defines a complete generic visitor for a parse tree produced by ExpressionParser.

class ExpressionParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExpressionParser#equation.
    def visitEquation(self, ctx: ExpressionParser.EquationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#right_equation.
    def visitRight_equation(self, ctx: ExpressionParser.Right_equationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#left_equation.
    def visitLeft_equation(self, ctx: ExpressionParser.Left_equationContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#nested_polynomial.
    def visitNested_polynomial(self, ctx: ExpressionParser.Nested_polynomialContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#polynomial.
    def visitPolynomial(self, ctx: ExpressionParser.PolynomialContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#monomial.
    def visitMonomial(self, ctx: ExpressionParser.MonomialContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#known_value.
    def visitKnown_value(self, ctx: ExpressionParser.Known_valueContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by ExpressionParser#incognita.
    def visitIncognita(self, ctx: ExpressionParser.IncognitaContext):
        return self.visitChildren(ctx)


del ExpressionParser
