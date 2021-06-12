import sys
sys.path.append("..")
from Semantic.SemanticAnalysis import *
from Semantic.IndexType import *
from Semantic.Common import *

def p_value(p):
    '''value : INTEGER 
              | BOOLEAN 
              | ID
              | list
              | len
              | range
              | matrix_dimensions 
              | arithmetic
              | math_value_negative
              | index_access '''
    
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


def p_index_assign(p):
     '''index_assign : index_type ASSIGN index_assign_value SEMICOLON'''
     print("INDEX ASSIGN")
     p[0] = IndexAssign(p[1],p[3])


def p_index_access(p):
     '''index_access : index_type'''
     print("INDEX ACCESS")
     p[0] = IndexAccess(p[1])


def p_index_one(p):
    '''index_one : ID LSBRACKET index_value RSBRACKET'''
    print("INDEX ONE")
    p[0] = IndexOne(p[1], p[3])


def p_index_matrix(p):
     '''index_matrix : ID LSBRACKET index_value RSBRACKET LSBRACKET index_value RSBRACKET'''
     print("MATRIX INDEX")
     p[0] = IndexPair(p[1], p[3],p[6])


def p_index_range(p):
    '''index_range : ID LSBRACKET index_value COLON index_value RSBRACKET'''
    print("INDEX RANGE")
    p[0] = IndexRange(p[1],p[3],p[5])


def p_index_pair(p):
    '''index_pair : ID LSBRACKET index_value COMMA index_value RSBRACKET'''
    print("INDEX PAIR")
    p[0] = IndexPair(p[1],p[3],p[5])


def p_index_column(p):
    '''index_column : ID LSBRACKET COLON COMMA index_value RSBRACKET '''
    print("INDEX COLUMN")
    p[0] = IndexColumn(p[1], p[5])


def p_index_type(p):
     '''index_type : index_matrix
                   | index_one
                   | index_pair
                   | index_range
                   | index_column'''

     p[0] = p[1]

def p_index_value(p):
     '''index_value : ID 
                    | INTEGER'''

     p[0] = p[1]



def p_index_assign_value(p):
     '''index_assign_value : INTEGER 
                             | BOOLEAN 
                             | ID
                             | list
                             | len
                             | range
                             | matrix_dimensions 
                             | math_operation
                             | index_access'''
     p[0] = IndexValue(p[1])
