
send_byte = 0x80 #arduino should echo back

rcv_byte = spi.xfer2([send_byte])#the transfer method that works with the arduino

# repeat to check for a response

rcv_byte = spi.xfer2([send_byte])

data_recv = rcv_byte[0]

if (data_recv != 0x80):

    print ("communication error")
    quit()

#library

import spidev  
import RPi.GPIO as GPIO
import time

LED = 21
GPIO.setmode(GPIO.BCM) #on utilise les numéro des broches (pas des GPIO)
GPIO.setup(LED,GPIO.OUT) #broche 21 en sortie

# active le BUS SPI  

spi = spidev.SpiDev()   #nouvel objet SPI 
spi.open(0,0)  # connexion dispo sur port GPIO SPI 0 CS 0 
spi.max_speed_hz = 1000000  # vitesse en Hz (1MHz)

spi2 = spidev.SpiDev()
spi2.open(0, 1)# sur port SPI 0 CS 1 
spi2.max_speed_hz = 976000


if spi.readbytes(1) != 0:
    #LED ON pendant 5 secondes
    GPIO.output(LED,GPIO.HIGH)
    time.sleep(5)
    GPIO.output(LED,GPIO.LOW)
else:
    GPIO.output(LED,GPIO.LOW)

spi.close() # ferme le peripherique