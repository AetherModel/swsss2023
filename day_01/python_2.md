---
title: Python: II
description: First Python lecture
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Qusai Al Shidi | qusai@umich.edu | CSRB 2118

# Python: II

----------

# numpy

----------

- With `numpy` you can make arrays and do vector arithmetic.
- This is faster than making `for` loops and adding.
    - *Python is not C.* 🐍
- `numpy` is optimized for math operations.
- `numpy` is well [documented](https://numpy.org/).
    - In the face of ambiguity, refuse the temptation to guess. 🧘
```python
import numpy as np  # convention use np

vec = np.linspace(start=0, stop=1, num=3)  # evenly spaced numbers
vec*vec  # element-wise multiplication
vec*vec == vec**2  # array([True, True, True])
mat = np.matrix([[1, 2],
                 [3, 4]])
mat*mat == mat**2
mat.transpose()  # Very useful
```

----------

## element access

```python
my_list = [1, 2, 3, 4, 5]
my_list[1]  # 2
my_array = np.array(my_list)
my_array[1:3]  # array([2, 3])
my_list[1:3]  # [2, 3]
my_array[:3]  # array([1, 2, 3])
my_array[3:]  # array([4, 5])
my_array[:-1]  # array([1, 2, 3, 4])
```

----------

# matplotlib

----------

- Most popular Python plotting library.
- Very good [documentation](https://matplotlib.org/).

Let's plot $f(x) = e^x , 0 \le x < 1$.

```python
import matplotlib.pyplot as plt  # here is the good stuff

x = np.linspace(0, 1)  # default num is 50
plt.plot(x, np.exp(x))
plt.xlabel(r'$0 \le x < 1$')
plt.ylabel(r'$e^x$')
plt.title('Exponential function')
plt.show()  # shows plot, can be saved
```
