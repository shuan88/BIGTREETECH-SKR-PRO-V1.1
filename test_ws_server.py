import asyncio
import websockets
import time
import json
import numpy as np
# from multiprocessing import Process, Pool
import threading
import multiprocessing as mp



# def muti_send(data):
#     async def send_data(websocket, path):
#             await websocket.send(data)
#             print("send")
#         # while True:
#             # print(data)
#             await websocket.send(data)
#             print("send")
#             # time.sleep(1)
#     return True

file = open("test.txt", "r" )
data = file.read()

async def send_data(websocket, path):
    print("send")
    # await websocket.send("open")
    # time.sleep(1)
    await websocket.send(data)
    time.sleep(1)




start_server = websockets.serve(send_data, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)

# ws = websocket.WebSocketApp("ws://echo.websocket.org/",
#  on_message = on_message, on_close = on_close)
# wst = threading.Thread(target=start_server)

wst = threading.Thread(target=asyncio.get_event_loop().run_forever())

# wst.daemon = True
wst.run_forever()
print("run")
# asyncio.get_event_loop().run_forever()

# await asyncio.gather(server1.wait_closed(), server2.wait_closed())