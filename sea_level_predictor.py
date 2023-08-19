import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(x, y, label='Historical data')

    # Create first line of best fit
    res = linregress(x, y)
    x_extrapolated = range(x.min(), 2051)
    plt.plot(x_extrapolated, res.intercept + res.slope * x_extrapolated, 'g', label='Extrapolated from 1880')

    # Create second line of best fit
    reduced_df = df[df['Year'] >= 2000]
    reduced_x = reduced_df['Year']
    reduced_y = reduced_df['CSIRO Adjusted Sea Level']
    res = linregress(reduced_x, reduced_y)
    x_extrapolated = range(reduced_x.min(), 2051)
    plt.plot(x_extrapolated, res.intercept + res.slope * x_extrapolated, 'r', label='Extrapolated from 2000')

    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.legend()
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()