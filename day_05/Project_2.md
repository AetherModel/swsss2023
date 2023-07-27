# Group Project 2: User interface to display the JB2008 and TIE-GCM models and comparison
Description: In the project, the students will work together to analyze and visualize the difference in predicted densities by the JB2008 density model and the TIE-GCM density model by creating functions that display differences in the models.


## Task 1: Download the dst index for the year 2002 from the NASA OmniWeb database
For this work, we are only interested in evaluating the differences between the two density models during high space weather events (i.e. large dst value). You first need to select a time period where the dst index is high in the year 2002 (including 5 hours prior and 5 hours after the high space weather event), save also the data for the whole month. *Note: as the density data are in hourly format, we will first need to convert the high temporal resolution of the dst index into a lower temporal resolution of an hour. This can be achieved using data slicing.*

## Task 2: Evaluete Mean and Standard Deviation of the models
After identifying the period of interest, evaluate the mean density for both models and the relative standard deviation at a given day as a function of the altitude. Display the values together on the same figure as $3\sigma$ around the relative mean. What can we say about the two models?

## Task 3: Latitude and Longitude statistic analysis
Create a new function that displays mean and standard deviation boundaries as a function of latitude and longitude (2 graphs) for each density model. Let the function ask as input the altitude and a time step inside the selected period.

## Task 4: Create a function where you can select the altitude and return the two different densities models 
First, keep the period of time fixed at the moment of highest dst, then add the time as an additional variable. You can select the methodology that, according to you, best fits the visualization of data: among getting as an additional input the time period, or a specific date.

## Task 5: Plot the differences between the predicted densities at given altitude during the selected period of high space activity (dst)
create a function that plots the differences between the two predicted densities at a given altitude among well-selected options: [100:50:500]. Subsequently, modify the function such that the user can decide to plot the absolute percentage difference between the two models. *Note: absolute percentage difference = $\dfrac {abs(\rho_{TIE-GCM} - \rho_{JB2008})}{\rho_{TIE-GCM}}$

## Task 6: Create your own tasks
Now that you worked with the data, which function do you think is needed? Which representation, according to you, gives the best understanding of the density behaviour during a storm? In the same way, which visualization shows the main difference between the 2 density models? Maybe a video (Qusai class on day 4) is the best solution. Go back to the assigments from previous days and get inspired: look at the solution posted and look for missing inputs, afterall, this is what being a researcer is. 



