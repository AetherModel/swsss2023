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

t = 0.0
p = plot(xlabel = "altitude [km]", ylabel = "Temperature", legend=false)

# sets the heating terms to apply in the middle third of the domain
Q = zeros(N)
Q[ceil(Int, N/3):ceil(Int, 2N/3)] .= max(cos(t),0)*sun_heat + background_heat


# with the nomenclature from yesterday:
# Recall the meaning of A, B, C and D,
# A is the first subdiagonal, B is the diagonal and C is the first superdiagonal.
a = vcat(ones(N), -1)           # [0, 1, ..., 1] this vector should have length N+1
b = vcat(1, -2*ones(N), 1)      # [1, -2, ..., -2, 1] this vector should have length N+2
c = vcat(0, ones(N))            # [0, 1, ..., 1, 0] this vector should have length N+1
d = vcat(200, -Q*Δx^2/λ, 0)     # [200, -Q[1]*Δx^2/λ, ..., -Q[N]*Δx^2/λ, 1000] this vector should haave length N+2

# assemble tridiagonal matrix with the Tridiagonal function 
Δ = Tridiagonal(a,b,c)

# solve tridiagonal system with \
T = Δ\d

plot!(p, x_range, T[2:end-1], color = :black, linewidth=2)
plot!(p, x_range, 640*ones(length(x_range)), linestyle=:dash, color = :red, linewidth=2)
display(p)

