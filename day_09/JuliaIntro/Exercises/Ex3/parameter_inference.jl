# Now we want to use Newton's method to find λ so that for t = 0.0, we have T[end] = 640

# Let us therefore first define a function that computs T[end] and returns the difference to
# the target value of 640. 

function ΔT_upper(λ)
    # copy paste your code over here 

    return # return the difference between T_upper and the target of 640K
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


