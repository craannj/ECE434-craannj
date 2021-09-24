from Adafruit_BBIO.Encoder import RotaryEncoder, eQEP1, eQEP2
import time

left = RotaryEncoder(eQEP2)
left.setAbsolute()
left.enable()

right = RotaryEncoder(eQEP1)
right.setAbsolute()
right.enable()

while True:
    print(left.position, right.position, end="\r")
    time.sleep(0.1)