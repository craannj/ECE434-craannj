
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

while user_in != q:
	print("Input u, d, l, r, c or q: ")
	user_in = input()
	#print(user_in)	#Debuging purposes
#Handles user-input in loop if L, R, U or D
	if user_in == "l":
		default_x -= 1
		if default_x < 1:
			default_x = 1
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif user_in == "r":
		default_x += 1
		if default_x > rows:
			default_x = rows
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif user_in == "u":
		default_y -= 1
		if default_y < 1:
			default_y = 1
		Sketch[default_y][default_x] = "X"
		#Prints the updated sketch
		for x in Sketch:
			for k in x:
				print(k, end = " ")
			print()

	elif user_in == "d":
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
	elif user_in == "c":
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
	elif user_in == "q":
		print("Thanks for playing!")
		break
