import numpy as np

# array = np.loadtxt(open("may2018comm.csv", "rb"), dtype="str", delimiter=";", skiprows=1)

array = np.genfromtxt(open("may2018comm.csv", "rb"), dtype="str", delimiter=";", skip_header=1)
print(array)