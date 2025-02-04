import numpy as np
import matplotlib.pyplot as plt
import math


####### P1
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
#########

#### P3
theta = np.linspace(0, 2*math.pi, 100)
Cp = []

for angle in theta:
    Cp.append(1-(4*(math.sin(angle))**2))
######
##### P4
theta4 = np.linspace(0, 2*math.pi, 100)
crit_vals = [0, math.pi/4, math.pi/2, 3*math.pi/4, math.pi, 5*math.pi/4, 3*math.pi/2, 7*math.pi/4]
vals= []

Cp4 = []
for angle in theta4:
    Cp4.append(1-(4*(math.sin(angle))**2 - 2.25*math.sin(angle)*2/(3.6*math.pi*.1) + 2.25**2/(4*(3.6**2)*(math.pi**2)*(.1**2))))

for angle in crit_vals:
    vals.append(1-(4*(math.sin(angle))**2 - 2.25*math.sin(angle)*2/(3.6*math.pi*.1) + 2.25**2/(4*(3.6**2)*(math.pi**2)*(.1**2))))

print(vals)

##### P1 Plotting
levels = [0, .1, .25, .5, .75, 1, 1.5, 2, 2.5, 3, 3.5, 4]
plt.figure(1)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,psi, levels=levels)
plt.title("Prob. 1b Streamlines")
plt.contour

levels = np.linspace(-2,2,13)

plt.figure(2)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,phi, levels=levels)
plt.title("Prob. 1 Velocity Potential")
plt.contour

levels= np.linspace(0,16,15)

plt.figure(3)
q = plt.quiver(X[::refine,::refine], Y[::refine,::refine], u[::refine,::refine], v[::refine,::refine], pivot='mid')
plt.quiverkey(q, X=.5, Y=-.08, U=10, label='Flow Direction', labelpos='S')
c = plt.contour(X,Y,pressures, levels=levels)
plt.title("Prob. 1d Pressure Contours")
plt.contour
########

####### P3 Plotting
plt.figure(4)
plt.plot(theta, Cp)
plt.title("Prob. 3b Pressure Distribution on a Cylinder as a Function of Angle")
plt.xlabel('Radians')
plt.ylabel("Cp")
#######

######## P4 Plotting
plt.figure(5)
plt.plot(theta4, Cp4)
plt.title("Prob. 4c Pressure Distribution on a Lifting Cylinder as a Function of Angle")
plt.xlabel('Radians')
plt.ylabel("Cp")
#########


#######
plt.show()
