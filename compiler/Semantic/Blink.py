from compiler.Semantic.Common import Instruction
from Semantic.SemanticError import*
import sys
from Semantic.Common import*


class Blink(Instruction):
    def __init__(self,col, row,value, time, timeRange, state):
        self.col = col
        self.row = row
        self.value = value
        self.time = time
        self.timeRange = timeRange
        self.state = state

    def eval(self, program):
        if not (isinstance(self.col, int)):
            print("Semantic error: Invalid data for col, an int is expected")
        if not (isinstance(self.row, int)):
            print("Semantic error: Invalid data for row, an int is expected")
        if not (isinstance(self.value, int)):
            print("Semantic error: Invalid data for value, an int is expected")
        if not (isinstance(self.time, int)):
            print("Semantic error: Invalid data for time, an int is expected")
        if not (self.timeRange == "seg" or self.timeRange == "mil" or self.timeRange == "min"):
            print("Semantic error: Invalid argument for timeRange. Mil, seg, min, is expected")
        if not(isinstance(self.state,bool)):
            print("Semantic error: Invalid data for sate, a bool is expected")
    #Funcionamiento del blink
    def blink(self, program):
        pass

