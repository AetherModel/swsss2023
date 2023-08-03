##################################
#### assignment and unicode symbols 🔥🔥🔥
##################################

# silly example 

# Golden ratio (nice vs. old)

# pi 

# Navier stokes 


##################################
#### Arrays/Vectors/Matrices
##################################

# defining a vector
powers_of_two = [1, 2, 4]
some_random_stuff = 

# appending stuff/mutating vectors: push!, append!

# defining a matrix
vandermonde = [1 2 4 8;  # first row
                 1 3 9 27] # second row

# concatenating 
# adding rows 

# adding columns

# indexing starts at 1!

# slicing

# last element is indexed by end keyword

##################################
#### loops + printing
##################################


#in particular ranges are written with : instead of range function
#range(5) in python <=> 0:4 in julia 

##################################
#### if-elseif-else 
##################################
a = 5.0


##################################
#### functions
##################################

# functional programming style
function my_add(a, b)
    
end

Σ = my_add(5, 3)

# for simple functions we may prefer the assignment form 
# to resemble standard math notation more closely
f(x) = 1/(2π)*exp(-1/2*x^2)

# evaluation 
p = f(0.5)

# vectorization/(map-reduce)
# evaluates our function at every element of the supplied 
# vector/array and returns the result in the same shape!


# differences between python and julia
# Why Julia was created
# https://julialang.org/blog/2012/02/why-we-created-julia/# 
# Julia documentation: Noteworthy differences to other common languages
# https://docs.julialang.org/en/v1/manual/noteworthy-differences/
# Julia for data science
# https://www.imaginarycloud.com/blog/julia-vs-python/#future