# Applying Cuts


### Filtering NumPy arrays
When performing data analysis, we want an object where our data can be stored and queried. This can be done with NumPy arrays.
``` python
# assume there are 3 columns representing the time, position and velocity of a particle
data = get_data_from_csv() 

# We can split the 2-Dimensional array into single columns
time = data[:, 0]
position = data[:, 1]
velocity = data[:, 2]

# Lets only get the datapoints in which time > 0.5 seconds
trimmed_data = data[time > 0.5]

# We can also use multiple conditions
trimmed_data = data[(time > 1) & (position >= 0)]

# You can also change columns
data[:,2] = data[:, 2] ** 2 # Square the third column
```
