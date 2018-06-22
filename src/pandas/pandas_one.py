import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
dict = {'a':10,'b':20,'c':30}

ser_one = pd.Series(data = my_data)
print(ser_one)

print(pd.Series(data = my_data, index=labels))
ser_two = pd.Series(my_data, labels)
print(ser_two)

print(pd.Series(arr))
#python list works the same as an array

print(pd.Series(dict))

ser1 = pd.Series([1,2,3,4],['USA','CAN','GER','USSR'])
print(ser1)
ser2 = pd.Series([1,2,5,4],['USA','CAN','JPN','CHN'])
print(ser2)
print(ser2['USA'])
ser3 = pd.Series(labels)
print(ser3)

print(ser1 + ser2)