import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder3 = glob.glob(base_dir + '28-00000cf9d76a')[0]
device_file3 = device_folder3 + '/w1_slave'

device_folder2 = glob.glob(base_dir + '28-00000cf9c527')[0]
device_file2 = device_folder2 + '/w1_slave'

device_folder1 = glob.glob(base_dir + '28-00000cfa4fc9')[0]
device_file1 = device_folder1 + '/w1_slave'

def read_temp_raw(device_file):
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp(device_folder, device_file):
    lines = read_temp_raw(device_file)
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw(device_file)
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_f


while True:
    print("Temp 1: %.2fF" % read_temp(device_folder1, device_file1), "   Temp 2: %.2fF" % read_temp(device_folder2, device_file2), "   Temp 3: %.2fF" % read_temp(device_folder3, device_file3), end="\r")
    time.sleep(0.1)