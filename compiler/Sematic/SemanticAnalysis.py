import sys
sys.path.append("..")
from Sematic.SemanticError import *
from Sematic.SymbolTable.SymbolTable import *
from enum import Enum


class Program:

    def __init__(self, expressions_set):
        self.expressions_set = expressions_set
        self.main = None
        self.semanticError = SemanticError()
        self.progrmaOutput = []
        self.output = []
        self.tableSymbol = SymbolTable()


    def execute(self):
        main_count = 0 
        for expression in self.expressions_set:
        
            if(expression.ID == "Main"):
                main_count += 1
                if(expression.parameters == []):
                    self.main = expression
                else:
                    self.semanticError.main_cannot_receive_parameters()

        if(main_count == 0):
            self.semanticError.main_not_found()
            return self.progrmaOutput
        if(main_count > 1):
            self.semanticError.main_multiple_definitions()
            return self.progrmaOutput
        
        else:
            self.main.solve(self)
    


class Procedure:

    def __init__(self,ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions
        self.local_symbol_table = SymbolTable()

        
    def getID(self):
        return self.ID
    
    def getParameters(self):
        return self.parameters

    def getExpression(self):
        return self.expression



class MainProcedure():

    def __init__(self, ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions

    def solve(self, program):

        for expression in self.expressions:
            if expression:
                print(expression)
                if isinstance(expression, VariableAssign):
                    expression.scope = "global"
                
                expression.solve(program)
        pass



class VariableAssign:

    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.scope = "local"
        self.type = type(value)

    
    def solve(self, program):
        print("Is" + str(isinstance(self.value, list)))

        pass



def semantic_analysis(program):
    program.execute()

