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
        if (isinstance(self.col, int)):
            if (isinstance(self.row, int)):
                if(isinstance(self.value, int)):
                    self.printLed(program)
                else:
                    program.semanticError.addError("Semantic error: Invalid data for value, an int is expected")
            else:
                program.semanticError.addError("Semantic error: Invalid data for row, an int is expected")
        
        else:
            program.semanticError.addError("Semantic error: Invalid data for col, an int is expected")
        
    def printLed(self, program):
        output = "PrintLed{\n col: " + self.col + "\n row: " + self.row + "\n value: " + self.value + "\n}"
