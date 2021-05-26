import sys
sys.path.append("..")
from Lexical.lexer import *
from Syntax.syntax import * 
from Sematic.SemanticAnalysis import *

def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)
    res = systaxAnalysis(code, lexer)

    if erorrs == []:
        program = semantic_analysis(res)
        if program.getErrors() != []:
            program.semanticError.printErrors()

    else:
        for i in range(len(erorrs)):
            print(erorrs[i])

file = open('example.txt', 'r')
compile(file.read())
file.close()