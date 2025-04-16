import pandas as pd
import matplotlib.pyplot as plt

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    annual_rainfall = ds['rain'].groupby('time.year').sum(dim='time')
    annual_rainfall_df = annual_rainfall.to_dataframe().reset_index()
    annual_rainfall_df = annual_rainfall_df.groupby('year').mean().reset_index()

    mean_rainfall = annual_rainfall_df['rain'].mean()
    anomalies = annual_rainfall_df['rain'] - mean_rainfall

    plt.figure(figsize=(12, 6))
    plt.bar(annual_rainfall_df['year'], anomalies, color='b')
    plt.axhline(0, color='red', linestyle='--')
    plt.title('Rainfall Anomalies')
    plt.xlabel('Year')
    plt.ylabel('Anomaly (mm)')
    plt.grid(True)
    plt.show()
