
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

String input;

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
    
    input= Serial.readString();
    }
  if (input.substring(0,1)=="1"){
     if (input.substring(1,2)=="1"){
        prenderColumna(input.substring(2,3).toInt());        
      }
      if (input.substring(1,2)=="0"){
        apagarColumna(input.substring(2,3).toInt());        
      }      
    }
   if (input.substring(0,1)=="2"){
     if (input.substring(1,2)=="1"){
        prenderFila(input.substring(2,3).toInt());        
      }
      if (input.substring(1,2)=="0"){
        apagarFila(input.substring(2,3).toInt());        
      }      
    }
    if (input.substring(0,1)=="3"){
     if (input.substring(1,2)=="1"){
        prenderPunto(input.substring(2,3).toInt(),input.substring(3,4).toInt());        
      }
      if (input.substring(1,2)=="0"){
        apagarPunto(input.substring(2,3).toInt(),input.substring(3,4).toInt());            
      }      
    }
    if (input.substring(0,1)=="4"){
     if (input.substring(1,2)=="1"){
        prenderMatriz();        
      }
      if (input.substring(1,2)=="0"){
        apagarMatriz();            
      }      
    }
    if (input.substring(0,1)=="5"){
      int y=input.substring(1,2).toInt();
      for (int i=0;i<8;i++){
        int valor=input.substring(i+2,i+3).toInt();
        leds[y][i]=valor;
        } 
    }
    if (input.substring(0,1)=="6"){
      int x=input.substring(1,2).toInt();
      for (int i=0;i<8;i++){
        int valor=input.substring(i+2,i+3).toInt();
        leds[i][x]=valor;
        } 
    }
  refreshScreen();
  
  
  
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
