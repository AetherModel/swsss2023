# Group Project 4: Visualize the density values along the trajectory of the CHAMP satellite for the first 50 days in 2002
Description: In the project, the students will work together to analyze and visualize the difference in predicted densities by the JB2008 density model and the TIE-GCM density model with the accelerometer-derived density from the CHAMP dataset (Density_New (kg/m^3)).
*Note: There are days with missing data in the CHAMP dataset; the output length for each file can be different.*


## Task 1: Download and extract the CHAMP trajectory data from https://zenodo.org/record/4602380#.Ytn6DC-B28W 
Download and unzip the CHAMP trajectory and density data to a folder of your choice. Read the trajectory data (local solar time, latitude, and altitude) from the daily CHAMP data for the first 50 days in 2002

*Hint 1: You can use the "os.listdir" command to list all files in the current folder.*

*Hint 2: You can use the "sorted" command to sort a list.*

*Hint 3: You can use the "pandas.read_csv()" command to read a space delimited text file*

## Task 2: Extract the hourly trajectory data
The CHAMP dataset was generated using a temporal resolution of 10 seconds. Slice the data such that the data has a temporal resolution of 1 hour.

*Hint 1: You can use the "np.where" command to locate the index of the row of interest.*

*Hint 2: The remainder operator that is given by "%" might be useful.*

## Task 3: Obtain the hourly JB2008 density values along the CHAMP's trajectory and visualize the JB2008 density value as a function of time
Load the data from Day 3 and use 3d interpolation to obtain the JB2008 density value along the CHAMP's trajectory. Then, visualize the JB2008 density along the CHAMP's trajectory as a function of time.

## Task 4: Obtain the hourly TIE-GCM density values along the CHAMP's trajectory and visualize TIE-GCM density value as a function of time on the same plot
Load the data from Day 3 and use 3d interpolation to obtain the TIE-GCM density value along the CHAMP's trajectory. Then, visualize the TIE-GCM density along the CHAMP's trajectory as a function of time.

## Task 5: Plot the hourly JB2008 density value (task 3), TIE-GCM density value (task 4), and the accelerometer-derived density from the CHAMP data
Use the same steps in task 2 to extract the accelerometer-derived density data. Then plot all three hourly density data in the same plot. 

## Task 6: Plot the daily average density for the JB2008 density value, TIE-GCM density value, and accelerometer-derived density value
Let's calculate the daily average density for the different density values and plot those. 

## Task 7: Create a function that will plot the hourly density values for the JB2008 density model, the TIE-GCM density model, and the accelerometer-derived density along the trajectory of the CHAMP satellite for a selected month in 2002
The function should take in the following input (month) and output the plot in task 5 for the selected month.

## Task 8 (optional): Download the dst index for the year 2002 from the NASA OmniWeb database and examine the effect of the dst index on the hourly density value
