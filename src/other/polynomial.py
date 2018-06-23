import numpy as np
import matplotlib.pyplot as plt

def secondDegree(a, b, c, start, end):
    Y = []
    for i in range(start, end):
        print(a)
        Y.append(a*(i**2) + b*i + c)
    return Y

def display(X,Y):
    plt.plot(X,Y)
    plt.show()

start = -10
end = 10
X = np.arange(start,end)

a = 2
b = 6
c = 12
Y = secondDegree(a,b,c,start,end)
print(Y)
print(min(Y))
print(max(Y))

plt.ylim(min(Y),max(Y))

display(X,Y)