# Basic Plotting
In order to use Matplotlib, we need to import it.
``` python
import matplotlib.pyplot as plt 
```
We use the `as` keyword to substitute for the longer part with `plt`.
It will be assumed that you have this line for the rest of this chapter.

> If you get an error related to this line, make sure your have installed Matplotlib correctly

The function `plt.plot()` allows us to plot straight line graphs quickly.
``` python
import matplotlib.pyplot as plt

x = np.array([1, 2, 3, 4, 5]); # Create a 1D numpy array
y = 2 * x # Use element-wise operations to generate f(x)
plt.plot(x, y) # Create a plot element on the current figure
plt.show() # Display the current figure in a window
```
Here, we are plotting \\( f(x) = 2x \\) between 1 and 5 and showing the result in a window.
Note that `plt.plot()` uses an `x` list and `y` list to represent the locations on those axes.
These lists can be normal Python lists or most other list-like objects you'll find in the wild.

We can include multiple plots in a single figure by calling multiple functions that add plots to the figure.
```python
t = np.linspace(0, 2*np.pi, 100) # list representing time steps from 0 to 10 seconds
x = np.sin(t) # Position over time
v = np.cos(t) # Velocity over time

plt.plot(t, x)
plt.plot(t, v)
plt.show()
```

### Saving Plots
Plots can be manually saved through the window that pops up when using `plt.show()` or through Python code using `plt.savefig()`.

```python
plt.plot([1, 2, 3], [1, 2, 3]) # Add linear plot to figure
plt.savefig("name_of_image.png") # Save figure to current directory
plt.clf() # Clears your figure
```

### scatter()
The function `plt.scatter()` allows us to plot dots representing two different variables.
```python
x = [1, 2, 3]
y = [2, 4, 6]
plt.scatter(x, y) # similar usage to plt.plot()
plt.scatter(x, y, s=5) # s represents the size of dots plotted
```
Full documentation is available [online](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.scatter.html).

### errorbar()
The `plt.errorbar()` function is one of the most used in experimental labs.
It allows use to produce a scatter-like plot but with lovely uncertainty markers.
```python
# list showing time from 0 to 4 seconds
time = np.arange(0, 5) 

# numpy array of measured temprature data
temperature = np.array([82, 71, 63, 56, 50]) 

# Some uncertainty associated with the measurement
uncertainty = np.array([1.2, 1.0, 1.0, 0.8, 0.8]) 

# This will produce a plot with errorbars representing the uncertainty on the y axis
# The yerr parameter can either be a constant value
plt.errorbar(time, temperature, yerr=1.0)

# or yerr can be a list of the same length as the x and y parameters
plt.errorbar(time, temperature, yerr=uncertainty)

# Including the linestyle parameter as "None" 
# will remove that annoying straight line between points
plt.errorbar(time, temperature, yerr=uncertainty, linestyle="None")
```
Full documentation is available [online](https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.errorbar.html).

## Exercises
1. Plot an exponential function \\( f(x)= e^{2x} \\) between -10 and 10 using `np.exp()`
2. In the same plot, include the derivative of the function over the same domain.
3. Save the figure and put it on the fridge.
