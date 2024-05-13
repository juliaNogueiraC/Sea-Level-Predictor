import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def import_data(filename):
    """Import data from a CSV file."""
    return pd.read_csv(filename)

def create_scatter_plot(data):
    """Create a scatter plot."""
    plt.figure(figsize=(10, 6))
    plt.scatter(data["Year"], data["CSIRO Adjusted Sea Level"], color="blue", label="Sea Level")

def plot_line_of_best_fit(x, y, label):
    """Plot the line of best fit."""
    slope, intercept, _, _, _ = linregress(x, y)
    plt.plot(x, slope * x + intercept, label=label)

def predict_sea_level(year, slope, intercept):
    """Predict sea level rise for a given year."""
    return slope * year + intercept

def add_annotations(year, sea_level, xytext_offset):
    """Add annotations for predicted sea level rise."""
    plt.annotate(f"Predicted Sea Level in {year}: {sea_level:.2f} inches", 
                 xy=(year, sea_level), 
                 xytext=(year - xytext_offset, sea_level + 2), 
                 arrowprops=dict(facecolor='black', arrowstyle='->'))

def add_labels_and_title(xlabel, ylabel, title):
    """Add labels and title to the plot."""
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

def show_plot():
    """Show the plot."""
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

