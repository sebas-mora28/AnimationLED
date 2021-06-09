import sys
sys.path.append("..")

from Semantic.Common import * 



class ArithmeticOperation(Instruction):

    def __init__(self, operation):

        self.operation = operation

    


    def eval(self, program, symbolTable):

        value = self.solveOperation(self.operation,program, symbolTable)
        if value !=None:
            return value



        

    
    def solveOperation(self, operation, program, symbolTable):
        for i in range(len(operation)):
            if operation[i].isalpha() == True:
                symbol = searchSymbolByID(operation[i], program, symbolTable) 
                if symbol != None:
                    if verifyType(symbol.value, int):
                        operation = operation[:i] + str(symbol.value) + operation[i+1:]
                    else:
                        program.semanticError.incompatibleType(symbol.ID)
                        return None
                else:
                    return None
        
        return int(eval(operation))





class MathOperation:

    def __init__(self, left, operator, right):

        pass