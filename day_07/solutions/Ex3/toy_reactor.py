# numpy for fast arrays and some linear algebra.
import numpy as np 
# import matplotlib for plotting
import matplotlib.pyplot as plt
# import Dormand-Prince Butcher tableau
import dormand_prince as dp
# import our Runge-Kutta integrators
import runge_kutta as rk
# import time to measure performance
import time 

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

# time horizon
tspan = (0.0,5.0)
# time step 
h = 1e-4

# define explicit dormand
def dormand_prince_stepper(f,x,t,h):
    return rk.explicit_RK_stepper(f,x,t,h,dp.a,dp.b,dp.c)

# define dormandprince_stepper
def adaptive_dormand_prince_stepper(f,x,t,h):
    return rk.adaptive_explicit_RK_stepper(f,x,t,h,dp.a,dp.b,dp.c,dp.b_control)


########################################
### hereafter no more code modification necessary
########################################

# compare performance
t_begin = time.time()
trajectory, time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                       c_0, 
                                       tspan, 
                                       h,
                                       dormand_prince_stepper)
print("Fixed time step Dormand-Prince method executed in "+str(time.time() - t_begin)+" seconds.")

t_begin = time.time()
trajectory, time_points = rk.adaptive_integrate(lambda c, t: reactor(c, t, k, S), 
                                                c_0, 
                                                tspan, 
                                                h,
                                                adaptive_dormand_prince_stepper)
print("Adaptive Dormand-Prince method executed in "+str(time.time() - t_begin)+" seconds.")



# compare trajectories
tspan = (0.0,0.2)
adaptive_trajectory, adaptive_time_points = rk.adaptive_integrate(lambda c, t: reactor(c, t, k, S), 
                                                                  c_0, 
                                                                  tspan, 
                                                                  h,
                                                                  adaptive_dormand_prince_stepper)

fixed_trajectory, fixed_time_points = rk.integrate(lambda c, t: reactor(c, t, k, S), 
                                                          c_0, 
                                                          tspan, 
                                                          h,
                                                          dormand_prince_stepper)                                               
species_names = ["A", "B", "C"]
colors = ["red", "blue", "black"]

fig, axs = plt.subplots(2)
ax = axs[0]
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(fixed_time_points, [c[i] for c in fixed_trajectory],
            color = colors[i], 
            marker = "o",
            linewidth = 2, 
            label = species_names[i])

ax = axs[1]
ax.set_xlabel("time")
ax.set_ylabel("concentration")
for i in range(3):
    ax.plot(adaptive_time_points, [c[i] for c in adaptive_trajectory],
            color = colors[i], 
            marker = "o",
            linewidth = 2, 
            label = species_names[i])
fig.savefig("adaptive_vs_fixed.pdf")

