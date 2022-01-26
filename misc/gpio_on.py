'''
gpio_on.py 

By Ethan Turner
12/7/21

script programs gpio using python
turns on gpio pin
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

def main():
	enable(pinout)
	sleep(5)

if __name__ == '__main__':
	main()

