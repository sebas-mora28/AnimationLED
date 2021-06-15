import sys 
sys.path.append("..")
from Semantic.Common import * 
from Semantic.IndexType import *

class MatrixDimension(Instruction):

    def __init__(self, ID, dimension):
        self.ID = ID
        self.dimension = dimension

    
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:

            if isMatrix(symbol.value):

                if self.dimension == ".shapeF":
                    return len(symbol.value)
                
                if self.dimension == ".shapeC":
                    return len(symbol.value[0])

            else:
                program.semanticError.isNotAMatrix(self.ID)
    




class ListInsert(Instruction):

    def __init__(self, ID, index, value):
        self.ID = ID
        self.index = index
        self.value = value
    
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:

            if isList(symbol.value):

                if self.index <= len(symbol.value):

                    if verifyType(self.value, bool):

                        symbol.value.insert(self.index, self.value)

                    else:

                        program.semanticError.incompatibleType(self.ID)

                else:

                    program.semanticError.insertIndexOutRange(self.ID)

            else:

                program.semanticError.insertListProcedureError(self.ID)


class ListDelete(Instruction):

    def __init__(self, ID, index):
        self.ID = ID
        self.index = index
    
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:

            if isList(symbol.value):

                if self.index < len(symbol.value):

                    symbol.value.pop(self.index)

                else:

                    program.semanticError.deleteIndexOutRange(self.ID)

            else:

                program.semanticError.deleteListProcedureError(self.ID)
    



class MatrixInsert(Instruction):

    def __init__(self, ID, value, insertionType, index):
        self.ID = ID
        self.value = value 
        self.insertionType = insertionType
        self.index = index
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:

            if isMatrix(symbol.value):

                if self.insertionType == 1 or self.insertionType == 0:

                    if verifyType(self.value, list):

                            if self.insertionType == 0:

                                self.insertRow(symbol, program)
        

                            elif self.insertionType == 1:

                                self.insertColumn(symbol, program)

                    else:

                        program.semanticError.insertMatrixProcedureInvalidArguments(self.ID)

                else:

                    program.semanticError.insertMatrixProcedureInvalidArguments(self.ID)
            else:
                
                program.semanticError.insertMatrixProcedureError(self.ID)





    def insertColumn(self, symbol, program):
        if len(self.value) == len(symbol.value):
                if self.index == None:
                    for i in range(len(symbol.value)):
                        symbol.value[i].append(self.value[i][0])
                else:
                    if self.index <= len(symbol.value[0]):
                        for i in range(len(symbol.value)):
                            symbol.value[i].insert(self.index, self.value[i][0])
                    else:
                        program.semanticError.insertIndexOutRange(self.ID)
        else:
            program.semanticError.invalidDimensions(self.ID)


        
    def insertRow(self, symbol, program):


            if len(self.value[0]) == len(symbol.value[0]):
                if self.index == None:
                    symbol.value.append(self.value[0])
                else:
                    if self.index <= len(symbol.value):
                        symbol.value.insert(self.index, self.value[0])
                    else:
                        program.semanticError.insertIndexOutRange(self.ID)
            else:
                program.semanticError.invalidDimensions(self.ID)




class MatrixDelete(Instruction):

    def __init__(self, ID, index, eliminationType):
        self.ID = ID 
        self.index = index
        self.eliminationType = eliminationType

    

    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if verifyType(self.index, int) and verifyType(self.eliminationType, int):

                    if self.eliminationType == 0:
                        self.deleteRow(symbol, program)

                    elif self.eliminationType == 1:
                        self.deletColumn(symbol, program)
                else:
                    program.semanticError.insertMatrixProcedureInvalidArguments(self.ID)
            else:
                program.semanticError.deleteMatrixProcedureError(self.ID)
   

    
    def deleteRow(self, symbol, program):
        if self.index < len(symbol.value):
                symbol.value.pop(self.index)
        else:
            program.semanticError.deleteIndexOutRange(self.ID)

    def deletColumn(self, symbol, program):
        if self.index < len(symbol.value[0]):
            for i in range(len(symbol.value)):
                symbol.value[i].pop(self.index)
        else:
            program.semanticError.deleteIndexOutRange(self.ID)
        




