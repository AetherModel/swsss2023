# Now we want to use Newton's method to find λ so that for t = 0.0, we have T[end] = 640

# Let us therefore first define a function that computs T[end] and returns the difference to
# the target value of 640. 
function ΔT_upper(λ)
    N = 1000 # number of grid points
    sun_heat = 0.05 # sun heating 
    background_heat = 0.05 # background heating
    
    # spatial discretization
    x_range = range(100, 500, N)
    Δx = step(x_range)
    
    
    # sets the heating terms to apply in the middle third of the domain
    Q = zeros(N)
    Q[ceil(Int, N/3):ceil(Int, 2N/3)] .= max(cos(0.0),0)*sun_heat + background_heat
    
    
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

    return T[end] - 640.0 # return the difference between T_upper and the target of 640 
end

# now we will use Newton's method to find the right λ* such that ΔT_upper(λ*)

function newton(f,g,x0)
    # inputs:
    #   f = function for which we want to find a root
    #   g = derivative of f  
    # outputs:
    #   x_star = (approximate) root of f
    

    # Pseudo-code:
    # compute x_k+1 = x_k - f(x_k)/g(x_k)
    # if abs(f(x_k+1)) < tolerance (choose a small value here)
    #     return x_k+1
    # else increase k <- k+1 and repeat the process

    x = x0
    k = 0
    while abs(f(x)) > 1e-4 
        x = x - f(x)/g(x)
        k += 1
        if k > 1000
            println("Newton method did not converge. Try a different initial guess.")
            break
        end
    end
    return x
end

# the following will compute the EXACT derivative of ΔT_upper with respect to λ 
# using very clever programming tricks. 
dΔT_upper(λ) = ForwardDiff.derivative(ΔT_upper, λ)

λ = newton(ΔT_upper, dΔT_upper, 1.0)


