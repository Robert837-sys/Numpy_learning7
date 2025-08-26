import numpy as np 
arr=np.array([10,15,25,5])
newarr=np.diff(arr)

print(newarr)

# Compute discrete difference of the following array twice:
arr1=np.array([10,15,25,5])
newarr1=np.diff(arr1,n=2)
print(newarr1)