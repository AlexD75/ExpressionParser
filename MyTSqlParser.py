from gen.TSqlLexer import *
from gen.TSqlParser import *
from gen.TSqlParserListener import *
from antlr4.error.ErrorListener import *


class TransliteTSqlParser (TSqlParserListener):

    def __init__(self):
        self.converted_query = ""
        self.warnings_message = []


    def enterSelect_statement_standalone(self,ctx:TSqlParser.Select_statement_standaloneContext):
        print(ctx.getText())
        print(self.get_source(ctx))

        select_statement: TSqlParser.Select_statementContext = ctx.select_statement()
        query_expression: TSqlParser.Query_expressionContext = select_statement.query_expression()
        query_specification: TSqlParser.Query_specificationContext = query_expression.query_specification()
        select_list: TSqlParser.Select_listContext = query_specification.select_list()
        print (self.get_source(select_list))

        select_list = ctx.select_statement().query_expression().query_specification().select_list()
        print (self.get_source(select_list))

        table_sources: TSqlParser.Table_sourcesContext= query_specification.table_sources()
        print (self.get_source(table_sources))

        where_condition: TSqlParser.Search_conditionContext = query_specification.search_condition()
        for i in range(len(where_condition)):
            print (self.get_source(where_condition[i]))

    def enterCreate_table(self, ctx: TSqlParser.Create_tableContext):
        print ('CREATE TABLE')
        table_name: TSqlParser.Table_nameContext = ctx.table_name()
        print (f'table name= {self.get_source(table_name)}')

    def enterInsert_statement(self, ctx: TSqlParser.Insert_statementContext):
        print ('INSERT INTO')
        table_name: TSqlParser.Table_nameContext = ctx.ddl_object()
        print (f'table name= {self.get_source(table_name)}')
        col_list: TSqlParser.Table_nameContext = ctx.insert_column_name_list()
        print (self.get_source(col_list))







    def get_source(self, rule:ParserRuleContext):
        """
        Returns the original piece of input stream matching the rule passed
        :param rule:
        :return:
        """
        src=""
        start_index = rule.start.start
        stop_index = rule.stop.stop
        src = rule.start.getInputStream().getText(start_index, stop_index)
        return src


class CustomErrorListener(ErrorListener):
    """
    Custom management of  ANTLR syntax errors: raise exception instead print on console out (default behaviour)
    """

    def __init__(self):
        super(CustomErrorListener, self).__init__()

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(99, "Syntax not supported by the translator. Details: line " + str(line) + ":" + str(column) + " " + msg)







