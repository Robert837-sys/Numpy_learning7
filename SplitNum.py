import numpy as np 
# splitting 1-D
"""
arr=np.array([1,2,3,4,5,6])
newarr=np.array_split(arr,3)
print(newarr[0])
print(newarr[1])
print(newarr[2])
"""
# Splitting 2-D
arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr=np.array_split(arr,3,axis=1)
print(newarr)
# Use the hsplit() method to split the 2-D array into 3 2-D along columns

arr=np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr=np.hsplit(arr,3)
print(newarr)