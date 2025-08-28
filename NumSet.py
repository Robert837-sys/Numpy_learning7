import numpy as np 
# Convert following array with repeated elements to a set:
array_2=np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
z=np.unique(array_2)
print(z)
# Find union of the following two set arrays:
arr1=np.array([1, 2, 3, 4])
arr2=np.array([3, 4, 5, 6])

newarr=np.union1d(arr1,arr2)
print(newarr)

# Find intersection of the following two set arrays:
arr3=np.array([1, 2, 3, 4])
arr4=np.array([3, 4, 5, 6])

newarr1=np.intersect1d(arr3,arr4,assume_unique=True)
print(newarr1)
# Find the difference of the set1 from set2:

set1=np.array([1, 2, 3, 4])
set2=np.array([3, 4, 5, 6])

newarr2=np.setdiff1d(set1,set2,assume_unique=True)

print(newarr2)
# Find the symmetric difference of the set1 and set2:
set3=np.array([1,2,3,4])
set4=np.array([3,4,5,6])

newarr4=np.setxor1d(set3,set4,assume_unique=True)
print(newarr4)