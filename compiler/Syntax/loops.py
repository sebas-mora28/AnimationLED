

def p_for_loop_step(p):
    '''for_loop : FOR ID IN iterable STEP INTEGER LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("FOR LOOP STEP")
    p[0] = p[1]


def p_for_loop(p):
    '''for_loop : FOR ID IN iterable LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("FOR LOOP")
    p[0] = p[1]


def p_iterable(p):
    '''iterable : ID
                 | list'''
    p[0] = p[1]

