'''
soil_i2c.py

by Ethan Turner

script with commands for use of the soil moisture sensor.

'''
import os
import time

class Soil:
	def __init__(self, bus, address):
		self.bus = bus
		self.address = address

	def __str__(self):
		return f"sensor address:{hex(self.address)}"

	def read(self):
		'''returns an integer 0 to 1023 reading from the sensor'''
		read_command = 0x05
		reading = self.bus.read_word_data(self.address, read_command)
		return reading

	def ledOn(self):
		'''tells sensor to turn led on'''
		led_on_command = 0x01
		register = 0
		self.bus.write_byte(self.address, led_on_command)

	def ledOff(self):
		'''tells sensor to turn led off'''
		led_off_command = 0x00
		register = 0
		self.bus.write_byte(self.address, led_off_command)

