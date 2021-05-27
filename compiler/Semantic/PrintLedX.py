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
            if not(isinstance(self.index, int)):
                print("Semantic error: Invalid index, an int is expected")
            if not (isList(self.list)):
                print("Semantic error: Invalid argument for list, expected list")
        elif self.objectType =="M":
            if not(isinstance(self.index, int)):
                print("Semantic error: Invalid index, an int is expected")
            if not (isMatrix(self.list)):
                print("Semantic error: Invalid argument for list, expected Matrix")
        else:
            print("Semantic error: invalid object type. expected F,C or M")
    
    def printLedX(self, program):
        #agregar funcionalidad
        pass
