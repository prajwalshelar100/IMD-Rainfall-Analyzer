import matplotlib.pyplot as plt
import xarray as xr

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values


    data_slice = ds['rain'].sel(time='2023-06-01')


    # Plotting contour plot
    plt.figure(figsize=(10, 6))
    contour_plot = data_slice.plot.contourf(x='lon', y='lat', levels=20, cmap='plasma')
    plt.title('Rainfall on June 1, 2023')
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')

    plt.colorbar(contour_plot, label='Rainfall (mm)')
    plt.grid(True)
    plt.show()
