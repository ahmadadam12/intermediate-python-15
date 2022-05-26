from turtle import shape
import numpy as np
import random

#Soal Nomor 1
arr = np.zeros((5,5))
i = 0
j = 3
while i<5 and j<=7:
    arr[:,i] = j
    i += 1
    j += 1
print(arr)

#Soal Nomor 2
z = np.random.randint(1, high = 5, size = (4,4))
a = np.array_split(z, 2, axis = 1)
print("\n",z)
print("\n",a)

