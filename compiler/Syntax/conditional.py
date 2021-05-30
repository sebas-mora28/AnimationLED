import sys 
sys.path.append("..")
from Semantic.Conditional import *



def p_if_integer(p):
    '''conditional : IF conditional_iterable COMPARATOR INTEGER LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("IF integer")
    p[0] = If(p[2], p[3], p[4], p[6])


def p_if_boolean(p):
    '''conditional : IF conditional_iterable COMPARATOR BOOLEAN LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("IF BOOLEAN")
    p[0] = If(p[2], p[3], p[4], p[6])



def p_conditional_iterable(p):
    '''conditional_iterable : ID
                            | list
                            | index_access'''
    p[0] = p[1]
