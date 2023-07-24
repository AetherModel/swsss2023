# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 13:51:02 2023

@author: mayan
"""
import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0,1)
plt.plot(x, np.exp(x))
plt.xlabel(r'$ 0 \leq x < 1 $')
plt.ylabel(r'$E^x$')
plt.title('Exponential function')
plt.show()


 