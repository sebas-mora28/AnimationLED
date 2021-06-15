from Semantic.Common import isList, isMatrix, searchSymbolByID, verifyType
import sys
sys.path.append("..")
from Semantic.SemanticError import*
from Semantic.Common import*

# Clase encargada de las instrucciones Delay
class Delay(Instruction):
    # Constructor de la clase
    # time: int del tiempo que se desea que dure el delay
    # timeRange: strinf con el rango de tiempo deseado (Seg, Mil,Min)
    def __init__(self, time, timeRange):
        self.time = time
        self.timeRange = timeRange
    # Funcion que valida si lo enviado como parametro time es una variable
    # program: programa
    # symbolTable: tabla de simbolos
    # Retorna un bool que valida la variable
    def verifySeg(self,program, symbolTable):
        temp = searchSymbolByID(self.time,program,symbolTable)
        if temp != None:
            if verifyType(temp.value, int):
                self.time = str(temp.value)
                return True
            else:
                return False
        else:
            return False
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):
        if (verifyType(self.time, int) or self.verifySeg(program,symbolTable)):
            if (self.timeRange == "Seg"):
                self.delay(program)
            elif self.timeRange == "Mil":
                self.time = int(self.time) / 1000
                self.delay(program)
            elif self.timeRange == "Min":
                self.time = int(self.time) *60
                self.delay(program)
            else:
                program.semanticError.delayInvalidArgumentTimeRange()
        else:
            program.semanticError.delayInvalidArgumentTime()

    # Funcion encargada de la creacion y almacenamiento del output de la instruccion
    # program: programa que maneja la ejecucion del compilador 
    def delay(self, program):
       output= "Delay;"+ str(self.time) + ";" + self.timeRange
       program.programOutput.append(output)



# Clase encargada del manejo de la intruccion Blink
class Blink(Instruction):
    # Constructor
    # col: int numero de columna
    # row: int numero de fila
    # time: int duracion del blink 
    # timeRange: string del rango de tiempo que se desea manejar (Seg, Mil, Min)
    # state: bool con el estado del blink
    def __init__(self,col, row, time, timeRange, state):
        self.col = col
        self.row = row
        self.time = time
        self.timeRange = timeRange
        self.state = state
    # Funcion que valida si lo enviado como parametros son variables
    # program: programa
    # symbolTable: tabla de simbolos
    # Retorna un bool que valida la variable
    def verifyVar(self,program, symbolTable,type):
        if type == "c":# Verifica si en la tabla de simbolos existe una variable que sirva para col, según el ID dado
            temp = searchSymbolByID(self.col,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, int):
                    self.col = str(temp.value)
                    return True
                else:
                    return False
            else:
                return False
        
        elif type == "r":# Verifica si en la tabla de simbolos existe una variable que sirva para row, según el ID dado
            temp = searchSymbolByID(self.row,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, int):
                    self.row = str(temp.value)
                    return True
                else:
                    return False
            else:
                return False
        
        elif type == "t":# Verifica si en la tabla de simbolos existe una variable que sirva para time, según el ID dado
            temp = searchSymbolByID(self.time,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, int):
                    self.time = str(temp.value)
                    return True
                else:
                    return False
            else:
                return False
        
        else:# Verifica si en la tabla de simbolos existe una variable que sirva para state, según el ID dado
            temp = searchSymbolByID(self.state,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, bool):
                    self.state = temp.value
                    return True
                else:
                    return False
            else:
                return False

        
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self, program, symbolTable):
        if (verifyType(self.col, int) or self.verifyVar(program,symbolTable,"c")):
            if (verifyType(self.row, int) or self.verifyVar(program,symbolTable,"r")):
                if (verifyType(self.time, int)or self.verifyVar(program,symbolTable,"t")):
                    if (self.timeRange == "Seg"):
                        if (verifyType(self.state,bool) or self.verifyVar(program,symbolTable,"s")):
                                self.blink(program)
                        else:
                            program.semanticError.blinkInvalidArgumentState()
                    elif self.timeRange == "Mil":
                        self.time = self.time / 1000
                        if (verifyType(self.state,bool)):
                                self.blink(program)
                        else:
                            program.semanticError.blinkInvalidArgumentState()
                    elif self.timeRange == "Min":
                        self.time = self.time *60
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
        
        
    # Funcion que crea y almacena el output de la instruccion blink 
    # program: programa que maneja la ejecucion del compilador 
    def blink(self, program):
        output = "Blink;"+str(self.col) +";"+ str(self.row) +";" +str(self.time)+";" + self.timeRange +";" +str(int(self.state))
        program.programOutput.append(output)



