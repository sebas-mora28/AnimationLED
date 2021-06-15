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

        if program.symbolTable.existProcedure(self.ID):

            procedureSymbol = program.symbolTable.getProcedureByID(self.ID)

            if not self.existProcedureSign(procedureSymbol):

                program.symbolTable.addProcedureSymbol(self.ID, self)

            else:

                program.semanticError.sameProcedureSign(self.ID)
                
        else:

            program.symbolTable.addProcedureSymbol(self.ID, self)



    def existProcedureSign(self, procedureSymbol):

        for procedure in procedureSymbol.getProcedures():

                if len(self.parameters) == len(procedure.getParameters()):
                    return True
        
        return False

class CallProcedure(Instruction):

    def __init__(self, ID, arguments):
        self.ID = ID
        self.arguments = arguments
        self.localsymbolTable = SymbolTable()
    
    def eval(self, program, symbolTable):

        self.localsymbolTable.clean()
        symbolProcedure = program.symbolTable.getProcedureByID(self.ID)

        if symbolProcedure:

            procedure =  self.verifyProcedure(program, symbolProcedure.getProcedures())
            if procedure:

                parameters = procedure.getParameters()
                expressions = procedure.getExpressions()
                self.set_arguments(program, symbolTable, self.arguments, parameters)

                for expression in expressions:
                    
                    expression.eval(program, self.localsymbolTable)

                self.localsymbolTable.print()

            else:

                program.semanticError.procedureSignNotFound(self.ID, len(self.arguments))
                
        else:

            program.semanticError.procedureNotFound(self.ID)


    def verifyProcedure(self, program, procedureSymbol):

        for procedure in procedureSymbol:

            if len(self.arguments) == len(procedure.getParameters()):
                return procedure
        
        return None



    
    def set_arguments(self, program, symbolTable,  arguments, parameters):

        for i in range(len(parameters)):

            if not verifyType(arguments[i], str):
                self.localsymbolTable.addSymbol(parameters[i], arguments[i], type(arguments[i]), "local")

            else:
                symbol = searchSymbolByID(arguments[i], program, symbolTable)

                if symbol != None:

                    self.localsymbolTable.addSymbol(parameters[i], symbol.value, symbol.type, "local")

                else:

                    program.semanticError.symbolNotFound(self.ID)