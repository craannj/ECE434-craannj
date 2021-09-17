!/usr/bin/python3
!chmod +x
#//////////////////////////////////////	
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time
out = "P9_12"
GPIO.setup(out, GPIO.OUT)
while True:
	GPIO.output(out, GPIO.HIGH)
	GPIO.output(out, GPIO.LOW)