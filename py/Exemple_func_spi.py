#!/usr/bin/env python
#
# Bitbang'd SPI interface with an MCP3008 ADC device
# MCP3008 is 8-channel 10-bit analog to digital converter
#  Connections are:
#     CLK => SCLK  
#     DOUT =>  MISO
#     DIN => MOSI
#     CS => CE0

import time
import sys
import spidev

spi = spidev.SpiDev()
spi.open(0,0)

def buildReadCommand(channel):
    startBit = 0x01
    singleEnded = 0x08

    # Return python list of 3 bytes
    #   Build a python list using [1, 2, 3]
    #   First byte is the start bit
    #   Second byte contains single ended along with channel #
    #   3rd byte is 0
    return []
    
def processAdcValue(result):
    '''Take in result as array of three bytes. 
       Return the two lowest bits of the 2nd byte and
       all of the third byte'''
    pass
        
def readAdc(channel):
    if ((channel > 7) or (channel < 0)):
        return -1
    r = spi.xfer2(buildReadCommand(channel))
    return processAdcValue(r)
        
if __name__ == '__main__':
    try:
        while True:
            val = readAdc(0)
            print("ADC Result: ", str(val))
            time.sleep(5)
    except KeyboardInterrupt:
        spi.close() 
        sys.exit(0)


"-------------------------------------------------------------------------------------------------------------------------"

#!/usr/bin/env python
#
# Bitbang'd SPI interface with an MCP3008 ADC device
# MCP3008 is 8-channel 10-bit analog to digital converter
#  Connections are:
#     CLK => 18  
#     DOUT => 23 (chip's data out, RPi's MISO)
#     DIN => 24  (chip's data in, RPi's MOSI)
#     CS => 25 

import RPi.GPIO as GPIO
import time
import sys

CLK = 18
MISO = 23
MOSI = 24
CS = 25

def setupSpiPins(clkPin, misoPin, mosiPin, csPin):
    ''' Set all pins as an output except MISO (Master Input, Slave Output)'''
    pass     

def readAdc(channel, clkPin, misoPin, mosiPin, csPin):
    if (channel < 0) or (channel > 7):
        print ("Invalid ADC Channel number, must be between [0,7]")
        return -1
        
    # Datasheet says chip select must be pulled high between conversions

    
    # Start the read with both clock and chip select low

    
    # read command is:
    # start bit = 1
    # single-ended comparison = 1 (vs. pseudo-differential)
    # channel num bit 2
    # channel num bit 1
    # channel num bit 0 (LSB)
    read_command = 0x18
    read_command |= channel
    
    sendBits(read_command, 5, clkPin, mosiPin)
    
    adcValue = recvBits(12, clkPin, misoPin)
    
    # Set chip select high to end the read


  
    return adcValue
    
def sendBits(data, numBits, clkPin, mosiPin):
    ''' Sends 1 Byte or less of data'''
    
    data <<= (8 - numBits)
    
    for bit in range(numBits):
        pass
        # Set RPi's output pin high or low depending on highest bit of data field
        
        # Advance data to the next bit
        
        # Pulse the clock pin HIGH then immediately low


def recvBits(numBits, clkPin, misoPin):
    '''Receives arbitrary number of bits'''
    retVal = 0
    
    # For each bit to receive
        # Pulse clock pin high then immediately low
        
        # Read 1 data bit in and include in retVal
        
        # Advance input to next bit
    
    # Divide by two to drop the NULL bit
    return (retVal/2)
    
    
if __name__ == '__main__':
    try:
        GPIO.setmode(GPIO.BCM)
        setupSpiPins(CLK, MISO, MOSI, CS)
    
        while True:
            val = readAdc(0, CLK, MISO, MOSI, CS)
            print ("ADC Result: ", str(val))
            time.sleep(5)
    except KeyboardInterrupt:
        GPIO.cleanup()
        sys.exit(0)