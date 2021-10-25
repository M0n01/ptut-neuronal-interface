//Slave

#include <SPI.h>

#define led 3

bool flag=0;
byte s_recv;
int el = 0;

void setup() {
 
  Serial.begin(9600);
  pinMode(MISO, OUTPUT);
  pinMode(led, OUTPUT);

  SPCR = (1<< SPE)|(1<< SPIE);
}

ISR (SPI_STC_vect) {
  s_recv = SPDR;
}

void loop() {

 if (char(s_recv) == 'B') {
  el++;
  digitalWrite(led, el%2);
  Serial.print(char(s_recv));
  s_recv = 'A';
  }
 

}
