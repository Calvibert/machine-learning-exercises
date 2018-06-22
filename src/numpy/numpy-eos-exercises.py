import numpy as np
import math
import random

zeros = np.zeros(10)
print(zeros)

ones = np.ones(10)
print(ones)

fives = np.zeros(10)
fives[:] = 5
print(fives)

space_out = np.linspace(10, 50, 41)
print(space_out)

space_out_even = np.linspace(10, 50, 21)
print(space_out_even)

three_by_three = np.arange(9).reshape(3,3)
print(three_by_three)

r = np.random.rand(1)
print(r)

rn = np.random.randn(25)
print(rn)

ten_by_ten = np.linspace(0.01, 1, 100).reshape(10, 10)
print(ten_by_ten)

twenty_lin_space = np.linspace(0, 1, 20)
print(twenty_lin_space)

#Section 2
print('\nSection two:\n')

mat = np.arange(1,26).reshape(5,5)
print(mat)

print(mat[2:,1:])

print(mat[3,4])

print(mat[0:3,1:2])

print(mat[4:,:])

print(mat[3:,:])

#Section 3
print('\nSection three:\n')

print(mat.sum())

print(mat.std())

print(mat.sum(axis=0))