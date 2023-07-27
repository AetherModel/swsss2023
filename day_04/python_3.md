As a reminder:

- We downloaded files from the WAM-IPE model forecasts on the Space Weather
    Prediction Center website.
- Be careful with adding the data files into the git repository 🤐!!
    - `git` is for source code and not data.

----------------------------------

```python
import netCDF4 as nc

dataset = nc.Dataset('filename.nc')
print(dataset)

dataset['tec'][:]  # How you get the numpy array of the data
dataset['tec'].units  # How you get the units of data
```

---------

- Let's make a `plt.pcolormesh()` plot of the *Total Electron Content*
- Create a function like

```python
def plot_tec(dataset, figsize=(12,6)):
    fig, ax = plt.subplots(nrows=1,
                           ncols=1,
                           figsize=figsize)
    # other things
    ax.pcolormesh()
    # other things
    return fig, ax
```

- Review each others' code
- *Challenge*: Write the same thing but takes as an argument the different types of plots that are *not* TEC.
    - `def plot_wam_ipe()`

---------------------------

Make another function that saves the figures instead of showing.

```python
# You can concatenate strings in python with +
outfilename = infilename + '.png'
```

- Code review when you are done

---------------------------

## Let's make a python module!!

- Save the file with a nice file name like `wam_ipe_plotter.py`
- Modules are python files with functions that you can import.
- Create a new "script" file `tec_plot.py` in the same directory and import the module

```python
from wam_ipe_plotter import plot_tec, save_tec  # and others you made
```

------------

## sys.argv

- It is a list of strings.
- Stands for *argument values*.
    - The command line arguments.
- The first argument is always the file name (i.e. `tec_plot.py`)
- The second argument is the second element `sys.argv[1]`

Write a plotting script that if run from the terminal this way saves a file:

```bash
# example
python tec_plot.py wfs.t12z.ipe05.20220719_010000.nc
# challenge allow any number of arguments and save png figures for all
```

- Create a directory `frames` with your data *both should be outside your git
    repo directory*.

---------------------------

- You can slice `sys.argv` to get all the arguments that are not the script file
    name
```python
command_arguments = sys.argv[1:]
```

- Make your script able to loop across your arguments and save images.

```bash
# example
python tec_plot.py *ipe05*.nc  # will expand to all file names
```

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
