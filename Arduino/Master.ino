//Master

#include <SPI.h>

#define bp 3

const int slaveSelect = 10;

void setup() {

  SPI.begin();
  pinMode(MISO, OUTPUT);
  pinMode(slaveSelect, OUTPUT);
  pinMode(bp, INPUT_PULLUP);
  Serial.begin(9600);
  SPCR |= _BV(SPE);
  
}

void loop() {
  
  if (digitalRead(bp) == 0){
    
    digitalWrite(slaveSelect, 0);
    SPI.transfer('B');
    delay(100);
    digitalWrite(slaveSelect, 1);
    
  }
  byte in_byte;

  // SPIF indicates transmission complete (byte received)

  if ((SPSR & (1 << SPIF)) != 0)
  {
    in_byte = SPDR;

    SPDR = 20;  // valeur qu'on envoie
  }
  
  byte data[] = {0x11, 0x00, 0x00, 0x00};  // 24 bits (8bits/octets * 4 octets)
  // envoie de 24 bits de data
  for (int i=0; i<4; i++) {
    SPI.transfer(data[i]);   // envoi 8 bits
  }
}


