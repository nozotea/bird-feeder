#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time
import Servo
import PIR
import sys

Servo.setup()
PIR.setup()

while True:
    isCaptured = PIR.search()

    if isCaptured == 1:
        Servo.turn()
        time.sleep(60)

PIR.destroy()
Servo.destroy()
sys.exit()

