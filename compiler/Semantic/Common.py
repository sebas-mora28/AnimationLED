import sys
sys.path.append("..")


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

                val = searchSymbolByID(i, program, symbolTable)
                if val != None:

                    if verifyType(val, bool):

                        lista[i] = val  

                    else:

                        program.semanticError.invalidListValue()
                        return 

            else:

                program.semanticError.invalidListValue()
    
    return matrix