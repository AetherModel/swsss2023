using DifferentialEquations, CairoMakie

N = 100 # number of grid points
λ = 1000.0 # heat conductivity
sun_heat = 10.0 # sun heating 
background_heat = 10.0 # background heating

# spatial discretization
x_range = range(100, 500, N)
Δx = step(x_range)

# source terms
Q_back = zeros(N)
Q_back[round(Int, N/3):round(Int, 2N/3)] .= background_heat

Q_heat = zeros(N)
Q_heat[round(Int, N/3):round(Int, 2N/3)] .= sun_heat

function dTdt(T, p, t)
    λ, Tlower, Δx = p

    fac = 1.0 # or max(cos(t),0) if you want time dependence
    
    Qeuv = fac*Q_heat + Q_back 

    dT = zeros(length(T))

    dT[1] = # here you need to add the finite difference approximation for the 1st grid point
    for i in 2:length(T)-1
        dT[i] = # here you need to add the finite difference approximation for the ith grid point
    end
    dT[N] = # here you need to add the finite difference approximation for the ith grid point

    return dT
end

T0 = 200*ones(N) # a uniform flat temperature profile
Tlower = 200 # this value is the temperature at the lower boundary
parameters = (λ, Tlower, Δx) # this is just to keep all the parameters in one place
tspan =  (0.0, 100.0) # time horizon over which we want to solve our IVP

prob = ODEProblem(dTdt, T0, tspan, parameters) # this defines the IVP 
# dTdt = right-hand-side of the IVP
# T0 = initial temperature profile 
# tspan = time horizon over which we want to solve our IVP
# parameters = parameters of the model

sol = solve(prob) # this solves the IVP 


import CairoMakie as CM
function generate_movie(sol, steps = 1000)

    t_range = range(0.0, sol.t[end], steps)
    fig = CM.Figure()
    ax = CM.Axis(fig[1,1], xlabel = "altitude [km]", ylabel = "T [k]")
    CM.ylims!(ax, 200, 800)
    T_profile = CM.Observable(sol(0.0))
    CM.lines!(ax, x_range, T_profile, color = :black, linewidth = 2)
    
    CM.record(fig, string(@__DIR__, "/movie.mp4"), t_range, framerate=80) do t
        T_profile[] = sol(t)
    end 
end

generate_movie(sol)