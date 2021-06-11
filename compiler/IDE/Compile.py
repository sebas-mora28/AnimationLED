import sys
sys.path.append("..")
from Lexical.Lexer import *
from Syntax.Syntax import * 
from Semantic.SemanticAnalysis import *
from Traductor import *



#Funcion que compila y ejecuta el codigo
def run(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)


    if(lexer.errors == []): #Erorres en el analisis de lexico 
        res = systaxAnalysis(code, lexer)
        if syntaxError.getErrors()== []:
            program = semantic_analysis(res)
            if program.getErrors() != []:
                return program.getErrors()
            else:
                trad = Traductor(program.programOutput) #Hace la traduccion del codigo
                print("\n output: "+ trad.Traducir()) # agregar la funcion de envio
                return ["Archivo compilado con exito!!"]

        else:
            return syntaxError.getErrors()

    else:
        return lexer.errors
#Funcion que compila el programa pero no lo ejecuta    
def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)


    if(lexer.errors == []): #Erorres en el analisis de lexico 
        res = systaxAnalysis(code, lexer)
        if syntaxError.getErrors()== []:
            program = semantic_analysis(res)
            if program.getErrors() != []:
                return program.getErrors()
            else:
                return ["Archivo compilado con exito!!"]

        else:
            return syntaxError.getErrors()

    else:
        return lexer.errors