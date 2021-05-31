import sys 
sys.path.append("..")

from Semantic.Procedures import *
from Semantic.SemanticAnalysis import *


def p_procedure(p):
    '''procedure : PROCEDURE ID LPAREN RPAREN LCBRACKET expressions_set RCBRACKET SEMICOLON'''    
    if(p[2] == "Main"):
        p[0] = MainProcedure(p[2], [], p[6])
    else:
        p[0] = Procedure(p[2],p[4],p[6])



def p_procedure_parameters(p):
    '''procedure : PROCEDURE ID LPAREN parameters_set RPAREN LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("PROCEDURE PARAMETER")
    if(p[2] == "Main"):
        p[0] = MainProcedure(p[2], p[4], p[7])
    else:
        p[0] = Procedure(p[2],p[4],p[7])


def p_parameter_set(p):
    '''parameters_set : ID COMMA parameters_set'''
    p[0] = [p[1]] + p[3]


def p_parameter_1(p):
    '''parameters_set : ID'''
    p[0] = [p[1]]
