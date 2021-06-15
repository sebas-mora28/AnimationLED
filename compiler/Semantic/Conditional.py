from Semantic.SymbolTable.SymbolTable import SymbolTable, SymbolVariable
from Semantic.IndexType import IndexAccess
import sys 
sys.path.append("..")

from Semantic.Common import *



class If(Instruction):

    def __init__(self, iterable, comparator, value, expressions):
        self.iterable = iterable
        self.comparator = comparator
        self.value = value
        self.expressions = expressions
        self.localSymbolTable = SymbolTable()
        self.continueEvaluating = True


    
    def verifyComparation(self, program, symbolTable):
        
        if verifyType(self.iterable, str):

            self.evaluatedIterable = searchSymbolByID(self.iterable, program, symbolTable).value
        
        elif verifyType(self.iterable, IndexAccess):

            self.evaluatedIterable = self.iterable.getValues(program, symbolTable)

        else:

            self.evaluatedIterable = None
            self.continueEvaluating = False
            program.semanticError.invalidIterable()
    
    def evalComparation(self, program, element):


        if verifyType(element, bool) and verifyType(self.value, bool):

            if self.comparator == "==" or self.comparator == "!=":

                return eval(f"{element} {self.comparator} {self.value}")

            else:

                program.semanticError.invalidComparatorBoolean()

        
        elif verifyType(element, int) and verifyType(self.value, int):

            return eval(f"{element} {self.comparator} {self.value}")
        
        else:

            self.continueEvaluating = False
            program.semanticError.IncompatibleIteratorAndValuesInIf()




    def eval(self, program, symbolTable):

        if program.symbolTable != symbolTable:
            self.localSymbolTable.attachSymboltable(symbolTable)


        self.verifyComparation(program, symbolTable)
        error_len  = len(program.semanticError.getErrors())
     

        if self.evaluatedIterable != None:


            if verifyType(self.evaluatedIterable, list):


                for element in self.evaluatedIterable:
                    evaluatedComparation = self.evalComparation(program, element)


                    if evaluatedComparation:


                        for expression in self.expressions:

                            if error_len == len(program.semanticError.getErrors()):

                                expression.eval(program, self.localSymbolTable)

                            else:

                                print(len(program.semanticError.getErrors()))
                                break


                    elif evaluatedComparation == None:
                        break
            else:
                
                if self.evalComparation(program, self.evaluatedIterable):

                    for expression in self.expressions:

                        if error_len == len(program.semanticError.getErrors()) and self.continueEvaluating:
                                expression.eval(program, self.localSymbolTable)

                        else:
                            break
                            



