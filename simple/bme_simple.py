#comment
import bme280
import smbus2
from time import sleep

port = 1
address = 0x76 # BME280 address - system specific. Other BME280s may be different
bus = smbus2.SMBus(port)

#calibration from bme library
bme280.load_calibration_params(bus,address)


#display on screen 10 values seperated by 2 seconds (humidity, pressure, temp)
for i in  range(1,10):
	bme280_data = bme280.sample(bus,address)
	humidity  = bme280_data.humidity
	pressure  = bme280_data.pressure
	ambient_temperature = bme280_data.temperature
	print(humidity, pressure, ambient_temperature)
	sleep(2)

