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
        
        program.semanticError.indexOutOfRange(self.ID)
        return False





class IndexAccess:

    def __init__(self, ID, index):
        self.ID = ID
        self.index = index

    def getValues(self, program, symbolTable):
        return self.index.getValuesFromIndex(self.ID, program, symbolTable)


class IndexPair(Index):

    def __init__(self, index1, index2):
        self.indexValue1 = index1
        self.indexValue2 = index2


    def checkIndexValues(self, ID, program, symbolTable):
        self.indexValue1 = checkIndexValue(ID, self.indexValue1, program, symbolTable)
        self.indexValue2 = checkIndexValue(ID, self.indexValue2, program, symbolTable)

    
    def getValuesFromIndex(self, ID, program, symbolTable):


        self.checkIndexValues(ID, program, symbolTable)
        symbol = searchSymbolByID(ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.indexValue1 != None and self.indexValue2 != None:
                    if verifyListBoundaries_2(self.indexValue1, self.indexValue2, symbol.value):
                        return symbol.value[self.indexValue1][self.indexValue2]
                    else:
                        program.semanticError.indexOutOfRange(self.ID)
            else:
                program.semanticError.invalidIndexAccessMatrix(self.ID)
        else:
            program.semanticError.symbolNotFound(self.ID)

        
    def assignValue(self, ID, symbol, value, program, symbolTable):  
           
            self.checkIndexValues(ID, program, symbolTable)

            if self.indexValue1 != None and self.indexValue2 != None:
                if verifyListBoundaries_2(self.indexValue1, self.indexValue2, symbol.value):
                    if isMatrix(symbol.value):
                        if isinstance(value, bool):
                            symbol.value[self.indexValue1][self.indexValue2] = value
                        else:
                            program.semanticError.incompatibleType(ID)
                    else:
                        program.semanticError.invalidIndexAccessList(ID)
                else:
                    program.semanticError.indexOutOfRange(ID)
            else:
                program.semanticError.symbolNotFound(ID)






class IndexRange(Index):

    def __init__(self, fromIndex , toIndex):
        self.fromIndex = fromIndex 
        self.toIndex = toIndex
   


    def checkIndexValues(self, ID, program, symbolTable):
        self.fromIndex = checkIndexValue(ID, self.fromIndex, program, symbolTable)
        self.toIndex = checkIndexValue(ID, self.toIndex, program, symbolTable)


    def getValuesFromIndex(self, ID,  program, symbolTable):

        self.checkIndexValue(ID, program, symbolTable)

        symbol = searchSymbolByID(ID, program, symbolTable)
        if symbol != None:
            if isList(symbol.value):
                if self.fromIndex != None and self.toIndex != None:

                    if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                            return symbol.value[self.fromIndex:self.toIndex]
                    else:
                        program.semanticError.indexOutOfRange(ID)
            else:
                program.semanticError.invalidIndexAccessList(ID)
        else:
            program.semanticError.symbolNotFound(ID)


    def assignValue(self, ID, symbol, value, program, symbolTable):

            
            self.checkIndexValues(ID, program, symbolTable)

            if self.fromIndex != None and self.toIndex != None:
                if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                    if isList(symbol.value):
                        if isinstance(value, list):
                            symbol.value[self.fromIndex:self.toIndex] = value
                        else:
                            program.semanticError.incompatibleType(ID)
                    else:
                        program.semanticError.invalidIndexAccessList(ID)
                else:
                    program.semanticError.indexOutOfRange(ID)
            else:
                program.semanticError.symbolNotFound(ID)


class IndexColumn(Index):

    def __init__(self, column):
        self.column = column
 

    def checkIndexValues(self, ID, program, symbolTable):
            self.column = checkIndexValue(ID, self.indexValue, program, symbolTable)

    def getValuesFromIndex(self, ID, program, symbolTable):

        symbol = searchSymbolByID(ID, program, symbolTable)

        self.checkIndexValues(ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.column != None:
                    if verifyListBoundariesOne(self.column, symbol.value[0]):
                            return getColumn(self.column, symbol.value)
                    else:
                        program.semanticError.indexOutOfRange(ID)
            else:
                program.semanticError.invalidIndexAccessMatrix(ID)
        else:
            program.semanticError.symbolNotFound(ID)
            

    def assignValue(self, ID, symbol, value, program, symbolTable):

            self.column = checkIndexValue(ID, self.column, program, symbolTable)
            if self.column != None:
                if verifyListBoundariesOne(self.column, symbol.value[0]):
                    if isMatrix(symbol.value):
                        if isinstance(value, list):
                            print(value)
                            symbol.value[self.column] = value
                        else:
                            program.semanticError.incompatibleType(ID)
                    else:
                        program.semanticError.invalidIndexAccessMatrix(ID)
                else:
                    program.semanticError.indexOutOfRange(ID)
            else:
                program.semanticError.symbolNotFound(ID)



 
class IndexOne(Index):
        def __init__(self, index):
            self.indexValue = index

        def checkIndexValues(self, ID, program, symbolTable):
            self.indexValue = checkIndexValue(ID, self.indexValue, program, symbolTable)


        def getValuesFromIndex(self, ID,  program, symbolTable):

            self.checkIndexValues(ID, program, symbolTable)


            symbol = searchSymbolByID(ID, program, symbolTable)
            if symbol != None:
                if isList(symbol.value) or isMatrix(symbol.value):
                    if self.indexValue != None:
                        if verifyListBoundariesOne(self.indexValue, symbol.value):
                            return symbol.value[self.indexValue]
                        else:
                            program.semanticError.indexOutOfRange(ID)
                else:
                    program.semanticError.invalidIndexAccess(ID)
            else:
                program.semanticError.symbolNotFound(ID)




        def assignValue(self, ID, symbol, value, program, symbolTable):

            self.checkIndexValues(ID, program, symbolTable)

            print(self.indexValue)
            if self.indexValue != None:
                if verifyListBoundariesOne(self.indexValue, symbol.value):
                    if isList(symbol.value):
                        if isinstance(value, bool):
                            symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    elif isMatrix(symbol.value):
                        if isinstance(value, list):
                            symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.incompatibleType(self.ID)
                    else:
                        program.semanticError.invalidIndexAccess(ID)
                else:
                    program.semanticError.indexOutRange(ID)
            
                    

        
            



