import sys
sys.path.append("..")
import lex


class Lexer(object):

    def __init__(self):
        self.lexer = lex.lex(object=self)


    reserved = {

        'if' : 'IF',
        'then': 'THEN',
        'else': 'ELSE',
        'while': 'WHILE',
        'for': 'FOR',
        'begin':'BEGIN',
        'end': 'END',
        'in': 'IN',
        'step': 'STEP',

        'list':'LIST',
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

    
    def t_newline(self, t):
        r'\n+'
        t.lexer.lineno += len(t.value)



    def t_INSERT(self , t):
        r'\.insert'
        return t 


    def t_DELETE(self, t):
        r'\.del'
        return t



    def t_LISTOPERATOR(self , t):
        r'\.(T|F|Neg)'
        return t 



    def t_TIMERANGE(self, t):
        r'\"(Seg|Min|Mil)\"'
        t.value = t.value[1:-1]
        return t



    def t_OBJECTTYPE(self, t):
        r'\ "C"|"F"|"M"'

    def t_LISTSHAPE(self, t):
        r'\.shape( F | C)'
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
        print("Illegal character '%s' in line '%d'" ,t.value[0], t.lineno)
        t.lexer.skip(1)


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
            print(tok)





    
    
    