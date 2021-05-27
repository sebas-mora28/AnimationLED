import sys 
sys.path.append("..")
from Semantic.SemanticAnalysis import *
from Semantic.Common import *

class indexAccess:

    def __init__(self, ID, index):
        self.ID = index
        self.index = index




class IndexPair:

    def __init__(self, index1, index2):
        self.index1 = index1
        self.index2 = index2


class IndexRange:

    def __init__(self, fromIndex , toIndex):
        self.fromIndex = fromIndex 
        self.toIndex = toIndex

    def eval(self, program, SymbolTable):

        if isinstance(self.fromIndex, int) and isinstance(self.toIndex, int):
            return [self.fromIndex, self.toIndex]


class IndexColumn:

    def __init__(self, column):
        self.column = column


class IndexOne:
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




