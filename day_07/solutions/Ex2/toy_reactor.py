# numpy for fast arrays and some linear algebra.
import numpy as np 
# import matplotlib for plotting
import matplotlib.pyplot as plt
# import Dormand-Prince Butcher tableau
import dormand_prince as dp
# import our Runge-Kutta integrators
import runge_kutta as rk

#############################
#### setup simulation
#############################

def reaction_rates(c,k):
    """
        Function implementing the reaction rate computation of our toy reactor
        
        inputs:
            c - concentration of species A, B, C (numpy array)
            k - rate constants (organized as list)

        outputs:
            reaction rates (numpy array)
    """
    return k*[c[0],c[1],c[2]**2]

def reactor(c,t,k,S):
    """
        Function returing the rhs of our toy reactor model 
        
        inputs:
            c - concentration of species  (numpy array)
            t - time 
            k - rate constants (organized as list)
            S - stoichiometry matrix (numpy array)

        outputs: 
            dc/dt - numpy array
    """
    return S @ reaction_rates(c,k)

# stoichiometry
S = np.array([[-1, 0, 0],
              [1, -1, 1],
              [0, 2, -2]])

# rate coefficients
k = np.array([100.0, 0.25, 1.0])

# initial condition
c_0 = np.array([1.0, 0, 0])

########################
### Exercise 2: use your RK method to simulate the model
########################

# time horizon
tspan = (0.0,5.0)
# time step 
h = 1e-3
# define dormant_prince_stepper
def dormant_prince_stepper(f,x,t,h):
    return rk.explicit_RK_stepper(f,x,t,h,dp.a,dp.b,dp.c)

trajectory, time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                       c_0, 
                                       tspan, 
                                       h,
                                       dormant_prince_stepper)

species_names = ["A", "B", "C"]
colors = ["red", "blue", "black"]

fig, axs = plt.subplots(2)
ax = axs[0]
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(time_points, [c[i] for c in trajectory],
            color=colors[i], 
            linewidth=2, 
            label = species_names[i])
ax.legend(loc="center right")
fig.savefig("concentration_traces.pdf")

tspan = (0.0,0.1)
trajectory, time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                       c_0, 
                                       tspan, 
                                       h,
                                       dormant_prince_stepper)

ax = axs[1] 
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(time_points, [c[i] for c in trajectory],
            color=colors[i], 
            linewidth=2, 
            label = species_names[i])
ax.legend()
fig.savefig("zoomed_concentration_traces.pdf")
