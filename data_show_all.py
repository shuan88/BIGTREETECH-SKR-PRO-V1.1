from os import listdir
from os.path import isdir, isfile, join
from scipy import signal
from sklearn.preprocessing import MinMaxScaler

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns
# import tensorflow as tf
import os
import sys
import shutil
from numba import jit
from numba import vectorize

# Reshape Data funtion


def data_process_reshape(data, point=1000):
    data = data.reshape(-1, point, data.shape[-1])
    return data


def generate_noise(train_data, scale=0.05, noise_factor=0.4):
    noise = np.random.normal(loc=0, scale=scale, size=train_data.shape)
    x_train_noisy = train_data + noise_factor * noise
    x_train_noisy = np.clip(x_train_noisy, 0.0, 1.0)
    return x_train_noisy


@jit(nopython=True)
def delete_outlier(data, filter_range=5):
    bad_count = 0
    if filter_range < 10:
        for i in range(data.shape[1]):
            i_mean = np.mean(data[:, i])
            i_n_std = filter_range * np.std(data[:, i])
            for j in range(data.shape[0]-1):
                if np.abs(data[j, i]-i_mean) > i_n_std:
                    # print(data[j,i],i,j)
                    data[j, i] = (data[j-1, i] + data[j+1, i])/2
                    bad_count += 1
            if np.abs(data[-1, i]-i_mean) > i_n_std:
                data[-1, i] = i_mean
    return data, bad_count


################################################################
# 合併資料
state = ["N", "RU", "RB", "SS"]
speed = [100, 75, 50, 25, 0]
load = [125, 100, 75, 50, 25, 0]

main_dir = "/Users/shuan/PycharmProjects/Data_Separate"
# os.listdir(main_dir)

N_path = "{}/N/".format(main_dir)

file_dir = os.listdir(N_path)
full_file_dir = []
for file_name in file_dir:
    full_file_dir.append("{}{}".format(N_path, file_name))


data_input = np.load(full_file_dir[0])

data_input_dir = "{}/N_all.npy".format(main_dir)
if not os.path.isfile(data_input_dir):
    for load_name in full_file_dir[1:-1]:
        data_input = np.vstack([data_input, np.load(load_name)])
        # print(load_name)
        # print(np.load(load_name).shape[:])
    np.save(data_input_dir, data_input)
else:
    print("{} is existed ".format(data_input_dir))

data = np.load(data_input_dir)
print(data.shape[:])
# plt.plot(data)
# plt.show()

