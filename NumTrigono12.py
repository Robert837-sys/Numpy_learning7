import numpy as np 
arr=np.array([np.pi/2,np.pi/3,np.pi/4,np.pi/5])
x=np.sin(arr)
print(x)
# Convert all of the values in following array arr to radians:
arr3=np.array([90,180,270,360])
y=np.deg2rad(arr3)
print(y)
# Convert all of the values in following array arr to degrees:
arr4=np.array([np.pi/2,np.pi,1.5*np.pi,2*np.pi])
z=np.rad2deg(arr)
print(z)
# Find the angle of 1.0:
t=np.arcsin(1.0)
print(t)
#Find the angle for all of the sine values in the array
arr4=np.array([1,-1,0.1])
g=np.arcsin(arr4)
print(g)
h=np.rad2deg(g)
print(h)
# Find the hypotenues for 4 base and 3 perpendicular:
base=3
perp=4
x=np.hypot(base,perp)
print(x)