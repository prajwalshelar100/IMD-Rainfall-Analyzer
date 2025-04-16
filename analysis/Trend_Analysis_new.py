import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    annual_rainfall = ds['rain'].groupby('time.year').sum(dim='time')
    annual_rainfall_df = annual_rainfall.to_dataframe().reset_index()
    annual_rainfall_df = annual_rainfall_df.groupby('year').mean().reset_index()

    X = annual_rainfall_df[['year']]
    y = annual_rainfall_df['rain']

    model = LinearRegression()
    model.fit(X, y)

    trend = model.predict(X)

    plt.figure(figsize=(12, 6))
    plt.plot(X['year'], y, marker='o', linestyle='-', label='Annual Rainfall')
    plt.plot(X['year'], trend, color='red', linestyle='-', label='Trend')
    plt.title('Rainfall Trend Analysis')
    plt.xlabel('Year')
    plt.ylabel('Rainfall (mm)')
    plt.legend()
    plt.grid(True)
    plt.show()
