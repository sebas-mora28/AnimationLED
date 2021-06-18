from Semantic.Common import isList, isMatrix, searchSymbolByID, verifyType
import sys
sys.path.append("..")
from Semantic.SemanticError import*
from Semantic.Common import*
from Semantic.VariableAssignment import *

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

    def checkTimeValue(self, program, symbolTable):

        if verifyType(self.time, int):
            return self.time

        elif verifyType(self.time, str):
            symbol = searchSymbolByID(self.time, program, symbolTable)

            if symbol != None:

                if verifyType(symbol.value, int):
                    return symbol.value
        
        else:
            program.semanticError.delayInvalidArgumentTime()


    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):

        evaluatedTime = self.checkTimeValue(program, symbolTable)

        if evaluatedTime != None:

            if (self.timeRange == "Seg"):
                self.delay(program, evaluatedTime)
            elif self.timeRange == "Mil":
                evaluatedTime = evaluatedTime / 1000
                self.delay(program, evaluatedTime)
            elif self.timeRange == "Min":
                evaluatedTime = evaluatedTime *60
                self.delay(program, evaluatedTime)
            else:
                program.semanticError.delayInvalidArgumentTimeRange()
      

    # Funcion encargada de la creacion y almacenamiento del output de la instruccion
    # program: programa que maneja la ejecucion del compilador 
    def delay(self, program, time):
       output= "Delay;"+ str(time) + ";" + self.timeRange
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
  



    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self, program, symbolTable):

        evaluatedCol = checkValue(self.col, int, program, symbolTable, program.semanticError.blinkInvalidArgumentCol)
        print(evaluatedCol)
        if evaluatedCol != None:

            evaluatedRow = checkValue(self.row, int, program, symbolTable, program.semanticError.blinkInvalidArgumentRow)
            if evaluatedRow != None:

                evaluatedTime = checkValue(self.time, int,  program, symbolTable, program.semanticError.blinkInvalidArgumentTime)
                if evaluatedTime != None:

                    if (self.timeRange == "Seg"):


                        evaluatedState = checkValue(self.state, bool,  program, symbolTable,  program.semanticError.blinkInvalidArgumentState)
                        if evaluatedState != None:

                                self.blink(program, evaluatedCol, evaluatedRow, evaluatedTime, self.timeRange, evaluatedState)


                    elif self.timeRange == "Mil":

                        evaluatedTime = evaluatedTime / 1000
                        evaluatedState = checkValue(self.state, bool,  program, symbolTable,  program.semanticError.blinkInvalidArgumentState)
                        if evaluatedState != None:

                                self.blink(program, evaluatedCol, evaluatedRow, evaluatedTime, self.timeRange, evaluatedState)


                    elif self.timeRange == "Min":

                        evaluatedTime = evaluatedTime *60
                        evaluatedState = checkValue(self.state, bool,  program, symbolTable,  program.semanticError.blinkInvalidArgumentState)
                        if evaluatedState != None:

                                self.blink(program, evaluatedCol, evaluatedRow, evaluatedTime, self.timeRange, evaluatedState)

                    else:

                        program.semanticError.blinkInvalidArgumentTimeRange() 

        
    # Funcion que crea y almacena el output de la instruccion blink 
    # program: programa que maneja la ejecucion del compilador 
    def blink(self, program, col, row, time, timeRange, state):
        output = "Blink;"+str(col) +";"+ str(row) +";" +str(time)+";" + timeRange +";" +str(int(state))
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
   
   
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):

        evaluatedCol = checkValue(self.col, int,  program, symbolTable,  program.semanticError.printLedInvalidArgumentCol)
        if evaluatedCol != None:

            evaluatedRow = checkValue(self.row, int,  program, symbolTable,  program.semanticError.printLedInvalidArgumentRow)
            if evaluatedRow != None:

                evaluatedValue = checkValue(self.value, bool,  program, symbolTable, program.semanticError.printLedInvalidArgumentValue)
                if evaluatedValue != None:
                    
                    self.printLed(program, evaluatedCol, evaluatedRow, evaluatedValue)
             


    # Funcion que crea y almacena el output de la instruccion PrintLed 
    # program: programa que maneja la ejecucion del compilador 
    def printLed(self, program, col , row, value):
        output = "PrintLed;" + str(col) + ";" + str(row) + ";" + str(int(value))
        program.programOutput.append(output)



