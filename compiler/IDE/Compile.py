import sys
sys.path.append("..")
from Lexical.Lexer import *
from Syntax.Syntax import * 
from Semantic.SemanticAnalysis import *
from Traductor import *
from Comunicacion import *




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
                #program.semanticError.printErrors()
                
            else:
                trad = Traductor(program.programOutput) #Hace la traduccion del codigo
                abrir()
                enviar(trad.Traducir())
                cerrar()
                print(trad.output)
                print("\n output: "+ trad.Traducir()) # agregar la funcion de envio
                program.getPrints().insert(0, "Archivo compilado con exito !!")
                return program.getPrints()
                #pass

        else:
            #for i in range(len(syntaxError.getErrors())):
            #    print(syntaxError.getErrors()[i])
            return syntaxError.getErrors()

    else:
        #for i in range(lexer.errors):
        #        print(lexer.errors[i])
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
                program.getPrints().insert(0, "Archivo compilado con exito !!")
                return program.getPrints()

        else:
            return syntaxError.getErrors()

    else:
        return lexer.errors


#file = open("example.txt", 'r')
#run(file.read())
