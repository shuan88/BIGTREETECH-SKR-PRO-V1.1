from os import listdir
from os.path import isdir, isfile, join

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import signal
from sklearn.preprocessing import MinMaxScaler

mypath = "/Volumes/mac/August09_16_39_24/"
files = listdir(mypath)
fulllpath  = []

# fulllpath = ("{}/August09_16_39_24".format(mypath))
# for path in files:
#     if not isfile(path):
#         fulllpath.append("{}/{}".format(mypath,path))
#         # print(path)
# print(fulllpath)

# print(files)

for path in files:
    if isfile("{}/{}".format(mypath,path)):
        fulllpath.append("{}/{}".format(mypath,path))
        # print(path)
# print(fulllpath)
print(len(fulllpath))


load_data= np.loadtxt("{}/data0.txt".format(mypath),delimiter=',')

for i in range(1,len(fulllpath)-1):
    data_read = np.loadtxt("{}/data{}.txt".format(mypath,i),delimiter=',')
    load_data = np.vstack([load_data,data_read])
    
np.save("./August09_16_39_24_1050Hz".format() ,load_data)
# np.save("./data/{}_{}Hz".format(f,1050),load_data)
freq = 10000

N = len(load_data) #1040105
freq = np.fft.rfftfreq(N,d=freq**-1)
for i in range(3):
    plt.subplot(3, 3, i+1)
    sp = np.fft.rfft(load_data[:,i])
    # sp = np.fft.rfft(data[:,i],norm="forward")
    ymax = (np.argmax(sp[1:-1]) / N)*freq 
    # print(sp.shape[:])
    # print(np.fft.rfftfreq(data.shape[0] , d=1./N))
    # print ("data {} max:{}".format(i,ymax))
    plt.plot( load_data[1:-1] , np.abs(sp[1:-1]))
    # plt.xlim([1, 100])
    plt.subplot(3, 3, i+4)
    plt.plot( load_data[:,i])
    plt.subplot(3, 3, i+7)
    plt.plot( load_data[0:100,i])
plt.show()
# print(data)

# np.loadtxt(path)
