#edit for soil sensor

import smbus
from time import sleep
import soil_i2c
import RPi.GPIO as GPIO

channel = 1 #I2C chennel1 is connected to the GPIO pins
address = 0x38 # Soil sensor address default
bus = smbus.SMBus(channel) #initialize I2C (SMBus)

#trigger reading
pinpow = 8 #pin to output 3.3V (HIGH)
GPIO.setmode(GPIO.BCM) #setup gpio
GPIO.setup(pinpow, GPIO.OUT)

soil = soil_i2c.Soil(bus, address)
#display on screen some readings
while 1:
	#print(bus.process_call(address,0,0x00))
	#bus.write_byte(address, 0x01) #turns on LED
	print(soil)
	GPIO.output(pinpow, 1) #turn on i2cpin
	sleep(2)
	soil.ledOn()
	sleep(2)
	print(soil.read())
	sleep(2)
	soil.ledOff()
	GPIO.output(pinpow, 0) #turn off i2cpin
	sleep(10)
