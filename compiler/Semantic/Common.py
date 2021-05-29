import sys
sys.path.append("..")
from Semantic.IndexType import *


class Instruction:

    def eval(self, program, symbolTable):
        pass


def verifyListBoundariesOne(index, listSymbol):
        print(index)
        if index < len(listSymbol.value):
            return True
        return False

    
def verifyListBoundaries_2(index1, index2, listSymbol):
        print(index2)
        if(index1 >= 0 and index2 < len(listSymbol.value)):
            return True  
        return False



def getColumn(index, matrix):
    res = []
    for i in range(len(matrix)):
        res += matrix[i][index]
    
    return res


def getIndex(ID, index, program, symbolTable):

        symbol = searchSymbolByID(ID, program, symbolTable)
        if symbol != None:
            if isinstance(index, IndexOne):
                if isList(symbol.value):
                    if verifyListBoundariesOne(index.indexValue, symbol):
                        return symbol.value[index.index.Value]

            if isinstance(index, IndexPair):
                if isMatrix(symbol.value):
                    if verifyListBoundaries_2(index.indexValue1, index.indexValue2, symbol):
                        return symbol.value[index.indexValue1][index.indexValue2] 
            
            if isinstance(index, IndexRange):
                if isList(symbol.value):
                    if verifyListBoundaries_2(index.fromIndex, index.toIndex, symbol):
                        return symbol.value[index.fromIndex:index.toIndex]
            
            if isinstance(index, IndexColumn):
                if isMatrix(symbol.value):
                    if verifyListBoundariesOne(index.column, symbol.value[0]):
                        return getColumn(index.column, symbol)






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


    