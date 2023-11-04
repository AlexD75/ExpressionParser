from gen.TSqlLexer import *
from gen.TSqlParser import *

from MyTSqlParser import *


def run_parser(in_file) -> [str, int, str, []]:
    lexer = stream = parser = tree = listener = walker = None
    err_code: int = 0
    err_msg: str = ""

    input_stream = in_file.read()
    lexer = TSqlLexer(InputStream(input_stream))
    stream = CommonTokenStream(lexer)
    parser = TSqlParser(stream)
    # substitute default ErrorListener (writing syntax error on console)
    # with custom ErrorListener
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    try:
        tree = parser.tsql_file()  # ! START RULE of the GRAMMAR
    except Exception as exc:
        err_code = exc.args[0]
        err_msg = exc.args[1]
        return '', err_code, err_msg, []

    listener = TransliteTSqlParser()
    walker = ParseTreeWalker()

    try:
        walker.walk(listener, tree)
    except Exception as exc:
        err_code = exc.args[0]
        err_msg = exc.args[1]

    return listener.converted_query, err_code, err_msg, listener.warnings_message


def main(argv):
    input_file = None
    input_number = input("SQL filename number  (InputTestxx.txt)=")
    input_filename = "./InputTest/InputTest" + input_number + ".txt"
    try:
        input_file = open(input_filename, "r")
    except FileNotFoundError as exc:
        print(f'File {input_filename} doesn''t exist')
        quit(1)
    log_file = open(".\converted_queries.txt", 'w')
    cnv_qry, err_code, err_msg, warn_msg_list = run_parser(input_file)

    if err_code != 0:
        log_file.write(f"ERROR {err_code}:{err_msg}")
        print(f"ERROR {err_code}:{err_msg}")
    else:
        log_file.write(cnv_qry)
        if len(warn_msg_list) > 0:
            for warn_msg in warn_msg_list:
                print(warn_msg)
        print(cnv_qry)

    input_file.close()
    log_file.close()


if __name__ == '__main__':
    main(sys.argv)
