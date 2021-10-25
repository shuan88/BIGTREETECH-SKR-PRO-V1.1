import asyncio
import websockets
import numpy as np
import datetime
# from websocket import create_connection

# uri="ws://localhost:8765"
# uri = "ws://192.168.0.129:80"
# uri = "ws://192.168.50.65:80"
uri = "ws://192.168.10.54:80"
# uri = "192.168.50.142:80"
# time1 = int(datetime.datetime.utcnow().timestamp())


async def hello(uri):
# async def hello(websocket, path):
    # try:
    async with websockets.connect(uri) as websocket:
        recv_text = await websocket.recv()
        print(recv_text)
        while True:
            recv_text = await websocket.recv()
            try :
                Device,SN,data = recv_text.split("_")
                print(Device,SN,data)
            except :
                print(recv_text)


# start_server = websockets.serve(hello, 'ws://192.168.50.142', 80)
# asyncio.get_event_loop().run_until_complete(start_server)

asyncio.get_event_loop().run_until_complete(hello(uri))
asyncio.get_event_loop().run_forever()
# asyncio 多線程
# https://docs.python.org/zh-tw/3/library/asyncio-task.html


# print("RUN")

# ws = create_connection("ws://192.168.50.142:80")
# ws.send('{"method": "recentbuytrades"}')

# while True:
#   result =  ws.recv()
#   print ("Received '%s'" % result)

# ws.close()