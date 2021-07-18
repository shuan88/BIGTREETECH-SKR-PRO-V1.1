#!/usr/bin/env python

# WS server example

import asyncio
import websockets
import serial 
import time
import datetime
import pymongo
import json
import numpy as np

quantity = 30 # How many k data you want 

##### select COM PORT
# COM_PORT = '/dev/tty.usbmodem14101'    # port name
# COM_PORT = '/dev/tty.usbmodem141301'    # port name
COM_PORT = '/dev/cu.usbserial-0001'    # port name
# COM_PORT = 'COM14' # for windows use "COM[number]"

##### SET BAUD_RATES '9600','115200' , '2500000 * n'
# BAUD_RATES = 115200    # SET BAUD_RATES
BAUD_RATES = 1000000/2    # SET BAUD_RATES

ser = serial.Serial(COM_PORT, BAUD_RATES)   # init Serial settings

IncommingNum = ser.readline()

counter=0
for i in range(10):
    IncommingNum = ser.readline()
    # print(IncommingNum.decode('utf-8'))
print("RUN")

async def send_data(websocket, path):
    while True:
        IncommingNum = ser.readline()
        data = IncommingNum.decode('utf-8')
        # print(data)
        websocket.send(data)
        # await websocket.send(data)

start_server = websockets.serve(send_data, 'localhost', 8765)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

