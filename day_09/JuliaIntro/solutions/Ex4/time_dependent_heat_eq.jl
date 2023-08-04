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
Q_back[ceil(Int, N/3):ceil(Int, 2N/3)] .= background_heat

Q_heat = zeros(N)
Q_heat[round(Int, N/3):ceil(Int, 2N/3)] .= sun_heat

function dTdt(T, p, t)
    λ, Tlower, Δx = p

    fac = 1.0 #max(cos(t),0)

    dT = zeros(length(T))

    dT[1] = λ/Δx^2 * (T[2] - 2T[1] + Tlower) + (fac*Q_heat[1] + Q_back[1])
    for i in 2:length(T)-1
        dT[i] = λ/Δx^2 * (T[i+1] - 2*T[i] + T[i-1]) + (fac*Q_heat[i] + Q_back[i])
    end
    dT[N] = λ/Δx^2 * (T[N-1] - T[N]) + (fac*Q_heat[end] + Q_back[end])

    return dT
end

T0 = 200*ones(N)
Tlower = 200
parameters = (λ, Tlower, Δx)

prob = ODEProblem(dTdt, T0, (0.0, 100.0), parameters)

sol = solve(prob)



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