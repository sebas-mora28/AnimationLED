

def p_procedureCall_no_arguments(p):
    '''procedureCall : CALL ID LPAREN RPAREN SEMICOLON'''
    p[0] = p[1]


def p_procedureCall_with_arguments(p):
    '''procedureCall : CALL ID LPAREN arguments_set RPAREN SEMICOLON'''
    print("PROCEDURE CALL")
    p[0] = p[1]


def p_argument(p):
    '''argument : ID
                | INTEGER
                | BOOLEAN'''
    p[0] = p[1]


def p_argument_set(p):
    '''arguments_set : argument COMMA arguments_set'''
    p[0] = p[1]


def p_argument_set_1(p):
    '''arguments_set : argument'''
    p[0] = p[1]


