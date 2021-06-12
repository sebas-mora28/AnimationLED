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
      print(p[1])
      p[0] = ArithmeticOperation(p[1])


def p_math_operator_1(p):
     '''math_operation : math_operation operator math_operation'''
     
     #print(str(p[1]) + str(p[2]) + str(p[3]))
     #p[0] = str(p[1]) + str(p[2]) + str(p[3])
     p[0] = MathOperation(p[1], p[2], p[3])

def p_math_operator_2(p):
     '''math_operation : math_operation operator math_value'''

     #print(str(p[1]) + str(p[2]) + str(p[3]))
     #p[0] = str(p[1]) + str(p[2]) + str(p[3])
     p[0] = MathOperation(p[1], p[2], p[3])

def p_math_operator_2(p):
     '''math_operation : math_value operator math_operation'''
     #print(str(p[1]) + str(p[2]) + str(p[3]))
     #p[0] = str(p[1]) + str(p[2]) + str(p[3])
     p[0] = MathOperation(p[1], p[2], p[3])

def p_math_operator_3(p):
     '''math_operation : math_value operator math_value'''
     #print(str(p[1]) + str(p[2]) + str(p[3]))
     #p[0] = str(p[1]) + str(p[2]) + str(p[3])
     p[0] = MathOperation(p[1], p[2], p[3]) 

def p_math_operation_4(p):
     '''math_operation_paren : LPAREN math_operation RPAREN'''
     #print(str(p[1]) + str(p[2]) + str(p[3]))
     #p[0] = str(p[1]) + str(p[2]) + str(p[3])
     p[0] = MathOperation(p[1], p[2], p[3])


def p_math_value(p):
     '''math_value : ID
                    | INTEGER
                    | math_value_negative
                    | math_operation_paren'''


     #p[0] = str(p[1])
     p[0] = MathValue(p[1])

def p_math_value_negative(p):
     '''math_value_negative : MINUS ID %prec UMINUS
                            | MINUS INTEGER %prec UMINUS '''


     #p[0] = str(p[1]) + str(p[2])
     p[0] = MathValueNegative(p[2])
def p_operator(p):
    '''operator : PLUS
                  | MINUS
                  | TIMES
                  | POWER
                  | MODULE
                  | DIVIDE 
                  | DIVIDEENTIRE'''
    p[0] = p[1]