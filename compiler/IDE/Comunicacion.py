import time
import serial
ser=""

def enviar(cadena):
    time.sleep(2)
    ser.write(cadena.encode('ascii'))

    
def abrir():
   global ser
   ser=serial.Serial("COM3",9600)
   
def cerrar():
    ser.close()
    

