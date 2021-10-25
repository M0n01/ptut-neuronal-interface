//Master

#include <SPI.h>

#define bp 3

const int slaveSelect = 10;

void setup() {

  SPI.begin();
  pinMode(slaveSelect, OUTPUT);
  pinMode(bp, INPUT_PULLUP);
  Serial.begin(9600);
  
}

void loop() {
  
  if (digitalRead(bp) == 0){
    
    digitalWrite(slaveSelect, 0);
    SPI.transfer('B');
    delay(100);
    digitalWrite(slaveSelect, 1);
    
  }
}
