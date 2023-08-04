using Plots

# This is our test function
f(x) = x^2 - 2
grad(x) = 2*x

# Let's plot it to get an idea
x_range = range(0, 5, 100)
p = plot(x_range, f.(x_range), legend=false)
scatter!(p, [sqrt(2)], [0.0], color = :red)
display(p)

# below we define a newton method to find a root of a function using function and derivative evaluations
function newton(f,g,x0)
    # inputs:
    #   f = function for which we want to find a root
    #   g = derivative of f  
    # outputs:
    #   x_star = (approximate) root of f
    

    # Pseudo-code:
    # Initialize x = x_0
    # while |f(x)| > 1e-6
    #   x = x - f(x)/g(x)
    # end
    # return x 

    return ... # implement the pseudocode above
end

x_sol = newton(f, grad, 10.0)

println("The difference between the analytical and numerical solution is ", x_sol - sqrt(2))

