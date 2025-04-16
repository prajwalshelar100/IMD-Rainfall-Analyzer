import matplotlib.pyplot as plt


def perform_analysis(data):
    ds = data.get_xarray()

    # Calculate summary statistics
    summary_stats = ds['rain'].mean()
    max_rainfall = ds['rain'].max()
    min_rainfall = ds['rain'].min()

    # Display summary
    print(f"Mean Rainfall: {summary_stats.values} mm")
    print(f"Maximum Rainfall: {max_rainfall.values} mm")
    print(f"Minimum Rainfall: {min_rainfall.values} mm")

    plt.figure(figsize=(10, 6))
    ds['rain'].mean(dim=['time']).plot()
    plt.title('Mean Daily Rainfall')
    plt.xlabel('Time')
    plt.ylabel('Mean Rainfall (mm)')
    plt.grid(True)
    plt.show()
