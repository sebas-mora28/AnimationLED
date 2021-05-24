

def p_built_in_functions(p):
    '''built_in_functions : delay 
                          | blink 
                          | printLed
                          | printLedX
                          | len
                          | list_insert 
                          | list_delete 
                          | matrix_insert
                          | matrix_delete
                          | matrix_dimensions
                          | list_boolean_operation'''
    p[0] = p[1]


#LED functions
def p_delay(p):
    '''delay : DELAY LPAREN INTEGER COMMA TIMERANGE RPAREN SEMICOLON'''
    print("delay %d %s" % (p[3], p[5]))
    p[0] = p[1]


def p_blink(p):
    '''blink : BLINK LPAREN index_access COMMA INTEGER COMMA TIMERANGE COMMA BOOLEAN RPAREN SEMICOLON'''
    print("blink")


def p_printLed(p):
    '''printLed : PRINTLED LPAREN INTEGER COMMA INTEGER COMMA BOOLEAN RPAREN'''
    print("printLED")


def p_printLed_value(p):
    '''printLed_value : ID
                      | INTEGER
                      | index_access'''

def p_printLedX(p):
    '''printLedX : PRINTLEDX LPAREN OBJECTTYPE COMMA INTEGER COMMA printLed_value RPAREN SEMICOLON'''
    print("printLEDX")


#list functions


#len 
def p_len(p):
    '''len : LEN LPAREN ID RPAREN SEMICOLON'''

def p_len_index(p):
    '''len : LEN LPAREN ID index RPAREN SEMICOLON'''
    print("LEN")



#list insert 


def p_insert_value(p):
    '''insert_value : list 
                    | BOOLEAN'''

def p_list_insert(p):
    '''list_insert : ID INSERT LPAREN INTEGER COMMA insert_value RPAREN SEMICOLON'''
    print("INSERT LIST")

def p_list_delete(p):
    '''list_delete : ID DELETE LPAREN INTEGER RPAREN SEMICOLON'''
    print("DELETE LIST")



#matrix insert

def p_matrix_insert(p):
    '''matrix_insert : ID INSERT LPAREN insert_value COMMA INTEGER RPAREN SEMICOLON'''
    print("INSERT MATRIX")

def p_matrix_insert_index(p):
    '''matrix_insert : ID INSERT LPAREN insert_value COMMA INTEGER COMMA INTEGER RPAREN SEMICOLON'''
    print("INSERT MATRIX INSERT")

def p_matrix_delete(p):
    '''matrix_delete : ID DELETE LPAREN INTEGER COMMA INTEGER RPAREN SEMICOLON'''
    print("DELETE MATRIX")


def p_matrix_dimension(p):
    '''matrix_dimensions : ID LISTSHAPE SEMICOLON '''
    print("MATRIX DIMENSIONS")

# list boolean operation 

def p_list_boolean_operation(p):
    '''list_boolean_operation : ID LISTOPERATOR SEMICOLON '''
    print("LIST BOOLEAN OPERATION")

def p_list_boolean_operation_index(p):
    '''list_boolean_operation : ID index LISTOPERATOR SEMICOLON''' 
    print("LIST BOOLEAN OPERATION INDEX")