import numpy as np 
arr=np.array([1,2,3,4])
x=np.prod(arr)
print(x)

# Find the product of the elements of two arrays:
arr1=np.array([1,2,3,4])
arr2=np.array([5,6,7,8])
x=np.prod([arr1,arr2],axis=1)
print(x)

# Take cummulative product of all elements for following array:
arr3=np.array([5,6,7,8])
newarr=np.cumprod(arr3)
print(newarr)