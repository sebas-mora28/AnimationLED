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
        'step': 'STEP',
        'range':'RANGE',
        'len':'LEN',
        'Call':'CALL',
        'Blink': 'BLINK',
        'Delay': 'DELAY',
        'PrintLed':'PRINTLED',
        'PrintLedX':'PRINTLEDX',
        'Procedure': 'PROCEDURE',
        'type':'TYPE',
    }



    tokens = [
        'ID',

        'TIMERANGE',
        'OBJECTTYPE',


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
    t_ignore  = ' \t\r'

    
    def t_INTEGER(self, t):
        r'\d+'
        t.value = int(t.value)
        return t

    def t_SPACETAB(self,t):
        r'[ \t]+'

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

    def t_LISTOPERATOR(self , t):
        r'\.(Neg|N|T)'
        t.value = t.value[1:]
        return t 

    def t_TIMERANGE(self, t):
        r'\"(Seg|Min|Mil)\"'
        t.value = t.value[1:-1]
        return t

    def t_OBJECTTYPE(self, t):
        r'\"(C|F|M)\"'
        t.value = t.value[1:-1]
        return t

    def t_LISTSHAPE(self, t):
        r'\.shape(F|C)'
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
        r"""[a-zA-Z][a-zA-Z0-9_@&?]*"""
        t.type = self.reserved.get(t.value, 'ID')
        return t
    

    def t_error(self, t):
        self.errors.append(f"Illegal character {t.value[0]} in line {t.lineno}")


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




    
