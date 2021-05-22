


def p_expression_set(p):
    '''expression_set : expression 
                        | expression expression_set  
                        | empty'''
    p[0] = p[1]


def p_expression(p):
    '''expression : variableAssign 
                  | built_in_functions'''
        
    p[0] = p[1]

def p_empty(p):
        '''empty : '''
        p[0] = None

