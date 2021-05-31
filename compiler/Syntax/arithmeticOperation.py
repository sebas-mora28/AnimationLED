precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'DIVIDEENTIRE', 'MODULE'),
    ('left', 'POWER'),
    ('left', 'LPAREN', 'RPAREN'),
)

def p_arithmetic(p):
    '''arithmetic : math_operation'''
    p[0] = p[1]



def p_math_operation(p):
    '''math_operation : LPAREN math_operation RPAREN'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_math_operation_1(p):
    '''math_operation : math_operation operator math_operation'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_math_operator_2(p):
    '''math_operation : math_operation operator math_value'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_math_operator_2(p):
    '''math_operation : math_value operator math_operation'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_math_operator_3(p):
    '''math_operation : math_value operator math_value'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_math_value(p):
    '''math_value : ID 
                  | INTEGER'''
    p[0] = p[1]

def p_comparator(p):
    '''operator : PLUS
                  | MINUS
                  | TIMES
                  | POWER
                  | MODULE
                  | DIVIDE 
                  | DIVIDEENTIRE'''
    p[0] = p[1]