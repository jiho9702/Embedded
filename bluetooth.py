import serial
from serial import *


bluetooth_port = '/dev/rfcomm0'

baud_rate = 9600

bluetooth = serial.Serial(bluetooth_port, baud_rate)

data = 'Hello Arduino'
bluetooth.write(data.encode())

# received_data = bluetooth.readline()
# print(received_data.encode())

bluetooth.close()