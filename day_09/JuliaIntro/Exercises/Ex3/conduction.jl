using LinearAlgebra, Plots, ForwardDiff

# the following are model parameters 
N = 1000 # number of grid points
λ = 10.0 # heat conductivity
sun_heat = 0.05 # sun heating 
background_heat = 0.05 # background heating
t = 0 # later we will loop through time 

# spatial discretization
x_range = range(100, 500, N)
Δx = step(x_range)

p = plot(xlabel = "altitude [km]", ylabel = "Temperature", legend=false)

# sets the heating terms to apply in the middle third of the domain
fac = max(cos(0.0),0) # time factor for sun heating 
Q = zeros(N)
Q[round(Int, N/3):round(Int, 2N/3)] .= fac*sun_heat + background_heat


# with the nomenclature from yesterday:
# Recall the meaning of A, B, C and D,
# a is the first subdiagonal, b is the diagonal and c is the first superdiagonal.
a = ...      # [1, ..., 1] this vector should have length N+1
b = ...      # [1, -2, ..., -2, 1] this vector should have length N+2
c = ...      # [0, 1, ..., 1] this vector should have length N+1
d = ...      # [200, -Q[1]*Δx^2/λ, ..., -Q[N]*Δx^2/λ, 0] this vector should haave length N+2

# assemble tridiagonal matrix with the Tridiagonal function 
L = ... # L for Laplacian

# solve tridiagonal system with \
T = ...

# plotting 
plot!(p, x_range, T[2:end-1], color = :black, linewidth=2)
plot!(p, x_range, 640*ones(length(x_range)), linestyle=:dash, color = :red, linewidth=2)
display(p)

