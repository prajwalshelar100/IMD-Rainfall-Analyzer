import pandas as pd
import matplotlib.pyplot as plt

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    monthly_mean_rainfall = ds['rain'].groupby('time.month').mean(dim='time')
    monthly_mean_rainfall_df = monthly_mean_rainfall.to_dataframe().reset_index()

    plt.figure(figsize=(12, 6))
    plt.plot(monthly_mean_rainfall_df['month'], monthly_mean_rainfall_df['rain'], marker='o', linestyle='-', color='b')
    plt.title('Monthly Mean Rainfall')
    plt.xlabel('Month')
    plt.ylabel('Rainfall (mm)')
    plt.grid(True)
    plt.show()
