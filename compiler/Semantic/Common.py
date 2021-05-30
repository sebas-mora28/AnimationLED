import sys
sys.path.append("..")


class Instruction:

    def eval(self, program, symbolTable):
        pass


def verifyListBoundariesOne(index, listSymbol):
        if index < len(listSymbol):
            return True
        return False

    
def verifyListBoundaries_2(index1, index2, listSymbol):
        if index1 >= 0 and index2 < len(listSymbol):
            return True  
        return False



def getColumn(index, matrix):
    res = []
    for i in range(len(matrix)):
        res += [matrix[i][index]]
    
    return res


def isList(lista):

    if not isinstance(lista, list):
        return False

    if(lista == []):
        return True

    for i in range(len(lista)):
        if isinstance(lista[i], list):
            return False
    
    return True


def isMatrix(matrix):

    if not isinstance(matrix, list):
        return False

    if(matrix == []):
        return True

    for i in range(len(matrix)):
        if not isinstance(matrix[i], list):
            return False
    
    return True






def checkIndexValue(ID, indexValue, program, symbolTable):

    if isinstance(indexValue, int):
        return indexValue

    if isinstance(indexValue, str):
                temp = searchSymbolByID(indexValue, program, symbolTable)
                if temp != None:
                    if isinstance(temp.value, int):
                        return temp.value
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid index value in {ID}")
                        return
                else:
                    program.semanticError.addError(f"Semantic error: Symbol {indexValue} not found")
                    return 






def searchSymbolByID(ID, program, symbolTable):

    if symbolTable.exist(ID):
        return symbolTable.getSymbolByID(ID)

    elif program.symbolTable.exist(ID):
        return program.symbolTable.getSymbolByID(ID)

    else:
        return None


    