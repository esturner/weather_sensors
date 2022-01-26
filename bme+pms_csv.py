'''
bme+pms_csv.py

uses the bme280 and the pms5003 sensors to detect temperature, pressure, humidity, and
and particle size.

script generates a csv of all this data
'''

#import sensors
from pms5003 import PMS5003
import bme280
import smbus2

#timing
import time
from time import sleep
from datetime import datetime


import sys
import os

#file for saving data
filename = 'data_weather_sensors_11_30'
filewrite=open(filename + '.csv', 'a')
if os.stat(filename + '.csv').st_size == 0:
	filewrite.write('Time, humidity, pressure, temperature, counts of .3, counts of .5, counts of 1.0 counts of 2.5, counts of 10\n')
filewrite.close()

#i2c ---------------------------------------
port = 1
address = 0x76 #BME280 address - system specific. Other BME 280s may be diff
bus = smbus2.SMBus(port)

#calibration from bme lib
bme280.load_calibration_params(bus, address)

#pms setup----------------------------------
pms5003=PMS5003(
	device = '/dev/ttyAMA0',
	baudrate=9600,
	pin_enable=22, 
	pin_reset=27
)
i = 0
interval = 10  #minutes
duration = 2*60 #minutes
while (i*interval)<duration:
	now = datetime.now() #get current time
	part_dat = pms5003.read()
	bme_dat = bme280.sample(bus,address)
	humidity = bme_dat.humidity
	pressure = bme_dat.pressure
	ambient_temperature = bme_dat.temperature
	print(bme_dat)
	print(part_dat)
	#write to file
	with open(filename + '.csv', 'a') as filewrite:
		filewrite.write(f"{now}, {humidity}, {pressure}, {ambient_temperature}, \
		{part_dat.pm_per_1l_air(.3)}, {part_dat.pm_per_1l_air(.5)},\
		{part_dat.pm_per_1l_air(1.0)}, {part_dat.pm_per_1l_air(2.5)}, \
		{part_dat.pm_per_1l_air(10)}\n")
	sleep(interval*60) #convert to seconds
	i += 1
