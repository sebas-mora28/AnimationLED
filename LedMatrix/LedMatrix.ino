
// array de pines de las filas
const int filas[8]={
  2, 7, 19, 5, 13, 18, 12, 16
  };

// array de pines de las columnas 
const int columnas[8]={
  6, 11, 10, 3, 17, 4, 8, 9
  };
//Matriz de leds
int leds[8][8];
const int H=1;
const int L=0;

void setup() {
  Serial.begin(9600); 
  //Se inicializan los pines como OUTPUT
  for (int pin=0;pin<8;pin++){
    pinMode(columnas[pin],OUTPUT);
    pinMode(filas[pin],OUTPUT);
    //Se ponen las columnas en HIGH para apagar todos los leds
    digitalWrite(filas[pin],H);
    }

   //Se inicializa la matriz de led
   for (int x = 0; x < 8; x++) {
    for (int y = 0; y < 8; y++) {
      leds[x][y] = H;
    }
  }
}

void loop() {
  //prenderMatriz();
  //prenderColumna(4);
  //prenderColumna(0);
  //prenderColumna(7);
  //prenderFila(5);
  //prenderFila(0);
  //prenderFila(7);
  //prenderPunto(7,7);
  delay(1000);

  //apagarMatriz();
  //apagarColumna(1);
  //apagarColumna(0);
  //apagarColumna(7);  
  //apagarFila(1);
  //apagarFila(0);
  //apagarFila(7);
  //apagarPunto(7,7);
  delay(1000); 

}

void prenderMatriz(){
  for(int i=0;i<8;i++){
      prenderFila(i);
    }    
  }

void apagarMatriz(){
    for(int i=0;i<8;i++){
      apagarFila(i);
    }   
  }  
void prenderColumna(int col){
  digitalWrite(columnas[col], H);
  for(int fila=0;fila<8;fila++){
      digitalWrite(filas[fila], L);
    }
  }

void apagarColumna(int col){
  digitalWrite(columnas[col], L);
  for(int fila=0;fila<8;fila++){
      digitalWrite(filas[fila], H);
    }
  }

void prenderFila(int fil){
  digitalWrite(filas[fil], L);
  for(int columma=0;columma<8;columma++){
      digitalWrite(columnas[columma], H);
    }
  }
void apagarFila(int fil){
  digitalWrite(filas[fil], H);
  for(int columma=0;columma<8;columma++){
      digitalWrite(columnas[columma], L);
    }
  }  
void prenderPunto(int col, int fil){
  digitalWrite(filas[fil], L);
  digitalWrite(columnas[col], H);
  }

  
void apagarPunto(int col, int fil){
  digitalWrite(filas[fil], H);
  digitalWrite(columnas[col], L);
  //Serial.print(1);
  }
