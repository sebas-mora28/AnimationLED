import sys 
sys.path.append("..")
from Semantic.Common import * 


class matrixDimension(Instruction):

    def __init__(self, ID, dimension):
        self.ID = ID
        self.dimension = dimension

    
    def eval(self, program, symbolTable):

        symbolVariable = searchSymbolByID(self.ID, program, symbolTable)

        if symbolTable != None:

            if isMatrix(symbolVariable.value):

                if self.dimension == ".shapeF":
                    return len(symbolVariable.value)
                
                if self.dimension == ".shapeC":
                    return len(symbolVariable.value[0])

            else:
                program.semanticError.addError(f"Semantic error: {self.ID} is not a matrix")

        else:
            program.semanticError.addError(f"Semantic error: Variable {self.ID} not found")



class ListInsert(Instruction):

    def __init__(self, ID, index, value):
        self.ID = ID
        self.index = index
        self.value = value
    
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)
        if symbol != None:
            if isList(symbol.value):
                if self.index <= len(symbol.value):
                    if isinstance(self.value, bool):
                        symbol.value.insert(self.index, self.value)
                    else:
                        program.semanticError.addError(f"Semantic error: Incompatible type in variable {self.ID}")
                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
            else:
                program.semanticError.addError(f"Semantic error: insert procedure only applicable in list, {self.ID} is not a list")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {self.ID} not found")


class ListDelete(Instruction):

    def __init__(self, ID, index):
        self.ID = ID
        self.index = index
    
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)
        if symbol != None:
            if isList(symbol.value):
                if self.index < len(symbol.value):
                    symbol.value.pop(self.index)
                else:
                    program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
            else:
                program.semanticError.addError(f"Semantic error: insert procedure only applicable in list, {self.ID} is not a list")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {self.ID} not found")



class MatrixInsert(Instruction):

    def __init__(self, ID, value, insertionType, index):
        self.ID = ID
        self.value = value 
        self.insertionType = insertionType
        self.index = index
    def eval(self, program, symbolTable):

        symbol = searchSymbolByID(self.ID, program, symbolTable)

        if symbol != None:
            if isMatrix(symbol.value):
                if self.insertionType == 1 or self.insertionType == 0:
                    if isinstance(self.value, list):
                            if self.insertionType == 0:
                                if len(self.value[0]) == len(symbol.value[0]):
                                    if self.index == None:
                                            symbol.value.append(self.value[0])
                                    else:
                                        if self.index <= len(symbol.value):
                                            symbol.value.insert(self.index, self.value[0])
                                        else:
                                            program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
                                else:
                                    program.semanticError.addError(f"Semantic error: Trying to insert a list with diferent dimentions in {self.ID}")
                        
                            if self.insertionType == 1:
                                if len(self.value) == len(symbol.value):
                                    if self.index == None:
                                        for i in range(len(symbol.value)):
                                            symbol.value[i].append(self.value[i][0])
                                    else:
                                        if self.index <= len(symbol.value[0]):
                                            for i in range(len(symbol.value)):
                                                symbol.value[i].insert(self.index, self.value[i][0])
                                        else:
                                            program.semanticError.addError(f"Semantic error: Index out of range in {self.ID}")
                                else:
                                    program.semanticError.addError(f"Semantic error: Trying to insert a list with diferent dimentions in {self.ID}")
                    else:
                        program.semanticError.addError(f"Semantic error: Invalid argument in insert function")
                else:
                    program.semanticError.addError(f"Semantic error: Invalid insertion type in insert function")
            else:
                program.semanticError.addError(f"Semantic error: insert procedure only applicable in matrix, {self.ID} is not a matrix")
        else:
            program.semanticError.addError(f"Semantic error: Symbol {self.ID} not found")