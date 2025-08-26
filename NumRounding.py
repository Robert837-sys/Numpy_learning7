# numpy Truncation
import numpy as np 
# arr=np.trunc([-3.1666, 3.6667])
arr=np.fix([-3.1666, 3.6667])

print(arr)

# numpy Rounding
arr1=np.around(3.1666, 2)
print(arr1)

# Numpy Floor
arr2=np.floor([-3.1666, 3.6667])
print(arr2)
# Numpy ceil
arr3=np.ceil([5.998, 1.455])
print(arr3)