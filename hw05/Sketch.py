#!/usr/bin/env python3
import Adafruit_BBIO.GPIO as GPIO
from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP2, eQEP1
import smbus
import time

bus = smbus.SMBus(1)
bus2 = smbus.SMBus(2) 
matrix = 0x70
adxl = 0x53

button1 = "P9_42"
out = "P9_12"
GPIO.setup(out, GPIO.OUT)
GPIO.setup(button1, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#Start in top left corner of the matrix
xpos = 15   #Horizontal starting point
ypos= 1     #Vertical starting point

screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]

# Start oscillator (p10)
bus.write_byte_data(matrix, 0x21, 0)
# Disp on, blink off (p11)
bus.write_byte_data(matrix, 0x81, 0)
# Full brightness (p15)
bus.write_byte_data(matrix, 0xe7, 0)

bus.write_i2c_block_data(matrix, 0, screen)


bus2.write_byte_data(adxl, 0x2c, 0x08)
bus2.write_byte_data(adxl, 0x2d, 0x08)
bus2.write_byte_data(adxl, 0x31, 0x08)


while True:
    GPIO.output(out, GPIO.LOW)
    accl1 = bus2.read_byte_data(adxl, 0x32)
    accl2 = bus2.read_byte_data(adxl, 0x33)
    accl3 = bus2.read_byte_data(adxl, 0x34)
    accl4 = bus2.read_byte_data(adxl, 0x35)
    
    acclx = ((accl2&0x03)) + accl1
    accly = ((accl4&0x03)) + accl3
    
    #Handle up and down
    if(accly < 230 and accly > 128):
        if(ypos < 72):
            ypos = ypos << 1
    elif(accly > 30 and accly < 128):
        if(ypos > 1):
            ypos = ypos >> 1
   
    
    #Handle left and right
    if(acclx < 230 and acclx > 128):
        if(xpos < 15):
            xpos = xpos + 2
            
    elif(acclx > 30 and acclx < 128):
        if(xpos > 1):
            xpos = xpos - 2
    
    
    #Update the matrix
    screen[xpos] = screen[xpos] | ypos
    bus.write_i2c_block_data(matrix, 0, screen)
    if GPIO.input(button1) == GPIO.HIGH:
        GPIO.output(out, GPIO.HIGH)
        #xpos = 15   #Horizontal starting point
        #ypos= 1     #Vertical starting point
        screen = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
                    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00]
        bus.write_i2c_block_data(matrix, 0, screen)
    time.sleep(0.3)
    