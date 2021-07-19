import matplotlib.pyplot as plt
import numpy as np

path = "STM_2021-07-19_N_S100_L25_Acc8_BW184_1158Hz.npy"
F = 952

# quantity = 1  # How many k data you want `60` is about 10 min  

# load_data = np.load("./{}/data0.npy".format(path))
# print(load_data)
# for i in range (quantity):
#     data_read = np.load("./{}/data{}.npy".format(path,i))
#     # data_read = np.load("./test_3_1/data" + str(i) + ".npy")
#     load_data = np.vstack([load_data,data_read])

# data = load_data

# np.save("./{}_{}Hz".format(path,frequency),load_data)

data = np.load("./{}".format(path))
# data = np.load("{}.npy".format(path))

print(np.mean(data,axis=0))
# 0.01031709   0.4881932  -10.27560595
# for i in data[:,2]:
data[:,1] -= 0.4881932
data[:,2] += 10.27560595

N = len(data) #1040105
freq = np.fft.rfftfreq(N,d=F**-1)
for i in range(3):
    plt.subplot(3, 3, i+1)
    sp = np.fft.rfft(data[:,i],norm="forward")
    ymax = np.argmax(sp) / N
    # print(sp.shape[:])
    print ("data {} max:{}".format(i,ymax))
    plt.plot( freq , np.abs(sp))
    plt.subplot(3, 3, i+4)
    plt.plot( data[:,i])
    plt.subplot(3, 3, i+7)
    plt.plot( data[0:100,i])

plt.savefig('{}.png'.format(path))         #保存图片
plt.show()
