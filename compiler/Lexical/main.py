import sys
sys.path.append("..")
from Lexical.lexer import *


def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)





file = open('example.txt', 'r')
compile(file.read())
file.close()