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
            print(self.value)
            self.value = getValuesFromIndex(self.value.ID, self.value.index, program, symbolTable)
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






class IndexValue:

    def __init__(self, value):
        self.value = value

    
    def eval(self, ID, program, symbolTable, scope):

        pass







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




    def evalValue(self):

        if isinstance(self.value, Index):
            return getValuesFromIndex(self.value)
        if isinstance(self.value, str):
            symbol = searchSymbolByID(self.value)
            if symbol != None:
                return symbol.value 
            return None
        else:
            return self.value


    def assignment(self, program, symbolTable):

    
       symbol = searchSymbolByID(self.ID, program, symbolTable)

       print(symbol.value)

       if symbol != None:
           if isinstance(self.value, IndexOne):
               if isList(symbol.value):
                   self.value = self.evalValue()
                   if isinstance(self.value, bool):
                       symbol.value[self.index.IndexValue] = self.value 


 


