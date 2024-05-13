import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
from sea_level_predictor import import_data, create_scatter_plot, plot_line_of_best_fit, predict_sea_level,  add_annotations

def main():
    # Import data
    data = import_data("epa-sea-level.csv")

    # Create scatter plot
    create_scatter_plot(data)

    # Plot the line of best fit for all data
    plot_line_of_best_fit(data["Year"], data["CSIRO Adjusted Sea Level"], label="Line of Best Fit (All Data)")

    # Get data from year 2000 to the most recent year
    recent_data = data[data["Year"] >= 2000]

    # Plot the line of best fit for recent data
    plot_line_of_best_fit(recent_data["Year"], recent_data["CSIRO Adjusted Sea Level"], label="Line of Best Fit (Since 2000)")

    # Predict sea level rise in 2050
    year_2050 = 2050
    sea_level_2050 = predict_sea_level(year_2050, slope, intercept)
    sea_level_2050_recent = predict_sea_level(year_2050, slope_recent, intercept_recent)

    # Add annotations for predicted sea level rise in 2050
    add_annotations(year_2050, sea_level_2050, xytext_offset=20)
    add_annotations(year_2050, sea_level_2050_recent, xytext_offset=20)

    # Add labels and title
    add_labels_and_title("Year", "Sea Level (inches)", "Rise in Sea Level")

    # Show plot
    show_plot()

if __name__ == "__main__":
    main()
