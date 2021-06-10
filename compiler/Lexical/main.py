import sys
sys.path.append("..")
from Lexical.Lexer import *
from Syntax.Syntax import * 
from Semantic.SemanticAnalysis import *
from Lexical.Traductor import*




def compile(code):
    print(code)
    lexer = Lexer()
    lexer.lexicalAnalysis(code)


    if(lexer.errors == []): #Erorres en el analisis de lexico 
        res = systaxAnalysis(code, lexer)
        if syntaxError.getErrors()== []:
            program = semantic_analysis(res)
            if program.getErrors() != []:
                return program.getErrors()
                #program.semanticError.printErrors() #comentar
            else:
                trad = Traductor(program.programOutput)
                print("\n output: "+ trad.Traducir())
                return ["Archivo compilado con exito!!"]

        else:
            return syntaxError.getErrors()
            #for i in range(len(syntaxErorrs)): # comentar
            #    print(syntaxErorrs[i])

    else:
        return lexer.errors
        #for i in range(len(lexer.errors)): #comentar
        #        print(lexer.errors[i])


#file = open('example.txt', 'r')
#compile(file.read())