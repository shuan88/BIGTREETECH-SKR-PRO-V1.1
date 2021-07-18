import numpy as np
# import pandas as pd

path = "2021-07-17_stm32_null_1154Hz.npy"

new_array = np.load(path)
# print(new_array.shape[:])
# np.savetxt("test_loaddata",new_array)

with open("test_loaddata.txt", 'a') as f:
    f.write(" ".join(map(str, new_array)))
