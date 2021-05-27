import sys 
sys.path.append("..")
from Semantic.SemanticAnalysis import *

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


class IndexColumn:

    def __init__(self, column):
        self.column = column


class IndexOne:
        def __init__(self, index):
            self.indexValue = index




class Blink(Instruction):

    def __init__(self, time, timeRange):

        self.time

    
    def eval(self, program, symbolTable):