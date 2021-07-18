import numpy as np
import matplotlib.pyplot   as plt
from scipy.fftpack import fft, fftfreq


a = []
b = []

# data = [0.335205,1.077446,-10.477561]
# for i in range (0,119):
#     data_read = np.load("./Motor/Data/testing3/data" + " " +"(" + str(i) + ").npy")
#     # C:\Users\j0011\Desktop\MyFile\Code\Python\Motor\Data\testing2\data (1).npy
#     data = np.vstack([data,data_read])
# print(len(data))

# data = np.load("0714_N_S75_L0_Acc_BW20_971Hz.npy")
# data = np.load("0714_N_S100_L0_925hz.npy")
data = np.load("75pa_acc_1k_normonal.npy")


N = len(data) #1040105
T = 10.63/10000 # 
x = np.linspace(0.0, N*T, N, endpoint=False) 
y = data[:,0]

# scaler = MinMaxScaler(feature_range=(-1,1))
# y = scaler.fit_transform(y)

y_fft = fft(y)
x_fft = fftfreq(N, T)[:N//2]

plt.subplot(1, 2, 1)
plt.title("Origin")
plt.plot(x, y)
plt.subplot(1, 2, 2)
plt.title("FFT")
plt.plot(x_fft, 2.0/N * np.abs(y_fft[:N//2]))
plt.show()

print("Done")