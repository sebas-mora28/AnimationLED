from compiler.Semantic.Common import Instruction
import sys
from Semantic.Common import*
from Semantic.SemanticError import*

class PrintLed(Instruction):
    def __init__(self, col, row, value):
        self.col = col
        self.row = row
        self.value = value
    
    def eval(self,program):
        if not (isinstance(self.col, int)):
            print("Semantic error: Invalid data for col, an int is expected")
        if not (isinstance(self.row, int)):
            print("Semantic error: Invalid data for row, an int is expected")
        if not (isinstance(self.value, int)):
            print("Semantic error: Invalid data for value, an int is expected")
    
    def printLed(self, program):
        #funcionalidad del la función
        pass
