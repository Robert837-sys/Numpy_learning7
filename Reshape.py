# Reshape From 1-D to 2-D
import numpy as np 
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(4,3)
print(newarr)
# Reshape From 1-D to 3-D
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr=arr.reshape(2,3,2)
print(newarr)
# Try converting 1D array with 8 elements to a 2D array with 3 elements in each dimension (will raise an error):
arr3=np.array([1,2,3,4,5,6,7,8])
print(arr3.reshape(2,4).base)

# Convert 1D array with 8 elements to 3D array with 2x2 elements:
# Pass -1 as the value, and NumPy will calculate this number for you.
arr=np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr=arr.reshape(2,2,-1)
print(newarr)