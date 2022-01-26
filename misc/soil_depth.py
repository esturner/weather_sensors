'''
soil_depth.py

by Ethan Turner

script to execute measurement of soil moisure as a function of depth.

Using four sensors we interface with sensors on the same circuit to take 
measurements, print,  record to csv, and generate a plot.

Also uses BME280 to record conditions.
'''
import numpy as np
import matplotlib.pyplot as plt

import os
import time
from datetime import datetime

from weather_utils import *
from soil_i2c import *
import bme280
import smbus2

#i2c----------------------
port = 1
bus = smbus2.SMBus(port)

bme_address = 0x76
soil_1_address = 0x18
soil_2_address = 0x28
soil_3_address = 0x38
soil_4_address = 0x48

bme280.load_calibration_params(bus, bme_address)
soil1 = Soil(bus, soil_1_address)
soil2 = Soil(bus, soil_2_address)
soil3 = Soil(bus, soil_3_address)
#soil4 = Soil(bus, soil_4_address)

soil_sensors = [soil1, soil2, soil3]
depth = [1,2,3]

filename = 'data_soil_depth'
with open(filename + '.csv', 'a') as f:
	if os.stat(filename + '.csv').st_size == 0:
		f.write(f"Time, Soil {depth[0]}, Soil {depth[1]}, Soil {depth[2]}, \
humidity, pressure, temperature \n") 

#prep data for plot
timeData = []
depth1Data = []

start = datetime.now()
interval = 60 #minutes
duration = 48*60 #minutes
i=0
while(i*interval)<duration:
	now = datetime.now() #get current time
	bme_dat = bme280.sample(bus, bme_address)
	humidity = bme_dat.humidity
	pressure = bme_dat.pressure
	ambient_temp = bme_dat.temperature
	time.sleep(2)
	soil_reading = []
	for sensor in soil_sensors:
		sensor.ledOn()
		time.sleep(1)
		reading = sensor.read()
		soil_reading.append(reading)
		time.sleep(1)
		sensor.ledOff()
		time.sleep(1)
	
	timeData.append((now-start).total_seconds())
	depth1Data.append(soil_reading[0])
	message = f"{now}, {soil_reading[0]}, {soil_reading[1]}, {soil_reading[2]}, \
{humidity}, {pressure}, {ambient_temp} \n"
	print(message)
	write_to_csv(filename, message)
	time.sleep(interval*60) #convert to seconds
	i +=1


gen_plot(timeData, depth1Data, 'top_soil_moisture', x_title = 'Time (s)', y_title = 'Soil Reading')

