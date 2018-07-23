import numpy as np
from prettytable import PrettyTable as pt

# array = np.loadtxt(open("may2018comm.csv", "rb"), dtype="str", delimiter=";", skiprows=1)

array = np.genfromtxt(open("may2018comm.csv", "rb"), dtype="str", delimiter=";", skip_header=1)
print(array)