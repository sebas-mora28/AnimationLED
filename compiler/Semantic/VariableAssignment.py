import sys
sys.path.append("..")
from Semantic.IndexType import *
from Semantic.Common import *
from Semantic.BuiltInFunctions import *

class value(Instruction):

    def __init__(self, value):
        self.value = value


    def eval(self, ID, program, symbolTable, scope):


        if isinstance(self.value, int) or isinstance(self.value, bool) or isinstance(self.value, list):
            self.assignment(ID, program, symbolTable, scope)
 
        if(isinstance(self.value, str)):
            if symbolTable.exist(self.value):    
                    self.value = symbolTable.getSymbolByID(self.value).value
                    self.assignment(ID, program, symbolTable, scope)
            else:
                if program.symbolTable.exist(self.value):
                    self.value = program.symbolTable.getSymbolByID(self.value).value
                    self.assignment(ID, program, symbolTable, scope)
                else:
                    program.semanticError.addError(f"Semantic error: Symbol {ID} not found")
        
        if isinstance(self.value, matrixDimension):
            self.value = self.value.eval(program, symbolTable)
            if self.value != None:
                self.assignment(ID, program, symbolTable, scope)
     
            

    def assignment(self, ID, program, symbolTable, scope):
        if(symbolTable.exist(ID)):
                old_value = symbolTable.getSymbolByID(ID)
                if(isinstance(old_value.value, type(self.value))):
                    symbolTable.changeSymbolValue(ID, self.value)
                else:
                    program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}")          
        else:
            symbolTable.addSymbol(ID, self.value, type(self.value), scope)





class VariableAssign(Instruction):

    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.scope = "local"

    def eval(self, program, symbolTable):
        print(f"Se asigna una variable {self.scope}")
    
        if(self.scope == "global"):
            self.value.eval(self.ID, program, program.symbolTable, "global")

        else:
            self.value.eval(self.ID, program, symbolTable, "local")
    
    
class  MultipleAssign(Instruction):

    def __init__(self, IDs, values):
        self.IDs = IDs
        self.values = values
        self.scope = "local"


    def eval(self, program, symbolTable):

        if(len(self.IDs) == len(self.values)):

            for i in range(len(self.IDs)):

                if(self.scope == "global"):
                    self.values[i].eval(self.IDs[i], program, program.symbolTable, "global")
                
                else:
                    self.values[i].eval(self.IDs[i], program, symbolTable, "local")

        else:
            program.semanticError.addError(f"Semantic error: Invalid multiple variable assigment")





class IndexAssign(Instruction):

    def __init__(self, ID, index, value):
        self.ID = ID
        self.index = index
        self.value = value
        self.scope = "local"



    def eval(self,program, symbolTable):

        if(self.scope == "global"):
            self.assigment(program, program.symbolTable)
        
        else:
            self.assigment(program, symbolTable)

        

    def assigment(self, program, symbolTable):
        symbolVariable = searchSymbolByID(self.ID, program, symbolTable)
        if symbolVariable:
            if isinstance(self.index, IndexOne):
                i = self.index.eval(program, symbolTable)
                if i != None:
                    if isList(symbolVariable.value):
                        if verifyListBoundariesOne(i, symbolVariable):
                            self.value = self.value.eval(program, symbolTable)
                            if isinstance(self.value, bool):
                                symbolVariable.value[i] = self.value
                            else:
                                program.semanticError.addError(f"Semantic error: Invalid index assignment in {self.ID}, is not a bool")
                        else:
                            program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
                    
                    elif isMatrix(symbolVariable.value):
                        if verifyListBoundariesOne(i, symbolVariable):
                            self.value = self.value.eval(program, symbolTable)
                            if isinstance(self.value, list):
                                symbolVariable.value[i] = self.value 
                            else:
                                program.semanticError.addError(f"Semantic error: Invalid index assignment in {self.ID}, is not a list")
                        else:
                            program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
                    else:
                        program.semanticError.addError(f"Semantic error: {self.ID} is not a list or matrix")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index argument in {self.ID}")


            
            elif isinstance(self.index, IndexRange):
                i = self.index.eval(program, symbolTable)
                if i != None:
                    if isList(symbolVariable.value):
                        if verifyListBoundaries_2(i[0], i[1], symbolVariable):
                            self.value = self.value.eval(program, symbolTable)
                            if isinstance(self.value, list):
                                tem_len = i[1] - i[0]
                                if tem_len == len(self.value):
                                    symbolVariable.value[i[0]:i[1]] = self.value
                                
                                else:
                                    program.semanticError.addError(f"Semantic error: Invalid assigment in {self.ID}")

                            else:
                                program.semanticError.addError(f"Semantic error: Invalid index assignment in {self.ID}, is not a list")

                        else:
                            program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")

                    else:
                        program.semanticError.addError(f"Semantic error: {self.ID} is not a list")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index argument in {self.ID}")


        else:
            program.semanticError.addError(f"Semantic error: Variable {self.ID} not found")


                
            

            
        



