#!/usr/bin/env python
# coding: utf-8

# In[ ]:

import numpy as np
import matplotlib.pyplot as plt

# first we define a single 1d rod to model our equation 

a = 110 # mm^2/2 this is thermal diffusability, unit of how fast 
length = 50 # mm length of the rod
time = 4 #seconds time taken for 
nodes = 10

# initialization 
dx = length / nodes #spatial discrete element basically the disance between the nodes
dt = 0.5 * dx**2 / a # derived from the stability analysis of the finite difference scheme ensuring the numerical solution remains stable
t_nodes = int(time/dt) 

#distribution before starting the simulation must also be known 

u = np.zeros(nodes) + 20 # we keep the plate initially at 20 degrees 

#Boundary conditions 
# the temperature at the ends of the rod must be known at any time 

u[0] = 100 #starting end of the rod
u[-1] = 100 #ending end of the rod

# Visualizing with a plot

fig, axis = plt.subplots()

pcm = axis.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=axis)
axis.set_ylim([-2, 3])

#Simulating
counter = 0

while counter < time :

    w = u.copy()

    for i in range(1, nodes - 1):

        u[i] = dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx ** 2 + w[i]

    counter += dt

    print("t: {:.3f} [s], Average temperature: {:.2f} Celcius".format(counter, np.average(u)))

    # Updating the plot

    pcm.set_array([u])
    axis.set_title("Distribution at t: {:.3f} [s].".format(counter))
    plt.pause(0.01)


plt.show()
