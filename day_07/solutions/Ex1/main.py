# numpy for fast arrays and some linear algebra.
import numpy as np 
# import matplotlib for plotting
import matplotlib.pyplot as plt
# import Dormand-Prince Butcher tableau
import dormand_prince as dp
# import our Runge-Kutta integrators
import runge_kutta as rk

#############################
#### setup toy problem simulation
#############################
def f(x,t):
    return -2*x

########################
### Exercise 1: use your RK method to simulate the model
########################
# time horizon
tspan = (0.0,2.0)
# time step 
h = 0.2
# initial condition
x_0 = 3.0

def dormand_prince_integrator(x, t, f, h):
    return rk.explicit_RK_stepper(x, t, f, h, dp.a, dp.b, dp.c)

# simulate model 
trajectory, time_points = rk.integrate(f, # ODE right-hand-side
                                       x_0, # initial condition
                                       tspan, # time horizon
                                       h, # time step 
                                       dormand_prince_integrator) # integrator

# analytical solution
time_points_analytical = np.linspace(tspan[0],tspan[1], 1000)
trajectory_analytical = x_0*np.exp(-2*time_points_analytical)

# plot trace
fig, ax = plt.subplots()
ax.set_xlabel("time")
ax.set_ylabel("x(t)")
ax.plot(time_points, trajectory, linewidth=2, color="red", marker = "o")
ax.plot(time_points_analytical, trajectory_analytical, linewidth=2, color="black", linestyle="dashed")