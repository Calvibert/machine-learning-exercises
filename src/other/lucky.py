import numpy as np
import matplotlib.pyplot as plt

noTerms = 40

X = np.arange(1,noTerms)

Y = list(range(1,noTerms))
count = 0
distance = 2

while distance < 10:
    temp = []
    print("The current parameters are: \nDistance: {distance}".format(distance=distance))
    for i in range(0,len(Y)):
        count = count+1
        if count != distance:
            print(Y[i])
            temp.append(Y[i])
        else:
            count = 0
    distance = temp[distance-1]
    Y = temp

print(Y)
