import matplotlib.pyplot as plt


def perform_analysis(data):
    ds = data.get_xarray()
    plt.figure(figsize=(12, 6))
    ds['rain'].plot()
    plt.title('Daily Rainfall Time Series')
    plt.xlabel('Time')
    plt.ylabel('Rainfall (mm)')
    plt.grid(True)
    plt.show()
