import asyncio
import websockets
import numpy as np
import datetime


uri="ws://localhost:8765"
time1 = int(datetime.datetime.utcnow().timestamp())


async def hello(uri):
    try:
        async with websockets.connect(uri) as websocket:
            # await websocket.send()
            # print("hello")
            i=0
            while True:
                try:
                    # recv_text = await websocket.recv()
                    recv_text = websocket.recv()
                    # print(recv_text)
                    print("{}> {}".format(i,recv_text))
                    i+=1

                except:
                    final_time = (datetime.datetime.utcnow().timestamp()- time1)
                    print(str(final_time))
                    print("f = " ,str(i/final_time),"Hz" )
                    print("failed in {}" .format(i))
                    break
    except:
        print("Error")

asyncio.get_event_loop().run_until_complete(hello(uri))

# asyncio.get_event_loop().run_forever()