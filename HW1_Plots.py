import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
constant = 4

[X, Y] = np.meshgrid(x, y)

v = (-constant)*Y
u = constant*X

phi = constant*np.multiply(X, Y)

plt.figure()
plt.streamplot(X, Y, u, v)
plt.contour(X,Y,phi)
plt.show()