import matplotlib.pyplot as plt

def perform_analysis(data):
    ds = data.get_xarray()
    plt.figure(figsize=(12, 6))
    ds['rain'].resample(time='1MS').mean(dim=['lat', 'lon']).plot(marker='o')
    plt.title('Monthly Mean Rainfall')
    plt.xlabel('Time')
    plt.ylabel('Mean Monthly Rainfall (mm)')
    plt.grid(True)
    plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout for better spacing
    plt.show()
