from random import randint
import numpy as np

z = np.arange(10)
v = np.random.uniform(0,100)
index = (np.abs(z-v)).argmin()
print(z[index])