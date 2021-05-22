import sys
sys.path.append("..")



def p_value(p):
    ''' value : INTEGER 
              | BOOLEAN 
              | ID'''

def p_variablAssign_1(p):
    '''variableAssign : ID ASSIGN value SEMICOLON'''
    p[0] = p[1]
    #Se asigna el valor de la variable


def p_variableAssign_2(p):
    '''variableAssign : ID COMMA ID ASSIGN value COMMA value SEMICOLON'''
    p[0] = p[1]
    #Se asgina los valores a la variables
    