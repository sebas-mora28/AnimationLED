



class Symbol:

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


class SymbolTable:

    def __init__(self):
        self.symbol_table = {}


    def add_symbol(self, ID, value, symbol_type, scope):
        new_symbol = Symbol(ID, value, symbol_type, scope)
        symbol_table[ID] = new_symbol

    def get_symbol_by_ID(self , ID):
        return self.symbol_table[ID]
     