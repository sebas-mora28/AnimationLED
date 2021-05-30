import time
import serial
ser=serial.Serial("COM3",9600)

def prueba():
    cont=0
    #while(cont<10):
    cad="111"
    ser.write(cad.encode('ascii'))
    time.sleep(3)
    cad="211"
    ser.write(cad.encode('ascii'))
    time.sleep(3)

def cerrar():
    ser.close()
    
