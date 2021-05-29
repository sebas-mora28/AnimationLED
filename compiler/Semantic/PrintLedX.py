from compiler.Semantic.Common import isList, isMatrix
import sys
from Semantic.Common import*
from Semantic.SemanticError import*

class PrintLedX(Instruction):
    def __init__(self,objectType, index, list):
        self.objectType = objectType
        self.index = index
        self.list = list
    
    def eval(self,program):
        if(self.objectType == "F" or self.objectType == "C"):
            if (isinstance(self.index, int)):
                if (isList(self.list)):
                    self.printLedX(program)
                else:
                       program.semanticError.addError("Semantic error: Invalid argument for list, expected list") 
            else:
                program.semanticError.addError("Semantic error: Invalid index, an int is expected")
        elif self.objectType =="M":
            if (isinstance(self.index, int)):
                if (isMatrix(self.list)):
                    self.printLedX(program)
                else:
                    program.semanticError.addError("Semantic error: Invalid argument for list, expected Matrix")
            else:
                program.semanticError.addError("Semantic error: Invalid index, an int is expected")

        else:
             program.semanticError.addError("Semantic error: invalid object type. expected F,C or M")
            
        
    def printLedX(self, program):
        output = "PrintLedX{\n objectType: " + self.objectType + "\n index: " + self.index +"\n list:  "+ str(self.list)+ "\n }"
    
