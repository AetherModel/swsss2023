#!/usr/bin/env python

import numpy as np

#-----------------------------------------------------------------------------
# Define some useful constants
#-----------------------------------------------------------------------------

cKB_ = 1.38064852e-23
cRE_ = 6371.0
cG_ = 9.81
cAMU_ = 1.6726219e-27
cH_ = 6.6261e-34
cC_ = 2.9979e8
cE_ = 1.6022e-19
cD2R_ = 3.1415927 / 180.0

#-----------------------------------------------------------------------------
# calculate the scale height, which is KT/mg, where:
#   k - boltzmann's constant
#   t = temperature
#   m = mass
#   g = gravity
#  Feed in 
#-----------------------------------------------------------------------------

def calc_scale_height(mass_in_amu, alt_in_km, temp_in_k):

    gravity = cG_ * (cRE_ / (cRE_ + alt_in_km))
    mass_in_kg = mass_in_amu * cAMU_
    h_in_km = cKB_ * temp_in_k / mass_in_kg / gravity / 1000.0;

    return h_in_km

#-----------------------------------------------------------------------------
# Calculate a hydrostatic solution:
#  n(i+1) = n(i) * t(i+1)/t(i) * exp(dz / H)
#  where:
#  n = density
#  t = temperature
#  dz = delta-z (delta altitude)
#  H = scale-height
#-----------------------------------------------------------------------------

def calc_hydrostatic(density_bc, scale_height_in_km, temp_in_k, alt_in_km):

    nAlts = len(alt_in_km)
    density = np.zeros(nAlts)

    # define our boundary condition
    density[0] = density_bc
    for iAlt in range(1, nAlts):
        tRatio = temp_in_k[iAlt] / temp_in_k[iAlt - 1]
        dz = alt_in_km[iAlt] - alt_in_km[iAlt - 1]
        h = scale_height_in_km[iAlt]
        density[iAlt] = density[iAlt-1] * tRatio * np.exp(-dz / h)

    return density

#-----------------------------------------------------------------------------
# EUVAC - take F107 and F107a and return solar spectrum
# See Schunk and Nagy, page 259
#-----------------------------------------------------------------------------

def EUVAC(f74113, afac, f107, f107a):
    p = (f107 + f107a)/2.0
    if (p < 80):
        p = 80.0
    intensity = f74113 * (1.0 + afac * (p-80))
    return intensity
        
#-----------------------------------------------------------------------------
# Take a wavelength in m and convert it to energy in Joules:
# e = plank's constant * speed of light / wavelength
#-----------------------------------------------------------------------------

def convert_wavelength_to_joules(wavelength):
    energy = cH_ * cC_ / wavelength
    return energy

#-----------------------------------------------------------------------------
# Calculate Tau for a given species, given:
#  - solar zenity angle (in degrees)
#  - density in /m3
#  - scale height in km
#  - cross sections in /m2
#-----------------------------------------------------------------------------

def calc_tau(SZA_in_deg, density_in_m3, scale_height_in_km, cross_section):

    # We are only going to do this for a single wavelength for now!

    cs = cross_section[0]

    # convert scale height to m:
    h = scale_height_in_km * 1000.0

    # convert SZA to radians:
    sza = SZA_in_deg * cD2R_

    # calculate integrated density (which is density * scale height):
    integrated_density = density_in_m3 * h

    nWaves = len(cross_section)
    nAlts = len(density_in_m3)
    tau = np.zeros((nWaves, nAlts))

    # calculate Tau:
    iWave = 5
    tau[iWave][:] = integrated_density * cross_section[iWave]

    return tau

#-----------------------------------------------------------------------------
# Calculate energy deposition as a function of altitude, given:
#  - density of a given species in /m3 as a function of altitude
#  - intensity at infinity as a function of wavelength
#  - tau as a function of wavelength and altitude
#  - cross_section of the given species as a function of wavelength
#  - energies of the wavelengths
#  - efficiency of the heating (say 30%)
#-----------------------------------------------------------------------------

def calculate_Qeuv(density_in_m3,
                   intensity_inf,
                   tau,
                   cross_section,
                   energies,
                   efficiency):

    nAlts = len(density_in_m3)
    nWaves = len(intensity_inf)

    Qeuv = np.zeros(nAlts)

    iWave = 5

    # intensity is a function of altitude (for a given wavelength):
    intensity = intensity_inf[iWave] * np.exp(-tau[iWave][:])
    Qeuv = Qeuv + \
        efficiency * \
        density_in_m3 * \
        intensity * \
        cross_section[iWave] * \
        energies[iWave]

    return Qeuv

#-----------------------------------------------------------------------------
# calculate rho given densities of O (and N2 and O2)
#-----------------------------------------------------------------------------

def calc_rho(density_o, mass_o):
    rho = density_o * mass_o * cAMU_
    return rho

#-----------------------------------------------------------------------------
# calculate cp.  We have hard coded this to be 1500, which is for O, but
# we could pass densities and vibrational states and get the real Cp.
#-----------------------------------------------------------------------------

def calculate_cp():
    cp = 1500.0
    return cp

#-----------------------------------------------------------------------------
# calculate dT/dt from Q and rho:
#-----------------------------------------------------------------------------

def convert_Q_to_dTdt(Qeuv, rho, cp):
    dTdt = Qeuv / (rho * cp)
    return dTdt

