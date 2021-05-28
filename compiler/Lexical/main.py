import sys
sys.path.append("..")
from Lexical.Lexer import *
from Syntax.Syntax import * 
from Semantic.SemanticAnalysis import *

def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)


    if(lexer.errors == []): #Erorres en el analisis de lexico 
        res = systaxAnalysis(code, lexer)
        if syntaxErorrs == []:
            program = semantic_analysis(res)
            if program.getErrors() != []:
                program.semanticError.printErrors()

        else:
            for i in range(len(syntaxErorrs)):
                print(syntaxErorrs[i])

    else:
        for i in range(len(lexer.errors)):
                print(lexer.errors[i])

file = open('example.txt', 'r')
compile(file.read())
file.close()