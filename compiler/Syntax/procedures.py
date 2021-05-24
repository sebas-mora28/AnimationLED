

def p_procedure(p):
    '''procedure : PROCEDURE ID LPAREN RPAREN BEGIN expressions_set END SEMICOLON'''
    print("PROCEDURE")
    p[0] = p[1]

def p_procedure_parameters(p):
    '''procedure : PROCEDURE ID LPAREN parameters_set RPAREN BEGIN expressions_set END SEMICOLON'''
    p[0] = p[1]

def p_parameter(p):
    '''parameter : ID'''
    p[0] = p[1]

def p_parameter_set(p):
    '''parameters_set : parameter COMMA parameters_set'''
    p[0] = p[1]


def p_parameter_1(p):
    '''parameters_set : parameter'''
    p[0] = p[1]
