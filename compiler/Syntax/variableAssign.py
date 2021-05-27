import sys
sys.path.append("..")
from Semantic.SemanticAnalysis import *
from Semantic.IndexType import *
from Semantic.Atomic import *

def p_value(p):
    '''value : INTEGER 
              | BOOLEAN 
              | ID
              | list
              | len
              | list_creation
              | matrix_dimensions
              | arithmetic'''
    p[0] = value(p[1])




# Asignacion de variable 

def p_variable_assign_single(p):
    '''variable_assign : ID ASSIGN value SEMICOLON'''
    p[0] = VariableAssign(p[1], p[3])


def p_variable_assign_multiple(p):
    '''variable_assign : ID COMMA ID_set ASSIGN values_set SEMICOLON'''

    IDs = [p[1]] + p[3]
    p[0] = MultipleAssign(IDs, p[5])


def p_ID_set(p):
    '''ID_set : ID COMMA ID_set'''
    var = [p[1]] + p[3]
    p[0] = [p[1]] + p[3]

def p_ID_single(p):
    '''ID_set : ID'''
    p[0] = [p[1]]


def p_values_set(p):
    '''values_set : value COMMA values_set'''
    p[0] = [p[1]] + p[3]

def p_values_single(p):
    '''values_set : value'''
    p[0] = [p[1]]




#Manejo de indices
def p_index_access(p):
    '''index_access : ID index'''
    p[0] = p[1]


def p_index_assign_value(p):
    '''index_assign_value : BOOLEAN
                          | ID
                          | list '''
    p[0] = p[1]



def p_index_assign(p):
    '''index_assign : ID index ASSIGN index_assign_value SEMICOLON'''
    print("INDEX ASSIGN")
    print(type(p[2]))
    p[0] = IndexAssign(p[1],p[2],p[4])



def p_index_list(p):
    '''index : LSBRACKET index_type RSBRACKET'''
    print("LIST INDEX")

    p[0] = p[2]

def p_index_matrix(p):
    '''index :  LSBRACKET index_type RSBRACKET LSBRACKET index_type RSBRACKET '''
    print("MATRIX INDEX")

    p[0] = p[2]



def p_index_type(p):
    '''index_type : index_range
                  | index_pair
                  | index_column
                  | index_one'''

    p[0] = p[1]


def p_index_one(p):  
    '''index_one : INTEGER
                 | ID'''
    p[0] = IndexOne(p[1])
    

def p_index_range(p):
    '''index_range : index_value COLON index_value'''
    print("INDEX RANGE")
    p[0] = IndexRange(p[1], p[3])

def p_index_pair(p):
    '''index_pair : index_value COMMA index_value'''
    p[0] = IndexPair(p[1], p[2])

def p_index_column(p):
    '''index_column : COLON COMMA index_value'''
    p[0] = IndexColumn([3])


def p_index_value(p):
    '''index_value : ID 
                   | INTEGER'''

    p[0] = p[1]