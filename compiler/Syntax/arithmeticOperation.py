import sys 
sys.path.append("..")
from Semantic.ArithmeticOperation import *


precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIVIDEENTIRE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'LPAREN', 'RPAREN'),
    ('right', 'UMINUS')
)

def p_arithmetic(p):
     '''arithmetic : math_operation'''
     print("Math operation")
     p[0] = ArithmeticOperation(p[1])


def p_math_operation(p):
     '''xd : LPAREN math_operation RPAREN'''
     p[0] = str(p[1]) + str(p[2]) + str(p[3])
     print(p[0])


def p_math_operation_1(p):
     '''math_operation : math_operation operator math_operation'''
     p[0] = str(p[1]) + str(p[2]) + str(p[3])
     print(p[0])

def p_math_operator_2(p):
     '''math_operation : math_operation operator math_value'''
     p[0] = str(p[1]) + str(p[2]) + str(p[3])
     print(p[0])


def p_math_operator_2(p):
     '''math_operation : math_value operator math_operation'''
     p[0] = str(p[1]) + str(p[2]) + str(p[3])
     print(p[0])


def p_math_operator_3(p):
     '''math_operation : math_value operator math_value'''
     p[0] = str(p[1]) + str(p[2]) + str(p[3])
     print(p[0])
     

def p_math_operator_uminus(p):
    '''math_operation : MINUS math_value 
                      | MINUS math_operation'''
    p[0] = p[1] + str(p[2])


def p_math_value(p):
     '''math_value : ID 
                   | INTEGER
                   | MINUS ID %prec UMINUS
                   | MINUS INTEGER %prec UMINUS'''
     p[0] = p[1]

def p_operator(p):
    '''operator : PLUS
                  | MINUS
                  | TIMES
                  | POWER
                  | MODULE
                  | DIVIDE 
                  | DIVIDEENTIRE'''
    p[0] = p[1]