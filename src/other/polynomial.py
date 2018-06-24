import numpy as np
import matplotlib.pyplot as plt


class Quadratic:

    def __init__(self, a, b, c, start=0, end=10):
        self.a = a
        self.b = b
        self.c = c
        self.start = start
        self.end = end
        self.Y=[]
        self.X=np.arange(start, end)
        self.secondDegree()

    def secondDegree(self):
        for i in range(self.start, self.end):
            self.Y.append(self.a*(i**2) + self.b*i + self.c)

    def display(self):
        plt.plot(self.X, self.Y)
        self.setLims()
        plt.show()

    def setLims(self):
        ymin = min(self.Y) - abs(0.1*min(self.Y))
        ymax = max(self.Y) + abs(0.1*max(self.Y))
        plt.ylim(ymin, ymax)



quad = Quadratic(2,6,12,-10,11)
quad.display()