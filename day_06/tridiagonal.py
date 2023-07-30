
import numpy as np

# ----------------------------------------------------------------------
# Taken from:
# https://en.wikipedia.org/wiki/Tridiagonal_matrix_algorithm
# BUT - they go from 1 -> n and python goes from 0 -> n-1
# ----------------------------------------------------------------------

def solve_tridiagonal(a, b, c, d):

    """ Function that solves a tridiagonal matrix

    Parameters
    ----------
    a - i-1 coefficient
    b - i coefficient
    c - i+1 coefficient
    d - source term

    Returns
    -------
    x - solution to tri-diagonal matrix

    Notes
    -----
    Solve system of equation

    """
    
    nPts = len(a)

    cp = np.zeros(nPts)
    dp = np.zeros(nPts)
    x = np.zeros(nPts)

    # calculate c':
    i = 0
    cp[i] = c[i]/b[i]
    for i in range(1, nPts-1):
        cp[i] = c[i] / (b[i] - a[i] * cp[i-1])

    # calculate d':
    i = 0
    dp[i] = d[i]/b[i]
    for i in range(1, nPts):
        dp[i] = (d[i] - a[i] * dp[i-1]) / (b[i] - a[i] * cp[i-1])

    # calculate x:
    i = nPts - 1
    x[i] = dp[i]
    for i in range(nPts-2, -1, -1):
        x[i] = dp[i] - cp[i] * x[i + 1]

    return x

