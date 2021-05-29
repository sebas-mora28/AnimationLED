from Semantic.SemanticError import*
import sys
from Semantic.Common import*
import time

class Delay(Instruction):
    def __init__(self, time, timeRange):
        self.time = time
        self.timeRange = timeRange
    
    def eval(self,program):
        if (isinstance(self.time, int)):
            if (self.timeRange == "seg" or self.timeRange == "mil" or self.timeRange == "min"):
                self.delay(program)
            else:
                program.semanticError.addError("Semantic error: Invalid argument for timeRange. Mil, seg, min, is expected")
        else:
            program.semanticError.addError("Semantic error: Invalid argument for time, an int is expected")

    #Ejemplo de ejecución
    def delay(self, program):
       output= "Delay{\n time: " + self.time +"\n"+ "timeRange:" + self.timeRange+ "\n}"

