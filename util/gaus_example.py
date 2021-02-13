import pathlib

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

IMAGE_DIR = pathlib.Path(__file__).parent.parent.absolute() / "src/images/"

def gaussian_func(x, mean, std, A):
    return (
        A * np.exp(-((x - mean) ** 2) / (2 * std ** 2))
    )

def get_centres(edges):
    # Take the edges of a histogram and return the centres of each bin as a list
    # Also need to remove the last edge
    bin_width = edges[1] - edges[0]
    return edges[:-1] + bin_width/2

def plot_random_gaus(N):
    data = np.random.normal(0, 1, N) # Generate randomly distributed data

    # Bin the data and approximate the error due to binning using Poisson statistics
    counts, edges = np.histogram(data)
    counts_uncertainty = counts/np.sqrt(N)

    initial_values = [0, 1, 300]

    x_data = get_centres(edges)
    y_data = counts
    yerr_data = counts_uncertainty

    popt, pcov = curve_fit(gaussian_func, x_data, y_data, p0=initial_values, sigma=yerr_data)

    # Plot the results
    x = np.linspace(-3, 3, 100)
    y = gaussian_func(x, popt[0], popt[1], popt[2])

    plt.errorbar(x_data, y_data, yerr=yerr_data, linestyle="None", label="Data")
    plt.plot(x, y, label="Gaus Model")
    plt.legend()
    plt.title("Gaussian Example")
    plt.ylabel("Counts")
    plt.savefig(IMAGE_DIR / "fitting_gaus_example.png", dpi=150)
    plt.clf()
