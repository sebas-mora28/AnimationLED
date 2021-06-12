import sys
sys.path.append("..")
import yacc 
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


class SyntaxError:

    def __init__(self):
        self.errors = []

    def addError(self, error):
        self.errors.append(error)
    
    def clean(self):
        self.errors = []
    
    def getErrors(self):
        return self.errors

syntaxError = SyntaxError()


def p_program(p):
    '''program : procedure_set''' 
    p[0] = Program(p[1])


def p_procedure_set(p):
   '''procedure_set : procedure procedure_set'''
   p[0] = [p[1]] + p[2]
 
def p_procedure_set_2(p):
   '''procedure_set : procedure
                    | empty'''
   p[0] = [p[1]]


def p_error(p):
    if p:
        syntaxError.addError(f"Syntax error in input: line {p.lineno} before {p.value} token")
    else:
       syntaxError.addError(f"Syntax error at EOF")


def systaxAnalysis(sourceCode, lexer):
    syntaxError.clean()
    tokens = lexer.tokens
    parser = yacc.yacc(start="program")
    result = parser.parse(sourceCode, lexer)
    return result

