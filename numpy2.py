# Array attrtibute and shapes manipulation
import numpy as np
a=np.array([[1,2,3],[4,5,6]])
print("Shapes:-",a.shape)
print("Dimension:-",a.ndim)
print("Size:-",a.size)
print("Datatype:-",a.dtype)

# reshape the array
reshaped=a.reshape(3,2)
print(reshaped)

#indexing and slicing
arr = np.array([[10,20,30],[40,50,60],[70,80,90]])
print(arr[0])
print(arr[0:2])
#arr[row_starting point:row_ending point,column starting point:row ending point]
print(arr[0:2,1:3])

#multiplication operation
x=np.array([1,2,3])
y=np.array([4,5,6])
print("addition:-",x+y)
print("subtraction:-",x-y)
print("multiplication:-",x*y)
print("division:-",y/x)
print("square:-",np.sqrt(x))
print("exponent:-",np.exp(x))
print("logarithm:-",np.log(x))