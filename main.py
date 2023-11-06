from MyParser import *
from gen.ExpressionLexer import *
from gen.ExpressionParser import *


def run_parser(source: str) -> [str, int, str, []]:
    lexer = stream = parser = tree = listener = walker = None
    err_code: int = 0
    err_msg: str = ""

    lexer = ExpressionLexer(InputStream(source))
    stream = CommonTokenStream(lexer)
    parser = ExpressionParser(stream)
    # substitute default ErrorListener (writing syntax error on console)
    # with custom ErrorListener
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())

    try:
        tree = parser.equation()  # ! START RULE of the GRAMMAR
        print(tree)
    except Exception as exc:
        err_code = exc.args[0]
        err_msg = exc.args[1]
        return '', err_code, err_msg, []

    listener = MyParser()
    walker = ParseTreeWalker()

    try:
        walker.walk(listener, tree)
    except Exception as exc:
        err_code = exc.args[0]
        err_msg = exc.args[1]

    return "", err_code, err_msg, ""


def main(argv):
    input_filename = "./InputTest/InputTest01.txt"

    try:
        with open(input_filename, "r") as source:
            lines = source.readlines()

            cnv_qry, err_code, err_msg, warn_msg_list = run_parser(lines[0])
            print(cnv_qry)

            # for line in lines:
            #     cnv_qry, err_code, err_msg, warn_msg_list = run_parser(line)
            #     print(cnv_qry)

    except FileNotFoundError as exc:
        print(f'File {input_filename} doesn''t exist')
        quit(1)


if __name__ == '__main__':
    main(sys.argv)
