import numpy as np
import pandas as pd
from numpy.random import randn

data = {'Company':['GOOG','GOOG','MSFT','MSFT','FB','FB'],
       'Person':['Sam','Charlie','Amy','Vanessa','Carl','Sarah'],
       'Sales':[200,120,340,124,243,350]}

df = pd.DataFrame(data)
print(df)

by_comp = df.groupby('Company')
print(by_comp.mean())
print(by_comp.std())
print(by_comp.sum().loc['GOOG'])

print(df.groupby('Company').describe().transpose())