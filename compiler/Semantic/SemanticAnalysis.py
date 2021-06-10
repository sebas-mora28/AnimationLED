import sys
sys.path.append("..")
from Semantic.SemanticError import *
from Semantic.SymbolTable.SymbolTable import *
from Semantic.IndexType import * 
from Semantic.VariableAssignment import * 
from Semantic.Common import *

class Program:

    def __init__(self, expressions_set):
        self.expressions_set = expressions_set
        self.main = None
        self.semanticError = SemanticError()
        self.programOutput = []
        self.symbolTable = SymbolTable()


    def getErrors(self):
        return self.semanticError.errors

    def isEmpty(self):
        return self.expressions_set[0] == None


    def execute(self):
        main_count = 0 
        if not self.isEmpty():
            for expression in self.expressions_set:
                if expression != None:
                    if(expression.ID == "Main"):
                        main_count += 1
                        if(expression.parameters == []):
                            self.main = expression
                            continue
                        else:
                            self.semanticError.mainCannotReceiveParameter()
                            return
                    expression.eval(self, self.symbolTable)

        if(main_count == 0):
            self.semanticError.mainNotFound()
            return 
        if(main_count > 1):
            self.semanticError.mainMultipleDefinition()
            return 

        else:
            self.main.eval(self, self.symbolTable)
            print("\n----- GLOBAL ----------\n")
            self.symbolTable.print()
            
    





class MainProcedure(Instruction):

    def __init__(self, ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions

    def eval(self, program, symbolTable):

        for expression in self.expressions:
            if expression:
            
                if verifyType(expression, VariableAssign) or verifyType(expression, MultipleAssign) or verifyType(expression, IndexAssign):
                    expression.scope = "global"
                
                expression.eval(program, symbolTable)
    





def semantic_analysis(program):
    program.execute()
    return program
