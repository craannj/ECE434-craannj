#!/bin/bash
#Prints out the temperature

temp1=$(i2cget -y 1 0x4a)
temp2=$(i2cget -y 2 0x4a)

temp1calc=$((((temp1*9) / 5) + 32))
temp2calc=$((((temp2*9) / 5) + 32))

echo $temp1calc
echo $temp2calc