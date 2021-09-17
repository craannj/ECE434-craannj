#!/usr/bin/env python3
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

print("Input a height: ")
height = input()
print("Height set to " + height)
rows = int(height) 

print("Input a width: ")
width = input()
print("Width set to " + width)
cols = int(width) 


#Initialize the size and sets default for each entry
Display = []
Display.append("  ")
for q in range(rows):
	Display.append(str(q))
Sketch = []
Row = []
Sketch.append(Display)
for i in range(rows):
	Row.append(str(i)+":")
	for j in range(cols):
		Row.append(' ')
	Sketch.append(Row)
	Row = []

#Prints the initial sketch without user input
for x in Sketch:
	for k in x:
		print(k, end = " ")
	print()

default_x = 1
default_y = 1
user_in = "placeholder"

print("Press a button to play:")
while True:
	#user_in = input()
	#print(user_in)	#Debuging purposes
	#Handles user-input in loop if L, R, U or D
	#GPIO.output(out, GPIO.LOW)
	#GPIO.output(out2, GPIO.LOW)
	#GPIO.output(out3, GPIO.LOW)
	#GPIO.output(out4, GPIO.LOW)
	#GPIO.output(out5, GPIO.LOW)
	time.sleep(0.2)
	if GPIO.input(button1) == GPIO.HIGH:
		GPIO.output(out, GPIO.HIGH)
		GPIO.output(out2, GPIO.LOW)
		GPIO.output(out3, GPIO.LOW)
		GPIO.output(out4, GPIO.LOW)
		GPIO.output(out5, GPIO.LOW)
		default_x -= 1
		if default_x < 1:
			default_x = 1
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif GPIO.input(button2) == GPIO.HIGH:
		GPIO.output(out2, GPIO.HIGH)
		GPIO.output(out, GPIO.LOW)
		GPIO.output(out3, GPIO.LOW)
		GPIO.output(out4, GPIO.LOW)
		GPIO.output(out5, GPIO.LOW)
		default_x += 1
		if default_x > rows:
			default_x = rows
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif GPIO.input(button3) == GPIO.HIGH:
		GPIO.output(out3, GPIO.HIGH)
		GPIO.output(out2, GPIO.LOW)
		GPIO.output(out, GPIO.LOW)
		GPIO.output(out4, GPIO.LOW)
		GPIO.output(out5, GPIO.LOW)
		default_y -= 1
		if default_y < 1:
			default_y = 1
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif GPIO.input(button4) == GPIO.HIGH:
		GPIO.output(out4, GPIO.HIGH)
		GPIO.output(out2, GPIO.LOW)
		GPIO.output(out3, GPIO.LOW)
		GPIO.output(out, GPIO.LOW)
		GPIO.output(out5, GPIO.LOW)
		default_y += 1
		if default_y > cols:
			default_y = cols
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	#Handles user-input in loop if clear
	elif GPIO.input(button5) == GPIO.HIGH:
		GPIO.output(out5, GPIO.HIGH)
		GPIO.output(out2, GPIO.LOW)
		GPIO.output(out3, GPIO.LOW)
		GPIO.output(out4, GPIO.LOW)
		GPIO.output(out, GPIO.LOW)
		Display = []
		Display.append("  ")
		for q in range(rows):
			Display.append(str(q))
		Sketch = []
		Row = []
		Sketch.append(Display)
		for i in range(rows):
			Row.append(str(i)+":")
			for j in range(cols):
				Row.append(' ')
			Sketch.append(Row)
			Row = []
		#Prints the initial sketch without user input
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()
	elif GPIO.input(button1) == GPIO.HIGH and GPIO.input(button2) == GPIO.HIGH:
		print("Thanks for playing!")
		break