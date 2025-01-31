import numpy as np
import matplotlib.pyplot as plt



x = np.linspace(0,1,100)
y = np.linspace(0,1,100)
constant = 4
refine = 5

[X, Y] = np.meshgrid(x, y)

v = (-constant)*Y
u = constant*X

psi = constant*np.multiply(X, Y)

phi = constant/2*np.subtract(np.power(X,2), np.power(Y,2))

pressures = .5*(np.add(np.power(u,2),np.power(v,2)))

levels = [0, .1, .25, .5, .75, 1, 1.5, 2, 2.5, 3, 3.5, 4]

plt.figure(1)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,psi, levels=levels)
plt.title("Streamlines")
plt.contour

levels = np.linspace(-2,2,13)

plt.figure(2)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,phi, levels=levels)
plt.title("Velocity Potential")
plt.contour

levels= np.linspace(0,16,15)

plt.figure(3)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,pressures, levels=levels)
plt.title("Pressure Contours")
plt.contour
plt.show()