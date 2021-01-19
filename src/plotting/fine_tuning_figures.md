# Fine-Tuning Figures

We can place our data onto figures but it is neccessary to make sure that our plot is labeled and readable to all people.

The default text size for Matplotlib is a bit on the small side and can produce hard to read plots when included in \\(\LaTeX\\) documents.
This can be changed to something more reasonable.
``` python
plt.rcParams.update({'font.size': 22}) # Adjust 22 to the size you need
```

### Labeling your Plots
A plot is useless without clear label with the associated physical units. We can easily include these in our plots with some self-explanatory functions.
```python
fig = plt.figure()
t = np.linspace(0, 10, 100)
x = np.sin(t)

fig.plot(t, x)
fig.xlabel("Time [s]")
fig.ylabel("Position [m]")
fig.title("Position vs. Time")
fig.show()
```



### Adding Legends

### Styling your Plots
