import sys 
sys.path.append("..")
from Semantic.Common import *


class Index:

    def checkValues(self, ID, program, symbolTable):
         pass
    
    def getValuesFromIndex(self, ID, program, symbolTable):
        pass 

    def assignValue(self, ID, symbol, value, program, symbolTable):
        pass





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


    def checkValues(self, ID, program, symbolTable):
        self.indexValue1 = checkIndexValue(ID, self.indexValue1, program, symbolTable)
        self.indexValue2 = checkIndexValue(ID, self.indexValue2, program, symbolTable)

    
    def getValuesFromIndex(self, ID, program, symbolTable):

        self.indexValue1 = checkIndexValue(ID, self.indexValue1, program, symbolTable)
        self.indexValue2 = checkIndexValue(ID, self.indexValue2, program, symbolTable)
        symbol = searchSymbolByID(ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.indexValue1 != None and self.indexValue2 != None:
                    if verifyListBoundaries_2(self.indexValue1, self.indexValue2, symbol.value):
                        return symbol.value[self.indexValue1][self.indexValue2]
                    else:
                        program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {ID} not found")

        
    def assignValue(self, ID, symbol, value, program, symbolTable):

            
            self.checkValues(ID, program, symbolTable)

            if self.indexValue1 != None and self.indexValue2 != None:
                if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                    if isList(symbol.value):
                        if isinstance(value, list):
                            symbol.value[self.fromIndex:self.toIndex] = value
                        else:
                            program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}") 
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list")
                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Symbol {ID} not found")






class IndexRange(Index):

    def __init__(self, fromIndex , toIndex):
        self.fromIndex = fromIndex 
        self.toIndex = toIndex
   


    def checkValues(self, ID, program, symbolTable):
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
                            program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list")

        else:
            program.semanticError.addError(f"Semantic error: Symbol {ID} not found")


    def assignValue(self, ID, symbol, value, program, symbolTable):

            
            self.checkValues(ID, program, symbolTable)

            if self.fromIndex != None and self.toIndex != None:
                if verifyListBoundaries_2(self.fromIndex, self.toIndex, symbol.value):
                    if isList(symbol.value):
                        if isinstance(value, list):
                            symbol.value[self.fromIndex:self.toIndex] = value
                        else:
                            program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}") 
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list")
                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Symbol {ID} not found")


class IndexColumn(Index):

    def __init__(self, column):
        self.column = column
 

    def checkValues(self, ID, program, symbolTable):
            self.column = checkIndexValue(ID, self.indexValue, program, symbolTable)

    def getValuesFromIndex(self, ID, program, symbolTable):

        symbol = searchSymbolByID(ID, program, symbolTable)

        self.checkValues(ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.column != None:
                    if verifyListBoundariesOne(self.column, symbol.value[0]):
                            return getColumn(self.column, symbol.value)
                    else:
                        program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {ID} not found")
            

    def assignValue(self, ID, symbol, value, program, symbolTable):

            self.column = checkIndexValue(ID, self.column, program, symbolTable)
            if self.column != None:
                if verifyListBoundariesOne(self.column, symbol.value[0]):
                    if isMatrix(symbol.value):
                        if isinstance(value, list):
                            print(value)
                            symbol.value[self.column] = value
                        else:
                            program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}") 
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list or matrix")
                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            else:
                program.semanticError.addError(f"Semantic error: Symbol {ID} not found")

class IndexOne(Index):
        def __init__(self, index):
            self.indexValue = index


        def checkValues(self, ID, program, symbolTable):
            self.indexValue = checkIndexValue(ID, self.indexValue, program, symbolTable)


        def getValuesFromIndex(self, ID,  program, symbolTable):

            self.checkIndexValue(ID, program, symbolTable)


            symbol = searchSymbolByID(ID, program, symbolTable)
            if symbol != None:
                if isList(symbol.value) or isMatrix(symbol.value):
                    if self.indexValue != None:
                        if verifyListBoundariesOne(self.indexValue, symbol.value):
                            return symbol.value[self.indexValue]
                        else:
                            program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix or list")
            else:
                program.semanticError.addError(f"Semantic error: Symbol {ID} not found")




        def assignValue(self, ID, symbol, value, program, symbolTable):

            self.checkIndexValue(ID, program, symbolTable)

            print(self.indexValue)
            if self.indexValue != None:
                if verifyListBoundariesOne(self.indexValue, symbol.value):
                    if isList(symbol.value):
                        if isinstance(value, bool):
                            symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}") 
                    elif isMatrix(symbol.value):
                        if isinstance(value, list):
                            symbol.value[self.indexValue] = value
                        else:
                            program.semanticError.addError(f"Semantic error: Incompatible type in symbol {ID}") 
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list or matrix")

                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
            
                    

        
            



