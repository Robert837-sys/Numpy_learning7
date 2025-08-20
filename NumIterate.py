import numpy as np 
"""
arr=np.array([1,2,3])

for x in arr:
  print(x)

arr3=np.array([[1,2,3],[4,5,6]])
for y in arr3:
  for z in y:
    print(z)

arr4=np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr4:
  for y in x:
    for z in y:
      print(z)

"""
arr=np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print(x)

# Iterating With Different Step Size
arr7=np.array([[1,2,3,4],[5,6,7,8]])

for x in np.nditer(arr7[:,::2]):
  print(x)