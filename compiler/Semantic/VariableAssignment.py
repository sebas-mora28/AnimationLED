from copy import deepcopy
import sys
sys.path.append("..")
from Semantic.IndexType import *
from Semantic.Common import *
from Semantic.ListFunctions import *
from Semantic.ArithmeticOperation import *


class value(Instruction):

    def __init__(self, value):
        self.value = value


    def eval(self, ID, program, symbolTable, scope):
        if verifyType(self.value, int) or verifyType(self.value, bool):
            self.assignment(ID, self.value, program, symbolTable, scope)
 
        elif verifyType(self.value, list):
            if isList(self.value):
                self.value = verifyListValueList(self.value, program, symbolTable)
                if self.value != None:
                    self.assignment(ID, self.value, program, symbolTable, scope)
            elif isMatrix(self.value):
                self.value = verifyListValueMatrix(self.value, program, symbolTable)
                if self.value != None:
                    self.assignment(ID, self.value, program, symbolTable, scope)

        elif verifyType(self.value, str):
            symbol = searchSymbolByID(self.value, program, symbolTable)
            if symbol != None:
                self.assignment(ID, symbol.value, program, symbolTable, scope)
          
        elif verifyType(self.value, MatrixDimension):
            value = self.value.eval(program, symbolTable)
            if value != None:
                self.assignment(ID, value, program, symbolTable, scope)
    
        elif verifyType(self.value, Len):
            value = self.value.eval(program, symbolTable)
            if value != None:
                self.assignment(ID, value,program, symbolTable, scope)
        
        elif verifyType(self.value, Range):
            value = self.value.eval(program, symbolTable)
            if value != None:
                self.assignment(ID, value, program, symbolTable, scope)

        elif verifyType(self.value, IndexAccess):
            value = self.value.getValues(program, symbolTable)
            if value != None:
                self.assignment(ID, value, program, symbolTable, scope)
        
        elif verifyType(self.value, ArithmeticOperation):
            value = self.value.eval(program, symbolTable)
            if value != None:
                self.assignment(ID, value, program, symbolTable, scope)

        elif verifyType(self.value, MathValueNegative):
            value = self.value.eval(program, symbolTable)
            if value != None:
                self.assignment(ID, int(value), program, symbolTable, scope)
        
    def assignment(self, ID, value, program, symbolTable, scope):
        if(symbolTable.exist(ID)):
                old_value = symbolTable.getSymbolByID(ID)
                if verifyType(old_value.value, type(value)):
                    symbolTable.changeSymbolValue(ID, value)
                else:
                    program.semanticError.invalidSymbolType(ID)        
        else:
            symbolTable.addSymbol(ID, value, type(value), scope)





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

        if verifyType(self.value, str):
            symbol = searchSymbolByID(self.value, program, symbolTable)
            if symbol:
                return symbol.value
        elif verifyType(self.value, IndexAccess):
            return self.value.getValues(program, symbolTable)
        
        else:
            return self.value 


class IndexAssign(Instruction):

    def __init__(self, index, value):
        self.ID = index.ID 
        self.index = index
        self.value = value
        self.scope = "local"
      

    def eval(self, program, symbolTable):

        if(self.scope == "global"):
            self.assignment(program, program.symbolTable)
        
        else:
            self.assignment(program, symbolTable)


    def assignment(self, program, symbolTable):
        evaluatedValue = self.value.eval(program, symbolTable)
    
       

        self.index.assignValue(evaluatedValue, program, symbolTable)


 


