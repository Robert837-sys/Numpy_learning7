import numpy as np 
# Addition
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])

newarr=np.add(arr1,arr2)
print(newarr)
# Summation 
newarr1=np.sum([arr1,arr2])
print(newarr1)

newarr2=np.sum([arr1,arr2],axis=1) # If you specify axis=1, NumPy will sum the numbers in each array.
print(newarr2)

arr31=np.array([1,2,3])
newarr31=np.cumsum(arr31)

print(newarr31)