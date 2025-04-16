
import matplotlib.pyplot as plt

def perform_analysis(data):
    ds = data.get_xarray()
    ds['rain'] = ds['rain'].where(ds['rain'] != -999.0)
    mean_rainfall = ds['rain'].mean(dim=['lat', 'lon'])

    plt.figure(figsize=(12, 6))
    mean_rainfall.plot()
    plt.title('Mean Daily Rainfall in India')
    plt.xlabel('Date')
    plt.ylabel('Rainfall (mm)')
    plt.grid(True)
    plt.show()
