import sys
sys.path.append("..")
import yacc 
from Lexical.lexer import Lexer
from Syntax.builtInFunction import * 
from Syntax.variableAssign import *
from Syntax.expressions import *
from Syntax.list import * 
from Syntax.proceduresCall import *
from Syntax.procedures import *
from Syntax.conditional import *
from Syntax.loops import * 
from Sematic.SemanticAnalysis import *




def p_program(p):
    '''program : expressions_set'''
    print(p[1])
    p[0] = Program(p[1])

def p_error(p):
        #print("error")
        print(f"Syntax error in input: line {p.lineno} in {p.value} token")



def systaxAnalysis(sourceCode, lexer):
    tokens = lexer.tokens
    parser = yacc.yacc(start="program")
    result = parser.parse(sourceCode, lexer)
    return result

