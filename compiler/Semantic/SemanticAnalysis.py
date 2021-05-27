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
                    program.semanticError.addError(f"Semantic error: Expect { len(procedure.getParameters())} arguments given {len(self.arguments)}")
            
            else:
                program.semanticError.addError(f"Semantic error: {self.ID} is not a procedure")

        else:
            program.semanticError.addError(f"Semantic error: Procedure {self.ID} not found")





class MainProcedure(Instruction):

    def __init__(self, ID, parameters, expressions):
        self.ID = ID
        self.parameters = parameters
        self.expressions = expressions

    def eval(self, program, symbolTable):

        for expression in self.expressions:
            if expression:
                if isinstance(expression, VariableAssign) or isinstance(expression, MultipleAssign) or isinstance(expression, IndexAssign):
                    expression.scope = "global"
                
                expression.eval(program, symbolTable)
        pass





def semantic_analysis(program):
    program.execute()
    return program
