


def p_expressions_set(p):
    '''expressions_set :  expression expressions_set'''
    p[0] = p[1]



def p_expressions_set_1(p):
    '''expressions_set : expression'''


def p_expression(p):
    '''expression : variable_assign 
                  | built_in_functions
                  | procedure
                  | index_assign
                  | procedureCall
                  | conditional
                  | for_loop
                  | empty'''
        
    p[0] = p[1]

def p_empty(p):
        '''empty : '''
        p[0] = None