class Len(Instruction):
    def __init__(self, ID):
        self.ID = ID

    def eval(self, program, symbolTable):
        symbol = searchSymbolByID(self.ID, program, symbolTable)
        if symbol != None:
            if isList(symbol.value) or isMatrix(symbol.value):
                return len(symbol.value) 
            else:
                program.semanticError.lenInvalidArgument(self.ID)
       



class Range(Instruction):

    def __init__(self, list_size, value):
        self.list_size = list_size
        self.value = value

    def eval(self, program, symbolTable):
        if verifyType(self.list_size, int) or verifyType(self.value, bool):
                return [self.value] * self.list_size
        else:
            program.semanticError.rangeInvalidArguments()



class BooleanOperationIndex(Instruction):

    def __init__(self, index_type, operation):
        
      
        self.ID = index_type.ID
        self.index_type = index_type
        self.operation = operation
    
    def eval(self, program, symbolTable):
          
        
            if self.operation == "T":
                value = self.booleanOperator(True, program, symbolTable)
                if value != None:
                    self.index_type.assignValue(value, program, symbolTable)

            if self.operation == "F":
                value = self.booleanOperator(False, program, symbolTable)
                if value != None:
                    self.index_type.assignValue(value, program, symbolTable)
                
            if self.operation == "Neg":
                value = self.notOperator(program, symbolTable)
                if value != None:
                    self.index_type.assignValue(self.notOperator(program, symbolTable), program, symbolTable)


    def booleanOperator(self, boolValue, program, symbolTable):


        if isinstance(self.index_type, IndexOne):

            ID = self.index_type.ID
            symbol = searchSymbolByID(ID, program, symbolTable)
    
           
            if symbol != None:
                
                if isList(symbol.value):
                    return boolValue
                
                elif isMatrix(symbol.value):

                    value = self.index_type.getValuesFromIndex(program, symbolTable)

                    if value != None:

                        return [boolValue]*len(value)

                else:
                     program.semanticError.invalidIndexAccess(ID)



        elif isinstance(self.index_type, IndexPair):
            return boolValue 
        
        elif isinstance(self.index_type, IndexRange):
            value = self.index_type.getValuesFromIndex(program, symbolTable)
            
            if value != None:
                return [boolValue]*len(value)

        elif isinstance(self.index_type, IndexColumn):
            value = self.index_type.getValuesFromIndex(program, symbolTable)
            if value != None:
                return [boolValue]*len(value)



    def notOperator(self, program, symbolTable):
        value = self.index_type.getValuesFromIndex(program, symbolTable)
        if value != None:
            if isinstance(self.index_type, IndexOne) or isinstance(self.index_type, IndexPair):
                return not(value)
        
            if isinstance(self.index_type, IndexRange) or isinstance(self.index_type, IndexColumn):
                res = []
                for i in range(len(value)):
                    res.insert(i, not(value[i]))
                return res
            
    

class BooleanOperation(Instruction):

    def __init__(self, ID, operation):
        
        self.ID = ID
        self.operation = operation

    

    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)


        if self.operation == "T":
            self.booleanOperator(True, symbol, program)
    
        elif self.operation == "F":
            self.boolOperator(False, symbol, program)

        elif self.operation == "Neg":
            self.notOperator(symbol, program)

    def boolOperator(self, boolValue, symbol, program):
        if isList(symbol.value):
            for i in range(len(symbol.value)):
                symbol.value[i] = boolValue

        elif isMatrix(symbol.value):

            for i in range(len(symbol.value)):
                for j in range(len(symbol.value[i])):
                    symbol.value[i][j] = boolValue

        else:
            program.semanticError.booleanOperatorError(self.ID)

    def notOperator(self, symbol, program):
     
        if isList(symbol.value):
            for i in range(len(symbol.value)):
                symbol.value[i] = not(symbol.value[i])

        elif isMatrix(symbol.value):

            for i in range(len(symbol.value)):
                for j in range(len(symbol.value[i])):
                    symbol.value[i][j] = not(symbol.value[i][j])
        else:
            program.semanticError.booleanOperatorError(self.ID)