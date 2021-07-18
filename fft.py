import matplotlib.pyplot as plt
import numpy as np

path = "0714_N_S100_L0_925hz"
quantity = 24  # How many k data you want `60` is about 10 min  
data = np.load("{}.npy".format(path))

"""
    load_data = np.load("./{}/data0.npy".format(path))
    print(load_data)
    for i in range (1, quantity-1):
        data_read = np.load("./{}/data{}.npy".format(path,i))
        # data_read = np.load("./test_3_1/data" + str(i) + ".npy")
        load_data = np.vstack([load_data,data_read])

    data = load_data
"""

# np.save("./{}_{}Hz".format(path,frequency),load_data)


# data = np.load("0714_N_S100_L0_925hz.npy")
# data = np.load("75pa_acc_1k_normonal.npy")
# data = np.load("0714_N_S75_L0_gyro_BW20_912Hz.npy")


# norm = np.linalg.norm(data ,axis=0)
# print (norm)
# data = data / norm

# T = 10.63/10000 # 
# x = np.linspace(0.0, N*T, N, endpoint=False) 

# print(data[:,0])


N = len(data) #1040105
F = 912
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
    plt.plot( data[0:200,i])

plt.savefig('{}.png'.format(path))         #保存图片
plt.show()
