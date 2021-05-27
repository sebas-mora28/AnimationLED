import time
import serial
ser=serial.Serial("COM3",9600)

def prueba():    
    cad="1"
    ser.write(cad.encode('ascii'))
    
    
