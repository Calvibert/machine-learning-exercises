import numpy as np
import matplotlib.pyplot as plt

noTerms = 100

X = np.arange(1,noTerms)

Y = list(range(1,noTerms))
count = 0
distance = 2
dCount = 0

while dCount < 10:
    temp = []
    count = 0
    for i in range(0,len(Y)):
        count = count+1
        if count != distance:
            temp.append(Y[i])
        else:
            count = 0
    dCount = dCount+1
    distance = temp[dCount]
    Y = temp

X = np.arange(0,len(Y))

plt.plot(X,Y,color="purple",label="Lucky series")

plt.legend(loc='upper left', frameon=False)
plt.annotate('Value at x=5', xy=(5,15), xytext=(1,25), arrowprops=dict(arrowstyle="->"))

plt.savefig("figures/luckySeries.png",dip=100)
plt.show()
