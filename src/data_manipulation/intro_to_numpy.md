# Intro to NumPy

NumPy is one of the most important packages needed for smart Python data analysis.
If you have never used the package before, read the [guide for absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) in the NumPy documentation.

### Creating NumPy arrays
NumPy provides us a fast and elegant method of creating multidimensional arrays known as `ndarray` objects or more commonly as NumPy arrays.
- `np.ones(n)`: Creates an array of `n` elements with 1 as entries [[link](https://numpy.org/doc/stable/reference/generated/numpy.ones.html)]
- `np.zeros(n)`: Like `np.ones()` but with 0 [[link](https://numpy.org/doc/stable/reference/generated/numpy.zeros.html)]
- `np.arange(n, m)`: Like `range()`, but creates a NumPy array of integers from `n` to `m` [[link](https://numpy.org/doc/stable/reference/generated/numpy.arange.html)]
- `np.linspace(a, b, n)`: Create a NumPy array from `a` to `b` with `n` evenly spaced elements between them [[link](https://numpy.org/doc/stable/reference/generated/numpy.linspace.html)]

### Operators and Functions

### Using NumPy arrays as matrices
NumPy allows us to create multidimensional array where 1 and 2-dimensional arrays will be the most commonly used.
2-dimensional arrays can be thought of as matrices and we can perform operations that should be familiar from linear algebra. 

``` python
triangular_matrix = np.array([[1, 1], [0, 1]])
identity_matrix = np.array([[1, 0], [0, 1]])

# np.matmul(A, B) performs the matrix multiplication AB if suitable dimensions
new_matrix = np.matmul(triangular_matrix, identity_matrix)
print(new_matrix) 
# output: 
# [[1, 1] 
#  [0, 1]]

transposed_matrix = triangular_matrix.T
print(transposed_matrix) 
# output: 
# [[1, 0] 
#  [1, 1]]

# Can also reshape array
numbers = np.arange(0, 6)

print(numbers.reshape((2,3))) 
# output: 
# [[0 1 2] 
#  [3 4 5]]

print(numbers.reshape((3,2))) 
# output: 
# [[0 1] 
#  [2 3] 
#  [4 5]]
```

More on [`reshape()`](https://numpy.org/doc/stable/reference/generated/numpy.reshape.html) and [`np.matmul()`](https://numpy.org/doc/stable/reference/generated/numpy.matmul.html) can be found online.

### Assessing elements
We can index NumPy arrays similarly to Python lists.
```
primes = np.array([2, 3, 5, 7, 11])

print(primes[2]) 
# output: 
# 5

print(primes[1:3]) 
# output: 
# [3, 5, 7]

# we can index 2d arrays using array[i][j] or array[i, j]
three_by_two = np.arange(0, 6).reshape((3,2))

print(three_by_two[0,0]) # output: 0
print(three_by_two[0,1]) # output: 1
print(three_by_two[1,0]) # output: 2
```
