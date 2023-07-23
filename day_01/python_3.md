---
title: Python: III
description: First Python lecture
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Qusai Al Shidi | qusai@umich.edu 

# Python: III

-----------

# One more basic type!

----------

## Dictionaries

- A dictionary is an *iterable* with conjoining *keys* and *values* as the elements (*items*).
- Useful to encapsulate data.

```python
solar_system = {'planets': ('Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter',
                            'Saturn', 'Uranus', 'Neptune'),
                'star': 'Sol',
                'dwarf_planets': ('Pluto', )
               }

solar_system['dwarf_planets']  # ('Pluto')
planets = [planet for planet in solar_system['planets']]
# or
planets = list(solar_system['planets'])
print(sorted(planets))  # Alphabet sort
```

---------------

# Iterables

---------------

- Iterables allow you to iterate through each element.
- We've already been dealing with them! Examples:
    - Lists
    - Tuples
    - Arrays
    - Dictionaries

----------

To iterate we use `for` syntax:

```python

for key in solar_system.keys():
    print(key)

for value in solar_system.values():
    print(element)

for key, value in solar_system.items():
    print(key, value)

```

---------------

## Don't use for loops to do basic linear algebra!

- We have `numpy` and arrays, matrices..etc. to do that for us :).

---------------

# Time to get comfortable with the terminal

----------

Let's use Python's package manager `pip`.

```bash
$ conda install pip
$ pip install swmfpy
# if it doesn't work try
$ pip install --user swmfpy
```

----------

- Plot your birthday AL using data from `swmfpy.web.get_omni_data()`

Do the following in `IPython`:
```python
from datetime import datetime
from swmfpy.web import get_omni_data

start_time = datetime(1990, 10, 2)
end_time = datetime(1990, 10, 3)
data = get_omni_data(start_time, end_time)  # returns a dictionary
data.keys()
```

-----------

- Good code has good metadata and documentation.
    - Now is better than never 🧘. 

Using your favorite text editor
```python
"""A 3D plot script for spherical coordinates.
"""
__author__ = 'Haskell Curry'
__email__ = 'i_died_too_old_for_email@mathlovers.com'
```

-----------

# Make a function that converts spherical coordinates to cartesian.

$$
x = r \cdot \sin(\phi) \cdot \cos(\theta)
$$
$$
y = r \cdot \sin(\phi) \cdot \sin(\theta)
$$
$$
z = r \cdot \cos(\phi)
$$

----------

# 😯😯😯 __SURPRISE__ 😯😯😯. Revise each other's code. Are you still getting surprised?

----------

```python
def spherical_cartesian(radius, azimuth, zentith):
    """Convert spherical coordinates to cartesian"""
    x = radius*sin(zentith)*cos(azimuth)
    y = radius*sin(zentith)*sin(azimuth)
    z = radius*cos(zentith)
    return x, y, z

fig = plt.figure()  # better control
axes = fig.gca(projection='3d')  # make 3d axes
r = np.linspace(0, 1)
theta = np.linspace(0, 2*np.pi)
phi = np.linspace(0, 2*np.pi)
x, y, z = spherical_cartesian(r, theta, phi)
axes.plot(x, y, z)
```

---------

# Ending the day 

It is time to commit your code changes
- BEFORE COMMITING make sure you are on your personal branch
- `git branch` there must be a asterisk next to `personal`
- `git commit cos_approx.py -m 'My cos_approx edits'`
- `git push origin personal`
