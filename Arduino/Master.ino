//Master

#include <SPI.h>

#define bp 3

const int slaveSelect = 10;
unsigned char tps_com[5];

void setup() {

  SPI.begin();
  pinMode(slaveSelect, OUTPUT);
  pinMode(bp, INPUT_PULLUP);
  Serial.begin(9600);

  tps_com[0] = 0b10010011;
  tps_com[1] = 0b01110101;
  tps_com[2] = 0b10011010;
  tps_com[3] = 0b01010100;
  tps_com[4] = 0b01100011;

}

void loop() {
  
  if (digitalRead(bp) == 0){
    
    digitalWrite(slaveSelect, 0);
    
    for (int i = 0; i < 5; i++){
      SPI.transfer(tps_com[i]);
      delay(10);
    }

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

