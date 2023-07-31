# Space Weather Simulation Summer School -- Day 7

Today we will cover the basics of modeling and simulating chemically reacting systems. To that end, we will develop a generic mass/mole balance model template for reacting systems and discuss some common simplifying assumptions. We will further cover the basic principles of chemical kinetic modeling, including the law of mass action kinetics and Arrhenius relations for the description of temperature dependence of the rate coefficients. To make sure we are well-equipped to simulate these models, we will dive deep into numerical techniques for solving initial value problems. We will cover several concepts ranging from generic explicit Runge-Kutta methods over timestep adaptivity to implicit methods. Special emphasis will be placed on the issue of stiffness and its interaction with stability. As a capstone, we will take all the learned and implement a simplified ionospheric reaction model. 


## Exercise 0:
Extrapolate your knowledge about finite differences to construct the explicit Euler method for solving initial value problems. Implement it to solve a simple test equation.

## Exercise 1:
Implement a generic explicit Runge-Kutta stepper and use to implement the famous Dormand-Prince RK45 method. 

## Exercise 2: 
Modeling toy reaction networks and simulate them with the Runge-Kutta integrator interface implemented in Exercise 1.

## Exercise 3:
Implement a generic explicit Runge-Kutta method with adaptive time-stepping. 

## Exercise 4:
Implement four different IVP solution routines and compare their accuracy and stability properties. 

## Exercise 5:
Implement simplified ionospheric reaction model. 


