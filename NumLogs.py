from math import log 
import numpy as np
arr=np.arange(1,10)
print(np.log2(arr))

# log at Base 10
print(np.log10(arr))

# Natural Log, Log at Base e
print(np.log(arr))
# Log at any Base
nplog=np.frompyfunc(log,2,1)
print(nplog(100,15))

