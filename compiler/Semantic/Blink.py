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
        if (isinstance(self.col, int)):
            if (isinstance(self.row, int)):
                if (isinstance(self.value, int)):
                    if (isinstance(self.time, int)):
                        if (self.timeRange == "seg" or self.timeRange == "mil" or self.timeRange == "min"):
                            if (isinstance(self.state,bool)):
                                self.blink(program)
                            else:
                                program.semanticError.addError("Semantic error: Invalid data for sate, a bool is expected")
                        
                        else:
                             program.semanticError.addError("Semantic error: Invalid argument for timeRange. Mil, seg, min, is expected")
                    
                    else:
                         program.semanticError.addError("Semantic error: Invalid data for time, an int is expected")
                
                else:
                     program.semanticError.addError("Semantic error: Invalid data for value, an int is expected")

            else:
                program.semanticError.addError("Semantic error: Invalid data for row, an int is expected") 

        else:
            program.semanticError.addError("Semantic error: Invalid data for col, an int is expected")  
        
        
    #Funcionamiento del blink
    def blink(self, program, col, row,time,timeRange, state):
        string = "Blink {\n col :"+col +"\n"+ "row: " + row +"\n"+ "time: " +time+"\n"+"timeRange: " + timeRange +"\n"+ "state: " +state + "\n}"
        #Añadir al output
