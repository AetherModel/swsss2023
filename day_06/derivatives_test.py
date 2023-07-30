#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# ----------------------------------------------------------------------
# Take first derivative of a function
# ----------------------------------------------------------------------

def first_derivative(f, x):

    """ Function that takes the first derivative

    Parameters
    ----------
    f - values of a function that is dependent on x -> f(x)
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    dfdx - the first derivative of f(x)

    Notes
    -----
    take the first derivative of f(x) here

    """

    nPts = len(f)
    
    dfdx = np.zeros(nPts)

    # do calculation here - need 3 statements:
    #  1. left boundary ( dfdx(0) = ...)
    #  2. central region (using spans, like dfdx(1:nPts-2) = ...)
    #  3. right boundary ( dfdx(nPts-1) = ... )

    return dfdx

# ----------------------------------------------------------------------
# Take second derivative of a function
# ----------------------------------------------------------------------

def second_derivative(f, x):

    """ Function that takes the second derivative

    Parameters
    ----------
    f - values of a function that is dependent on x -> f(x)
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    d2fdx2 - the second derivative of f(x)

    Notes
    -----
    take the second derivative of f(x) here

    """

    nPts = len(f)
    
    d2fdx2 = np.zeros(nPts)

    # do calculation here - need 3 statements:
    #  1. left boundary ( dfdx(0) = ...)
    #  2. central region (using spans, like dfdx(1:nPts-2) = ...)
    #  3. right boundary ( dfdx(nPts-1) = ... )

    return d2fdx2

# ----------------------------------------------------------------------
# Get the analytic solution to f(x), dfdx(x) and d2fdx2(x)
# ----------------------------------------------------------------------

def analytic(x):

    """ Function that gets analytic solutions

    Parameters
    ----------
    x - the location of the point at which f(x) is evaluated

    Returns
    -------
    f - the function evaluated at x
    dfdx - the first derivative of f(x)
    d2fdx2 - the second derivative of f(x)

    Notes
    -----
    These are analytic solutions!

    """

    f = 4 * x ** 2 - 3 * x -7
    dfdx = 8 * x - 3
    d2fdx2 = np.zeros(len(f)) + 8.0

    return f, dfdx, d2fdx2

# ----------------------------------------------------------------------
# Main code
# ----------------------------------------------------------------------

if __name__ == "__main__":

    # get figures:
    fig = plt.figure(figsize = (10,10))
    ax1 = fig.add_subplot(311)
    ax2 = fig.add_subplot(312)
    ax3 = fig.add_subplot(313)
    
    # define dx:
    dx = np.pi / 4
    
    # arange doesn't include last point, so add explicitely:
    x = np.arange(-2.0 * np.pi, 2.0 * np.pi + dx, dx)

    # get analytic solutions:
    f, a_dfdx, a_d2fdx2 = analytic(x)

    # get numeric first derivative:
    n_dfdx = first_derivative(f, x)

    # get numeric first derivative:
    n_d2fdx2 = second_derivative(f, x)

    # plot:

    ax1.plot(x, f)

    # plot first derivatives:
    error = np.sum(np.abs(n_dfdx - a_dfdx)) / len(n_dfdx)
    sError = ' (Err: %5.1f)' % error
    ax2.plot(x, a_dfdx, color = 'black', label = 'Analytic')
    ax2.plot(x, n_dfdx, color = 'red', label = 'Numeric'+ sError)
    ax2.scatter(x, n_dfdx, color = 'red')
    ax2.legend()

    # plot second derivatives:
    
    plotfile = 'plot.png'
    print('writing : ',plotfile)    
    fig.savefig(plotfile)
    plt.close()
    
