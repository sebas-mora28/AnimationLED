import sys
sys.path.append("..")
from Semantic.ForLoops import * 



def p_for_loop_step(p):
    '''for_loop : FOR ID IN iterable STEP INTEGER LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("FOR LOOP STEP")
    p[0] = ForLoop(p[2], p[4],p[6], p[8])


def p_for_loop(p):
    '''for_loop : FOR ID IN iterable LCBRACKET expressions_set RCBRACKET SEMICOLON'''
    print("FOR LOOP")
    p[0] = ForLoop(p[2],p[4], 1, p[6])


def p_iterable(p):
    '''iterable : ID
                 | INTEGER'''
    p[0] = p[1]

