import sys 
sys.path.append("..")

from Semantic.ListFunctions import *
from Semantic.ReservedProcedures import *



def p_reserved_procedures(p):
    '''reserved_procedures : delay 
                          | blink 
                          | printLed
                          | printLedX
                          | list_insert 
                          | list_delete 
                          | matrix_insert
                          | matrix_delete
                          | list_boolean_operation'''
    p[0] = p[1]


#LED functions
def p_delay(p):
    '''delay : DELAY LPAREN INTEGER COMMA TIMERANGE RPAREN SEMICOLON'''
    print("delay %d %s" % (p[3], p[5]))
    p[0] = Delay(p[3], p[5])


def p_blink(p):
    '''blink : BLINK LPAREN OBJECTTYPE COMMA INTEGER COMMA TIMERANGE COMMA BOOLEAN RPAREN SEMICOLON'''
    print("blink")


def p_printLed(p):
    '''printLed : PRINTLED LPAREN INTEGER COMMA INTEGER COMMA BOOLEAN RPAREN SEMICOLON'''
    print("printLED")
    p[0] = PrintLed(p[3], p[5],p[7])


def p_printLed_value(p):
    '''printLed_value : ID
                      | list'''
    p[0] = p[1]

def p_printLedX(p):
    '''printLedX : PRINTLEDX LPAREN OBJECTTYPE COMMA INTEGER COMMA printLed_value RPAREN SEMICOLON'''
    print("printLEDX")
    p[0] = PrintLedX(p[3], p[5], p[7])

#list functions




#len 
def p_len(p):
    '''len : LEN LPAREN ID RPAREN'''
    print("leeeen")
    p[0] = Len(p[3])


#range
def p_range(p):
    'range : RANGE LPAREN INTEGER COMMA BOOLEAN RPAREN'
    p[0] = Range(p[3], p[5])


#list insert 


def p_insert_value(p):
    '''insert_value : list 
                    | BOOLEAN'''

    p[0] = p[1]


def p_list_insert(p):
    '''list_insert : ID INSERT LPAREN INTEGER COMMA BOOLEAN RPAREN SEMICOLON'''
    print("INSERT LIST" + str(p[6]))
    p[0] = ListInsert(p[1], p[4], p[6])

def p_list_delete(p):
    '''list_delete : ID DELETE LPAREN INTEGER RPAREN SEMICOLON'''
    print("DELETE LIST")
    p[0] = ListDelete(p[1], p[4])



#matrix insert

def p_matrix_insert(p):
    '''matrix_insert : ID INSERT LPAREN insert_value COMMA INTEGER RPAREN SEMICOLON'''
    p[0] = MatrixInsert(p[1], p[4], p[6], None)

def p_matrix_insert_index(p):
    '''matrix_insert : ID INSERT LPAREN insert_value COMMA INTEGER COMMA INTEGER RPAREN SEMICOLON'''
    print("INSERT MATRIX INSERT")
    p[0] = MatrixInsert(p[1], p[4], p[6], p[8])

def p_matrix_delete(p):
    '''matrix_delete : ID DELETE LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'''
    print("DELETE MATRIX")
    p[0] = MatrixDelete(p[1], p[4], p[6])


def p_matrix_dimension(p):
    '''matrix_dimensions : ID LISTSHAPE '''
    print("MATRIX DIMENSIONS")
    print(p[2])
    p[0] = MatrixDimension(p[1], p[2])
 



# list boolean operation 
def p_list_boolean_operation(p):
    '''list_boolean_operation : ID LISTOPERATOR SEMICOLON '''
    print("LIST BOOLEAN OPERATION")

def p_list_boolean_operation_index(p):
    '''list_boolean_operation : ID index_type LISTOPERATOR SEMICOLON''' 
    print("LIST BOOLEAN OPERATION INDEX")