# NOTES python

ports SPI de la RPI travaillent en 3.3V 
arduino à 5V

Possibilité d'utilisé un logic level convertor entre la rasp et l'arduino. Par exemple le "4-channel I2C-safe Bi-directional Logic Level Converter - BSS138" fait pour l'I2C mais fonctionne très bien pour le SPI jusqu'a 2MHz

utilisation de la librairie spidev

Pin rasp:

MOSI - pin 19
MISO - pin 21
SCLK - pin 23
CE0 - pin 24
CE1 - pin 26
Ground - pin 25 

Fonctions de la bibliothèque SPI : 

bits_per_word  
Description: nombre de bits par transfert (généralement 8).  
8 ou 16    ex : bits_per_word=8 

close  
Syntax: close()  
Retournes: Rine  
Description: désactive l’interface.  

cshigh  
Description: indique si CS est actif à l’état haut (généralement CS est actif à l’état bas) 
ex : cehight=false  

loop  
Description: boucle pour tester l’interface. Ex loop=false 

lsbfirst  
Si le poids faible doit être transmis en premier  
ex : lsbfirst=false 
 
max_speed_hz  
Description: Vitesse de transfert en Hz 
ex : max_speed=100000  

mode  
Polarité du bus SPI : [CPOL|CPHA]  (voir data sheet du périphérique) 
x est compris entre 0b00 = 0 .. 0b11 = 3     ex : mode=0 

open  
Syntaxe: open(bus, device)  
Description: active SPI (0 ou 1). Device est le numéro du CS (0 ou 1)  

readbytes  
Syntaxe: read(x)  
Retourne: [values]  
Description: Lit x octets sur l’esclave.  
 
threewire  
Description: Propriété des périphériques ne disposant que d’une ligne I/O (voir datasheet du périphérique) 
ex : threewire=Thrue 

writebytes  
Syntaxe: write([values])  
Retournes: rien 
Description: Ecrit un octet vers l’esclave.  
 
Retourne: [values]  
Description : Echange les données Maitre‐Esclave, CS repasse à l’état haut entre les octets. Tempo en μsec 
entre les octets 

xfer2  
Syntaxe: xfer2([values])  
Retourne: [values]  
Description: Echange les données Maitre‐Esclave, CS reste à l’état bas entre les octets
