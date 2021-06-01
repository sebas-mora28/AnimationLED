import sys 
sys.path.append("..")
from Semantic.Common import *


class Index:

    def checkIndexValues(self, ID, program, symbolTable):
         pass
    
    def getValuesFromIndex(self, ID, program, symbolTable):
        pass 

    def assignValue(self, ID, symbol, value, program, symbolTable):
        pass

    def isOutOfRange(self, index, symbolList, program, ID):
        if verifyListBoundariesOne(index, symbolList):
            return False 
        
        program.semanticError.indexOutRange(ID)
        return False





class IndexAccess:

    def __init__(self, index):
        self.index = index

    def getValues(self, program, symbolTable):
        return self.index.getValuesFromIndex(program, symbolTable)





class IndexPair(Index):

    def __init__(self, ID, index1, index2):
        self.ID = ID
        self.indexValue1 = index1
        self.indexValue2 = index2


    def checkIndexValues(self, program, symbolTable):
        self.indexValue1 = checkIndexValue(self.ID, self.indexValue1, program, symbolTable)
        self.indexValue2 = checkIndexValue(self.ID, self.indexValue2, program, symbolTable)

    
    def getValuesFromIndex(self, program, symbolTable):


        self.checkIndexValues(program, symbolTable)
        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.indexValue1 != None and self.indexValue2 != None:
                    if verifyListBoundaries_2(self.indexValue1, self.indexValue2, symbol.value):
                        return symbol.value[self.indexValue1][self.indexValue2]
                    else:
                        program.semanticError.indexOutRange(self.ID)
            else:
                program.semanticError.invalidIndexAccessMatrix(self.ID)
       

        
    def assignValue(self, value, program, symbolTable):  
           
            self.checkIndexValues(program, symbolTable)
            symbol = searchSymbolByID(self.ID, program, symbolTable)


            if self.indexValue1 != None and self.indexValue2 != None and symbol != None:
                if verifyListBoundaries_2(self.indexValue1, self.indexValue2, symbol.value):
                    if isMatrix(symbol.value):
                        if verifyType(value, bool):
                            symbol.value[self.indexValue1][self.indexValue2] = value
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    else:
                        program.semanticError.invalidIndexAccessMatrix(self.ID)
                else:
                    program.semanticError.indexOutRange(self.ID)
            else:
                program.semanticError.symbolNotFound(self.ID)






class IndexRange(Index):

    def __init__(self, ID, fromIndex , toIndex):
        self.ID = ID
        self.fromIndex = fromIndex 
        self.toIndex = toIndex
   


    def checkIndexValues(self, program, symbolTable):
        self.fromIndex = checkIndexValue(self.ID, self.fromIndex, program, symbolTable)
        self.toIndex = checkIndexValue(self.ID, self.toIndex, program, symbolTable)


    def getValuesFromIndex(self, program, symbolTable):

        self.checkIndexValues(program, symbolTable)

        symbol = searchSymbolByID(self.ID, program, symbolTable)
        if symbol != None:
            if isList(symbol.value):
                if self.fromIndex != None and self.toIndex != None:

                    if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                            return symbol.value[self.fromIndex:self.toIndex]
                    else:
                        program.semanticError.indexOutRange(self.ID)
            else:
                program.semanticError.invalidIndexAccessList(self.ID)
     


    def assignValue(self, value, program, symbolTable):

            symbol = searchSymbolByID(self.ID, program, symbolTable)
            self.checkIndexValues(program, symbolTable)

            if self.fromIndex != None and self.toIndex != None and symbol != None:
                if isList(symbol.value):
                    if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                        if verifyType(value, list):
                            if (self.toIndex - self.fromIndex) == len(value):
                                symbol.value[self.fromIndex:self.toIndex] = value
                            else:
                                program.semanticError.rangeInvalidListLength(self.ID)
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    else:
                        program.semanticError.indexOutRange(self.ID)
                else:
                    program.semanticError.invalidIndexAccessList(self.ID)
        

class IndexColumn(Index):

    def __init__(self, ID, columnIndex):
        self.ID = ID
        self.columnIndex = columnIndex
 

    def checkIndexValues(self, program, symbolTable):
            self.columnIndex = checkIndexValue(self.ID, self.columnIndex, program, symbolTable)

    def getValuesFromIndex(self, program, symbolTable):


        symbol = searchSymbolByID(self.ID, program, symbolTable)
        self.checkIndexValues(program, symbolTable)
    
        if symbol != None:
            if isMatrix(symbol.value):
                if self.columnIndex != None:
                    if verifyListBoundariesOne(self.columnIndex, symbol.value[0]):
                            return getColumn(self.columnIndex, symbol.value)
                    else:
                        program.semanticError.indexOutRange(self.ID)
            else:
                program.semanticError.invalidIndexAccessMatrix(self.ID)
          




    def assignValue(self, value, program, symbolTable):

            symbol = searchSymbolByID(self.ID, program, symbolTable)
            self.checkIndexValues(program,symbolTable)

            print(self.columnIndex and symbol)

            if self.columnIndex != None and symbol != None:
                if isMatrix(symbol.value):
                    if verifyListBoundariesOne(self.columnIndex, symbol.value[0]):
                            if verifyType(value, list):
                                symbol.value = setColumn(self.columnIndex, symbol.value, value)
                            else:
                                program.semanticError.incompatibleType(self.ID)
                    else:
                        program.semanticError.indexOutRange(self.ID)
                else:
                    program.semanticError.invalidIndexAccessMatrix(self.ID)



 
class IndexOne(Index):
        def __init__(self, ID, index):
            self.ID = ID
            self.indexValue = index

        def checkIndexValues(self, program, symbolTable):
            self.indexValue = checkIndexValue(self.ID, self.indexValue, program, symbolTable)


        def getValuesFromIndex(self,  program, symbolTable):

            self.checkIndexValues(program, symbolTable)
            symbol = searchSymbolByID(self.ID, program, symbolTable)


            if symbol != None:
                if isList(symbol.value) or isMatrix(symbol.value):
                    if self.indexValue != None:
                        if verifyListBoundariesOne(self.indexValue, symbol.value):
                            return symbol.value[self.indexValue]
                        else:
                            program.semanticError.indexOutRange(self.ID)
                else:
                    program.semanticError.invalidIndexAccess(self.ID)
         



        def assignValue(self, value, program, symbolTable):

            symbol = searchSymbolByID(self.ID, program, symbolTable)
            self.checkIndexValues(program, symbolTable)
    
            if self.indexValue != None and symbol != None:
                if verifyListBoundariesOne(self.indexValue, symbol.value):
                    if isList(symbol.value):
                        if verifyType(value, bool):
                                symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    elif isMatrix(symbol.value):
                        if verifyType(value, list):
                            symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    else:
                        program.semanticError.invalidIndexAccess(self.ID)
                else:
                    program.semanticError.indexOutRange(self.ID)
            
                    

        
            



