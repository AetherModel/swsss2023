#!/usr/bin/env python

import argparse

# ----------------------------------------------------------------------
# Example 1 with a few more input arguments
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
    
    parser = argparse.ArgumentParser(description = 'My Example Code')

    parser.add_argument('in_var_1', nargs = 1, \
                        help = 'Input Variable - only need one!')

    args = parser.parse_args()

    return args


# ----------------------------------------------------------------------
# My Main code:
# ----------------------------------------------------------------------

args = parse_args()

print(args)

in_var = args.in_var_1

print(in_var)

