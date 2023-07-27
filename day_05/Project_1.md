# Group Project 1: Analyze the differences in predicted densities by JB2008 and TIE-GCM as a function of dst
Description: In the project, the students will work together to analyze and visualize the difference in predicted densities by the JB2008 density model and the TIE-GCM density model as a function of the disturbance storm time (dst) index. 


## Task 1: Download the dst index for the year 2002 from the NASA OmniWeb database
For this work, we are only interested in evaluating the differences between the two density models during high space weather events (i.e. large dst value). You first need to select a time period where the dst index is high in the year 2002 (including 5 hours prior and 5 hours after the high space weather event). *Note: as the density data are in hourly format, we will first need to convert the high temporal resolution of the dst index into a lower temporal resolution of an hour. This can be achieved using data slicing.*


## Task 2: Extract and plot the predicted densities at 450 km the selected period of high space activity (dst)
After identifying the time period of interest, plot the densities predicted by JB2008 and TIE-GCM for these periods at an altitude of 450 km. *Note: You will have to use 3D interpolation in order to obtain the correct density values.*

## Task 3: Plot the differences between the predicted densities at 450 km during the selected period of high space activity (dst)
Then, plot the differences between the two predicted densities. Subsequently, plot the absolute percentage difference between the two models. *Note: absolute percentage difference = $\dfrac {abs(\rho_{TIE-GCM} - \rho_{JB2008})}{\rho_{TIE-GCM}}$

## Task 4: Generate a video for the absolute percentage difference plots at 450 km over the selected time period
Using the materials covered on day 4, generate a video to show the evolution of the absolute percentage difference between the two models at 450 km.

## Task 5: Plot the hourly mean absolute percentage difference and the hourly dst index.
Calculate the hourly mean absolute percentage difference and plot this in the same plot with the hourly dst index. Is there any correlation between the dst index and the hourly mean absolute percentage difference?

## Task 6: Create a function to be run from the terminal that can calculate the hourly mean absolute percentage difference for any arbitrary altitude over the same time period
The function needs to take in an *altitude (float)* as an argument and save the hourly mean absolute percentage difference over the same time period. At the same time, the function also needs to generate a anumation to show the evolution of the absolute percentage difference between the two models at the selected altitude.

## Task 7: Plot the mean absolute percentage difference for multiple altitudes
Run the function with the following altitudes [100, 200, 250, 300, 350, 400, 450] and plot the mean absolute percentage difference for these altitudes. Is there any noticeable trend in the plots?

## Task 8: Create a function to be run from the terminal that can calculate the hourly mean absolute percentage difference for any arbitrary altitude and over an arbitrary time period
Now, let's extend our previously created function such that it can take in 3 arguments *altitude (float), start day of year (int), start hour (int), end day of year (int), end hour (int)*, save the hourly mean absolute percentage difference over the provided time period. *Note: the day of year (doy) system ignores months and numbers each day of the year consecutively.

## Task 9: (Optional) Plot the density along CHAMP over the initial selected period of high space weather activity
Download the trajectory data for CHAMP from https://zenodo.org/record/4602380#.Ytn6DC-B28W and using data slicing to change it into a hourly position data. Then, calculate the density along CHAMP trajectory. *Note: There is missing data in the CHAMP dataset. Use interpolation to fill in the blank.*
