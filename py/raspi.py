
##### Code fonctionnel pour reception de décimaux

from re import S
import spidev
import RPi.GPIO as GPIO
import time

LED = 21
GPIO.setmode(GPIO.BCM) #on utilise les numéro des broches (pas des GPIO)
GPIO.setup(LED,GPIO.OUT) #broche 21 en sortie

tram = [] #tableau stockant toutes les trams reçu en fin de communication
tps_com = 10 #durée de la communication (nombre de trams que l'on va recevoir)

spi_bus = 0

spi_device = 0 # first device

spi = spidev.SpiDev()

spi.open(spi_bus, spi_device)

spi.max_speed_hz = 1000000
# Send a null byte to check for value

for i in range(tps_com):
	send_byte = 0x80

	rcv_byte = spi.xfer2([send_byte])

	# repeat to check for a response

	rcv_byte = spi.xfer2([send_byte])

	data_recv = rcv_byte[0]
	if (data_recv != 0x80):
		print("ready to communicate"+str(data_recv)) 
		print(data_recv) #affiche la donné envoyé par l'arduino
		tram.append(bin(data_recv))
		quit()

for i in range(len(tram)):
	print(tram[i])


	# transmission d'un nombre binaire en python
	# on prendra un nombre en hexa quelconque 

#	a = bin(0x1) # on envoie 0x1 en binaire sous la forme '0b1' -> le 0b car binaire
#	a = a[2::] # supprime le 0b pour obtenir que le nombre binaire
#	print(a) # a = 1

#	b = bin(0x0) # ici on envoie 0 en binaire 
#	b = b[2::]
#	print(b)

	# on a ainsi des bit 1 et 0 que l'on peut envoyer à la suite
	# il faut juste traduire en language C pour arduino
