import sys
sys.path.append("..")
import yacc 
from Lexical.lexer import Lexer

class Syntax(object):

    def __init__(self, sourceCode):
        self.lexer= Lexer(); 
        self.sourceCode = sourceCode 
        self.tokens = self.lexer.tokens
        self.parser = yacc.yacc(module=self)

    def syntaxAnalysis(self):
        return self.parser.parse(self.sourceCode, self.lexer)


    def p_expression(self, p):
        '''expression : INTEGER 
                      | ID'''
        p[0] = p[1]


    def p_math_operation(self, p):
        '''expression : expression PLUS expression SEMICOLON
                      | expression MINUS expression SEMICOLON
                      | expression DIVIDE expression SEMICOLON
                      | expression DIVIDEENTIRE expression SEMICOLON
                      | expression TIMES expression SEMICOLON
                      | expression MODULE expression SEMICOLON'''

        p[0] = p[1] + p[3]



    def p_empty(self, p):
        '''empty : '''
        p[0] = None

    def p_error(self, p):
        print("Syntax error in input!")

