
Today we are going to work on solving the 1D conduction equation.

First we look at Taylor Series Expansion, which allows us to calculate
the first and second derivatives of an equation.

Then we investigate the Laplace equation (second derivative of a
function = 0), which is a boundary-value problem.

Then we investigate the Poisson equation (second derivatice of a
function = source term), which is a steady-state equation.

Then we do the steady-state equation over and over to make a time-series.

Then we solve for the time-dependent heat conduction with a source
equation.

##Assignment 1:
- Make a function that will return the first derivative of a numpy array.
- Make a function that will return the second derivative of a numpy array.
- Test these functions using functions that you make up that an
  analytic solution.
- Show that the mean(abs(difference)) between the numerical and
  analytic solutions improve as delta-x becomes smaller (divide by 2
  each time.)

##Assignment 2:

- Use the tri-diagonal solver to solve for a steady-state Laplace
equation in which x goes from 0 - 10, with dx = 0.25, and T(0) = 200.0
and T(10) = 800.0. 
- Add a source term that is 5.0 between x = 2 and x = 7.
- Make plots with nice labels and such to convince people that you
  have the correct solution.

##Assignment 3:

- Use the tri-diagonal solver to solve for a steady-state Poisson
equation in which x goes from 0 - 10, with dx = 0.25, and T(0) = 200.0
and T(-1) = T(-2) (i.e., zero gradient).
- Add a source term that is 5.0 between x = 2 and x = 7.
- Make plots with nice labels and such to convince people that you
  have the correct solution.

##Assignment 4:

- Use the tri-diagonal solver to solve for a series of steady-state
Poisson equations in which x goes from 0 - 10, with dx = 0.25, T(0) =
200.0 and T(-1) = T(-2) (i.e., zero gradient), and a source between x
= 1 and x = 7.5, that varies through-out a day (see the board).
- Make contour plots that show the temperature as a function of
  altitude and time with nice labels and such to convince people that
  you have the correct solution.

##Assignment 5:

- Use the tri-diagonal solver to solve for a series of steady-state
Poisson equations in which x goes from 0 - 10, with dx = 0.25, T(0) =
200.0 + f(t) with tidal structures (see board) and T(-1) = T(-2)
(i.e., zero gradient), and a source between x = 1 and x = 7.5, that
varies through-out a day (see the board).
- Make contour plots that show the temperature as a function of
  altitude and time with nice labels and such to convince people that
  you have the correct solution.

##Assignment 6:

- Solve a semi-realistic altitude dependent atmosphere with
  characteristics provided on the board.
- Make contour plots that show the temperature as a function of
  altitude and time with nice labels and such to convince people that
  you have the correct solution.
  