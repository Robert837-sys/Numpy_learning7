# The shape of an array is the number of elements in each dimension.
# NumPy provides the shape attribute of the array object to return the shape of the array.
# it  returns a tuple with each index having the number of corresponding elements.
import numpy as np 
arr=np.array([[1,2,3,4],[5,6,7,8]])
print(arr.shape)
# Create an array with 5 dimensions using ndmin using a vector with values 1,2,3,4 and verify that last dimension has value 4:
arr=np.array([1,2,3,4],ndmin=5)
print(arr)
print('Shape of array: ',arr.shape)

# 1D -Array
arr1=np.array([1,2,3,4,5])
print(arr1.shape)

arr3=np.array([
    [[1, 2], [3, 4]],
    [[5, 6], [7, 8]]
])
print(arr3.shape)