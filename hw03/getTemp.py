#!/usr/bin/env python3
# Read a TMP101 sensor

import smbus
import time
bus1 = smbus.SMBus(1)
bus2 = smbus.SMBus(2)    # Bus Number
address1 = 0x4a        # Device address
address2 = 0x4a
while True:
    temp1 = bus1.read_byte_data(address1, 0) # 0 is register to read
    temp2 = bus2.read_byte_data(address2, 0)
    temp1 = (temp1 * (9/5)) + 32
    temp2 = (temp2 * (9/5)) + 32
    print("Temp 1: %.2f F" % temp1, " Temp 2: %.2f F" % temp2, end="\r")
    time.sleep(0.25)
