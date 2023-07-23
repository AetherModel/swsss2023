---
title: Python I
description: First Python lecture
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Qusai Al Shidi | qusai@umich.edu

# Space 477: Python: I

----------

## Zen of Python (Coding) 🧘

- Beautiful is better than ugly.
- Explicit is better than implicit.
- Simple is better than complex.
- Complex is better than complicated.
- Flat is better than nested.
- Sparse is better than dense.
- Readability counts.
- Special cases aren't special enough to break the rules.
- In the face of ambiguity, refuse the temptation to guess.
- Now is better than never.

----------

## Python syntax

----------

- `#` | Comment
- `=` | Assignment
- `+` | Addition
- `-` | Subtraction
- `/` | Division
- `*` | Multiplication
- `**` | Power
- `""`, `''`, `"""  """` | String enclosure

```python
variable = 2
7 + variable  # 9
3**variable  # 9
variable**3  # 8
'Space rules!'
```


----------

- `==`  | Comparison: equal-to
- `!=`  | Comparison: doesn't equal
- `<`, `>`, `<=`, `>=` | Comparison
- `is`, `not` | Comparison of pythonic types
- `in` | Comparison: exists in.

```python
3 == 3  # True
's' in 'space'  # True
3 < 3  # False
not False  # True
```

----------

- `if condition:` Next indented (4 spaces) lines if true.
- `else:` Must be followed by an `if`
- `elif:` *else if*
- `for x in iterable:` A loop where `x` are the elements of an *iterable*.

```python
if True:  # Always true
    print("It's true!!")
if False:
    print("This code will never be executed :(")
else:
    print("This code will be executed :)!")

names = ('Ahmed', 'Becky', 'Cantor')
for name in names:
    print(name)  # Print all names
```

-----------

# Basic Pythonic Types

-----------

- Number: `int()  # 1`, `float()  # 1.0`
- String: `str()  # 'my string'`
- Boolean: `True` or `False`
- Tuple: `tuple()  # ('Tuple', 'of', 'strings')`
- List: `list()  # ['List', 'of', 'strings']`

```python
sequence = [1, 2, 3]
sequence*3  # ? what does this do
negative_ned = (False, False, False, False)  # He only likes to be negative
for elem in negative_ned:
    if not elem:
        print("Ned said no again")
    else:
        print("Ned did the impossible.")
```

------------

# All we care about are functions

------------

Which of these are *mathematical* functions?

- [ ] natural logarithm
- [ ] sine wave
- [ ] $f(x) = \pm x$

------------

Which of these are *mathematical* functions?

- [x] natural logarithm (domain: non-zero positive number, co-domain: real numbers)
- [x] sine wave (domain: real/imaginary numbers, co-domain: real/imaginary numbers)
- [ ] $f(x) = \pm x$ (domain: real numbers, co-domain: undefined/two real numbers)

Mathematical functions map a domain $X$ to a co-domain $Y$ (1 to 1 mapping).

-----------

# Before we continue

## Functional programming

Good programming functions are like good mathematical functions.

They may have multiple outputs, but have a *predictable* and
*repeatable* outputs with same inputs.

Make them short and sweet 😌.

------------

# Python functions

------------

# function skeleton ☠️

```python
def function_name(argument_1, argument_2, argument_3='default'):
    """Function documentation string"""
    # function body
    return argument_1, argument_2, argument_3

return_variable = function_name(1, 2)
return_variable  # (1, 2)
help(function_name)  # Function documentation string
```

- try to make sure functions return something
- it is possible to have a function body without a `return` but this is not
    considered good programming practice nowadays

--------------

# Make a function that returns the difference between the two arguments

--------------

# __SURPRISE__ time to review each others code

Your code *will* be seen by others 😟. Don't worry, we're all learning! 👍

--------------

- Did you make sure the function name and arguments are descriptive?
    - Explicit is better than implicit. 🧘
- Did you make sure to have a clear documentation string?
    - Now is better than never. 🧘
- Think of the other Coding Zen thoughts. `import this`

--------------

# Functional Programming concept: List comprehension

--------------

*List comprehension* comes from the mathematical *set comprehension*.

$$
L = \{2 \cdot x | x \in \mathbb{N}, x^2 > 3\}
$$

```python
# range() makes an integer iterable
simple_comprehension = [x for x in range(4)]  # [0, 1, 2, 3]

comprehended = [2*x for x in range(10) if x**2 > 3]  # limit to 10
```

Try it!

-----------

# THE ULTIMATE SHOW OF SKILL 🏋️‍♀️

Make a cosine function approximation using its taylor expansion.

$$
cos(x) \approx \sum_{n=0}^{10} \frac{(-1)^n}{(2n)!} x^{2n}
$$

----------

# I'll get you started

$$
cos(x) \approx \sum_{n=0}^{10} \frac{(-1)^n}{(2n)!} x^{2n}
$$

- The `sum()` Python built-in function may be helpful. (sum of an *iterable* like
    *lists*) `sum([1, 2, 3]) == 6  # True`
- Can you use list comprehension for this?

`cos_approx.py`
```python
from math import factorial  # now you can use factorial()
from math import pi  # now you can use pi

def cos_approx(x, accuracy=10):
    # Get started

```

------------

# Unit tests

# Tests

- use `assert <conditional (returns True or False)>, "Error Message"`

```python
assert cos_approx(0) < 1+1.e-2 and cos_approx(0) > 1-1.e-2, "cos(0) is not 1"
```
