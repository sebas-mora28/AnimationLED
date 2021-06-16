import sys
sys.path.append("..")
import copy

class Instruction:

    def eval(self, program, symbolTable):
        pass


def verifyListBoundariesOne(index, listSymbol):
        return index < len(listSymbol) and index >= 0
         

    
def verifyListBoundaries_2(index1, index2, listSymbol):
        return index1 >= 0 and index2 < len(listSymbol)
        

def verifyBoundariesMatrix(index1, index2, matrixSymbol):
    return index1 >= 0 and index1 < len(matrixSymbol) and index2 < len(matrixSymbol[index1])

def verifyType(value1, instance):
    return type(value1) == instance

def getColumn(index, matrix):
    
    res = []
    for i in range(len(matrix)):

        res += [matrix[i][index]]
    
    return res


def setColumn(index, matrix, column):
    for i in range(len(matrix)):

        matrix[i][index] = column[i]
    
    return matrix


def isList(lista):

    if not verifyType(lista, list):

        return False

    if(lista == []):

        return True

    for i in range(len(lista)):

        if verifyType(lista[i], list):

            return False
    
    return True


def isMatrix(matrix):

    if not verifyType(matrix, list):

        return False

    if(matrix == []):

        return True

    for i in range(len(matrix)):

        if not verifyType(matrix[i], list):

            return False
    
    return True



def checkIndexValue(ID, indexValue, program, symbolTable):

    if verifyType(indexValue, int):

        return indexValue

    if verifyType(indexValue, str):

                temp = searchSymbolByID(indexValue, program, symbolTable)
                if temp != None:

                    if verifyType(temp.value, int):
                        return temp.value

                    else:
                        program.semanticError.invalidIndexArguments(ID)
                        return
    else:
        program.semanticError.invalidIndexArguments(ID)




def checkValue(value, typeValue, program, symbolTable, error):
    
        if verifyType(value, typeValue):
            return value

        elif verifyType(value, str):

            symbol = searchSymbolByID(value, program, symbolTable)

            if symbol != None:

                if verifyType(symbol.value, typeValue ):
                    
                    return symbol.value
                else:
                    error()

        else:
            error() 

                
def searchSymbolByID(ID, program, symbolTable):

    if symbolTable.exist(ID):

        return symbolTable.getSymbolByID(ID)

    elif program.symbolTable.exist(ID):

        return program.symbolTable.getSymbolByID(ID)

    else:

        program.semanticError.symbolNotFound(ID)
        return None



def verifyListValueList(lista, program, symbolTable):

    for i in range(len(lista)):

        listValue = lista[i]

        if verifyType(listValue, bool):

            continue

        elif verifyType(listValue, str):

            symbol = searchSymbolByID(listValue, program, symbolTable)

            if symbol != None:

                if verifyType(symbol.value, bool):

                    lista[i] = symbol.value 

                else:

                    program.semanticError.invalidListValue()
                    return 
        else:

            program.semanticError.invalidListValue()   

    return lista



def verifyListValueMatrix(matrix, program, symbolTable):

    for i in range(len(matrix)):

        for j in range(len(matrix[i])):

            matrixValue = matrix[i][j]
            if verifyType(matrixValue, bool):

                continue

            elif verifyType(matrixValue, str):

                val = searchSymbolByID(matrixValue, program, symbolTable)
                print(val)
                if val != None:

                    if verifyType(val.value, bool):

                        matrix[i][j] = val.value  

                    else:

                        program.semanticError.invalidListValue()
                        return 

            else:

                program.semanticError.invalidListValue()
    
    return matrix




def is8x8(matrix):

    if len(matrix) != 8:
        return False
    
    for i in range(0, len(matrix)):

        if len(matrix[i]) != 8:
            return False

    
    return True
        



def fillList(value_):

    value = copy.deepcopy(value_)

    print(value)
    if isList(value):

        if len(value) == 8:
            return value
        else:
            i = len(value)
            for i in range(i, 8):
                value.append(False)

            return value
        
    elif isMatrix(value):


        if not is8x8(value):

            if len(value) < 8:
                for i in range(len(value), 8):
                    value.append([])

            for i in range(0, len(value)):
                
                if len(value[i]) == 8:
                    continue

                else:

                    j = len(value[i])
                    for j in range(j, 8):
                        value[i].append(False)


        print(len(value))
        for i in range(0, len(value)):
            print(len(value[i]))
        return value