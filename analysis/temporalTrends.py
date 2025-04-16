import matplotlib.pyplot as plt


def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values


    total_rainfall = ds['rain'].sum(dim=['lat', 'lon'])
    plt.figure(figsize=(12, 6))
    total_rainfall.plot(marker='o')
    plt.title('Total Rainfall Over Time')
    plt.xlabel('Time')
    plt.ylabel('Total Rainfall (mm)')
    plt.grid(True)
    plt.show()
