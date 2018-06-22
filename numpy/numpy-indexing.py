import numpy as np
import math

arr = np.arange(0,11)

print(arr)

print(arr[0])
print(arr[1:5])

slice_of_arr = arr[1:6]
print(slice_of_arr[:])

slice_of_arr[:] = 99
print(slice_of_arr)

arr_copy = arr.copy()
print(arr)
print(arr_copy)

arr_copy[:] = 100
print(arr)
print(arr_copy)

# 2D array

arr_2d = np.array([[5,10,15],[20,25,30],[35,40,45]])
print(arr_2d)
print(arr_2d[0][0])

print(arr_2d[0])
print(arr_2d[0,0])

print(arr_2d[:2,1:3])
print(arr_2d[1:3,:])

print('For loop:')
for i in range(0,4):
    print(arr_2d[math.floor(i/2):math.floor((i+2)/2),i:i+2])

print('Boolean comparison:')
bool_arr = arr_2d < 25
print(bool_arr)
print(arr_2d[bool_arr])
