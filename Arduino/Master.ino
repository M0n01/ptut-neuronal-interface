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
}
