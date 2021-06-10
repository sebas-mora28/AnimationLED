import time
import serial
ser=serial.Serial("COM3",9600)

def prueba():
    cont=0
    #while(cont<10):
    cad="70000000001000100010001000111110001000100010001000000000000000000902970000000000111000010001000100010001000100001110000000000000000000902970000000001000000010000000100000001000000011111000000000000000000902970000000000010000001010000100010001111100010001000000000000000000902970000000000100100001001000010010000000000010000100011110000000000"
    ser.write(cad.encode('ascii'))
    time.sleep(2)
    print(cad.encode('ascii'))


    

def cerrar():
    ser.close()
    
#02 delay de 2 segundos 
#113 prende la dolumna 3
#213 prende la fila 3
#3122 prende el led en 2,2
#41 prende toda la matriz
#5211001110 prende la fila 2 con los respectivos valores
#6411001110 prende la columna 4 con los respectivos valores
#71010110101011010110100101010010100111001100111011111111110010100
    #manda cada valor de led a la matriz
#81332 hace que el led 3,3 este en blink el segundo digito indica si esta on o off
    #del 4 digito en adelante es el tiempo de activación 
#9 esto es un separador, va desopues de cada indicación
