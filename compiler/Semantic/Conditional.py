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


    def comparation(self, program, symbolTable):
        
        if verifyType(self.iterable, str):
            self.iterable = searchSymbolByID(self.iterable, program, symbolTable).value
        
        elif verifyType(self.iterable, IndexAccess):
            self.iterable = self.iterable.getValues(program, symbolTable)

        else:
            program.semanticError.invalidIterable()


    def evalComparation(self, element):
        return eval(f"{element} {self.comparator} {self.value}")



    def eval(self, program, symbolTable):

        self.comparation(program, symbolTable)

        
        print(self.iterable)
        if verifyType(self.iterable, list):

            for element in self.iterable:
                if self.evalComparation(element):
                    for expression in self.expressions:
                        expression.eval(program, self.localSymbolTable)

        
        else:
            if self.evalComparation(self.iterable):
                for expression in self.expressions:
                            expression.eval(program, self.localSymbolTable)



