

from Semantic.ListFunctions import Len
from copy import deepcopy


class SemanticError:

    def __init__(self):
        self.errors = []

    def printErrors(self):
        for i in range(len(self.errors)):
            print(self.errors[i])


    def getErrors(self):
        return self.errors

    def addError(self, error):
        self.errors.append(error)


    #Main errors 
    def mainNotFound(self):
        self.errors.append(f"Semantic error: Main not found")

    def mainCannotReceiveParameter(self):
        self.errors.append(f"Semantic error: Main cannot receive parameters")

    def mainMultipleDefinition(self):
        self.errors.append(f"Semantic error: Main multiple definition")


    # if error 

    def invalidComparatorBoolean(self):
        self.errors.append(f"Semantic error: Invalid comparator for booleans")

    def IncompatibleIteratorAndValuesInIf(self):
        self.errors.append(f"Semantic error: Incompatible iterator and value in if statement")
  

    #Arithmetic operation errors

    def invalidArithmeticOperationValue(self):
        self.errors.append(f"Semantic error: Invalid value in arithmetic operation, value is not a integer")




    # Variables and procedures errors
    def symbolNotFound(self, ID):
        self.errors.append(f"Semantic error: Symbol {ID} not found")

    def invalidMultipleAssignment(self):
        self.errors.append(f"Semantic error: Invalid multiple assignment")
    
    def invalidSymbolType(self, ID):
        self.errors.append(f"Semantic error: Incompatible type in symbol {ID}")

    def invalidAmountOfParameters(self, parameters, arguments):
        self.errors.append(f"Semantic error: Expect {parameters} arguments given {arguments}")

    def isNotAProcedure(self, ID):
        self.errors.append(f"Semantic error: {ID} is not a procedure")

    def procedureNotFound(self, ID):
        self.errors.append(f"Semantic error: Procedure {ID} not found")
    
    def procedureSignNotFound(self, ID, numParameters):
        self.errors.append(f"Semantic error: Procedure {ID} with {numParameters} parameters not found")

    def incompatibleType(self, ID):
        self.errors.append(f"Semantic error: Incompatible type in variable {ID}")

    def sameProcedureSign(self, ID):
        self.errors.append(f"Semantic error: Procedure sign duplicate in {ID} procedure")

    def invalidListValue(self):
        self.errors.append(f"Semantic error: Invalid list value, must be a bool")
    
    # List functions
    def isNotAMatrix(self, ID):
        self.errors.append(f"Semantic error: {ID} is not a matrix")

    def indexOutRange(self, ID):
        self.errors.append(f"Semantic error: Index out of range in {ID}")

    def invalidIndexArguments(self, ID):
        self.errors.append(f"Semantic error: Invalid index value in {ID}")


    #Insert and delete list

        #Insert
    def invalidIndexValueInsert(self, ID):
        self.errors.append(f"Semantic error: Invalid index argument in insert procedure for {ID}, must be a integer")

    def invalidValueInsertList(self, ID):
        self.errors.append(f"Semantic error: Invalid value argument insert procedure for {ID}, must be a boolean")

    def insertListProcedureError(self, ID):
        self.errors.append(f"Semantic error: insert procedure only applicable in list, {ID} is not a list")

    def insertIndexOutRange(self, ID):
        self.errors.append(f"Semantic error: Index out of range in insert function for {ID} symbol")


    #delete 

    def invalidIndexValueDelete(self, ID):
        self.errors.append(f"Semantic error: Invalid index argument in delete procedure for {ID}, must be a integer")

    def deleteIndexOutRange(self, ID):
        self.errors.append(f"Semantic error: Index out of range in delete function for {ID} symbol")

    def deleteListProcedureError(self, ID):
        self.errors.append(f"Semantic error: delete procedure only applicable in list, {ID} is not a list")


    # Insert and delete matrix


    #insert 
    def invalidInsertionTypeValueInsertMatrix(self, ID):
        self.errors.append(f"Semantic error: Invalid index argument in insert procedure for {ID}, must be a integer")

    def invalidValueInsertMatrix(self, ID):
        self.errors.append(f"Semantic error: Invalid value argument in insert procedure for {ID}, must be a list")

    def invalidColumnDimensions(self, ID):
        self.errors.append(f"Semantic error: Invalid dimensions, trying to insert a list with diferent number of columns in {ID} symbol")

    def invalidRowDimensions(self, ID):
        self.errors.append(f"Semantic error: Invalid dimensions, trying to insert a list with diferent numbers of rows in {ID} symbol")

    def invalidColumnValueFormatInsert(self, ID):
        self.errors.append(f"Semantic error: Invalid column value format in insert function for {ID} symbol, must be [ [ ..] [..] [..] ]")

    def invalidRowValueFormatInsert(self, ID):
        self.errors.append(f"Semantic error: Invalid row value format in insert function for {ID} symbol, must be [ [ ... ] ]")

    def invalidInsertionTypeRange(self, ID):
        self.errors.append(f"Semantic error: Insertion type must be 0 or 1")  


    # Delete
    def deleteMatrixProcedureError(self, ID):
        self.errors.append(f"Semantic error: insert procedure only applicable in matrix, {ID} is not a matrix")

    def invalidInsertionTypeValueDeleteMatrix(self, ID):
        self.errors.append(f"Semantic error: Invalid insertion type argument in delete procedure for {ID}, must be a integer")

    def invalidIndexDeleteMatrix(self, ID):
        self.errors.append(f"Semantic error: Invalid index argument in delete procedure for {ID}, must be a integer")

    def invalidDeleteTypeRange(self, ID):
        self.errors.append(f"Semantic error: elimination type must be 0 or 1") 

    




    def invalidDimensions(self, ID):
        self.errors.append(f"Semantic error: Trying to insert a list with diferent dimentions in {ID} symbol")

    def lenInvalidArgument(self,ID):
        self.errors.append(f"Semantic error: Argument {ID} is not a list or matrix")

    def rangeInvalidArguments(self):
        self.errors.append(f"Semantic error: Invalid argument in range function")

    def invalidIndexAccessMatrix(self, ID):
        self.errors.append(f"Semantic error: Invalid index access, {ID} is not a matrix")

    def invalidIndexAccessList(self, ID):
        self.errors.append(f"Semantic error: Invalid index access, {ID} is not a list")

    def invalidIndexAccess(self, ID):
        self.errors.append(f"Semantic error: Invalid index access, {ID} is not a list or matrix")

    def invalidIterable(self):
        self.errors.append(f"Semantic error: Invalid iterable in if statement")

    def rangeInvalidListLength(self, ID):
        self.errors.append(f"Semantic error: length list does not match with range values in {ID}")

    def booleanOperatorError(self, ID):
        self.errors.append(f"Semantic error : Invalid symbol, {ID} is not a list or matrix")




    #Reserved procedures

    #Delay 
    def delayInvalidArgumentTimeRange(self):
        self.errors.append("Semantic error: Invalid argument for timeRange. Mil, Seg, Min, is expected")

    def delayInvalidArgumentTime(self):
        self.errors.append("Semantic error: Invalid argument for time, an int is expected")
    
    #Blink
    def blinkInvalidArgumentState(self):
        self.errors.append("Semantic error: Invalid data for sate, a bool is expected")

    def blinkInvalidArgumentTimeRange(self):
        self.errors.append("Semantic error: Invalid argument for timeRange. Mil, seg, min, is expected")
    
    def blinkInvalidArgumentTime(self):
        self.errors.append("Semantic error: Invalid data for time, an int is expected")

    def blinkInvalidArgumentValue(self):
        self.errors.append("Semantic error: Invalid data for value, an int is expected")
    
    def blinkInvalidArgumentRow(self):
        self.errors.append("Semantic error: Invalid data for row, an int is expected")

    def blinkInvalidArgumentCol(self):
        self.errors.append("Semantic error: Invalid data for Col, an int is expected")



    #PrintLed 

    def printLedInvalidArgumentValue(self):
        self.errors.append("Semantic error: Invalid data for value, an int is expected")

    def printLedInvalidArgumentRow(self):
        self.errors.append("Semantic error: Invalid data for row, an int is expected")
    
    def printLedInvalidArgumentCol(self):
        self.errors.append("Semantic error: Invalid data for col an int is expected") 


    #PrintLedX
    def printLedXInvalidArgumentList(self):
        self.errors.append("Semantic error: Invalid argument for list, expected list")

    def printLedXInvalidArgumentMatrix(self):
        self.errors.append("Semantic error: Invalid argument for list, expected Matrix")

    def printLedXInvalidArgumentIndex(self):
        self.errors.append("Semantic error: Invalid index, an int is expected")
    
    def printLedXInvalidArgumentObjectType(self):
        self.errors.append("Semantic error: invalid object type. expected F,C or M")




    # Loop errors 

    def invalidIterable(self):
        self.errors.append("Semantic error: Invalid iterable in foor loop")

    def invalidValueLoop(self):
        self.errors.append("Semantic error: Invalid value in for loop")
    