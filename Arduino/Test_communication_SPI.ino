#include <SPI.h>

const int SlaveSelect = 10; //pin du Slave Select
// MOSI -> pin 11
// MISO -> pin 12
// SCK  -> pin 13

//Arduino is the Master

void setup() {
  
  Serial.begin(9600);
  pinMode(SlaveSelect, OUTPUT);
  digitalWrite(SlaveSelect, 1);
  SPI.begin();

}

void loop() {

  delay(1000);
  
  digitalWrite(SlaveSelect, 0);
  
  SPI.transfer("01000001"); //Envoie lettre A
  Serial.println("A : 01000001");

  digitalWrite(SlaveSelect, 1);
  
  while(1);

}
