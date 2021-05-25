

def p_init_list(p):
    '''list : LSBRACKET RSBRACKET'''
    p[0] = p[1]


def p_list(p):
    '''list : LSBRACKET element_set RSBRACKET'''
    p[0] = p[1]


def p_element_set(p):
    '''element_set : element COMMA element_set
                    | element'''
    p[0] = p[1]


def p_element(p):
     '''element : BOOLEAN
                | list'''
     p[0] = p[1]