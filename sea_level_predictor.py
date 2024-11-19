import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    plt.figure(figsize=(12, 6))
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], label='Original Data', color='blue')

    # Create first line of best fit (all data)
    slope, intercept, _, _, _ = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_extended = pd.Series(range(1880, 2051))  # Extend to 2050
    sea_level_pred = slope * years_extended + intercept
    plt.plot(years_extended, sea_level_pred, 'r', label='Best Fit: All Data')

    # Create second line of best fit (from year 2000)
    df_recent = df[df['Year'] >= 2000]
    slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
    years_recent = pd.Series(range(2000, 2051))  # Extend to 2050
    sea_level_pred_recent = slope_recent * years_recent + intercept_recent
    plt.plot(years_recent, sea_level_pred_recent, 'green', label='Best Fit: From 2000')

    # Add labels and title
    plt.xlabel('Year')  # Fix xlabel
    plt.ylabel('Sea Level (inches)')  # Fix ylabel
    plt.title('Rise in Sea Level')  # Fix title
    plt.legend()  # Add legend for the lines

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
