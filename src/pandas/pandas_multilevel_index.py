import numpy as np
import pandas as pd
from numpy.random import randn
np.random.seed(101)

# Index Levels
outside = ['G1','G1','G1','G2','G2','G2']
inside = [1,2,3,1,2,3]
hier_index = list(zip(outside,inside))
hier_index = pd.MultiIndex.from_tuples(hier_index)

print(list(zip(outside,inside)))

df = pd.DataFrame(randn(6,2),hier_index,['A','B'])
print(df)

print(df.loc['G1'])
print(df.loc['G1'].loc[1])

df.index.names = ['Groups','Nums']
print(df)

print(df.loc['G2'].loc[2]['B'])

print(df.loc['G1'].loc[2]['B'])

print(df.xs('G1'))

print(df.xs(1,level='Nums'))