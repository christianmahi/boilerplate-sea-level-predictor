import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    data = pd.read_csv('epa-sea-level.csv')
    years = data['Year']
    sea_levels = data['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.scatter(years, sea_levels)

    # Create first line of best fit
    first_fit = linregress(years, sea_levels)
    first_fit_years = range(years.min(), 2051)
    plt.plot(
        first_fit_years,
        first_fit.intercept + first_fit.slope * first_fit_years
    )

    # Create second line of best fit
    recent_data = data[data['Year'] >= 2000]
    second_fit = linregress(
        recent_data['Year'],
        recent_data['CSIRO Adjusted Sea Level']
    )
    second_fit_years = range(2000, 2051)
    plt.plot(
        second_fit_years,
        second_fit.intercept + second_fit.slope * second_fit_years
    )

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()