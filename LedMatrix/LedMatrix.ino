
// Para prender un led la fila debe estar en low y la columna en high.

// array de pines de las filas
const int filas[8]={
  2, 7, 19, 5, 13, 18, 12, 16
  };

// array de pines de las columnas 
const int columnas[8]={
  6, 11, 10, 3, 17, 4, 8, 9
  };
  
//Matriz 8x8 que representara la matriz de leds
int leds[8][8];

//Constantes que representan un prendido y un apagado
const int H=1;
const int L=0;

//constante para pruebas
int cont;
int incomingByte = 0;

void setup() {
  cont=0;
  Serial.begin(9600); 
  //Se inicializan los pines como OUTPUT
  for (int pin=0;pin<8;pin++){
    pinMode(columnas[pin],OUTPUT);
    pinMode(filas[pin],OUTPUT);
    
    //Se ponen las filas en HIGH para apagar todos los leds
    digitalWrite(filas[pin],H);
    }

   //Se inicializa la matriz leds con todas sus posiciones en L
   //para que todos los leds esten apagados al inicio.
   for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      leds[x][y] = L;
    }
  }
}

//Ciclo principal de ejecución
void loop() {
  if (Serial.available() > 0){
    prenderPunto(0,0);
    String input= Serial.readString();
    }
  //serialRead();
  if (cont<3000){
  
    //cuadro
    /*
    apagarColumna(7) ;
    apagarColumna(0) ;
    apagarFila(0);
    apagarFila(7);
    */
    //apagarMatriz();

    //ojo der
    prenderPunto(1,2);
    prenderPunto(2,2);
    prenderPunto(3,2);

    //ojo izq
    prenderPunto(1,5);
    prenderPunto(2,5);
    prenderPunto(3,5);

    //boca
    prenderPunto(4,1);
    prenderPunto(4,6);
    prenderPunto(5,5);
    prenderPunto(5,4);
    prenderPunto(5,3);
    prenderPunto(5,2);
    }

   if (cont>3000){
    //cambio del ojo izq
    apagarPunto(1,2);
    apagarPunto(3,2);
   
    prenderPunto(2,1);
    //prenderPunto(3,1);
   }
  if (cont>6000){
    //cuadro
    //prenderMatriz();

     //ojo izq
    apagarPunto(2,1);
    apagarPunto(2,2);
    //apagarPunto(3,1);

    //ojo izq
    apagarPunto(1,5);
    apagarPunto(2,5);
    apagarPunto(3,5);

    //boca
    apagarPunto(4,1);
    apagarPunto(4,6);
    apagarPunto(5,5);
    apagarPunto(5,4);
    apagarPunto(5,3);
    apagarPunto(5,2);
    }
  refreshScreen();
  
  //delay(1000);
  if (cont>7000){
    cont=0;
  }
  cont++;
  
}

void serialRead(){
  
  if (Serial.available() > 0) {
    // read the incoming byte:
    incomingByte = Serial.read();
    prenderPunto(0,0);

    // say what you got:
    Serial.print("I received: ");
    Serial.println(incomingByte, DEC);
  }
  }

//Función que llama a prenderfila() para poder cambiar toda la matriz de leds a H
//Entradas: NONE
//Salidas: NONE
void prenderMatriz(){
  for(int i=0;i<8;i++){
      prenderFila(i);
    }    
  }

//Función que llama a prenderfila() para poder cambiar toda la matriz de leds a L
//Entradas: NONE
//Salidas: NONE
void apagarMatriz(){
    for(int i=0;i<8;i++){
      apagarFila(i);
    }   
  } 

//Función que pone todas las posiciones de una columna de la matriz leds en H
//Entradas: 
//  col: int que representa la columna que se desea poner en H
//Salidas: NONE
void prenderColumna(int col){
  digitalWrite(columnas[col], H);
  for(int fila=0;fila<8;fila++){
      leds[fila][col]=H;
    }
  }

//Función que pone todas las posiciones de una columna de la matriz leds en L
//Entradas: 
//  col: int que representa la columna que se desea poner en L
//Salidas: NONE
void apagarColumna(int col){
  digitalWrite(columnas[col], L);
  for(int fila=0;fila<8;fila++){
      leds[fila][col]=L;
    }
  }


//Función que pone todas las posiciones de una fila de la matriz leds en H
//Entradas: 
//  fila: int que representa la fila que se desea poner en H
//Salidas: NONE
void prenderFila(int fila){
  digitalWrite(filas[fila], L);
  for(int columna=0;columna<8;columna++){
      leds[fila][columna]=H;      
    }
  }

//Función que pone todas las posiciones de una fila de la matriz leds en L
//Entradas: 
//  fila: int que representa la fila que se desea poner en L
//Salidas: NONE
void apagarFila(int fila){
  digitalWrite(filas[fila], H);
  for(int columna=0;columna<8;columna++){
      leds[fila][columna]=L;
    }
  }  


//Función que pone un punto de la matriz leds en H
//Entradas: 
//  fila: int que representa la posición y que se desea poner en H
//  col: int que representa la posición x que se desea poner en H
//Salidas: NONE
void prenderPunto(int fila, int col){
  leds[fila][col]=H;
  }

  
//Función que pone un punto de la matriz leds en L
//Entradas: 
//  fila: int que representa la posición y que se desea poner en L
//  col: int que representa la posición x que se desea poner en L
//Salidas: NONE
void apagarPunto(int fila, int col){
  leds[fila][col]=L;
  }

//Función que revisa cada fila de la matriz y en esta revisa que columna esta H
//Primero pone la fila en L para permitir que los leds de esta se enciendan,
//Si la columna esta en H en la matriz el pin de la columna se pone en H para 
//asi prender el led una vez revisada la posición vuelve a apagar la columna 
//y al final apaga la fila y pasa a la siguiente
//Entrada:NONE
//Salidas: NONE
void refreshScreen() {
  // iterate over the rows :
  for (int thisRow = 0; thisRow < 8; thisRow++) {
    // take the row pin (anode) low:
    digitalWrite(filas[thisRow], L);
    // iterate over the cols (cathodes):
    for (int thisCol = 0; thisCol < 8; thisCol++) {
      // get the state of the current pixel;
      int thisPixel = leds[thisRow][thisCol];
      // when the row is LOW and the col is HIGH,
      // the LED where they meet turns on:
      digitalWrite(columnas[thisCol], thisPixel);
      // turn the pixel off:
      if (thisPixel == H) {
        digitalWrite(columnas[thisCol], L);
      }
    }
    // take the row pin low to turn off the whole row:
    digitalWrite(filas[thisRow], H);
  }
}
