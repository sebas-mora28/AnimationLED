import sys
sys.path.append("..")
from Semantic.IndexType import *
from Semantic.Atomic import *


class value(Instruction):

    def __init__(self, value):
        self.value = value


    def eval(self, program, symbolTable, scope):


        if(isinstance(self.value, int)):
            return self.value 
        if(isinstance(self.value, bool)):
            return self.value
        if(isinstance(self.value, list)):
            return self.value

        if(isinstance(self.value, str)):

            if symbolTable.exist(self.value):    
                    symbol = symbolTable.getSymbolByID(self.value)
                    return symbol.value
            else:
                if program.symbolTable.exist(self.value):
                    symbol = program.symbolTable.getSymbolByID(self.value)
                    return symbol.value
                else:
                    program.semanticError.symbol_variable_not_found(self.value)        





class VariableAssign(Instruction):

    def __init__(self, ID, value):
        self.ID = ID
        self.value = value
        self.scope = "local"

    def eval(self, program, symbolTable):
        print(f"Se asigna una variable {self.scope}")
    
        if(self.scope == "global"):
            self.assigment(program, program.symbolTable)
        
        else:
            self.assigment(program, symbolTable)
        

    def assigment(self, program, symbolTable):

        self.value = self.value.eval(program, symbolTable, self.scope)
        if(symbolTable.exist(self.ID)):
                old_value = symbolTable.getSymbolByID(self.ID)
                if(isinstance(old_value.value, type(self.value))):
                    symbolTable.changeSymbolValue(self.ID, self.value)
                else:
                    program.semanticError.incompatible_ariable_type(self.ID)            
        else:
            print("Entra a asignar " + self.ID)
            symbolTable.addSymbol(self.ID, self.value, type(self.value), self.scope)

     



class  MultipleAssign(Instruction):

    def __init__(self, IDs, values):
        self.IDs = IDs
        self.values = values
        self.scope = "local"

    

    def eval(self, program, symbolTable):

        if(len(self.IDs) == len(self.values)):

            for i in range(len(self.IDs)):

                if(self.scope == "global"):
                    self.assigment(program, program.symbolTable, self.IDs[i], self.values[i])
                
                else:
                    self.assigment(program, symbolTable, self.IDs[i], self.values[i])

        else:
            program.semanticError.multiple_variable_declaration()


    def assigment(self, program, symbolTable, ID, value):

        self.value = self.value.eval(program, symbolTable, self.scope)
        if(symbolTable.exist(ID)):
                old_value = symbolTable.getSymbolByID(ID)
                if(isinstance(old_value.value, type(value))):
                    symbolTable.changeSymbolValue(ID, value)
                else:
                    program.semanticError.incompatible_ariable_type(ID)            
        else:
            symbolTable.addSymbol(ID, value, type(value), self.scope)




class IndexAssign(Instruction):

    def __init__(self, ID, index, value):
        self.ID = ID
        self.index = index
        self.value = value
        self.scope = scope



    def eval(self,program, symbolTable):

        pass

        if(symbolTable.exist(self.ID)):
            variableSymbol = symbolTable.getSymbolByID(self.ID)
            if isinstance(variableSymbol.value, list):
                
                pass

            
        


        '''
        if(symbolTable.exist(self.ID)):
            variableSymbol = symbolTable.getSymbolByID(self.ID)
            if(isinstance(variableSymbol.value, list)):

                if isinstance(self.index, IndexOne):
                    if isinstance(self.index.indexValue, int):
                        if verifyListBoundaries(program, self.index.indexValue, variableSymbol):
                            variableSymbol.value[self.index.indexValue] = self.value

                    else:
                        i = getIndexByID(program, symbolTable, self.index.indexValue)
                        if verifyListBoundaries(program, i, variableSymbol):
                            variableSymbol.value[i] = self.value
                
                
                
                if isinstance(self.index, IndexColumn):
                    pass
                if isinstance(self.index, IndexPair):
                    pass
; 

                if isinstance(self.index, IndexRange):
                    if verifyListBoundaries_2(program, self.index.fromIndex, self.index.toIndex, variableSymbol):
                        
                        if(isinstance(self.value, list)):
                            len_list = self.index.toIndex - self.index.fromIndex
                            if(len_list == len(self.value)):
                                variableSymbol.value[self.index.fromIndex:self.index.toIndex] = self.value

                            else:
                                program.semanticError.invalid_range_assignment(self.ID)
                        else:
                            program.semanticError.invalid_range_assignment(self.ID)

                    else:
                        pass
            else:

                program.semanticError.variable_is_not_a_list(self.ID)
        
        else:
            program.semanticError.symbol_variable_not_found(self.ID)
        '''