# Clase encarg
class PrintLedX(Instruction):
    # Constructor
    # objectType: string con el tipo de objeto a enviar (M,C,F)
    # index: int del numero de columna, fila o en el caso de matriz 0
    # list: lista o matriz con los valores deseados
    def __init__(self,objectType, index, list_):
        self.objectType = objectType
        self.index = index
        self.list = list_
    
    # Funcion que evalua que los parametros ingresados sean los solicitados
    # program: programa que maneja la ejecucion del compilador 
    # SymbolTable: tabla de simbolos
    def eval(self,program, symbolTable):


        if(self.objectType == "F" or self.objectType == "C"):

            evaluatedIndex = checkValue(self.index, int,  program, symbolTable,  program.semanticError.printLedXInvalidArgumentIndex)
            if evaluatedIndex != None:


                if (isList(self.list)and len(self.list)<= 8):

                        self.printLedX(program,self.list)


                elif verifyType(self.list, str):

                    temp = searchSymbolByID(self.list,program,symbolTable)

                    if temp != None:

                        if isList(temp.value) and len(temp.value)<= 8:

                            self.printLedX(program, temp.value, evaluatedIndex)

                        else:

                            program.semanticError.printLedXInvalidArgumentList()

                else:

                       program.semanticError.printLedXInvalidArgumentList()


        elif self.objectType =="M":


            evaluatedIndex = checkValue(self.index, int,  program, symbolTable,  program.semanticError.printLedXInvalidArgumentIndex)
            if evaluatedIndex != None:

                if (isMatrix(self.list)and len(self.list) <= 8 and len(self.list[0]) <= 8):

                    self.printLedX(program, self.list)

                elif verifyType(self.list, str):

                    temp = searchSymbolByID(self.list,program,symbolTable)

                    if temp !=None:

                        if isMatrix(temp.value) and len(temp.value) <= 8 and len(temp.value[0]) <= 8:

                            self.printLedX(program, temp.value, evaluatedIndex)

                        else:

                            program.semanticError.printLedXInvalidArgumentMatrix()

                else:

                    program.semanticError.printLedXInvalidArgumentMatrix()
                

        else:

             program.semanticError.printLedXInvalidArgumentObjectType()
            
    # Funcion que crea y almacena el output de la instruccion PrintLedX
    # program: programa que maneja la ejecucion del compilador 
    def printLedX(self, program, value, index):
        value = fillList(value)
        output = "PrintLedX;" + str(self.objectType) + ";" + str(index) +";"+ str(value)
        program.programOutput.append(output)
    


class Type(Instruction):

    def __init__(self, value):
        self.value = value
    

    def eval(self, program, symbolTable):

        tempValue = self.value

        if verifyType(tempValue, str):
            symbol = searchSymbolByID(tempValue, program, symbolTable)
            if symbol != None:
                tempValue = symbol.value
                
        
        if verifyType(tempValue, list):
            return "type : list"

        if verifyType(tempValue, bool):
            return "type : bool"

        if verifyType(tempValue, int):
            return "type : int"
        
        else:
            program.semanticError.incompatibleError(self.value)





class Print(Instruction):

    def __init__(self, printArgument):
        self.printArgument = printArgument


    
    def eval(self, program, symbolTable):

        
        if verifyType(self.printArgument, int) or verifyType(self.printArgument, bool):

            program.prints.append(f"{str(self.printArgument)}")

        if verifyType(self.printArgument, Type) or verifyType(self.printArgument, Len):

            value = self.printArgument.eval(program, symbolTable)

            if value != None:
                program.prints.append(f"{str(value)}")

        if verifyType(self.printArgument, IndexAccess):
            value = self.printArgument.getValues(program, symbolTable)

            if value != None:
                program.prints.append(f"{str(value)}")

        if verifyType(self.printArgument, str):
            symbol = searchSymbolByID(self.printArgument, program, symbolTable)

            if symbol != None:

                program.prints.append(f"{str(symbol.value)}")

