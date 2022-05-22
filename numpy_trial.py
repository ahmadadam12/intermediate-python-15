import numpy as np
"""
arr1 = np.array(([1,2,3],
                [3,4,5],
                [5,6,7]))
arr2 = np.array(([1,2,3],
                [3,4,5],
                [5,6,7]))
arr3 = np.array(([1,2,3,7],
                [3,4,5,8],
                [5,6,7,9]))
mul1 = arr1.dot(arr2)
mul2 = mul1.dot(arr3)
t_mul2 = mul2.T

print(mul2)
print(mul2.shape)
#print("shape arr3: {}".format(arr3.shape))
#print("\n{}".format(mul2[0:2,1:]))
print("\n{}\nshape:{}".format(t_mul2,t_mul2.shape))
print("\n{}\nreshape:{}".format(t_mul2.reshape(6,2),t_mul2.shape))
"""

#arr1 = np.ones([3,2,3])
#print(arr1)
"""
arr2 = np.array([[[0,0,0,0],
                [0,0,0,0]],
                [[1,1,1,1],
                [1,1,1,1]],
                [[2,2,2,2],
                [2,2,2,2]]])
print(arr2,arr2.shape)
"""

arr3 = np.arange(1,21).reshape(5,2,2)
#print(arr3)
arr4 = np.arange(21,41).reshape(5,2,2)
#arr5 = np.concatenate((arr3,arr4),axis = 2)
#print(arr5,arr5.shape)
#print("\nslicing: \n",arr5[1:3,:,1:])
#print("\nslicing: \n",arr5[1,:,1:] + arr5[4,:,1:])

"""
arr6 = np.concatenate((arr3,arr4),axis = 1)
print(arr6,"shape:",arr6.shape)
print(arr6[2,:,:],"\n",arr6[3,:,:])
arr7 = np.concatenate((arr6[2,:,:],arr6[3,:,:]),axis = 1)
print(arr7) 
"""

"""
arr1 = np.array([[1,2],
                [1,2]])
arr2 = np.array([[3,4],
                [3,4]])
arr3 = arr1@arr2
print(arr3,arr3.mean())
"""


arr1 = np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12]],dtype = np.int32)
print(arr1[::2,1::2])