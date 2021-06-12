
import ast


def p_init_list(p):
    '''list : LSBRACKET RSBRACKET'''
    print("LIST INIT")
    lista = ast.literal_eval(p[1] + p[2])
    p[0] = lista


def p_list(p):
    '''list : LSBRACKET element_set RSBRACKET'''
    p[0] = p[2]



def p_element_set_1(p):
    '''element_set : element'''
    p[0] = p[1]

def p_element_set(p):
    '''element_set : element COMMA element_set'''

    p[0] = p[1] + p[3]


def p_element(p):
     '''element : BOOLEAN
                | list
                | ID'''
     p[0] = [p[1]]