#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Welcome back for Day 4.

In today's morning session, we will be working with panda dataframe and text 
files

Goal: Getting comfortable with reading and writing data, doing simple data 
manipulation, and visualizing data.

Task: Fill in the cells with the correct codes


@author: Peng Mun Siew
"""
#%%
"""
Unzipping a zip file using Python. On Tuesday, we showed how to use tar to 
unzip a zip file. Let's try using a Python function to unzip a file.
"""
# Importing the required packages
import zipfile

with zipfile.ZipFile('Data/jena_climate_2009_2016.csv.zip', 'r') as zip_ref:
    zip_ref.extractall('Data/jena_climate_2009_2016/')
    
    
#%%
"""
We will be reading the csv file using panda dataframe.

Using panda dataframe to read a csv file and doing some simple data manipulation
"""
# Importing the required packages
import pandas as pd

csv_path = 'Data/jena_climate_2009_2016/jena_climate_2009_2016.csv'
df = pd.read_csv(csv_path)

#%%
"""
TODO: Introduction to dataframe; data slicing, removing data from the 
dataframe, assessing first and last n-th elements
"""

#%%
"""
Plot a subset of data from the dataframe
"""

plot_cols = ['T (degC)', 'p (mbar)', 'rho (g/m**3)']


#%%
"""
Quickly visualize the statistic of our data
"""
df.describe().transpose()

#%%
"""
TODO: Data filtering. From our table above, we noticed that the wind speed (wv) 
and max. wv has unrealistic values (-9999). These outliers need to be removed 
from our data by substituting with an interpolated value.
"""


#%%
"""
TODO: Generating histogram and heatmap (2D histogram)
"""

#%%
"""
TODO: Generating heatmap (2D histogram)
"""


#%%
"""
Assignment 1: Visualize the density values along the trajectory of the CHAMP 
satellite for the first 50 days in 2002

Trajectory of CHAMP in year 2002 - Data interpolation - 
https://zenodo.org/record/4602380#.Ys--Fy-B2i5

Assignment 1(a): Extract hourly position location (local solar time, lattitude,
altitude) from the daily CHAMP data to obtain the hourly trajectory of the 
CHAMP satellite in 2002
"""
#%%
"""
Hint 1: How to identify dir path to files of interest
"""
import os


#%%
"""
Hint 2: How to read a tab delimited text file
"""
import pandas as pd

header_label = ['GPS Time (sec)','Geodetic Altitude (km)',
                'Geodetic Latitude (deg)','Geodetic Longitude (deg)',
                'Local Solar Time (hours)','Velocity Magnitude (m/s)',
                'Surface Temperature (K)','Free Stream Temperature (K)',
                'Yaw (rad)','Pitch (rad)','Proj_Area_Eric (m^2)','CD_Eric (~)',
                'Density_Eric (kg/m^3)','Proj_Area_New (m^2)','CD_New (~)',
                'Density_New (kg/m^3)','Density_HASDM (kg/m^3)',
                'Density_JB2008 (kg/m^3)' ]



#%%
"""
Hint 3: Data slicing (Identifying data index of interest and extracting the 
relevant data (local solar time, lattitude, altitude))
"""
import numpy as np

# get index of data that satisfy our condition
idx_interest = np.where(df['GPS Time (sec)']== 10)[0] 
print(df['Geodetic Altitude (km)'][idx_interest])


#%%
"""
Hint 4: The remainder operator is given by % and might be useful.
"""
arr = np.linspace(1,20,20)
print(arr%5)


#%%
"""
Assignment 1(b): Load the JB2008 date that we have used in the morning and use 
3d interpolation to obtain the density values along CHAMP's trajectory
"""


#%%
"""
### Hint 1: Follow the instruction from the morning section and use 
RegularGridInterpolator from the scipy.interpolate package
"""

# Example:
from scipy.interpolate import RegularGridInterpolator

# First create a set of sample data that we will be using 3D interpolant on
def f(x, y, z):
    return 2 * x**3 + 3 * y**2 - z

x = np.linspace(1, 4, 11)
y = np.linspace(4, 7, 22)
z = np.linspace(7, 9, 33)
xg, yg ,zg = np.meshgrid(x, y, z, indexing='ij', sparse=True)

sample_data = f(xg, yg, zg)

# Generate Interpolant (interpolating function)
my_interpolating_function = RegularGridInterpolator((x, y, z), sample_data)

# Say we are interested in the points [[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]]
pts = np.array([[2.1, 6.2, 8.3], [3.3, 5.2, 7.1]])
my_interpolating_function(pts)


#%%
"""
Assignment 1(c): Plot the variation in density along CHAMP's trajectory as a 
function of time
"""



#%%
"""
Assignment 1(d): Now do it using the TIE-GCM density data and plot both density 
variation under the same figure
"""



#%%
"""
Assignment 1(e): The plots look messy. Let's calculate the daily average 
density and plot those instead. 

Hint: Use np.reshape and np.mean
"""



#%%
"""
Assignment 1(f): Load the accelerometer derived density from the CHAMP data 
(Density_New (kg/m^3)). Calculate the daily mean density and plot this value 
together with the JB2008 density and TIE-GCM density calculated above.
"""


#%%
"""
Assignment 2: Make a python function that will parse the inputs to output the 
TIE-GCM density any arbritary position (local solar time, latitude, altitude) 
and an arbritary day of year and hour in 2002

"""


