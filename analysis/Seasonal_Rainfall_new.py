import pandas as pd
import matplotlib.pyplot as plt

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    seasons = {
        'Winter': [12, 1, 2],
        'Pre-Monsoon': [3, 4, 5],
        'Monsoon': [6, 7, 8, 9],
        'Post-Monsoon': [10, 11]
    }

    seasonal_rainfall = {}
    for season, months in seasons.items():
        seasonal_rainfall[season] = ds['rain'].sel(time=ds['time.month'].isin(months)).groupby('time.year').sum(dim='time')

    plt.figure(figsize=(12, 6))
    for season, data in seasonal_rainfall.items():
        data_df = data.to_dataframe().reset_index().groupby('year').mean().reset_index()
        plt.plot(data_df['year'], data_df['rain'], marker='o', linestyle='-', label=season)

    plt.title('Seasonal Rainfall')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (mm)')
    plt.legend()
    plt.grid(True)
    plt.show()
