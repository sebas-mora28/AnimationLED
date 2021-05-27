

def verifyListBoundaries(program, index, listSymbol):
        print(index)
        if index < len(listSymbol.value):
            return True
        program.semanticError.index_out_of_range(listSymbol.ID)
        return False

    
def verifyListBoundaries_2(program, index1, index2, listSymbol):
        print(index2)
        if(index1 >= 0 and index2 < len(listSymbol.value)):
            return True  
        program.semanticError.index_out_of_range(listSymbol.ID)
        return False


def getIndexByID(program, symbolTable, ID):

    
    if(symbolTable.exist(ID)):

        symbol = symbolTable.getSymbolByID(ID)

        if(symbol.scope == "local"):
            return symbol.value

        else:
            if program.symbolTable.exist(ID):
                return program.symbolTable.getSymbolByID(ID).value

            else:
                program.symbol_variable_not_found(ID)
                return None
    else:

        if program.symbolTable.exist(ID):
                return program.symbolTable.getSymbolByID(ID).value

        else:
                program.symbol_variable_not_found(ID)
                return None



def isList(lista):

    if not isinstance(lista, list):
        return False

    if(lista == []):
        return True

    for i in range(len(list)):
        if isinstance(lista[i], list):
            return False
    
    return True


def isMatrix(matrix):

    if not isinstance(matrix, list):
        return False

    if(matrix == []):
        return True

    for i in range(len(list)):
        if not isinstance(matrix[i], list):
            return False
    
    return True