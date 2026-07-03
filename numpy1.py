#1 check the version of numpy
import numpy as np

print(np.__version__)



#2 creating a array in numpy

a= np.array([1,2,3,4,5])
print("one dimensional array:\n", a)
b= np.zeros((3,3))
print("three dimensional array:\n",b)
c=np.ones((2,4))
print("two dimensional array of one:\n", c)
d=np.full((2,2),5)
print("two dimensional array of 5:\n",d)
e=np.arange(0,199,2)
print("array of even no. from 0to 100:\n",e)
f=np.linspace(0,1,5)
print("array of 5 number btw 0 and 1:\n",f)