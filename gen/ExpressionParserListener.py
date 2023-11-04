# Generated from C:/Users/aledi/source/ExpressionParser/ExpressionParser.g4 by ANTLR 4.13.1
from antlr4 import *

if "." in __name__:
    from .ExpressionParser import ExpressionParser
else:
    from ExpressionParser import ExpressionParser


# This class defines a complete listener for a parse tree produced by ExpressionParser.
class ExpressionParserListener(ParseTreeListener):

    # Enter a parse tree produced by ExpressionParser#equation.
    def enterEquation(self, ctx: ExpressionParser.EquationContext):
        pass

    # Exit a parse tree produced by ExpressionParser#equation.
    def exitEquation(self, ctx: ExpressionParser.EquationContext):
        pass

    # Enter a parse tree produced by ExpressionParser#right_equation.
    def enterRight_equation(self, ctx: ExpressionParser.Right_equationContext):
        pass

    # Exit a parse tree produced by ExpressionParser#right_equation.
    def exitRight_equation(self, ctx: ExpressionParser.Right_equationContext):
        pass

    # Enter a parse tree produced by ExpressionParser#left_equation.
    def enterLeft_equation(self, ctx: ExpressionParser.Left_equationContext):
        pass

    # Exit a parse tree produced by ExpressionParser#left_equation.
    def exitLeft_equation(self, ctx: ExpressionParser.Left_equationContext):
        pass

    # Enter a parse tree produced by ExpressionParser#nested_polynomial.
    def enterNested_polynomial(self, ctx: ExpressionParser.Nested_polynomialContext):
        pass

    # Exit a parse tree produced by ExpressionParser#nested_polynomial.
    def exitNested_polynomial(self, ctx: ExpressionParser.Nested_polynomialContext):
        pass

    # Enter a parse tree produced by ExpressionParser#polynomial.
    def enterPolynomial(self, ctx: ExpressionParser.PolynomialContext):
        pass

    # Exit a parse tree produced by ExpressionParser#polynomial.
    def exitPolynomial(self, ctx: ExpressionParser.PolynomialContext):
        pass

    # Enter a parse tree produced by ExpressionParser#monomial.
    def enterMonomial(self, ctx: ExpressionParser.MonomialContext):
        pass

    # Exit a parse tree produced by ExpressionParser#monomial.
    def exitMonomial(self, ctx: ExpressionParser.MonomialContext):
        pass

    # Enter a parse tree produced by ExpressionParser#known_value.
    def enterKnown_value(self, ctx: ExpressionParser.Known_valueContext):
        pass

    # Exit a parse tree produced by ExpressionParser#known_value.
    def exitKnown_value(self, ctx: ExpressionParser.Known_valueContext):
        pass

    # Enter a parse tree produced by ExpressionParser#incognita.
    def enterIncognita(self, ctx: ExpressionParser.IncognitaContext):
        pass

    # Exit a parse tree produced by ExpressionParser#incognita.
    def exitIncognita(self, ctx: ExpressionParser.IncognitaContext):
        pass


del ExpressionParser
