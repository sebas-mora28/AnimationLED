import sys
sys.path.append("..")
import yacc 
from Lexical.Lexer import Lexer
from Syntax.reservedProcedures import * 
from Syntax.variableAssign import *
from Syntax.expressions import *
from Syntax.list import * 
from Syntax.proceduresCall import *
from Syntax.procedures import *
from Syntax.conditional import *
from Syntax.loops import * 
from Syntax.arithmeticOperation import *
from Semantic.SemanticAnalysis import *


parsed = None


syntaxErorrs = []

def p_program(p):
    '''program : expressions_set'''
    p[0] = Program(p[1])



def p_error(p):
    if p:
        syntaxErorrs.append(f"Syntax error in input: line {p.lineno} before {p.value} token")
    else:
       syntaxErorrs.append(f"Syntax error at EOF")


def systaxAnalysis(sourceCode, lexer):
    tokens = lexer.tokens
    parser = yacc.yacc(start="program")
    result = parser.parse(sourceCode, lexer)
    return result

