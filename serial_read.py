import serial 
import time
import datetime
# import pymongo
# import json
import numpy as np
# import pandas as pd 
import os, sys
import matplotlib.pyplot as plt

"""import asyncio
    import websockets

    file = open("test.txt", "r" )
    data = file.read()
    async def send_data(websocket, path):
        print("send")
        # await websocket.send("open")
        # time.sleep(1)
        await websocket.send(data)
        # time.sleep(1)

    start_server = websockets.serve(send_data, 'localhost', 8765)
asyncio.get_event_loop().run_until_complete(start_server)
"""


""" linkit 
    ser = pyserial.Serial('/dev/tty.usbmodem14201',500000) """

# COM_PORT = '/dev/tty.usbmodem14101'    # port name
COM_PORT = '/dev/tty.usbmodem14103'    # port name
# COM_PORT = '/dev/cu.usbserial-0001'    # port name
# COM_PORT = 'COM5' # for windows USE "COM[number]"

BAUD_RATES = 500000    # SET BAUD_RATES 115200,250000,500000,1000000
ser = serial.Serial(COM_PORT, BAUD_RATES)   # init Serial settings

quantity = 3  # How many k data you want `60` is about 10 min  
data_size = 10000 # How many data size per saved file Recomand use 10000

path = "{}_N_S50_L0_Acc8_BW184" .format(datetime.date.today())
# path = "{}_null" .format(datetime.date.today())
""" 命名方式
    N：狀態，總共有四種(N=>正常馬達、RU=>轉子不平衡、RB=>轉子斷條、SS=>定子短路)
    S{}：速度與運轉功率=>S：speed，25：運轉%數(0,25,50,75,100)
    L{}：附載 : 0,25,50,75,100,125
    {} : 蒐集的資料總類 : Acc,gyro
    f{}：Sample rate (Hz)
    BW{}:濾波器頻寬　//184,92,41,20,10,5
    """
    

""" mongodb 
    myclient = pymongo.MongoClient("mongodb://140.134.29.211:27017/")
    mydb = myclient["shuan"]
    mycol = mydb["test"]
    mycol.delete_many({}) #drop table """

IncommingNum = ser.readline()
i = 0

if os.path.isdir("./{}".format(path)):
    path_temp = path
    while os.path.isdir("./{}".format(path_temp)):
        i+=1
        path_temp = str(path+ "_"+str(i))
        print(path_temp)
    path = path_temp
os.mkdir("./{}".format(path))

final_frequency = 0

# read MCU state detila 
# for _ in range(10):
#     # IncommingNum = ser.readline()
#     print(ser.readline())


# time0 = int(datetime.datetime.utcnow().timestamp())
time0 = int(time.time())

print ("Start")


for i in range(quantity):
    # time1 = int(datetime.datetime.utcnow().timestamp())
    time1 = int(time.time())
    new_array = np.fromstring(ser.readline().decode('utf-8'), dtype=float, sep=',')
    counter = 0
    # while counter<10000:  # data size  = 100000

    for counter in range(data_size - 1):
        IncommingNum = ser.readline()
        # data = IncommingNum.decode('utf-8')   # UTF-8 decoder
        data = np.fromstring(IncommingNum.decode('utf-8'), dtype=float, sep=',')
        try:
            if data.shape[0] ==3 :
                # print(data) 
                # print(counter," ",data)
                new_array = np.append(new_array,data)
            else :
                print(counter)
                counter -= 1
                print("{}noooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo".format(counter))
        except:
            print("errorrrrrrrrrrrrrrrrrrrrrrrrrrrrr")
            continue
    # data_time = (datetime.datetime.utcnow().timestamp()- time1)
    data_time = (time.time() - time1)
    frequency = np.int16(data_size/data_time)
    final_frequency += frequency
    # arr_size = np.int16((new_array.shape[0])/3)
    # np.save("./{}/data{}".format(path,i), (np.reshape(new_array, (arr_size,3))))
    np.save("./{}/data{}".format(path,i), (np.reshape(new_array, (data_size,3))))
    # pd.DataFrame(new_array).to_csv("./file_org.csv")
    print("time cost :" ,  str(data_time) ) # show time cost
    # print(arr_size)
    print(i,"> ","f = " ,str(frequency),"Hz" )
    del new_array
    

# print((datetime.datetime.utcnow().timestamp() - time0))
# final_frequency = (quantity * data_size)/(datetime.datetime.utcnow().timestamp() - time0)
# final_frequency = (quantity * data_size)/(time.time() - time0)
final_frequency = final_frequency / quantity
print("avg f = {}".format(final_frequency))

load_data = np.load("./{}/data0.npy".format(path))
print(load_data)
for i in range (1, quantity-1):
    data_read = np.load("./{}/data{}.npy".format(path,i))
    # data_read = np.load("./test_3_1/data" + str(i) + ".npy")
    load_data = np.vstack([load_data,data_read])

np.save("./{}_{}Hz".format(path,frequency),load_data)
load_data[:,1] += 0.4881932
load_data[:,2] += 10.27560595

N = len(load_data) 
F = final_frequency
freq = np.fft.rfftfreq(N,d=F**-1)
for i in range(3):
    plt.subplot(3, 3, i+1)
    sp = np.fft.rfft(load_data[:,i],norm="forward")
    ymax = np.argmax(sp)
    # print(sp.shape[:])
    print ("data {} max:{}".format(i,ymax))
    plt.plot( freq , np.abs(sp))
    plt.subplot(3, 3, i+4)
    plt.plot( load_data[:,i])
    plt.subplot(3, 3, i+7)
    plt.plot( load_data[0:100,i])

plt.savefig("./{}_{}Hz.png".format(path,frequency))
plt.show()

""" MongoDB
    # data = IncommingNum.decode()   # UTF-8 decoder
    # j = json.dumps(data, separators=(',', ':'))
    # print(data)
    # print(IncommingNum)
    # post = {"where": j,"date": datetime.datetime.utcnow()}
    # mycol.insert_one(post)

    # print(counter)

"""
