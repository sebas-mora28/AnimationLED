import sys
sys.path.append("..")
from Sematic.SemanticError import *
from Sematic.SymbolTable.SymbolTable import *
from enum import Enum




class Instruction:

    def eval(self, program, symbolTable):
        pass


class Program:



    def __init__(self, expressions_set):
        self.expressions_set = expressions_set
        self.main = None
        self.semanticError = SemanticError()
        self.progrmaOutput = []
        self.output = []
        self.symbolTable = SymbolTable()


    def getErrors(self):
        return self.semanticError.errors

    def execute(self):
        main_count = 0 
        for expression in self.expressions_set:

            if(expression.ID == "Main"):
                main_count += 1
                if(expression.parameters == []):
                    self.main = expression
                    continue
                else:
                    semanticError.main_cannot_receive_parameters()
                    return
            print(expression.ID)
            expression.eval(self, self.symbolTable)

        if(main_count == 0):
            semanticError.main_not_found()
            return self.progrmaOutput
        if(main_count > 1):
            semanticError.main_multiple_definitions()
            return self.progrmaOutput

        else:
            self.main.eval(self, self.symbolTable)
            self.symbolTable.print()
            
    


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

        symbolProcedure = symbolTable.getProcedureByID(self.ID)

        if symbolProcedure:
            procedure = symbolProcedure.procedure
            if(isinstance(procedure, Procedure)):
                parameters = procedure.getParameters()
                if len(self.arguments) == len(parameters):
                    expressions = procedure.getExpressions()

                    for expression in expressions:
                        expression.eval(program, self.localsymbolTable)

                    self.localsymbolTable.print()

                else:
                    program.semanticError.number_of_arguments_not_match(self.ID)
            
            else:
                program.semanticError.call_procedure_error(self.ID)

        else:
            program.semanticError.symbol_procedure_not_found(self.ID)





class MainProcedure(Instruction):

    def __init__(self, ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions

    def eval(self, program, symbolTable):

        for expression in self.expressions:
            if expression:
                if isinstance(expression, VariableAssign) or isinstance(expression, MultipleAssign):
                    expression.scope = "global"
                
                expression.eval(program, symbolTable)
        pass



class VariableAssign(Instruction):

    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.scope = "local"
        self.type = type(value)

    def eval(self, program, symbolTable):
        print(f"Se asigna una variable {self.scope}")
    
        if(self.scope == "global"):
            self.assigment(program, program.symbolTable)
        
        else:
            self.assigment(program, symbolTable)
        

    def assigment(self, program, symbolTable):
        if(symbolTable.exist(self.ID)):
                old_value = symbolTable.getSymbolByID(self.ID)
                if(isinstance(old_value.value, self.type)):
                    symbolTable.changeSymbolValue(self.ID, self.value)
                else:
                    program.semanticError.incompatible_ariable_type(self.ID)            
        else:
            symbolTable.addSymbol(self.ID, self.value, self.type, self.scope)

     
        

class  MultipleAssign(Instruction):

    def __init__(self, IDs, values):
        self.IDs = IDs
        self.values = values
        self.scope = "local"

    

    def eval(self, program, symbolTable):

        if(len(self.IDs) == len(self.values)):

            for i in range(len(self.IDs)):

                if(self.scope == "global"):
                    self.assigment(program, program.symbolTable, self.IDs[i], self.values[i])
                
                else:
                    self.assigment(program, symbolTable, self.IDs[i], self.values[i])

        else:
            program.semanticError.multiple_variable_declaration()


    def assigment(self, program, symbolTable, ID, value):
        if(symbolTable.exist(ID)):
                old_value = symbolTable.getSymbolByID(ID)
                if(isinstance(old_value.value, type(value))):
                    symbolTable.changeSymbolValue(ID, value)
                else:
                    program.semanticError.incompatible_ariable_type(ID)            
        else:
            symbolTable.addSymbol(ID, value, type(value), self.scope)




def semantic_analysis(program):
    program.execute()
    return program
