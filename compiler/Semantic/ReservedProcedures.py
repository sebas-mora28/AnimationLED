from Semantic.Common import isList, isMatrix, searchSymbolByID, verifyType
import sys
sys.path.append("..")
from Semantic.SemanticError import*
from Semantic.Common import*


class Delay(Instruction):
    def __init__(self, time, timeRange):
        self.time = time
        self.timeRange = timeRange
    
    def eval(self,program, SymbolTable):
        if (verifyType(self.time, int)):
            if (self.timeRange == "Seg" or self.timeRange == "Mil" or self.timeRange == "Min"):
                self.delay(program)
            else:
                program.semanticError.delayInvalidArgumentTimeRange()
        else:
            program.semanticError.delayInvalidArgumentTime()

    #Ejemplo de ejecución
    def delay(self, program):
       output= "Delay{\n time: " + str(self.time) +"\n"+ "timeRange:" + self.timeRange+ "\n}"




class Blink(Instruction):
    def __init__(self,col, row, time, timeRange, state):
        self.col = col
        self.row = row
        self.time = time
        self.timeRange = timeRange
        self.state = state

    def eval(self, program, SymbolTable):
        if (verifyType(self.col, int)):
            if (verifyType(self.row, int)):
                if (verifyType(self.time, int)):
                    if (self.timeRange == "Seg" or self.timeRange == "Mil" or self.timeRange == "Min"):
                        if (verifyType(self.state,bool)):
                                self.blink(program)
                        else:
                            program.semanticError.blinkInvalidArgumentState()
                    else:
                        program.semanticError.blinkInvalidArgumentTimeRange() 
                else:
                    program.semanticError.blinkInvalidArgumentTime()
            else:
                program.semanticError.blinkInvalidArgumentRow() 
        else:
            program.semanticError.blinkInvalidArgumentCol()
        
        
    #Funcionamiento del blink
    def blink(self, program):
        string = "Blink {\n col :"+str(self.col) +"\n"+ "row: " + str(self.row) +"\n"+ "time: " +str(self.time)+"\n"+"timeRange: " + self.timeRange +"\n"+ "state: " +str(self.state )+ "\n}"
        #Añadir al output




class PrintLed(Instruction):
    def __init__(self, col, row, value):
        self.col = col
        self.row = row
        self.value = value
    
    def eval(self,program, SymbolTable):
        if (verifyType(self.col, int)):
            if (verifyType(self.row, int)):
                if(verifyType(self.value, bool)):
                    self.printLed(program)
                else:
                    program.semanticError.printLedInvalidArgumentValue()
            else:
                program.semanticError.printLedInvalidArgumentRow()
        
        else:
            program.semanticError.printLedInvalidArgumentCol()
        
    def printLed(self, program):
        output = "PrintLed{\n col: " + str(self.col) + "\n row: " + str(self.row) + "\n value: " + str(self.value) + "\n}"




class PrintLedX(Instruction):
    def __init__(self,objectType, index, list):
        self.objectType = objectType
        self.index = index
        self.list = list
    
    def eval(self,program, SymbolTable):
        if(self.objectType == "F" or self.objectType == "C"):
            if (verifyType(self.index, int)):
                if (isList(self.list)and len(self.list)<= 8):
                    self.printLedX(program)
                elif verifyType(self.list, str):
                    temp = searchSymbolByID(self.list,program,SymbolTable)
                    if temp != None:
                        if isList(temp.value) and len(temp.value)<= 8:
                            self.printLedX(program)
                        else:
                            program.semanticError.printLedXInvalidArgumentList()
                else:
                       program.semanticError.printLedXInvalidArgumentList() 
            else:
                program.semanticError.printLedXInvalidArgumentIndex()
        elif self.objectType =="M":
            if (verifyType(self.index, int)):
                if (isMatrix(self.list)and len(self.list) <= 8 and len(self.list[0]) <= 8):
                    self.printLedX(program)
                elif verifyType(self.list, str):
                    temp = searchSymbolByID(self.list,program,SymbolTable)
                    if temp !=None:
                        if isMatrix(temp.value) and len(temp.value) <= 8 and len(temp.value[0]) <= 8:
                            self.printLedX(program)
                        else:
                            program.semanticError.printLedXInvalidArgumentMatrix()
                else:
                    program.semanticError.printLedXInvalidArgumentMatrix()
                
            else:
                program.semanticError.printLedXInvalidArgumentIndex()

        else:
             program.semanticError.printLedXInvalidArgumentObjectType()
            
   
    def printLedX(self, program):
        output = "PrintLedX{\n objectType: " + str(self.objectType) + "\n index: " + str(self.index) +"\n list:  "+ str(self.list)+ "\n }"
    
