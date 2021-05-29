import sys 
sys.path.append("..")
from Semantic.Common import *


class Index:

    pass 


class IndexAccess:

    def __init__(self, ID, index):
        self.ID = ID
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


        def eval(self, valueToAssign, program, symbolTable):

            pass 




