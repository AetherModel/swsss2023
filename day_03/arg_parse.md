
---
title: Understanding argparse
description: Day 2 - Afternoon
author: Aaron Ridley (ridley@umich.edu)
keywords: space-weather, space, python, argparse
---

# Python: Understanding argparse


# Introduction to argparse


## General Idea

- When we develop code, we don't want to hardcode variables
(e.g., filenames, number of elements, etc.)
- For example, this is bad:

```python
tot = 0.0
for n in range(10):
  tot = tot + (-1.0) ** n / factorial(2*n) * (3.14) ** (2 * n)
```

- If we want to change n or x, we need to find where we used these numbers, and then change them.  If we miss one of them, then we have a bug.

- This is better:
```python
nPts = 10
x = 3.14

tot = 0.0
for n in range(nPts):
  tot = tot + (-1.0) ** n / factorial(2*n) * x ** (2 * n)
```

- We only need to change them in one place now.
- Still not great, because we have to change the code itself.

There is a better way! Read on!

---------------

## Arguments



- When you run a code from the command line, you can specify variables when you run the code!
- This is a huge advantage of running code from the command line.
- That way, you don't need to change your code!

For example:

```bash
$ ./cos_approx.py 3.1415 10
$ ./plot_my_file.py --in=test.dat --out=output.png
```

- (one disadvantage of running things from the command line is that
  the plotting is not interactive.  But this is easy to work around.)

---------------

## argparse

- argparse is a package that helps you set up these input arguments.
- You can use this by typing:

```python
import argparse
```

- The reference manual for this can be found here: https://docs.python.org/3/library/argparse.html

---------------
## Example 1:

The code below is included as file called args_example_1.py:

```python
import argparse

# This is a function that parses the arguments that you feed:
def parse_args():
    parser = argparse.ArgumentParser(description = 'My Example Code')
    parser.add_argument('in_var_1', nargs = 1, \
                        help = 'Input Variable - only need one!')
    args = parser.parse_args()
    return args
    
# ---------------    
# Main code here:
args = parse_args()
print(args)
in_var = args.in_var_1
print(in_var)
```
If we save this as args_example_1.py, we can run this from the command line.  This means that we don't need to go into python or iPython, but can directly type into the terminal or command line:
```bash
$ python args_example_1.py test
```
which will print out:
```bash
$ python args_example_1.py test
Namespace(in_var_1=['test'])
['test']
$
```
One of the beautiful things about argparse, is that you can run the code with a --help, and it will tell you how to run the code. For example:

```bash
$ python ./args_example_1.py --help
usage: args_example_1.py [-h] in_var_1

My Example Code

positional arguments:
  in_var_1    Input Variable - only need one!

options:
  -h, --help  show this help message and exit
```

Let's take a closer look at some of the commands in the python code.

- This command will create a new argument parser. You can provide a description that describes the code that you have developed.
```python
parser = argparse.ArgumentParser(description = 'My Example Code')
```
- This creates a new input variable called in_var_1.  It will take one single argument, and provides a description of what the variable is. 
```python
parser.add_argument('in_var_1', nargs = 1, \
                    help = 'Input Variable - only need one!')
```
-  This will actually parse the arguments and make the variables that you can use.  Then returns them from the function.
```python
args = parser.parse_args()
return args
```
- In the main code, this calls the function and then prints out the variable that we created.  We can see that it is a Namespace, which is like a dictionary.
```python
args = parse_args()
print(args)
```
- This then grabs the specific variable that desire and prints that out to the screen.
```python
in_var = args.in_var_1
print(in_var)
```
Please note that in_var is list!  It is not a scalar value.

---------------
## Example 2:

Here is a second example. It introduces a bunch more types of variables to input.

```python
import argparse

def parse_args():
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
```
We can then run this using the help flag:
```bash
day_2% python ./args_example_2.py --help
usage: args_example_2.py [-h] [-in_scalar IN_SCALAR] [-npts NPTS] [-do_this]
                         in_var in_var

My Example Code V2

positional arguments:
  in_var                Input Variables - need two!

options:
  -h, --help            show this help message and exit
  -in_scalar IN_SCALAR  my scalar variable
  -npts NPTS            another scalar (default = 5)
  -do_this              Boolean to do something
```
If we don't provide any information at all, we get an error, but it is a helpful error:
```bash
$ python ./args_example_2.py 
usage: args_example_2.py [-h] [-in_scalar IN_SCALAR] [-npts NPTS] [-do_this]
                         in_var in_var
args_example_2.py: error: the following arguments are required: in_var
```
Final example:
```bash
$ python ./args_example_2.py test1 test2 -npts=4
Namespace(in_var=['test1', 'test2'], in_scalar=None, npts=4, do_this=False)
['test1', 'test2']
None
4
False
```
In this case, npts is defined as 4, in_scalar is not defined at all (we didn't provide a default!), and do_this is false.

You can try running the code with different inputs and see what the results are.

---------------
## Assignment 1:


Make a python function that will parse the inputs for running the cos estimation problem from yesterday. There should be two inputs:

- npts = the number of points to use for the cos approximation. Default should be 10.  Should be an integer.
- x = the angle to approximate cos for. Should be a float. Mandatory for input.

The code should print out:

- the number of points used in the approximation.
- the angle to approximate.
- the approximation.
- a judgement on whether this is a good approximation or not.


