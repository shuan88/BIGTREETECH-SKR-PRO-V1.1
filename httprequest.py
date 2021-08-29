# 引入 requests 模組
import requests
import matplotlib.pyplot as plt
import numpy as np


# 使用 GET 方式下載普通網頁
# r = requests.get('http://192.168.0.129')
r = requests.get('http://192.168.50.65')
# print(r.text)
# received = r.text
text_file = open("sample.txt", "w")
n = text_file.write(r.text)
text_file.close()

data= np.loadtxt("./{}".format("sample.txt"),delimiter=',')

# data = np.array(r.text)
# print(data)


# data = np.load("./{}".format(path))

print(np.mean(data,axis=0))
# 0.01031709   0.4881932  -10.27560595

data[:,1] -= 0.4881932
data[:,2] += 10.27560595

F = 1000
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

# plt.savefig('{}.png'.format(path))         #保存图片
plt.show()