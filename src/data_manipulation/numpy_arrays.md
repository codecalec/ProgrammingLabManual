# Intro to Numpy

Numpy is one of the most important packages needed for smart Python data analysis.
If you have never used the package before, read the [guide for absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) in the Numpy documentation.

### Creating Numpy arrays
Numpy provides us a fast and elegant method of creating multidimensional arrays.
We can convert usual Python list-like objects into Numpy arrays using the `np.array()` function.
Full documentaion is available [online](https://numpy.org/doc/stable/reference/generated/numpy.array.html).
The most useful feature of this type of array is the element-wise operations which allow use to map a function to each element of the array.

``` python
normal_list = [0, 1, 2, 3]
array = np.array(normal_list)
print(array) # output: [0, 1, 2, 3]

# We now add 2 to each element of the array and save it in array_plus_two
# These types of operators work for +,-,*,/ and most other operators
# Note that the original array is unchanged
array_plus_two = array + 2 
print(array_plus_two) # output: [2, 3, 4, 5]

# You can also do this with functions
array_sin = np.sin(array) # Numpy has a ton of nifty functions such as np.sin()
print(array_sin) # output: [0.         0.84147098 0.90929743 0.14112001]

# Your own suitably defined functions will also work
def time_by_three(x):
	return 3*x

array_times_three = times_by_three(array)
print(array_times_three) # output: [0, 3, 6, 9]
```

There are a few need to know functions for creating standard Numpy arrays.
- `np.ones(n)`: Creates an array of `n` elements with 1 as entries [[link](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)]
- `np.zeros(n)`: Like `np.ones()` but with 0 [[link](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)]
- `np.arange(n, m)`: Like `range()`, but creates a Numpy array of integers from `n` to `m` [[link](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)]
- `np.linspace(a, b, n)`: Create a Numpy array from `a` to `b` with `n` evenly spaced elements between them [[link](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)]

### Using Numpy arrays as matrices
#### WIP
``` python
triangular_matrix = np.array([[1, 1], [0, 1]])
identity_matrix = np.array([[1, 0], [0,1]])
new_matrix = np.matmul(triangular_matrix, identity_matrix)
```

### Filtering Numpy arrays
When performing data analysis, we want an object where our data can be stored and Numpy array can do this job.
``` python
data = get_data_from_csv() # assume there are 3 columns representing the time, position and velocity of a particle

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
