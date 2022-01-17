
##### Code fonctionnel pour reception de décimaux

import spidev
import RPi.GPIO as GPIO
import time

LED = 21
GPIO.setmode(GPIO.BCM) #on utilise les numéro des broches (pas des GPIO)
GPIO.setup(LED,GPIO.OUT) #broche 21 en sortie

spi_bus = 0

spi_device = 0 # first device

spi = spidev.SpiDev()

spi.open(spi_bus, spi_device)

spi.max_speed_hz = 1000000
# Send a null byte to check for value

send_byte = 0x80

rcv_byte = spi.xfer2([send_byte])

# repeat to check for a response

rcv_byte = spi.xfer2([send_byte])

data_recv = rcv_byte[0]

if (data_recv != 0x80):
	print("ready to communicate"+str(data_recv)) 
	print(data_recv) #affiche la donné envoyé par l'arduino
	GPIO.output(LED,GPIO.HIGH)
	time.sleep(2) #allume et éteint une LED 
	GPIO.output(LED,GPIO.LOW)
	quit()


