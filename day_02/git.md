---
title: Day 2
description: Day 2
author: Qusai Al Shidi
keywords: space-weather,space,python
math: mathjax
---

Let's get your personal access tokens so that you may push changes.

---------------------

# What is this git thing? 🤔

---------------------------

## Review

- Git is a *version* controlling software for your code.
- You've made changes to your local repository.
- You pushed changes to your fork on GitHub.

---------------------------

## Let's go through the commands

---------------------------

# git pull

- by itself, pull commits from the remote repository 'origin' (your fork on GitHub)
- `git pull <remote> <branch>` pulls changes from a similar repository on a
    different remote (AetherModel GitHub)

---------------------------

# git push

- by itself, push commits from your computer to remote repository 'origin'
    (GitHub)
- `git push <remote> <branch>` pushes the branch to remote repository

---------------------------

# git commit <file> -m 'A message'

- *stage* changes to be pushed, before this your edits are *unstaged*.
- commit messages should be useful and typically not more than 50 characters
    long.
- commit every time you have something in a working state

---------------------------

# git add <file/folder>

- *track* a file for changes. It will still be *unstaged* until you commit it.
- be careful adding folders, it will add __all__ files in it.

---------------------------

# git merge <branch-to-merge>

- merge two branches together,

```
           A---B---C topic                                          
          /                                                         
     D---E---F---G master                                           
```

- if on `master`, `git merge topic` will combine `topic` unto `master`

---------------------------

# rebase ???

- a rebase reapply commits onto a new base in your history, this might be
    necessary if you made commits based off a different point than the remote

```
      A---B---C topic
     /
D---E---F---G master


                A'--B'--C' topic                                 
               /                                                 
  D---E---F---G master                                           
```

---------------------------

# remember `--help` 😊
## git <command> --help

---------------------------

# Let's look at the changes you've made so far
## git log

- commit history with messages

---------------------------

# git show

- show the changes of the last commit
- `git show HEAD~2` will show changes since last 2 commits.
- `HEAD` is the current commit

---------------------------

# .gitignore

- Ask git to ignore certain files.
- This might be hidden `ls -a` to list *all* files

```bash
spyder .gitignore
# maybe on windows:
Notepad .gitignore
```

---------------------------

# refer to your git cheat sheets 📃 for other things!

# one more python tip!

- `zip()` generates tuples of its arguments sequentially (think of a zipper 🤐)

```python
names = ['Ahmed', 'Becky', 'Cantor']
ages = [21, 30, 45]
favorite_colors = ['Pink', 'Grey', 'Blue']

print(list(zip(names, ages, favorite_colors)))

for name, age, color in zip(names, ages, favorite_colors):
    print(name, age, color)
```

---------------------------

# how is this useful? 🤔

---------------------------

# a great example

```python
from datetime import datetime

num_of_days = 10
years = [2009]*num_of_days
months = [12]*num_of_days
days = list(range(start=1, stop=11))

times = [datetime(year, month, day)
         for year, month, day
         in zip(years, months, days)]
for time in times:
    print(time.isoformat())
```

---------------------------

# pcolormesh

- It's like a `plt.contourf` plot but with needing to make a `np.meshgrid()`

```python
import numpy as np
import matplotlib.pyplot as plt

num_of_x = 10
num_of_y = 20
x = np.linspace(0, 1, num_of_x)
y = np.linspace(0, 1, num_of_y)
z = np.random.randn(num_of_y, num_of_x)
plt.pcolormesh(x, y, z)
plt.colorbar()
```

---------------------------

# NetCDF

---------------------------

- A lot of space data is in this format
- Let's get its python package

```bash
conda install netcdf4
# if that doesn't work
pip install netCDF4
# you might need to do this *only* if the above didn't work:
pip install --user netCDF4
```

- It is similar to `h5py` or the `HDF5` format

---------------------------

- Let's download ionosphere forecast data from 
  https://www.swpc.noaa.gov/products/wam-ipe
- We want to extract the files

```bash
conda install -c conda-forge tar
tar -xvf wfs.*.tar
```

- We want the 2D files `ls *ipe05*.nc`
- `*` means match this pattern with any string of length
- `.nc` is a `NetCDF` file

---------------------------

```python
import netCDF4 as nc

dataset = nc.Dataset('filename.nc')
print(dataset)

dataset['tec'][:]  # How you get the numpy array of the data
dataset['tec'].units  # How you get the units of data
```

---------------------------

- Let's make a `plt.pcolormesh()` plot of the *Total Electron Content*
- Create a function like

```python
def plot_tec(dataset, figsize=(12,6)):
    fig, ax = plt.figure(figsize=figsize)
    # other things
    ax.pcolormesh()
    # other things
    return fig, ax
```

- Review each others' code

---------------------------

Make another function that saves the figures instead of showing.

```python
# You can concatenate strings in python with +
outfilename = infilename + '.png'
```

```bash
# example
python tec.py wfs.t12z.ipe05.20220719_010000.nc
# challenge allow any number of arguments and save png figures for all
```

- Code review when you are done

---------------------------

- Create a directory `frames` with your data *both should be outside your git
    repo directory*.

---------------------------

- Let's install `ffmpeg`

```bash
conda install ffmpeg
```

---------------------------

- https://trac.ffmpeg.org/wiki/Slideshow

```bash
cat *.png | ffmpeg -framerate 1/2 -f image2pipe -i - -c:v libx264 -pix_fmt yuv420p out.mp4
```

- Hopefully this works 😰
