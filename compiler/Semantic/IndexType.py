import sys 
sys.path.append("..")
from Semantic.Common import *


class Index:

    pass 


class indexAccess:

    def __init__(self, ID, index):
        self.ID = index
        self.index = index


class IndexPair(Index):

    def __init__(self, index1, index2):
        self.indexValue1 = index1
        self.indexValue2 = index2


class IndexRange(Index):

    def __init__(self, fromIndex , toIndex):
        self.fromIndex = fromIndex 
        self.toIndex = toIndex

    def eval(self, program, SymbolTable):

        if isinstance(self.fromIndex, int) and isinstance(self.toIndex, int):
            return [self.fromIndex, self.toIndex]


class IndexColumn(Index):

    def __init__(self, column):
        self.column = column


class IndexOne(Index):
        def __init__(self, index):
            self.indexValue = index


        def eval(self, program, symbolTable):
            if isinstance(self.indexValue, int):
                return self.indexValue
            if isinstance(self.indexValue, str):
                symbolValue = searchSymbolByID(self.indexValue, program, symbolTable)
                if symbolValue:
                    return symbolValue.value
                return None
            return None




