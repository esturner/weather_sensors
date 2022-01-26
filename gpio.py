'''
gpio.py 

By Ethan Turner
12/7/21

script programs gpio using python
'''

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
pinout = 8
GPIO.setup(pinout, GPIO.OUT)

def enable(pin):
	GPIO.output(pin, GPIO.HIGH)

def disable(pin):
	GPIO.output(pin, GPIO.LOW)

def test():
	'''turns on and off GPIO 3X'''
	try:
		for i in range(3):
			enable(pinout)
			sleep(2)
			print(GPIO.input(pinout))
			sleep(2)
			disable(pinout)
			sleep(2)
			print(GPIO.input(pinout))
			sleep(2)
		GPIO.cleanup()
	except KeyboardInterrupt:
		GPIO.cleanup()

if __name__ == '__main__':
	test()

