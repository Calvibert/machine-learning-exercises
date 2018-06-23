import numpy as np
import matplotlib.pyplot as plt

def list_fractions(amount):
    fractions = []
    difference = []
    for i in range(1, amount):
        fractions.append(1/i)
    return fractions

def list_differences(list):
    difference = []
    for i in range(0, len(list)):
        if list[int(i-1)]:
            diff = list[i-1] - list[i]
            difference.append(diff)
    return difference

amount = 20

fractions = list_fractions(amount)
numpy_fractions = np.array(fractions)

differences = list_differences(fractions)
del differences[0]
numpy_differences = np.array(differences)

plt.plot(range(1,amount), numpy_fractions)
plt.plot(range(2,amount), numpy_differences)

plt.show()