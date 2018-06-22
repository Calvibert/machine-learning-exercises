import numpy as np
import pandas as pd
from numpy.random import randn

np.random.seed(101)

df = pd.DataFrame(randn(5,4),['A','B','C','D','E'], ['W','X','Y','Z'])
print(df)
# Each column W,X,Y,Z is a pandas series

# Grab a series object
print(df['W'])
print(type(df['W']))
print(df.W)

print(df[['W','Z']])

df['new'] = df['W'] + df['X']
print(df)

df = df.drop('new',axis=1)
print(df)

#df.drop('new', axis=1, inplace=True)

print(df.shape)

print(df.loc['A'])

print(df.iloc[0])

print(df.loc['A','W'])

print(df.loc[['A','B'],['W','X']])