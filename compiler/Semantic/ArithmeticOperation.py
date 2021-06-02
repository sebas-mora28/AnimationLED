import sys
sys.path.append("..")

from Semantic.Common import * 



class ArithmeticOperation(Instruction):

    def __init__(self, operation):

        self.operation = operation

    


    def eval(self, program, symbolTable):

        value = self.solveOperation(program, symbolTable)
        if value !=None:
            return value



        

    
    def solveOperation(self, program, symbolTable):

        for i in range(len(self.operation)):
            if self.operation[i].isalpha() == True:
                symbol = searchSymbolByID(self.operation[i], program, symbolTable)
                if symbol != None:
                    if verifyType(symbol.value, int):
                        self.operation = self.operation[:i] + str(symbol.value) + self.operation[i+1:]
                    else:
                        program.semanticError.incompatibleType(symbol.ID)
                        return None
                else:
                    return None
        
        return int(eval(self.operation))
            