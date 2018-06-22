import numpy as np

my_list = [1,2,3]
print(my_list)

arr = np.array(my_list)
print(arr)

my_matrix = [[1,2,3],[4,5,6],[7,8,9]]

mat = np.array(my_matrix)
print(mat)

print(np.arange(0,10,2))
# step optional

print(np.zeros((2,4)))
# simple int instead of tuple does a row

print(np.ones((1,7)))
#simple int does a row

print(np.linspace(0,5,10))
# 10 evenly spaced points from 0 to 5

print(np.eye(4))
# identity matrix

print(np.random.rand(5))
print(np.random.rand(5,5))

# random number from a normal distribution
print(np.random.randn(2))

print(np.random.randint(0, 100, 6))

arr = np.arange(25)

arr = arr.reshape(5,5)
print(arr)

#print max/min value
print(arr.max())
print(arr.min())
# print index
print(arr.argmax())
print(arr.argmin())

# get the attribute
print(arr.shape)

#type in the array
print(arr.dtype)

