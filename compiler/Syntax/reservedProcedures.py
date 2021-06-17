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
                          | list_boolean_operation
                          | matrix_dimensions
                          | type'''
    p[0] = p[1]


#LED functions
def p_delay(p):
    '''delay : DELAY LPAREN procedure_value COMMA STRING RPAREN SEMICOLON'''
    p[0] = Delay(p[3], p[5])


def p_blink(p):
    '''blink : BLINK LPAREN procedure_value COMMA procedure_value COMMA procedure_value COMMA STRING COMMA procedure_value RPAREN SEMICOLON'''
    p[0] = Blink(p[3],p[5],p[7],p[9],p[11])


def p_printLed(p):
    '''printLed : PRINTLED LPAREN procedure_value COMMA procedure_value COMMA procedure_value RPAREN SEMICOLON'''
    print("printLED")
    p[0] = PrintLed(p[3], p[5],p[7])


def p_printLedX(p):
    '''printLedX : PRINTLEDX LPAREN STRING COMMA procedure_value COMMA procedure_value RPAREN SEMICOLON'''
    print("printLEDX")
    p[0] = PrintLedX(p[3], p[5], p[7])


def p_procedure_value(p):
    '''procedure_value : ID
                       | INTEGER
                       | BOOLEAN
                       | list'''
    p[0] = p[1]


#list functions
def p_type(p):
    '''type : TYPE LPAREN ID RPAREN 
            | TYPE LPAREN BOOLEAN RPAREN 
            | TYPE LPAREN INTEGER RPAREN  
            | TYPE LPAREN list RPAREN'''

    p[0] = Type(p[3])


#len 
def p_len(p):
    '''len : LEN LPAREN ID RPAREN'''
    print("LEN")
    p[0] = Len(p[3])


#range
def p_range(p):
    'range : LIST LPAREN RANGE LPAREN INTEGER COMMA BOOLEAN RPAREN RPAREN'
    p[0] = Range(p[5], p[7])


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
    '''matrix_dimensions : ID LISTSHAPE'''
    print("MATRIX DIMENSIONS")
    print(p[2])
    p[0] = MatrixDimension(p[1], p[2])
 



# list boolean operation 
def p_list_boolean_operation(p):
    '''list_boolean_operation : ID LISTOPERATOR SEMICOLON '''
    print("LIST BOOLEAN OPERATION")
    p[0] = BooleanOperation(p[1], p[2])

def p_list_boolean_operation_index(p):
    '''list_boolean_operation : index_type LISTOPERATOR SEMICOLON''' 
    print("LIST BOOLEAN OPERATION INDEX")
    p[0] = BooleanOperationIndex(p[1], p[2])



#Print 
def p_print(p):
    '''print : PRINT LPAREN print_argument RPAREN SEMICOLON'''
    p[0] = Print(p[3])


def p_print_argument(p):
    '''print_argument : type 
                      | len 
                      | ID
                      | BOOLEAN 
                      | INTEGER
                      | index_access'''
    p[0] = p[1]

    pass