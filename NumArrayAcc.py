import numpy as np
# 1-D array Access
arr=np.array([1,2,3,4])
print(arr[0])
print(arr[2]+arr[3])

# 2-D Array Access

arr=np.array([[1,2,3,4,5],[6,7,8,9,10]])
print('5th element on 2nd row: ',arr[1,4])

# 3-D Array Access
arr=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print('3rd element on 2nd row: ',arr[0,1,2])