import numpy as np
import matplotlib.pylab as plot
from math import *

#Model parameters
v = 30    # initial velocity  in m/s
g = 9.8 # gravitational acceleration in m/s^2

theta = np.arange(pi/6, pi/3, pi/30)  # Gererate different angles.
time = np.linspace(0, 5, 100) # Define time as a continuous variable.
for i in theta:
    X = []     # Define an empty array
    Y = []     # Define another empty array
    for t in time:
        x = ((v*t)*np.cos(i)) # positions at every point in time
        y = ((v*t)*np.sin(i))-((0.5*g)*(t**2))
        X.append(x)  # Fill up the empty array x1
        Y.append(y)  # Fill up the empty array y1
    p = [i for i, j in enumerate(Y) if j < 0]
    for i in sorted(p, reverse = True):
        del X[i]
        del Y[i]
    plot.plot(X, Y)

plot.show()
