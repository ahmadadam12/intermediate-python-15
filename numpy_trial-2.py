import numpy as np

"""
arr = np.arange(10)
arr1 = np.append(arr, (11,12,13))
print(arr1)
"""
"""
arr1 = np.array([[1,2,3],
                [2,4,6]])
y = np.append(arr1, [[2,1,1]], axis= 0)
print(y)
"""

"""
a = np.array([[1,2,8], [5,8,10]])
b = np.array([[8,2,1], [3,9,1]])
c = np.concatenate((a,b), axis = 1)
print(c)
"""

"""
arr = np.array([2,1,5,3,7,4,6,8])
print(np.sort(arr))


arr = np.arange(2,11).reshape(3,3)
print(arr)
"""

"""
arr = np.array([1,2,3,4,5,6])
arr2 = np.expand_dims(arr, axis = 0)
print(arr2)
"""

"""
arr = np.array([[ 1,  2,  3,  4],
       [ 5,  6,  7,  8],
       [ 9, 10, 11, 12]])
print(arr)
"""

"""
z = np.array([[[0, 1, 3],
               [5, 7, 9]],
              
              [[0, 2, 4],
               [6, 8, 10]]])
print(z[0,0].shape)
"""

"""
arr = np.ones((2,3)).reshape(3,2)
print(arr)
"""

"""
arr = np.ones((4,4))
arr[1:3,1:3] = 0
print(arr)
"""

#Assignment Part2_Numpy-materi
arr = np.zeros((5,5))
i = 0
j = 3
while i<5 and j<=7:
    arr[:,i] = j
    i += 1
    j += 1
print(arr)

"""
s = input()
d = {
    "W" : 0,
    "B" : 0
}
for i in range(len(s)):
    v = d.get(s[i])
    d[s[i]]= v + 1

if d.get("W") == d.get("B"):
    print("1")
else:
    print("0")
"""