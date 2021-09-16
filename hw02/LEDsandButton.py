#!/usr/bin/python3
#!chmod +x

import Adafruit_BBIO.GPIO as GPIO
import time

out = "P9_11"
out2 = "P9_13"
out3 = "P9_15"
out4 = "P9_17"
out5 = "P9_41"

button1 = "P9_12"
button2 = "P9_14"
button3 = "P9_30"
button4 = "P9_26"
button5 = "P9_42"
 
GPIO.setup(out, GPIO.OUT)
GPIO.setup(out2, GPIO.OUT)
GPIO.setup(out3, GPIO.OUT)
GPIO.setup(out4, GPIO.OUT)
GPIO.setup(out5, GPIO.OUT)
 
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button2, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button3, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button4, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(button5, GPIO.IN, pull_up_down = GPIO.PUD_DOWN) 
 
while True:
    if GPIO.input(button1) == GPIO.HIGH: 
         GPIO.output(out, GPIO.HIGH)
    elif GPIO.input(button2) == GPIO.HIGH:
        GPIO.output(out2, GPIO.HIGH)
    elif GPIO.input(button3) == GPIO.HIGH:
        GPIO.output(out3, GPIO.HIGH)
    elif GPIO.input(button4) == GPIO.HIGH:
        GPIO.output(out4, GPIO.HIGH)
    elif GPIO.input(button5) == GPIO.HIGH:
        GPIO.output(out5, GPIO.HIGH)    
    else:
        GPIO.output(out, GPIO.LOW)
        GPIO.output(out2, GPIO.LOW)
        GPIO.output(out3, GPIO.LOW)
        GPIO.output(out4, GPIO.LOW)
        GPIO.output(out5, GPIO.LOW)
    