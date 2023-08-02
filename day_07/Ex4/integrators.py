from scipy.optimize import fsolve
import numpy as np
import matplotlib.pyplot as plt
import time
import toy_reactor as model

def explicit_euler_step(f,x,t,h):
    return ... # please complete this function

def implicit_euler_step(f,x,t,h):    
    return ... # please complete this function

def crank_nicolson_step(f,x,t,h):
    return ... # please complete this function

def heun_step(f,x,t,h):
    return ... # please complete this function


# after implementing a time stepper, 
# add them to this list.
# Then, run the script and check if the figures are as expected!
integrators = []

####################################
### no modification needed beyond this point
####################################
def integrate(f, x_0, tspan, h, step):
    t, tf = tspan
    x = x_0
    trajectory = [x_0]
    ts = [t]
    while t < tf:
        h_eff = min(h, tf-t)
        x = step(f,x,t,h_eff)
        t = min(t+h_eff, tf)
        trajectory.append(x)
        ts.append(t)
    return trajectory, ts

# stoichiometry matrix 
S = np.array([[-1, 0, 0],
              [1, -1, 1],
              [0, 2, -2]])

k = np.array([100.0, 0.25, 1.0])

x_0 = np.array([1.0, 0.0, 0.0])

h_range = 10**np.linspace(-4,1,6)



#################################
## no need to edit the code below
## this just evaluates the problem
## and makes some interesting plots 
#################################
performance = dict()
for h in h_range:
    for integrator in integrators:
        t0 = time.time()
        sol = integrate(lambda x,t : model.reactor(x,t,k,S), x_0, (0.0,10.0), h, integrator)
        tf = time.time()
        performance[h, integrator, "CPU_time"] = tf-t0
        performance[h, integrator, "sol"] = sol 
   
# compare stability and computational performance
def plot_traces(ax, t_range, sol):
    colors = ["red", "dodgerblue", "black"]
    labels = ["A", "B", "C"]
    for i in range(3):
        ax.plot(t_range, [s[i] for s in sol], color = colors[i], linewidth = 2, label = labels[i])
    ax.set_xlabel("t")
    ax.set_ylabel("c(t)")
    plt.tight_layout()
        
integrator2name = {crank_nicolson_step : "Crank-Nicolson",
                   explicit_euler_step : "Explicit Euler",
                   implicit_euler_step : "Implicit Euler",
                   heun_step : "Heun"}

colors = {integrators[0] : "red",
          integrators[1] : "dodgerblue",
          integrators[2] : "green",
          integrators[3] : "black"}

for integrator in integrators:
    fig, axs = plt.subplots(3,2)
    fig.suptitle(integrator2name[integrator])
    for i in range(3):
        for j in range(2):
            h = h_range[i*2+j]
            sol, ts = performance[h, integrator, "sol"]
            axs[i,j].set_title("h = "+str(h))
            plot_traces(axs[i,j], ts, sol)   
    fig.show()
    fig.savefig(integrator2name[integrator]+"_traces.pdf")

def compute_error(sol, ref_sol):
    return sum(np.linalg.norm(sol[i]-ref_sol[i]) for i in range(len(ref_sol)))/len(sol)

benchmark = np.exp(-k[0]*0.01)*x_0[0]
fig, axs = plt.subplots(2)
for i in range(2):
    axs[i].set_yscale('log')
    axs[i].set_xscale('log')

axs[1].set_xlabel('h')
axs[0].set_ylabel('error')
axs[1].set_ylabel('CPU time [s]')
for integrator in integrators:
    times = [performance[h, integrator, "CPU_time"] for h in h_range]
    accuracy = [np.linalg.norm(performance[h, integrator, "sol"][0][round(0.01/h)][0] - benchmark) for h in h_range]
    axs[0].plot(h_range, accuracy, 'o-', color = colors[integrator], linewidth = 2, label = integrator2name[integrator])
    axs[1].plot(h_range, times, 'o-', color = colors[integrator], linewidth = 2)#, label = integrator2name[integrator])
axs[0].legend(loc = 'lower right')
plt.tight_layout()
fig.savefig("integrator_performance.pdf")
fig.show()


