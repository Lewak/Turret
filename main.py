#!/usr/bin/env python

# servo_demo.py
# 2016-10-07
# Public Domain

# servo_demo.py          # Send servo pulses to GPIO 4.
# servo_demo.py 23 24 25 # Send servo pulses to GPIO 23, 24, 25.

import sys
import time
import random
import pigpio
import RPi.GPIO as GPIO    # Import Raspberry Pi GPIO library
from laser import Laser
import atexit

NUM_GPIO = 32

MIN_WIDTH = 500
MAX_WIDTH = 2500
once = 0
step = [0] * NUM_GPIO
width = [0] * NUM_GPIO
used = [False] * NUM_GPIO

pi = pigpio.pi()
laser = Laser(4)
if not pi.connected:
    exit()

G = [2,3]

GPIO.setwarnings(False)    # Ignore warning for now
GPIO.setmode(GPIO.BCM)   # Use physical pin numbering
GPIO.setup(4, GPIO.OUT, initial=GPIO.LOW)   # Set pin 8 to be an output pin and set initial value to low (off)


def pack_the_shit():
    laser.turnOff()
    print("dupa")


atexit.register(pack_the_shit)
for g in G:
    step[g] = 1
    width[g] = 1000

while True:
    try:
        for g in G:
            pi.set_servo_pulsewidth(g, width[g])
            width[g] += step[g]
            if width[g] < MIN_WIDTH or width[g] > MAX_WIDTH:
                step[g] = -step[g]
                width[g] += step[g]
                if g == 2:
                    if once:
                        laser.turnOn()
                        once = 0
                    else:
                        once = 1
                        laser.turnOff()

        time.sleep(0.001)
    except KeyboardInterrupt:
        break

for g in G:
    pi.set_servo_pulsewidth(g, 0)


pi.stop()

