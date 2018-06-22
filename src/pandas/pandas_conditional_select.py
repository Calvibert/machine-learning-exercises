import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])

print(df)

booldf = df > 0
print(df[booldf])

print(df['W'] > 0)

print(df[df['W'] > 0])

resultdf = df[df['Z'] < 0]

print(resultdf['X'])

print(df[df['W'] > 0][['X','Y']])

print(df[(df['W']>0) | (df['Y']>1)])

print(df.reset_index())
#previous index becomes data and index becomes numerical
# must also specify inplace=True for inplace

newind = 'CA NY WY OR CO'.split()
#creates a list

df['States'] = newind
print(df)
df.set_index('States',True,False,True)
print(df)