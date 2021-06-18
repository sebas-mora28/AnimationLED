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

    def __init__(self, ID, index1Type, index2Type):
        self.ID = ID
        self.indexValue1Type = index1Type
        self.indexValue2Type = index2Type




    def checkIndexValues(self, program, symbolTable):
        self.indexValue1 = checkIndexValue(self.ID, self.indexValue1Type, program, symbolTable)
        self.indexValue2 = checkIndexValue(self.ID, self.indexValue2Type, program, symbolTable)


    def getValuesFromIndex(self, program, symbolTable):


        self.checkIndexValues(program, symbolTable)
        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:

            if isMatrix(symbol.value):

                if self.indexValue1 != None and self.indexValue2 != None:

                    if verifyBoundariesMatrix(self.indexValue1, self.indexValue2, symbol.value):

                        return symbol.value[self.indexValue1][self.indexValue2]

                    else:

                        program.semanticError.indexOutRange(self.ID)
            else:

                program.semanticError.invalidIndexAccessMatrix(self.ID)
       

        
    def assignValue(self, value, program, symbolTable):  
           
            self.checkIndexValues(program, symbolTable)
            symbol = searchSymbolByID(self.ID, program, symbolTable)

            if self.indexValue1 != None and self.indexValue2 != None and symbol != None and value !=None  :

                if isMatrix(symbol.value):

                    if verifyBoundariesMatrix(self.indexValue1, self.indexValue2, symbol.value):

                        if value != None:

                            if verifyType(value, bool):

                                symbol.value[self.indexValue1][self.indexValue2] = value

                            else:

                                program.semanticError.incompatibleType(self.ID)

                    else:

                        program.semanticError.indexOutRange(self.ID)

                else:

                    program.semanticError.invalidIndexAccessMatrix(self.ID)







class IndexRange(Index):

    def __init__(self, ID, fromIndexType , toIndexType):
        self.ID = ID
        self.fromIndexType = fromIndexType 
        self.toIndexType = toIndexType
   


    def checkIndexValues(self, program, symbolTable):
        self.fromIndex = checkIndexValue(self.ID, self.fromIndexType, program, symbolTable)
        self.toIndex = checkIndexValue(self.ID, self.toIndexType, program, symbolTable)


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

            if self.fromIndex != None and self.toIndex != None and symbol != None and value != None:
                
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

    def __init__(self, ID, indexType):
        self.ID = ID
        self.indexType = indexType
 

    def checkIndexValues(self, program, symbolTable):
            self.columnIndex = checkIndexValue(self.ID, self.indexType, program, symbolTable)

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

            if self.columnIndex != None and symbol != None and value != None:

                if isMatrix(symbol.value):

                    if verifyListBoundariesOne(self.columnIndex, symbol.value[0]):

                            if verifyType(value, list):

                                if len(value) == len(symbol.value):

                                    symbol.value = setColumn(self.columnIndex, symbol.value, value)

                                else:

                                    program.semanticError.invalidDimensionAssign(self.ID)

                            else:

                                program.semanticError.incompatibleType(self.ID)

                    else:

                        program.semanticError.indexOutRange(self.ID)

                else:

                    program.semanticError.invalidIndexAccessMatrix(self.ID)



 
class IndexOne(Index):
        def __init__(self, ID, index):
            self.ID = ID
            self.indexType = index


        def checkIndexValues(self, program, symbolTable):
            self.indexValue = checkIndexValue(self.ID, self.indexType, program, symbolTable)


        def getValuesFromIndex(self,  program, symbolTable):
            symbol = searchSymbolByID(self.ID, program, symbolTable)


            if symbol != None:

                if isList(symbol.value) or isMatrix(symbol.value):

                    self.checkIndexValues(program, symbolTable)
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
    
            if self.indexValue != None and symbol != None and value != None:
                
                    if isList(symbol.value):
                        if verifyListBoundariesOne(self.indexValue, symbol.value):

                            if verifyType(value, bool):

                                symbol.value[self.indexValue] = value

                            else:

                                program.semanticError.incompatibleType(self.ID)

                        else:
                            
                                program.semanticError.indexOutRange(self.ID)

                    elif isMatrix(symbol.value):

                        if verifyListBoundariesOne(self.indexValue, symbol.value):
    
                            if verifyType(value, list):

                                if len(value) == len(symbol.value[self.indexValue]):

                                        symbol.value[self.indexValue] = value

                                else:
                                    program.semanticError.invalidDimensionAssign(self.ID)

                            else:
                                program.semanticError.incompatibleType(self.ID)

                        else:

                            program.semanticError.indexOutRange(self.ID)

                    else: 
                        program.semanticError.invalidIndexAccess(self.ID)
               
            
                    

        
            



