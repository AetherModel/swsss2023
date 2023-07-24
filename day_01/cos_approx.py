#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Qusai Al Shidi'
__email__ = 'qusai@umich.edu'

from math import factorial
from math import pi
import numpy as np

def cos_approx(x, accuracy = 10):
    """Taylor series expansion of cosine function"""
    S = [((-1)**n * x **(2*n))/factorial(2*n) for n in range(accuracy + 1)]
    
    return sum(S)

#def cos_approx(x, accuracy=10):
#    """ Taylor series expansion of cosine function"""
#    test = []
#    for n in range(11):
#        S = [((-1)**n * x **(2*n))/factorial(2*n)]
#        test.append(S)
#    return sum(np.array(test))




# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
    
    import matplotlib.pyplot as plt
 #   x = np.linspace(0,1)
 #   plt.plot(x, np.exp(x))
 #   plt.xlabel(r'$ 0 \leq x < 1 $')
 #   plt.ylabel(r'$E^x$')
 #   plt.title('Exponential function')
 #   plt.show()
    
    from datetime import datetime # import of the module 
    from swmfpy.web import get_omni_data
    start_time = datetime(1998,4,18) # Putting the begining time mark
    end_time = datetime(1998,4,19) # Putting the end of time period
    data = get_omni_data(start_time, end_time) # collection ofthe data with arguments
    data.keys() # list down the keys from the dictionary
    
    plt.plot(data['times'], data['al']) # plot al as a function of AL
    plt.xlabel('time_period') # Assigning the time period on the x axis
    plt.ylabel('AL_data') # Assgining the data ont the y axis
    plt.title('AL activity when I was officially cake murderer') # we set the tittle
    savefig(fname, *, dpi='figure', format=None, metadata=None,
        bbox_inches=None, pad_inches=0.1,
        facecolor='auto', edgecolor='auto',
        backend=None, **kwargs
       )
    plt.show() # Show the plot.
    
