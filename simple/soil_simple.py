#edit for soil sensor

import smbus
from time import sleep
import soil_i2c

channel = 1 #I2C chennel1 is connected to the GPIO pins
address = 0x18 # Soil sensor address default
bus = smbus.SMBus(channel) #initialize I2C (SMBus)

soil = soil_i2c.Soil(bus, address)
#display on screen some readings
while 1:
	#print(bus.process_call(address,0,0x00))
	#bus.write_byte(address, 0x01) #turns on LED
	print(soil)
	soil.ledOn()
	sleep(2)
	print(soil.read())
	sleep(2)
	soil.ledOff()
	sleep(2)
