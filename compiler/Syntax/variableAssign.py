import sys
sys.path.append("..")



def p_value(p):
    '''value : INTEGER 
              | BOOLEAN 
              | ID
              | list'''
    p[0] = [1]


def p_variable_assign_1(p):
    '''variable_assign : ID ASSIGN value SEMICOLON'''
    p[0] = p[1]
    #Se asigna el valor de la variable

def p_variable_assign_2(p):
    '''variable_assign : ID COMMA ID ASSIGN value COMMA value SEMICOLON'''
    p[0] = p[1]
    #Se asgina los valores a la variables


def p_index_access(p):
    '''index_access : ID index'''
    p[0] = p[1]

def p_index_assign(p):
    '''index_assign : ID index ASSIGN value SEMICOLON'''


def p_index_list(p):
    '''index : LSBRACKET index_type RSBRACKET'''
    print("LIST INDEX")


def p_index_matrix(p):
    '''index :  LSBRACKET index_type RSBRACKET LSBRACKET index_type RSBRACKET '''
    print("MATRIX INDEX")


def p_index_type(p):
    '''index_type : index_range
                  | index_pair
                  | index_column
                  | ID 
                  | INTEGER'''

def p_index_value(p):
    '''index_value : ID 
                   | INTEGER'''

    p[0] = p[1]

def p_index_range(p):
    '''index_range : index_value COLON index_value'''
    p[0] = p[1]

def p_index_pair(p):
    '''index_pair : index_value COMMA index_value'''
    p[0] = p[1]

def p_index_column(p):
    '''index_column : COLON COMMA index_value'''
    p[0] = p[1]