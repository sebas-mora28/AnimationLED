import sys
sys.path.append("..")
from Lexical.lexer import *
from Syntax.syntax import * 

def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)
    res = systaxAnalysis(code, lexer)




file = open('example.txt', 'r')
compile(file.read())
file.close()