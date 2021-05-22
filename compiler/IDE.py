import sys
sys.path.append("..")
from tkinter import *
from Lexical.lexer import *
from Syntax.syntax import *

root = Tk()
root.geometry("900x600")



def compile(code):
    lexer = Lexer()
    lexer.lexicalAnalysis(code)
    result = systaxAnalysis(code, lexer)



canvas = Canvas(root, width=900, height=600)
canvas.place(x=0, y=0)




codePad = Text(canvas, width=105, height=20)
codePad.place(x=20, y=30)







compileButton = Button(canvas, width=5,text="Compile", command=lambda: compile(codePad.get("1.0", END)))
compileButton.place(x=20, y=500) 



#root.mainloop()
