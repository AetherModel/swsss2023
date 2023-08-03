using BenchmarkTools

function cos_approx(x, N)
    # approximation of cosine via power series expansion
    # inputs:
    #       - x : argument of cosine 
    #       - N : truncation order of the power series approximation
    # outputs:
    #       - cos_val : approximation of cos(x)
end

@btime cos_approx($(π/3),$(10)) 
@btime cos($(π/3))
@btime cos(π/3)