import numpy as np
import matplotlib.pyplot as plt

def list_fractions(amount):
    fractions = []
    difference = []
    for i in range(1, amount):
        fractions.append(1/i)
        print(fractions[i-1])
    return fractions

def list_differences(list):
    difference = []
    for i in range(0, len(list)):
        if list[int(i-1)]:
            diff = list[i-1] - list[i]
            difference.append(diff)
            print(diff)
    return difference

amount = 16

fractions = list_fractions(amount)
print(fractions)
numpy_fractions = np.array(fractions)

differences = list_differences(fractions)
print(differences)
numpy_differences = np.array(differences)
