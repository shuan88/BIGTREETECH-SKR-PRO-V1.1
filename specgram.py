from scipy import signal
from scipy.fft import fftshift
import matplotlib.pyplot as plt
import numpy as np

# Reshape Data funtion
def data_process_reshape(data, point=1024):
    data = data.reshape(-1,point,data.shape[-1])
    return data

def specgram_show(data , sample_rate = 1000):
    plt.subplots(figsize=(20,5))
    for i in range(data.shape[-1]):
        plt.subplot(1, data.shape[-1], i+1)
        plt.specgram(data[: 10000,i], Fs=sample_rate)
        plt.ylabel('Frequency [Hz]')
        # plt.yscale('symlog')
        plt.xlabel('Time [sec]')
    plt.show()

ims_data = np.load("./ims/2nd_test.npy")
sample_rate = 10240
data_second = data_process_reshape(ims_data,sample_rate)
print(data_second.shape[:])

for time in range(data_second.shape[0]):
    plt.subplots(figsize=(20,5))
    for i in range(data_second.shape[-1]):
        plt.subplot(1, 4, i+1)
        frequencies, times, spectrogram = signal.spectrogram(data_second[time,:,i], sample_rate)
        plt.pcolormesh(times, frequencies, spectrogram)
        plt.ylabel('Frequency [Hz]')
        # plt.yscale('symlog')
        plt.xlabel('Time [sec]')
    plt.savefig('./img/out_{}.png'.format(time))
print("Done!")