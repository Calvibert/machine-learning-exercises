import numpy as np
import pandas as pd
from numpy.random import randn

d = {'A':[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}

df = pd.DataFrame(d)
print(df)

#df.dropna(0,'any',None,None,True)
print(df.dropna())
print(df.dropna(thresh=2))

print(df.fillna(value='fill'))

print(df['A'].fillna(value=df['A'].mean()))