from numpy import random
x=random.randint(100)
print(x)
# Generate a random float from 0 to 1:
x=random.rand()
print(x)

x=random.randint(100,size=(5))
print(x)
# Generate a 2-D array with 3 rows, each row containing 5 random integers 

x=random.randint(100,size=(3,5))
print(x)


x=random.rand(3,5)
print(x)

x=random.choice([3,5,7,9],size=(3,5))
print(x)
"""
Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.

The probability for the value to be 3 is set to be 0.1

The probability for the value to be 5 is set to be 0.3

The probability for the value to be 7 is set to be 0.6

The probability for the value to be 9 is set to be 0
"""
x=random.choice([3,5,7,9],p=[0.1,0.3,0.6,0.0],size=(3,5))
print(x)