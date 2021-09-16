!/usr/bin/python3
!chmod +x
#//////////////////////////////////////
#	blink.py
#	Blinks one LED wired to P9_14.
#	Wiring:	P9_14 connects to the plus lead of an LED.  The negative lead of the
#			LED goes to a 220 Ohm resistor.  The other lead of the resistor goes
#			to ground.
#	Setup:	
#	See:	
#//////////////////////////////////////
import Adafruit_BBIO.GPIO as GPIO
import time

out = "P9_11"
out2 = "P9_13"
out3 = "P9_15"
out4 = "P9_17"
out5 = "P9_41"
 
GPIO.setup(out, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)
GPIO.setup(out5, GPIO.OUT)
 
 
while True:
    GPIO.output(out, GPIO.HIGH)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)
    GPIO.output(out5, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(out, GPIO.LOW)
    GPIO.output(out2, GPIO.HIGH)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)
    GPIO.output(out5, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(out, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.HIGH)
    GPIO.output(out4, GPIO.LOW)
    GPIO.output(out5, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(out, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.HIGH)
    GPIO.output(out5, GPIO.LOW)
    time.sleep(0.25)
    GPIO.output(out, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)
    GPIO.output(out5, GPIO.HIGH)    
    time.sleep(0.25)
    GPIO.output(out, GPIO.LOW)
    GPIO.output(out2, GPIO.LOW)
    GPIO.output(out3, GPIO.LOW)
    GPIO.output(out4, GPIO.LOW)
    GPIO.output(out5, GPIO.LOW)
    time.sleep(0.25)