# Reading Data Files

Now that we know how to read handle our data, how do we read and write from data files that we obtain in the lab.
One of the most common plain text data files you will find are Comma-Seperated Value (CSV) files which usually have the file extension `.csv`. 
They are formatted like this file which we will refer to as `example.csv`:
``` csv
time,posx,posy
0.0,0.0,-5.0
1.1111111111111112,0.5555555555555556,-4.444444444444445
2.2222222222222223,1.1111111111111112,-3.888888888888889
3.3333333333333335,1.6666666666666667,-3.333333333333333
4.444444444444445,2.2222222222222223,-2.7777777777777777
5.555555555555555,2.7777777777777777,-2.2222222222222223
6.666666666666667,3.3333333333333335,-1.6666666666666665
7.777777777777779,3.8888888888888893,-1.1111111111111107
8.88888888888889,4.444444444444445,-0.5555555555555554
10.0,5.0,0.0
```
The file consists of headers with columns seperated by commmas.
There also exist tab and space seperated files.

### Manually Reading Files

We will assume the data file `example.csv` is located in the same directory where you are running Python.

``` python
# Always have well named functions with suitable arguments 
def read_data_file(filename):
	time = []
	posx = []
	posy = []

	with open("data.csv") as f:
		# Read in the first line of the file which is usually column headers
		header_line = f.readline()
		headers = header_line.split(",")
		print("Reading in ", headers, "from", filename)
	
		# Loops over every remaining line in the file
		for line in f:
			# Split up the line and add each item to their list
			items = line.split(",")
			time.append(items[0])
			posx.append(items[1])
			posy.append(items[2])
	
	# Convert our 2d python lists into numpy array
	return np.array([time, posx, posy]).T # We need to transpose to get the correct dimensions
	
arr = read_data_file("example.csv")
```

Documentation for [`split()`](https://docs.python.org/3/library/stdtypes.html#str.split) and working with the [TextFile](https://docs.python.org/3/distutils/apiref.html#module-distutils.text_file) class are available.

The above code will work fine for our example but it could be better.
Let us change some code to make it more generalised for any csv formatted file.

``` python
def read_data_file_improved(filename):
        rows = [] # This list will store each row as a list of floating point numbers
        
        with open(filename) as f: # Opens the text file for reading
                header_line = f.readline()
                headers = header_line.strip().split(",")
                print("Reading in", headers, "from file", filename)

                for line in f:
                        items = line.strip().split(",")
                        items = [float(x) for x in items] 
                        rows.append(items)

        return np.array(rows)

arr = read_data_file_improved("example.csv")
```

This should work for well formated CSV files but may fail for others.
Be sure to understand the mechanics of this function as reading data from storage is the first hurdle in performing analysis.

### Reading directly into NumPy
If we want to convert our file directly into a NumPy array, we can use the function `np.genfromtxt()`.
The arguments include `fname` which is just the name of the file, `headers` which dictates the number of lines you want to skip in the file and `delimiter` which says what is being used to seperate the values.
`delimiter` can be changed to be a tab with `'\t'` or a space with `' '`.

``` python
arr = np.genfromtxt(fname="example.csv", headers=1, delimiter=',')
```
Documentation can be found [online](https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html).
