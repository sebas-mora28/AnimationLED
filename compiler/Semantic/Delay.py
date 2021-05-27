from Semantic.SemanticError import*
import sys
from Semantic.Common import*
import time

class Delay(Instruction):
    def __init__(self, time, timeRange):
        self.time = time
        self.timeRange = timeRange
    
    def eval(self,program):
        if not (isinstance(self.time, int)):
            print("Semantic error: Invalid argument for time, an int is expected")
        if not (self.timeRange == "seg" or self.timeRange == "mil" or self.timeRange == "min"):
            print("Semantic error: Invalid argument for timeRange. Mil, seg, min, is expected")
    #Ejemplo de ejecución
    #def delay(self, program):
     #   if self.timeRange == "seg":
      #      time.sleep(self.time)
       # elif self.timeRange == "mil":
        #    time.sleep(self.time/1000)
        #else:
         #   time.sleep(self.time*60)
        

