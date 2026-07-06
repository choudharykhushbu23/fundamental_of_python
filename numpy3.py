# array with standard python
import array
a=array.array("i",[1,2,3,4,5])
print(a)

# finding the time taken by standard python
import time
start=time.time()
a=[]
for i in range(1000000):
    a.append(i)
b=[]
for i in range(10000):
    b.append(i)
c=[]
for i in range(10000):
    c.append(a[i]+b[i])
print(time.time()-start)

import numpy as np
import time
start=time.time()
a=np.arange(10000)
b=np.arange(10000)
c=a+b
print(time.time()-start)

#array using numpy
import numpy as np
a=np.array([1,2,3,4,5,6])
print(a)

import numpy as np
a=np.array([1,2,3,4,5,6])
print(a.dtype)

#creating a different type of matrix
""" simple print"""
import numpy as np
a=np.array([[1,2],[3,4],[5,6]])
print(a)

""" for print all zeros"""
b=np.zeros((3,3),dtype=int)
print(b)

"""for print all ones"""
c=np.ones((3,3),dtype=int)
print(c)
c=np.ones((5,4),dtype=int)
print(c)

"""for print a number of our choice"""
d=np.full((3,4),7.5)
print(d)


import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print(np.shape(a))
print(np.ndim(a))

import numpy as np
a=np.array([[1,2,3],[4,5,6]])
b=a.astype(float)
print(b)
print(b.dtype)

"""airthmetic operation on single array(one dimension)"""
import numpy as np
a=np.array([1,2,3,4,5,6])
print(np.sum(a))
print(np.max(a))
print(np.min(a))
print(np.mean(a))
print(np.std(a))
print(np.var(a))

"""airthmatic operations on two array(two dimension)"""
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[10,20,30,40,],[50,60,70,80]])   
print(np.add(a,b))
print(np.subtract(a,b))
print(np.multiply(a,b))
print(np.divide(a,b))

"""indexing using numpy"""
a=np.array([1,2,3,4,5,6])
print(a[[1,2,3]])  # always use two brackets because in one bracket only one arrgument pass

""" slicing using numpy"""
a=np.array([1,2,3,4,5,6])
print(a[1:5:1])   #slicing-(start index,stop index(n-1),step(jump))
print(a[::-1])    #reverse slicing

"""dimension,size,shape and reshape of an array"""
a=np.array([1,2,3,4,5,6])
print(a.ndim)
print(a.shape)
print(a.size)
print(a.reshape(3,2))

""" how to insert element in array"""
a=np.array([1,2,3,4,5,6])
b=np.insert(a,2,4,axis=None) #(variable name where you want to add elemnt,index no.,element that you want to add)
print(b)

"""x axis = 0,y axis=1"""
a=np.array([[1,2,3,4],[5,6,7,8]])
b=np.array([[10,20,30,40,],[50,60,70,80]]) 
c=np.concatenate((a,b))
print(c)  

"""to delete"""
a=np.array([1,2,3,4,5,6,7])
b=np.delete(a,3,axis=None) # # axis=None means perform the operation on all elements of the array,without considering rows or columns
print(b)


"""horizontly and vertically"""
a=np.array([1,2,3,4])
b=np.array([1,2,3,4])  
print(np.vstack((a,b)))
print(np.hstack((a,b)))