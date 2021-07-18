import serial
import time

ser = serial.Serial('/dev/ttyS0',115200)


print ("Start")
while True:
    IncommingNum = ser.readline()
    print(IncommingNum)
