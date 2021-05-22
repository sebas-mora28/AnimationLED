import sys
sys.path.append("..")
import yacc 
from Lexical.lexer import Lexer
from Syntax.procedures import *
from Syntax.builtInFunction import * 
from Syntax.arithmetic_operation import *
from Syntax.variableAssign import *



def p_program(p):
    ''' program : expressions '''
    p[0] = p[1]



def p_error(p):
        print("Syntax error in input!")



def systaxAnalysis(sourceCode, lexer):
    tokens = lexer.tokens
    parser = yacc.yacc(start="program")
    result = parser.parse(sourceCode, lexer)
    print(result)
    return result

