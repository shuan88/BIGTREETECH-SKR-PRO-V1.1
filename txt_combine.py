from os import listdir
from os.path import isdir, isfile, join

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import signal
from sklearn.preprocessing import MinMaxScaler



mypath = "/Volumes/Untitled 1/September02_19_29_43"
files = listdir(mypath)
fulllpath  = []
print(files)

data_size = len(files)
load_data= np.loadtxt("{}/data1.txt".format(mypath),delimiter=',')
for i in range(2,data_size-1):
    # data_read = np.loadtxt("{}/data{}.txt".format(mypath,i),delimiter=',')
    load_data = np.vstack([load_data,np.loadtxt("{}/data{}.txt".format(mypath,i),delimiter=',')])
# np.save("./txt2np/{}_{}Hz".format(data_folder.split("/")[-1],1000),load_data)   
np.save("./txt2np{}_{}Hz".format("September02_19_29_43",1000),load_data)   