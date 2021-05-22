

def p_built_in_functions(p):
    '''built_in_functions : delay '''
    p[0] = p[1]


def p_delay(p):
    '''delay : DELAY LPAREN INTEGER COMMA TIMERANGE RPAREN SEMICOLON'''
    print("delay %d %s" % (p[3], p[5]))
    p[0] = p[1]



