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
push!(powers_of_two, 8)
append!(powers_of_two, [16, 32])

# defining a matrix
vandermonde = [1 2 4 8;  # first row
                 1 3 9 27] # second row

# concatenating 
# adding rows 
add_a_row = [vandermonde;
             1 4 16 64]
stacked_vandermonde = [vandermonde; 
                       vandermonde]

stacked_vandermonde = vcat(vandermonde, vandermonde) # alternative

# adding columns
bigger_vandermonde = [vandermonde vandermonde]

bigger_vandermonde = hcat(vandermonde, vandermonde) # alternative

# indexing starts at 1!
vandermonde[1,3]

# slicing
vandermonde[1:2,3]
vandermonde[1:2,2:3]

# last element is indexed by end keyword
powers_of_two[end]
powers_of_two[end-1]

##################################
#### loops + printing
##################################
for power in powers_of_two 
    println(power)
end

for i in 1:length(powers_of_two) # discouraged!
    println(powers_of_two[i])
end

for i in eachindex(powers_of_two)
    println(powers_of_two[i])
end

i = 0
while i <= 10
    println(i)
    i += 1
end

#in particular ranges are written with : instead of range function
#range(5) in python <=> 0:4 in julia 

##################################
#### if-elseif-else 
##################################
a = 5.0
if a < 2
    println("a is less than 2")
elseif a < 3
    println("a is less than 3")
else 
    println("a is greater or equal to 3")
end

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