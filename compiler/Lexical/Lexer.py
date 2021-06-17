import sys
sys.path.append("..")
import lex






class Lexer(object):

    def __init__(self):
        self.lexer = lex.lex(object=self)
        self.errors = []


    reserved = {

        'if' : 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'in': 'IN',
        'Step': 'STEP',
        'range':'RANGE',
        'len':'LEN',
        'Call':'CALL',
        'Blink': 'BLINK',
        'Delay': 'DELAY',
        'PrintLed':'PRINTLED',
        'PrintLedX':'PRINTLEDX',
        'Procedure': 'PROCEDURE',
        'type':'TYPE',
        'list':'LIST',
        'print':'PRINT',
    }



    tokens = [
        'ID',
        
        'STRING',


        # Data types 
        'INTEGER',
        'BOOLEAN',


        #Literals
        'PLUS', 
        'MINUS',
        'TIMES',
        'DIVIDE',
        'POWER',
        'MODULE',
        'DIVIDEENTIRE',
        'COMPARATOR',
        'COLON',
        'SEMICOLON',
        'COMMA',
        'ASSIGN',
        'EQUAL',
        'LPAREN',
        'RPAREN',
        'LSBRACKET',
        'RSBRACKET',
        'LCBRACKET',
        'RCBRACKET',
    
        #List
        'INSERT',
        'DELETE',
        'LISTOPERATOR',
        'LISTSHAPE'





        ] + list(reserved.values())


    t_PLUS    = r'\+'   
    t_MINUS   = r'-'
    t_TIMES   = r'\*'
    t_POWER   = r'\*\*'
    t_DIVIDEENTIRE = r'//'
    t_MODULE = r'\%'
    t_DIVIDE  = r'/'
    t_LPAREN  = r'\('
    t_RPAREN  = r'\)'
    t_LSBRACKET = r'\['
    t_RSBRACKET = r'\]'
    t_LCBRACKET = r'\{'
    t_RCBRACKET = r'\}'
    t_SEMICOLON = r'\;'

    t_COMMA = r'\,'
    t_COLON = r'\:'
    t_ASSIGN =  r'\='

    
    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_SPACETAB(self,t):
        r'[ \t]+'
        pass

    def t_newline(self, t):
        r"""[\n]"""
        t.lexer.lineno += 1
        pass

    def t_INSERT(self , t):
        r'\.insert'
        return t 

    def t_DELETE(self, t):
        r'\.del'
        return t
    
    def t_LISTSHAPE(self, t):
        r'\.shape(C|F)'
        return t

    def t_LISTOPERATOR(self , t):
        r'\.(Neg|F|T|)'
        t.value = t.value[1:]
        return t 
    
    def t_STRING(self, t):
        r'["]{1}[^"]*["]{1}'
        print(t.value)
        t.value = t.value[1:len(t.value) - 1]
        return t

    def t_COMMENT(self, t):
        r'\#.*'
        pass 

    def t_BOOLEAN(self, t):
        r'True|False'
        if(t.value == "True"):
            t.value = True
        else: 
            t.value = False
        return t


    def t_COMPARATOR(self, t):
        r'<\=|>\=|=\=|!\=|<|>'
        return t

    def t_ID(self, t):
        r'[a-zA-Z][a-zA-Z0-9_@?]*'
        current = self.reserved.get(t.value, 'ID')
        if len(t.value) > 10:
            self.t_error(t)
            return 
        if current == 'ID' and not t.value == "Main":
            if t.value[0].isupper():
                self.t_error(t)
        t.type = current
        return t


    #def t_invalid(self, t):
    #    r'.[a-zA-Z]'
    #    pass
    

    def t_error(self, t):
        self.errors.append(f"Lexical error: Illegal character {t.value} in line {t.lineno}")


    def input(self, sourceCode):
        self.lexer.input(sourceCode)
    
    def token(self):
        return self.lexer.token()


    
    def lexicalAnalysis(self, data):
        self.lexer.input(data)


        while True:
            tok = self.lexer.token()
            if not tok:
                break
            




    
