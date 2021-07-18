#!/usr/bin/env python

import asyncio
import websockets
import numpy as np
import datetime


# def hello():
async def hello():
    uri = "ws://localhost:8765"
    try :
        async with websockets.connect(uri) as websocket:
            while True:
                # await websocket.recv()
                received = await websocket.recv()
                # print(received)
                # print(type(received))
                # data = np.fromstring(received.decode('utf-8'), dtype=float, sep='\n')
                data = np.fromstring(received, dtype=float, sep='\n')
                print (data)
                # arr_size = np.int16((data.shape[0])/3)
                # np.save("./data{}_{}".format(1,datetime.datetime.utcnow().timestamp()), (np.reshape(data, (arr_size,3))))
    except :
        return

while True:
    asyncio.get_event_loop().run_until_complete(hello())