import sys
sys.path.append("..")
from Semantic.IndexType import *


class Instruction:

    def eval(self, program, symbolTable):
        pass


def verifyListBoundariesOne(index, listSymbol):
        print(index)
        if index < len(listSymbol):
            return True
        return False

    
def verifyListBoundaries_2(index1, index2, listSymbol):
        print(index2)
        if index1 >= 0 and index2 < len(listSymbol):
            return True  
        return False



def getColumn(index, matrix):
    res = []
    for i in range(len(matrix)):
        res += [matrix[i][index]]
    
    return res


def getValuesFromIndex(ID, indexType, program, symbolTable):

        
        symbol = searchSymbolByID(ID, program, symbolTable)
        if symbol != None:
            if isinstance(indexType, IndexOne):
                if isList(symbol.value) or isMatrix(symbol.value):
                    if verifyListBoundariesOne(indexType.indexValue, symbol.value):
                        return symbol.value[indexType.indexValue]
                    else:
                        program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix or list")


            if isinstance(indexType, IndexPair):
                if isMatrix(symbol.value):
                    if verifyListBoundaries_2(indexType.indexValue1, indexType.indexValue2, symbol.value):
                        return symbol.value[indexType.indexValue1][indexType.indexValue2]
                    else:
                        program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix")
            
            if isinstance(indexType, IndexRange):
                if isList(symbol.value):
                    if verifyListBoundaries_2(indexType.fromIndex, indexType.toIndex, symbol.value):
                        return symbol.value[indexType.fromIndex:indexType.toIndex]
                    else:
                        program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a list")
            
            if isinstance(indexType, IndexColumn):
                if isMatrix(symbol.value):
                    if verifyListBoundariesOne(indexType.column, symbol.value[0]):
                        return getColumn(indexType.column, symbol.value)
                    program.semanticError.addError(f"Semantic error: Index out of range in {ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid index access, {ID} is not a matrix")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {ID} not found")
            






def isList(lista):

    if not isinstance(lista, list):
        return False

    if(lista == []):
        return True

    for i in range(len(lista)):
        if isinstance(lista[i], list):
            return False
    
    return True


def isMatrix(matrix):

    if not isinstance(matrix, list):
        return False

    if(matrix == []):
        return True

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            return False
    
    return True




def searchSymbolByID(ID, program, symbolTable):

    if symbolTable.exist(ID):
        return symbolTable.getSymbolByID(ID)

    elif program.symbolTable.exist(ID):
        return program.symbolTable.getSymbolByID(ID)

    else:
        return None


    