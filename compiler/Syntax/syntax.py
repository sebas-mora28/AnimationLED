import sys
sys.path.append("..")
import yacc 
from Lexical.lexer import Lexer
from Syntax.procedures import *
from Syntax.builtInFunction import * 
from Syntax.arithmetic_operation import *
from Syntax.variableAssign import *
from Syntax.expressions import *
from Syntax.list import * 

def p_program(p):
    ''' program : expression_set '''
    p[0] = p[1]



def p_error(p):
        print("error")
        #print(f"Syntax error in input: line {p.lineno} in {p.value} token")



def systaxAnalysis(sourceCode, lexer):
    tokens = lexer.tokens
    parser = yacc.yacc(start="program")
    result = parser.parse(sourceCode, lexer)
    print(result)
    return result

