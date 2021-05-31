import sys 
sys.path.append("..")

from Semantic.Common import *
from Semantic.SymbolTable.SymbolTable import *


class Procedure(Instruction):

    def __init__(self,ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions
    
    def getID(self):
        return self.ID
    
    def getParameters(self):
        return self.parameters

    def getExpressions(self):
        return self.expressions

    def eval(self, program, symbolTable):
        symbolTable.addProcedureSymbol(self.ID, self)
        



class CallProcedure(Instruction):

    def __init__(self, ID, arguments):
        self.ID = ID
        self.arguments = arguments
        self.localsymbolTable = SymbolTable()
    
    def eval(self, program, symbolTable):

        symbolProcedure = program.symbolTable.getProcedureByID(self.ID)

        if symbolProcedure:
            procedure = symbolProcedure.procedure

            if(isinstance(procedure, Procedure)):
            
                parameters = procedure.getParameters()

                if len(self.arguments) == len(parameters):

                    expressions = procedure.getExpressions()

                    self.set_arguments(program, symbolTable, self.arguments, parameters)

                    for expression in expressions:

                        expression.eval(program, self.localsymbolTable)

                    self.localsymbolTable.print()

                else:
                    program.semanticError.invalidAmountOfParameters(len(procedure.getParameters()), len(self.arguments))
            else:
                program.semanticError.isNotAProcedure(self.ID)

        else:
            program.semanticError.procedureNotFound(self.ID)

    
    def set_arguments(self, program, symbolTable,  arguments, parameters):

        for i in range(len(parameters)):

            if not isinstance(arguments[i], str):
                self.localsymbolTable.addSymbol(parameters[i], arguments[i], type(arguments[i]), "local")

            else:
                symbol = searchSymbolByID(arguments[i], program, symbolTable)

                if symbol != None:

                    self.localsymbolTable.addSymbol(parameters[i], symbol.value, symbol.type, "local")

                else:
                    program.semanticError.symbolNotFound(self.ID)