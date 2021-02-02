import os
import pathlib

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 18}) # Adjust 18 to the size you need

IMAGE_DIR=pathlib.Path(__file__).parent.parent.absolute() / "src/images/"
print(f"Saving images to {IMAGE_DIR}")

def plt_plot_example():
    x = np.array([1, 2, 3, 4]); # Create a 1D numpy array
    y = 2 * x # Use element-wise operations to generate f(x)
    plt.plot(x, y) # Create a plot element on the current figure
    plt.savefig(IMAGE_DIR / "plt_plot_example.png", dpi=200)
    plt.clf()

def multiple_plot_example():
    t = np.linspace(0, 2*np.pi, 100) # list representing time steps from 0 to 10 seconds
    x = np.sin(t) # Position over time
    v = np.cos(t) # Velocity over time

    plt.plot(t, x)
    plt.plot(t, v)
    plt.savefig(IMAGE_DIR / "multiple_plot_example.png", dpi=200)
    plt.clf()

def plt_scatter_example():
    x = np.array([1, 2, 3])
    y = np.array([2, 4, 6])
    plt.scatter(x, y) # similar usage to plt.plot()
    plt.scatter(x, y + 1, s=100) # s represents the size of dots plotted
    plt.savefig(IMAGE_DIR / "plt_scatter_example.png", dpi=200)
    plt.clf()

def plt_errorbar_example():
    time = np.arange(0, 5)
    temperature = np.array([82, 71, 63, 56, 50])
    uncertainty = np.array([1.2, 1.0, 1.0, 0.8, 0.8])

    plt.errorbar(time, temperature, yerr=2.0)
    plt.errorbar(time, temperature - 5, yerr=uncertainty)
    plt.errorbar(time, temperature - 10, yerr= uncertainty, linestyle="None")
    plt.savefig(IMAGE_DIR / "plt_errorbar_example.png", dpi=200)
    plt.clf()

def labelling_example():
    t = np.linspace(0, 10, 100)
    x = np.sin(t)

    plt.plot(t, x)
    plt.xlabel("Time [s]") # Adds label for x-axis
    plt.ylabel("Position [m]") # Adds label for y-axis
    plt.title("Position vs. Time") # Adds title
    plt.savefig(IMAGE_DIR / "labelling_example.png", dpi=200, bbox_inches='tight')
    plt.clf()
    

def styling_example():
         
    def gaussian_func(x, mean, std):
        # Evaluate a Gaussian of mu=mean and sigma=std at x 
        return (
            1 / np.sqrt(2 * np.pi * std ** 2) * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
        )
    
    x = np.linspace(-3, 3, 1000) 
    lower_peak = gaussian_func(x, -0.5, 1)
    upper_peak = gaussian_func(x, 0.5, 1)
    combined = lower_peak + upper_peak

    # The linestyle argument changes the way our lines look
    # The color argument gives us flexibility in the choice of colour
    # Remember to use readable colours for white background
    plt.plot(lower_peak, linestyle="dashed", color="blue")
    plt.plot(upper_peak, linestyle="dotted", color="green")
    plt.plot(combined, color="red")
    plt.title("Double Peak")
    plt.savefig(IMAGE_DIR / "styling_example.png", dpi=200, bbox_inches='tight')
    plt.clf()

def legend_example():
    
    x = np.arange(0, 10)
    alpha = 2
    beta = 3

    f = alpha * x
    g = beta * x ** 2

    # We can also label our plots with LaTeX expressions.
    # Note the use of double \ instead of a single \ when writing commands
    plt.plot(x, f, label="$f(x) = \\alpha x$")
    plt.plot(x, g, label="$g(x) = \\beta x^{2}$")
    plt.legend()
    plt.savefig(IMAGE_DIR / "legend_example.png", dpi=200)
    plt.clf()

def hist_example():
    data = np.random.normal(5, 0.5, 1000)
    plt.hist(data)
    plt.savefig(IMAGE_DIR / "hist_example.png", dpi=200)
    plt.clf()

def hist_errorbar_example():
    N = 500
    data = np.random.normal(0, 1, N)

    counts, edges = np.histogram(data)
    counts_uncertainty = counts/np.sqrt(N) # Poisson error of each bin

    def get_centres(edges):
        # Take the edges of a histogram and return the centres of each bin as a list
        bin_width = edges[1] - edges[0]
        return edges[:-1] + bin_width/2

    centres = get_centres(edges)
    plt.errorbar(centres, counts, marker="o", yerr=counts_uncertainty, linestyle="None")
    plt.savefig(IMAGE_DIR / "hist_errorbar_example.png", dpi=200)
    plt.clf()

if __name__ == "__main__":
    plt_plot_example()
    multiple_plot_example()
    plt_scatter_example()
    plt_errorbar_example()
    labelling_example()
    styling_example()
    legend_example()
    hist_example()
    hist_errorbar_example()
