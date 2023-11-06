from gen.ExpressionParser import *
from gen.ExpressionParserListener import *
from antlr4.error.ErrorListener import ErrorListener


class MyParser(ExpressionParserListener):
    def enterIncognita(self, ctx: ExpressionParser.IncognitaContext):
        print(f"Incognita: {self.get_source(ctx)}")

    def enterEveryRule(self, ctx: ParserRuleContext):
        # print(f"enterEveryRule: {self.get_source(ctx)}")
        pass

    def get_source(self, ctx: ParserRuleContext):
        """
        Returns the original piece of input stream matching the rule passed
        :param ctx:
        :return:
        """
        _ = self
        src = ""
        start_index = ctx.start.start
        stop_index = ctx.stop.stop
        src = ctx.start.getInputStream().getText(start_index, stop_index)
        return src


class CustomErrorListener(ErrorListener):
    """
    Custom management of  ANTLR syntax errors: raise exception instead print on console out (default behaviour)
    """

    def __init__(self):
        super(CustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(99, f"Syntax not supported by the translator. Details: line {line}:{column} {msg}")
