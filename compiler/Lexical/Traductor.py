import sys

class Traductor():
    def __init__(self, output) -> None:
        self.output = output
        self.code = ""
    def getValuesM(self, datos):
        temp = datos.split("[")
        generado = ""
        for t in temp:
            generado += t
        temp = generado.split("]")
        generado = ""
        for t in temp:
            generado += t
        temp = generado.split(",")
        generado = ""
        for t in temp:
            if t == "True" or t == " True":
                generado += "1"
            else:
                generado += "0"
        return generado
        

    def getValues(self, lista):
        temp = lista[1: len(lista)-1]
        valores = temp.split(",")
        output = ""
        for v in valores:
            if v == "True" or v == " True":
                output += "1"
            else:
                output += "0"
        return output
    def codeBlink(self, datos):
        self.code += "8" + datos[5]+ datos[2]+datos[1]+ datos[3]
    def codeDelay(self,datos):
        self.code += "0" + datos[1]
    def codePrintLed(self,datos):
        self.code +="3" + datos[3] + datos[2] + datos[1]
    def codePrintLedX(self,datos):
        if datos[1]=="C":
            self.code += "6" + datos[2] + self.getValues(datos[3])
        elif datos[1] == "F":
            self.code += "5" + datos[2] + self.getValues(datos[3])
        else:
            self.code += "7" + self.getValuesM(datos[3])

    def Traducir(self):
        for instruct in self.output:
            datos = instruct.split(";")
            if datos[0] == "Blink":
                self.codeBlink(datos)
            elif datos[0] == "Delay":
                self.codeDelay(datos)
            elif datos[0] == "PrintLed":
                self.codePrintLed(datos) 
            elif datos[0] == "PrintLedX":
                self.codePrintLedX(datos)
            else:
                print("Error en el output " + datos[0]+ " no reconocido")
            self.code += "9"
        return self.code
