#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import sys

pirPin = 17    # the pir connect to pin17

def setup():
	GPIO.setmode(GPIO.BCM)		# Set the GPIO modes to BCM Numbering
	GPIO.setup(pirPin, GPIO.IN)    # Set pirPin to input

# Define a MAP function for mapping values.  Like from 0~255 to 0~100
def MAP(x, in_min, in_max, out_min, out_max):
	return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

def destroy():
	GPIO.cleanup()                     # Release resource

def search():
	pir_val = GPIO.input(pirPin)

	return pir_val

if __name__ == '__main__':     # Program start from here
	try:
		setup()
		search()
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
