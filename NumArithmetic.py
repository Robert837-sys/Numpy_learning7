import numpy as np 
arr1=np.array([10, 11, 12, 13, 14, 15])
arr2=np.array([20, 21, 22, 23, 24, 25])

newarr=np.add(arr1,arr2)
print(newarr)

# numpy array subtraction 
arr3=np.array([10, 20, 30, 40, 50, 60])
arr4=np.array([20, 21, 22, 23, 24, 25])

newarr2=np.subtract(arr3,arr4)
print(newarr2)

# numpy array multipilication
arr5=np.array([10, 20, 30, 40, 50, 60]) 
arr6=np.array([20, 21, 22, 23, 24, 25])

newarr3=np.multiply(arr5,arr6)
print(newarr3)

# numpy array division
arr7=np.array([10, 20, 30, 40, 50, 60])
arr8=np.array([3, 5, 10, 8, 2, 33])

newarr4=np.divide(arr7,arr8)
print(newarr4)

# numpy array power
arr9=np.array([10, 20, 30, 40, 50, 60]) 
arr10=np.array([3, 5, 6, 8, 2, 33])

newarr5=np.power(arr9,arr10)
print(newarr5)

# numpy array Remainder 
arr11=np.array([10, 20, 30, 40, 50, 60])
arr12=np.array([3, 5, 6, 8, 2, 33])

newarr6=np.remainder(arr11,arr12) # you'll get same results if you remainder()
print(newarr6)

# numpy Quotient and mod
arr13=np.array([10, 20, 30, 40, 50, 60])
arr14=np.array([3, 7, 9, 8, 2, 33])

newarr7=np.divmod(arr13,arr14)
print(newarr7)
# numpy Absolute values
arr15=np.array([-1, -2, 1, 2, 3, -4])
newarr8=np.absolute(arr15)

print(newarr8)