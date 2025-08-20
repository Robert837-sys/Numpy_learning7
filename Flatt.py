import numpy as np 
# Flattening array means converting a multidimensional array into a one-dimensional array.
# 1D array is a linear array of elements.
arr=np.array([[1, 2, 3], [4, 5, 6]])
newarr=arr.reshape(-1)
print(newarr)

arr=np.array([[1,2,3],[4,5,6]])
newarrr=arr.reshape(6)
print(newarrr)