import sys
sys.path.append("..")
from Lexical.lexer import *
from Syntax.syntax import * 
from Sematic.SemanticAnalysis import *

def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)
    res = systaxAnalysis(code, lexer)
    semantic_analysis(res)



file = open('example.txt', 'r')
compile(file.read())
file.close()