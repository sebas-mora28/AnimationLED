from Semantic.SemanticError import SemanticError
from ast import Index
from os import EX_CANTCREAT, execl, symlink
import sys
sys.path.append("..")

from Semantic.Common import * 
from Semantic.SymbolTable.SymbolTable import *
from Semantic.IndexType import *

class ForLoop(Instruction):

    def __init__(self, changingValue, iterable, step, expressions):

        self.changingValue = changingValue
        self.iterable = iterable
        self.step = step
        self.expressions = expressions
        self.localSymbolTable = SymbolTable()

    

    def eval(self, program, symbolTable):
        self.localSymbolTable.addSymbol(self.changingValue, 0, int, "local")
        if verifyType(self.changingValue, str):
            if verifyType(self.iterable, str):
                iterable = searchSymbolByID(self.iterable, program, symbolTable)
                if iterable != None:
                    if verifyType(iterable.value, list):
                        self.end = len(iterable.value)
                        self.startLoop(program, symbolTable)
                    elif verifyType(iterable.value, int):
                        self.end = iterable.value
                        self.startLoop(program, symbolTable)
                    else:
                        program.semanticError.invalidIterable()
            elif verifyType(self.iterable, IndexAccess):
                iterable = self.iterable.getValues(program, symbolTable)
                if iterable != None:
                    self.end = len(iterable)
                    self.startLoop(program, symbolTable)
            elif verifyType(self.iterable, int):
                self.end = self.iterable
                self.startLoop(program, symbolTable)
            
            else:
                program.semanticError.invalidIterable()

        else:
            program.semanticError.invalidValueLoop()
            




    def startLoop(self, program, symbolTable):
        self.localSymbolTable.print()

        if not symbolTable == program.symbolTable:
            self.localSymbolTable.attachSymboltable(symbolTable)

        for i in range(0, self.end,self.step):
            self.localSymbolTable.changeSymbolValue(self.changingValue, i)
            for expression in self.expressions:
                print("----------------------")
                self.localSymbolTable.print()
                print("-----------------------")
                expression.eval(program, self.localSymbolTable)
            i += self.step
        
  