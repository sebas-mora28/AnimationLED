from copy import deepcopy
import sys
sys.path.append("..")
from Semantic.IndexType import *
from Semantic.Common import *
from Semantic.ListFunctions import *



class value(Instruction):

    def __init__(self, value):
        self.value = value


    def eval(self, ID, program, symbolTable, scope):

        if isinstance(self.value, int) or isinstance(self.value, bool) or isinstance(self.value, list):
            self.assignment(ID, program, symbolTable, scope)
 
        if(isinstance(self.value, str)):
            symbol = searchSymbolByID(self.value, program, symbolTable)
            if symbol != None:
                self.value = symbol.value
                self.assignment(ID, program, symbolTable, scope)

        if isinstance(self.value, MatrixDimension):
            self.value = self.value.eval(program, symbolTable)
            if self.value != None:
                self.assignment(ID, program, symbolTable, scope)
    
        if isinstance(self.value, Len):
            self.value = self.value.eval(program, symbolTable)
            if self.value != None:
                self.assignment(ID, program, symbolTable, scope)
        
        if isinstance(self.value, Range):
            self.value = self.value.eval(program, symbolTable)
            if self.value != None:
                self.assignment(ID, program, symbolTable, scope)

        if isinstance(self.value, IndexAccess):
            self.value = self.value.getValues(program, symbolTable)
            if self.value != None:
                self.assignment(ID, program, symbolTable, scope)
            

    def assignment(self, ID, program, symbolTable, scope):
        if(symbolTable.exist(ID)):
                old_value = symbolTable.getSymbolByID(ID)
                if isinstance(old_value.value, type(self.value)):
                    symbolTable.changeSymbolValue(ID, self.value)
                else:
                    program.semanticError.invalidSymbolType(ID)        
        else:
            symbolTable.addSymbol(ID, self.value, type(self.value), scope)





class VariableAssign(Instruction):

    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.scope = "local"

    def eval(self, program, symbolTable):
    
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
            program.semanticError.invalidMultipleAssignment()






class IndexValue:

    def __init__(self, value):
        self.value = value

    
    def eval(self, program, symbolTable):

        if isinstance(self.value, str):
            symbol = searchSymbolByID(self.value, program, symbolTable)
            if symbol:
                return symbol.value


        if isinstance(self.value, bool) or isinstance(self.value, list):
            return self.value

        if isinstance(self.value, IndexAccess):
            return self.value.getValues(program, symbolTable)
        
        return None 


class IndexAssign(Instruction):

    def __init__(self, ID, index, value):
        self.ID = ID    
        self.index = index
        self.value = value
        self.scope = "local"


    def eval(self, program, symbolTable):

        if(self.scope == "global"):
            self.assignment(program, program.symbolTable)
        
        else:
            self.assignment(program, symbolTable)


    def assignment(self, program, symbolTable):



        self.value = self.value.eval(program, symbolTable)
  
        symbol = searchSymbolByID(self.ID, program, symbolTable)
        if symbol != None:
            self.index.assignValue(self.ID, symbol, self.value, program, symbolTable)

        else:
            program.semanticError.symbolNotFound(self.ID)


 


