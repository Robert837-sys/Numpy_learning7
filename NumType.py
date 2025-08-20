import numpy as np 
# checking data type of array
arr=np.array([1,2,3,4])
print(arr.dtype)

# create an array with data type string
arr=np.array([1,2,3,4])
print(arr)
print(arr.dtype)
# Create an array with data type 4 bytes integer:
arr=np.array([1,2,3,4],dtype='i4')
print(arr)
print(arr.dtype)
# Change data type from float to integer by using 'i' as parameter value:
arr=np.array([1.1,2.1,3.1])
newarr=arr.astype('i')
print(newarr)
print(newarr.dtype)
# Change data type from integer to boolean:
arr=np.array([1,0,3])
newarr=arr.astype(bool)
print(newarr)
print(newarr.dtype)