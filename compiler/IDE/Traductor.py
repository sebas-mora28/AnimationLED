import sys
sys.path.append("..")
#Clase encargada de la traduccion del codigo
class Traductor():
    # Constructor, recibe la lista de instrucciones generadas por el compilador
    def __init__(self, output) -> None:
        self.output = output
        self.code = ""
    # Funcion que obtiene los valores de la matriz y los convierte en 0 y 1
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
        
    #Funcion que toma los valores de las listas y los transforma en 0 y 1
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
    # Funcion que traduce la instruccion blink a en un formato para enviar a arduino
    # datos: lista con los datos de la instruccion
    def codeBlink(self, datos):
        self.code += "8" + datos[5]+ datos[2]+datos[1]+ datos[3]
    # Funcion que traduce la instruccion Delay a en un formato para enviar a arduino
    # datos: lista con los datos de la instruccion
    def codeDelay(self,datos):
        self.code += "0" + datos[1]
    # Funcion que traduce la instruccion PrintLed a en un formato para enviar a arduino
    # datos: lista con los datos de la instruccion
    def codePrintLed(self,datos):
        self.code +="3" + datos[3] + datos[2] + datos[1]
    # Funcion que traduce la instruccion PrintLedX a en un formato para enviar a arduino
    # datos: lista con los datos de la instruccion
    def codePrintLedX(self,datos):
        if datos[1]=="C":
            self.code += "6" + datos[2] + self.getValues(datos[3])
        elif datos[1] == "F":
            self.code += "5" + datos[2] + self.getValues(datos[3])
        else:
            self.code += "7" + self.getValuesM(datos[3])
    # Funcion encargada de enviar a traducion cada instruccion de la lista de instrucciones
    # Toma la instruccion y la divide por punto y coma
    #Analiza el primer elemento y dependiendo de lo obtenido envia a su respectiva traduccion
    def Traducir(self):
        for instruct in self.output:
            datos = instruct.split(";")#divide el string por punto y coma
            if datos[0] == "Blink": # analiza la primera posicion de la nueva lista
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