# Clase encargada del funcionamiento de la instruccion PrintLed
class PrintLed(Instruction):
    # Constructor 
    # col: int numero de columna
    # row: int numero de fila
    # Value:  bool con el estado del blink
    def __init__(self, col, row, value):
        self.col = col
        self.row = row
        self.value = value
    # Funcion que valida si lo enviado como parametros son variables
    # program: programa
    # symbolTable: tabla de simbolos
    # Retorna un bool que valida la variable
    def verifyVar(self,program, symbolTable,type):
        if type == "c": # Verifica si en la tabla de simbolos existe una variable que sirva para col, según el ID dado
            temp = searchSymbolByID(self.col,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, int):
                    self.col = str(temp.value)
                    return True
                else:
                    return False
            else:
                return False
        
        elif type == "r":# Verifica si en la tabla de simbolos existe una variable que sirva para row, según el ID dado
            temp = searchSymbolByID(self.row,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, int):
                    self.row = str(temp.value)
                    return True
                else:
                    return False
            else:
                return False
        else:# Verifica si en la tabla de simbolos existe una variable que sirva para value, según el ID dado
            temp = searchSymbolByID(self.value,program,symbolTable)
            if temp != None:
                if verifyType(temp.value, bool):
                    self.value = temp.value
                    return True
                else:
                    return False
            else:
                return False
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):
        if (verifyType(self.col, int) or self.verifyVar(program,symbolTable,"c")):
            if (verifyType(self.row, int)or self.verifyVar(program,symbolTable,"r")):
                if(verifyType(self.value, bool)or self.verifyVar(program,symbolTable,"s")):
                    self.printLed(program)
                else:
                    program.semanticError.printLedInvalidArgumentValue()
            else:
                program.semanticError.printLedInvalidArgumentRow()
        
        else:
            program.semanticError.printLedInvalidArgumentCol()
    # Funcion que crea y almacena el output de la instruccion PrintLed 
    # program: programa que maneja la ejecucion del compilador 
    def printLed(self, program):
        output = "PrintLed;" + str(self.col) + ";" + str(self.row) + ";" + str(int(self.value))
        program.programOutput.append(output)



# Clase encarg
class PrintLedX(Instruction):
    # Constructor
    # objectType: string con el tipo de objeto a enviar (M,C,F)
    # index: int del numero de columna, fila o en el caso de matriz 0
    # list: lista o matriz con los valores deseados
    def __init__(self,objectType, index, list):
        self.objectType = objectType
        self.index = index
        self.list = list
    
    def verifyIndex(self,program, symbolTable):
        temp = searchSymbolByID(self.index,program,symbolTable)
        if temp != None:
            if verifyType(temp.value, int):
                self.index = temp.value
                return True
            else:
                return False
        else:
            return False
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):
        if(self.objectType == "F" or self.objectType == "C"):
            if (verifyType(self.index, int)) or self.verifyIndex(program,symbolTable):
                if (isList(self.list)and len(self.list)<= 8):
                    self.printLedX(program,self.list)
                elif verifyType(self.list, str):
                    temp = searchSymbolByID(self.list,program,symbolTable)
                    if temp != None:
                        if isList(temp.value) and len(temp.value)<= 8:
                            self.printLedX(program, temp.value)
                        else:
                            program.semanticError.printLedXInvalidArgumentList()
                else:
                       program.semanticError.printLedXInvalidArgumentList() 
            else:
                program.semanticError.printLedXInvalidArgumentIndex()
        elif self.objectType =="M":
            if (verifyType(self.index, int) or self.verifyIndex(program,symbolTable)):
                if (isMatrix(self.list)and len(self.list) <= 8 and len(self.list[0]) <= 8):
                    self.printLedX(program, self.list)
                elif verifyType(self.list, str):
                    temp = searchSymbolByID(self.list,program,symbolTable)
                    if temp !=None:
                        if isMatrix(temp.value) and len(temp.value) <= 8 and len(temp.value[0]) <= 8:
                            self.printLedX(program, temp.value)
                        else:
                            program.semanticError.printLedXInvalidArgumentMatrix()
                else:
                    program.semanticError.printLedXInvalidArgumentMatrix()
                
            else:
                program.semanticError.printLedXInvalidArgumentIndex()

        else:
             program.semanticError.printLedXInvalidArgumentObjectType()
            
    # Funcion que crea y almacena el output de la instruccion PrintLedX
    # program: programa que maneja la ejecucion del compilador 
    def printLedX(self, program, value):
        value = fillList(value)
        output = "PrintLedX;" + str(self.objectType) + ";" + str(self.index) +";"+ str(value)
        program.programOutput.append(output)
    


class Type:

    def __init__(self, value):
        self.value = value
    

    def eval(self, program, symbolTable):

        if verifyType(self.value, str):
            symbol = searchSymbolByID(self.value, program, symbolTable)
            if symbol != None and (verifyType(symbol.value, int) or verifyType(symbol.value, bool)):
                return type(symbol)
        
        elif verifyType(self.value, bool):
            return bool

        elif verifyType(self.value, int):
            return int
        
        else:
            program.semanticError.incompatibleError(self.value)
