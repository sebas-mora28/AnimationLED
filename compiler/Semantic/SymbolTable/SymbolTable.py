


class SymbolVariable:

    def __init__(self, ID, value, symbol_type, scope):
        self.ID = ID
        self.value = value 
        self.type = symbol_type
        self.scope = scope


    def getID(self):
        return self.ID
    
    def getValue(self):
        return self.value 
    
    def getType(self):
        return self.type 

    def getScope(self):
        return self.scope


class SymbolProcedure:

    def __init__(self, ID, procedure):
        self.procedure = procedure
        self.ID = ID

    def getID(self):
        return ID
    
    def getProcedure(self):
        return self.procedure


class SymbolTable:

    def __init__(self):
        self.variableTable = {}
        self.procedureTable = {}


    def addSymbol(self, ID, value, symbol_type, scope):
        new_symbol = SymbolVariable(ID, value, symbol_type, scope)
        self.variableTable[ID] = new_symbol

    def getSymbolByID(self , ID):
        return self.variableTable[ID]

    def addProcedureSymbol(self, ID, procedure):
        new_procedure = SymbolProcedure(ID, procedure)
        self.procedureTable[ID] = new_procedure

    def changeSymbolValue(self, ID, value):
        temp = self.variableTable[ID]
        temp.value = value


    def getProcedureByID(self, ID):
        try:
            return self.procedureTable[ID] 
        except KeyError:
            return None

    def exist(self, ID):
        return ID in self.variableTable



    def print(self):
        for key in self.variableTable:
            var = self.variableTable[key]

            print(f"ID : {var.ID} value : {var.value} scope : {var.scope}")

    
     