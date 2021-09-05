import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import seaborn as sns
from scipy import signal




# path = "stm32_2021-07-21_N_S50_L0_Acc8_BW184_Q540_1139Hz.npy"
path = "./npydata/August09_16_39_24_1050Hz.npy"

# name = path.split("_ ")
# print(name)

freq = 1057

"""
    # quantity = 1  # How many k data you want `60` is about 10 min  

    # load_data = np.load("./{}/data0.npy".format(path))
    # print(load_data)
    # for i in range (quantity):
    #     data_read = np.load("./{}/data{}.npy".format(path,i))
    #     # data_read = np.load("./test_3_1/data" + str(i) + ".npy")
    #     load_data = np.vstack([load_data,data_read])

    # data = load_data

    # np.save("./{}_{}Hz".format(path,frequency),load_data)

"""
# sensor1_ML_data_rms1 = np.array(np.sqrt(np.mean(sensor1_ML_data1**2, axis=1)))
# data = np.array(np.sqrt(np.mean(data**2, axis=1)))

data = np.load("{}".format(path))

### Delete Outlier
for i in range(data.shape[1]):
    i_mean = np.mean(data[:,i]) 
    i_n_std = 5.0 * np.std(data[:,i])
    for j in range(data.shape[0]-1):
        if np.abs(data[j,i]-i_mean) > i_n_std :
            # print(data[j,i],i,j)
            data[j,i] = (data[j-1,i] + data[j+1,i])/2
    if np.abs(data[-1,i]-i_mean) > i_n_std :
        data[-1,i] = i_mean


### Filter https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.butter.html
### https://blog.csdn.net/weixin_41521681/article/details/108262389

# sos = signal.butter(2, 10, 'lp', fs=1000, output='sos')
# print(sos)
# data = signal.sosfilt(sos, data)


"""
    这里假设采样频率为1000hz,信号本身最大的频率为500hz，
    要滤除100hz以上，400hz以下频率成分，即截至频率为100，400hz,则wn1=2100/1000=0.2，Wn1=0.2； 
    wn2=2400/1000=0.8，Wn2=0.8。Wn=[0.02,0.8]，
    和带通相似，但是带通是保留中间，而带阻是去除。
"""

# High_bandwidth = 100
# Low_bandwidth = 5

# b, a = signal.butter(8, [Low_bandwidth / freq,High_bandwidth / freq], 'bandstop')   #配置滤波器 8 表示滤波器的阶数
# data = signal.filtfilt(b, a, data)  #data为要过滤的信号

### Normalize

scaler = MinMaxScaler()
scaler.fit(data)
data_nor = scaler.transform(data)
print(data_nor.shape[:])

### show distributions
### https://seaborn.pydata.org/tutorial/distributions.html
sns.set()
sns.displot(data_nor)
plt.figure(1)
plt.title("PDF")

# plt.show()
## fft
# data[:,0] -= 0.4881932
# data[:,1] -= 0.4881932
# data[:,2] += 10.27560595

N = len(data_nor) #1040105
freq = np.fft.rfftfreq(N,d=freq**-1)
plt.figure(2)

for i in range(3):
    plt.subplot(3, 3, i+1)
    sp = np.fft.rfft(data_nor[:,i])
    # sp = np.fft.rfft(data[:,i],norm="forward")
    ymax = (np.argmax(sp[1:-1]) / N)*freq 
    # print(sp.shape[:])
    # print(np.fft.rfftfreq(data.shape[0] , d=1./N))
    print ("data {} max:{}".format(i,ymax))
    plt.plot( freq[1:-1] , np.abs(sp[1:-1]))
    # plt.xlim([1, 100])
    plt.subplot(3, 3, i+4)
    plt.plot( data_nor[:,i])
    plt.subplot(3, 3, i+7)
    plt.plot( data_nor[0:100,i])
plt.show()

# plt.figure(3)
# for i in range(3):
#     plt.subplot(3, 3, i+1)
#     sp = np.fft.rfft(data[:,i])
#     # sp = np.fft.rfft(data[:,i],norm="forward")
#     ymax = (np.argmax(sp[1:-1]) / N)*F
#     # print(sp.shape[:])
#     # print(np.fft.rfftfreq(data.shape[0] , d=1./N))
#     print ("data {} max:{}".format(i,ymax))
#     plt.plot( freq[1:-1] , np.abs(sp[1:-1]))
#     # plt.xlim([1, 100])
#     plt.subplot(3, 3, i+4)
#     plt.plot( data[:,i])
#     plt.subplot(3, 3, i+7)
#     plt.plot( data[0:100,i])
# plt.show()

# plt.savefig('{}.png'.format(path)) #save image
