import numpy as np
import matplotlib.pyplot as plt

xRange = 15
X = np.arange(0,xRange)

Y = []
Y.append(0)
Y.append(1)
for i in range(2,xRange):
    Y.append(Y[i-2] + Y[i-1]) 

plt.plot(X,Y)

plt.show()