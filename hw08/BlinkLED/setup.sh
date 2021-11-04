#!/bin/bash

export TARGET=hello.pru0

echo TARGET=$TARGET
echo 110 > /sys/class/gpio/export
echo out > /sys/class/gpio/gpio110/direction
