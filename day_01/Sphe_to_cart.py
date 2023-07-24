# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 14:58:58 2023

@author: mayan
"""

""" A 3D plot script for spherical co-rodinate."""
__auther__ = 'Mayank Kumar'
__email__ = 'mayankgis786@gmail.com.'

import numpy as np # Here we have imported the numpy as a module

import matplotlib.pyplot as plt

# Below is the finction for converting the spherical co-ordinate to the cartesian co-ordinate""

def sphe_to_cart(r, theta, phi): # Define the function
    """Below is the main body of the function"""
    x = r*np.sin(theta)*np.cos(phi)
    y = r*np.sin(theta)*np.sin(phi)
    z = r*np.cos(theta)
    return x,y,z # We have return the output of the function 
                 # Output is the tuple
                 
r = 1 # Assigning the value to the argument
theta = 90
phi = 45

Output = sphe_to_cart(r, theta, phi) # Let's get some output after putting the arguments
print(Output)

# Below are the assertation tests

assert sphe_to_cart(1,0,0) == (0,0,1) 

#assert sphe_to_cart(1,np.pi, np.pi) = (0,0,-1)

assert np.allclose([sphe_to_cart(1,np.pi, np.pi)], [0,0,-1])

assert np.allclose([sphe_to_cart(1,2*np.pi, 2*np.pi)], [0,0,1])

assert np.allclose([sphe_to_cart(1,-np.pi/2, np.pi/2)], [0,-1,0])

assert np.allclose([sphe_to_cart(1,2*np.pi, np.pi/2)], [0, 0 , 1])

fig = plt.figure() # Better control # gives the empty plot

axes = plt.axes(projection = '3d') # create the 3D axes

#plt.show() # Show the created the 3D plot

r = np.linspace(0,1) # create the array for the variable r 

#print(type(r)), we can check this by uncommneting this line

theta = np.linspace(0,2*np.pi)  # create the array for the variable theta

phi = np.linspace(0, 2*np.pi) # create the array for the varible theta

x,y,z = sphe_to_cart(r, theta, phi) # this take the above created array.
# It basically convert it to the x, y and z using the function above

axes.plot(x,y,z)  # Here it plot x,y,z on the axes

plt.show() # We get to see the plot
