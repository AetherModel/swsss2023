#!/usr/bin/env python

import argparse

# ----------------------------------------------------------------------
# Example 2 with a few more input arguments
# ----------------------------------------------------------------------

def parse_args():

    """ Function to parse input arguments

    Parameters
    ----------
    None!

    Returns
    -------
    args namespace

    Notes
    -----
    Parses the input arguments. Created this for the summer school
    To see how all of this works and all of the full functionality,
    take a look here:
    https://docs.python.org/3/library/argparse.html

    """
    
    # https://docs.python.org/3/library/argparse.html

    # Create an argument parser:
    parser = argparse.ArgumentParser(description = \
                                     'My Example Code V2')
    
    # in_var: list of 2, no type defined -> string:
    parser.add_argument('in_var', nargs = 2, \
                        help = 'Input Variables - need two!')
    
    # in_scalar: scalar value, type float:
    parser.add_argument('-in_scalar', \
                        help = 'my scalar variable', \
                        type = float)
    
    # npts: scalar value, type integer, default 5:
    parser.add_argument('-npts', \
                        help = 'another scalar (default = 5)', \
                        type = int, default = 5)
    
    # do_this: scalar value, boolean, default false:
    parser.add_argument('-do_this', \
                        help = 'Boolean to do something', \
                        action = 'store_true')
    
    # actually parse the data now:
    args = parser.parse_args()
    
    return args

# ------------------------------------------------------
# My Main code:
# ------------------------------------------------------

# parse the input arguments:
args = parse_args()
print(args)

# grab the variable in_var 
#   (note, this will be a list of 2 elements):
in_var = args.in_var
print(in_var)

# grab the variable in_scalar (a scalar):
in_scal = args.in_scalar
print(in_scal)

# grab the number of points (an integer, default 5):
npts = args.npts
print(npts)

# grab the variable do_this (a boolean, default false):
do_this = args.do_this
print(do_this)
