# Applying Cuts

One of the essential skills when working with lab data is being able to trim and edit the data generated by your data acquisition system.
When performing data analysis, we want an object where our data can be stored and queried.
This can be done with NumPy arrays.
``` python
# Assume there are 3 columns representing the time, pos. and vel. of a particle
# We have a place holder function which gives us a NumPy array
data = get_data_from_csv("example.csv") 

# We can split the 2-Dimensional array into single columns
time = data[:, 0]
position = data[:, 1]
velocity = data[:, 2]
```

Now that we have the seperate NumPy array, we can use them to apply cuts to the wider data array.
``` python
# Lets only get the datapoints in which time > 0.5 seconds
trimmed_data = data[time > 0.5]

# We can also use multiple conditions
# Note: The brackets are required
trimmed_data = data[(time > 1) & (position >= 0)]

# You can also change columns
data[:,2] = data[:, 2] ** 2 # Square the third column
data[:,1] = np.exp(data[:,1]) # Exponentiate the second column
```