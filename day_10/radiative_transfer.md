
---
title: Solar EUV Drive Radiative Transfer in the Thermosphere

description: Week 2, Wednesday, Day 8 - Morning

author: Aaron Ridley (ridley@umich.edu)

keywords: space-weather, space, python, matplotlib, EUV
---

# Energy deposition

## General Idea

The description of how light is absorbed in a medium is called Radiative Transfer.  This can be very simple, or very complicated.  While what we are going to discuss may sound hard, it is just scratching the surface. Whole classes and carreers are focused on the study of radiative transfer, and we are going to cover it in this project!  We are barely touching it.

As light passes through a medium it is absorbed. Sometimes it is absorbed extremely quickly, and the medium is considered opaque to that particular wavelength of light. Sometimes barely any light is absorbed at all, and it is basically translucent to the wavelength.

This quality can be described with what is called an absorption cross section. Simplistically, this describes how transparent something is to a particular wavelength of light.  If is super small, then it will pass through lots of the medium before being absorbed.  If it is larger, then the light can't pass through much of the medium without being absorbed.

Extreme Ultraviolet (EUV) wavelengths of light are absorbed in the upper atmosphere of most planets.  This is because the energy of the EUV light is high enough that when it hits the major constituents in the atmosphere, it knocks of an electron (i.e., it ionizes).  Other wavelengths hit molecules and causes them to separate (disassociate).  Longer wavelenths don't have enough energy to do either, so they are not absorbed by the atmosphere and end up passing through (or being reflected by clouds) and hitting the ground where they are absorbed and heat the ground.

We want to work through the mathematics of how the EUV is absorbed in the atmosphere.  We then want to code this and have a model of how the atmosphere heats due to EUV absorption.

The mathematics of this is hand written here:
https://drive.google.com/file/d/1kVPylHsRwdBx_Gt5huHcoeR7_F4DPzvB

We will skip the math in this write up, but will outline the steps for making the code to do this.

A couple of things to understand before we start, though:

1. The solar EUV is in a spectrum.  While the spectrum is continuous, we describe it in terms of bins. We will be concentrating on 37 wavelength bins from rough 50 Angstroms to about 1000 Angstroms.  There are a variety of different models of the EUV spectrum, binned in a variety of ways.  We are going to use the EUVAC model to describe the spectrum.  This is dependent on the flux of 10.7 cm light, which can hit the ground and be measured.  It has been shown that this is an ok proxy for the different EUV wavelengths, and the EUVAC model describes this.

2. While there are a lot of different species in the upper atmosphere, O, N2, and O2 make up about 99% of the upper atmosphere, so we will concentrate on those.  Therefore, we need to cross sections for the 37 wavelengths for the 3 different species.


Here are steps on the road to producing a radiative transfer model of Earth's upper atmosphere. I am describing how I would code this from scratch and not the fastest way of coding it. I am going through the steps to make sure that it is coded correctly.

1. Download the solar EUV file (euv_37.csv).  Open this in excel or something so you can see the data. You should see rows for the wavelengths (Short, Long, which define the edges of the bins), F74113 and AFAC, which are used in the EUVAC model, and the abs cross sections for O, O2, and N2.  You will need these rows.  All of the other rows can be ignored.  Write a function that can read the CSV file and then returns the 37 values in each row that you need as a dictionary.

2. Make an altitude variable from about 100 - 500 km.

3. Make a function that takes the altitude and returns the initial temperature, which should be set to T = 200 + 600 * tanh( (alt - 100) / 100). Plot this out and verify that it looks as expected.

4. Make a function that takes the altitude, temperature, and the mass of a species and returns the scale-height as a function of altitude (including gravity).  Run this for O (16 AMU) and make sure it looks as expected.

5. Write an EUVAC function that takes F107 and F107a and returns I at infinity as a function of wavelengths for the 37 bins.

6. Make a function that takes the altitude, temperature, scale-height, and bottom density and returns the density as a function of altitude. Run this for O and make sure if looks as expected. (Use n(O, 100 km) = 5.0e17/m3.)

7. Make a function that takes SZA, n(O, z), H(O, z), sigma(O, wavelength) and returns Tau as a function of altitude. For a first pass, I would concentrate only on one wavelength (e.g., 50 - 100 Angstrom bin) and SZA = 0.  Plot out the single Tau as a function of wavelength.  Tau should pass through 1 somewhere between 120 - 150 km altitude.  Once this works, you can make the Tau for all of the 37 wavelength bins. Tau will then be a function of wavelength and altitude. 

8. Create a function that calculates the energy (QEUV) and ionization rates of O, O2, and N2 as a function of wavelength bin. It should take the wavelength and return energy and 3 ionization rates.

9. Create a function that calculates dT/dt given the source QEUV. Again, test the code out with just one wavelength to make sure that it works ok.  Then expand it to other wavelengths.

10. Expand all relevant functions that use n(O, z) to use n(O2, z) and n(N2, z) also. 

11. You can then implement SZA in the Tau calculation. Limit it to < 75 degrees, and have Tau be very large (say 10 or so) if SZA < 75 degrees.

11. Set a dt (less than 5 minutes), and then update T given dT/dt. Recalculate n(O, z), n(O2, z), and n(N2, z) using your functions.

12. Update the SZA given the time of day.

13. Repeat for 24 hours.

