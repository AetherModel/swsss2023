#!/usr/bin/env python

import numpy as np
import re
from datetime import datetime
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------
# Read in the EUV CSV file.  Get out:
#   - short and long wavelengths
#   - EUV parameters
#   - Absorption cross sections for N2, O2, and O
#-----------------------------------------------------------------------------

def read_euv_csv_file(file):

    fpin = open(file, 'r')

    iColStart = 5
    iColEnd = -1

    for line in fpin:
        cols = line.split(',')
        if (cols[0] == 'Short'):
            short = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'Long'):
            long = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'F74113'):
            f74113 = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'AFAC'):
            afac = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'N2' and cols[2] == 'abs'):
            n2cs = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'O2' and cols[2] == 'abs'):
            o2cs = np.asarray(cols[iColStart:iColEnd], dtype = float)
        if (cols[0] == 'O' and cols[2] == 'abs'):
            ocs = np.asarray(cols[iColStart:iColEnd], dtype = float)
    
    fpin.close()

    data = {'short': short * 1e-10,
            'long': long * 1e-10,
            'f74113': f74113 * 1e9 * 1e4, # /cm2 to /m2
            'afac': afac,
            'ocross': ocs * 1e-22,
            'o2cross': o2cs * 1e-22,
            'n2cross': n2cs * 1e-22}

    return data

#-----------------------------------------------------------------------------
# Plot out spectrum to a file
#-----------------------------------------------------------------------------

def plot_spectrum(wavelengths_in_m, intensities, filename):

    fig = plt.figure(figsize = (10,5))
    ax = fig.add_subplot(111)

    ax.scatter(wavelengths_in_m * 1e10, intensities)
    ax.set_xlabel('Wavelength (A)')
    ax.set_ylabel('Intensity (photons/m2/s)')

    fig.savefig(filename)
    plt.close()
    
#-----------------------------------------------------------------------------
# Plot var as a function of altitutde
#-----------------------------------------------------------------------------

def plot_value_vs_alt(alts, values, filename, var_name, is_log = False):

    fig = plt.figure(figsize = (5,10))
    ax = fig.add_subplot(111)

    ax.plot(values, alts)
    ax.set_xlabel(var_name)
    ax.set_ylabel('Altitude (km)')
    if (is_log):
        ax.set_xscale('log')
    
    fig.savefig(filename)
    plt.close()
    
