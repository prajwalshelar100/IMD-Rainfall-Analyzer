import rioxarray

def perform_analysis(data):
    ds = ds.set_coords(['lat', 'lon'])

    # Write the CRS to the dataset
    ds.rio.write_crs("epsg:4326", inplace=True)

    subset_time = ds.sel(time=slice('2019-07-01', '2019-07-30'))

    subset_geo = ds.sel(lat=slice(70, 21), lon=slice(70.25, 21.75))

    import matplotlib.pyplot as plt

    # Plot rainfall for a specific date
    specific_date = ds.sel(time='2019-07-01')
    specific_date['rain'].plot()
    plt.title('Rainfall on 2019-07-01')
    plt.show()
