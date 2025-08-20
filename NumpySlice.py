import numpy as np 
# 1-D slicing
arr=np.array([1,2,3,4,5,6,7])
print(arr[-3:-1])

# 2-D slicing
arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:4])
print(arr[0:2,1:4])
