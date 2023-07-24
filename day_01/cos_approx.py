#!/usr/bin/env python
"""Space 477: Python: I

cosine approximation function
"""
__author__ = 'Qusai Al Shidi'
__email__ = 'qusai@umich.edu'

from math import factorial
from math import pi


def cos_approx(x, accuracy=10):
    """
    """
    
    return 



# Will only run if this is run from command line as opposed to imported
if __name__ == '__main__':  # main code block
    print("cos(0) = ", cos_approx(0))
    print("cos(pi) = ", cos_approx(pi))
    print("cos(2*pi) = ", cos_approx(2*pi))
    print("more accurate cos(2*pi) = ", cos_approx(2*pi, accuracy=50))
