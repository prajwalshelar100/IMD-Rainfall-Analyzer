import geopandas as gpd
import rasterio
import numpy as np
import matplotlib.pyplot as plt
from rasterstats import zonal_stats
from affine import Affine

def perform_analysis(data):
    # Path to the shapefile
    shapefile_path = "C:\\Users\\prajw\\OneDrive\\Desktop\\CP\\IMDproject1\\resources\\India Shape\\india_ds.shp"

    # Path to the raster data
    raster_path = "C:\\Users\\prajw\\OneDrive\\Desktop\\CP\\IMDproject1\\resources\\rainfall_data.tif"

    try:
        shapefile = gpd.read_file(shapefile_path)

        # Check the first few rows of the shapefile to understand its structure
        print(shapefile.head())

        # Load the raster data using rasterio
        with rasterio.open(raster_path) as src:
            # Read the raster band as a numpy array
            rainfall_data = src.read(1, masked=True)

            # Mask out nodata values if present
            nodata = src.nodata
            if nodata is not None:
                rainfall_data = np.ma.masked_equal(rainfall_data, nodata)

            # Compute maximum rainfall across the years (modify as per your actual data and requirement)
            max_rainfall = np.ma.max(rainfall_data, axis=0)

            # Check the shape of max_rainfall and shapefile to ensure alignment
            print(f"Shape of max_rainfall: {max_rainfall.shape}")
            print(f"Shape of shapefile: {shapefile.shape}")

            # Define the affine transformation
            transform = src.transform

            # Perform zonal statistics to summarize raster values within each polygon
            stats = zonal_stats(shapefile, rainfall_data, stats="max", affine=transform, nodata=-999.0)

            # Extract maximum rainfall values from zonal statistics and update shapefile
            max_rainfall_values = [stat['max'] if stat else np.nan for stat in stats]
            shapefile['MaxRainfall'] = max_rainfall_values

            # Plotting
            fig, ax = plt.subplots(figsize=(10, 8))

            # Plot the shapefile with maximum rainfall values as colors
            shapefile.plot(column='MaxRainfall', ax=ax, legend=True, cmap='Blues', edgecolor='black', linewidth=0.5)

            # Customize plot parameters
            ax.set_title('Maximum Rainfall')
            ax.set_xlabel('Longitude')
            ax.set_ylabel('Latitude')

            plt.show()

    except FileNotFoundError:
        print(f"FileNotFoundError: '{raster_path}' not found. Please check the file path.")
    except rasterio.errors.RasterioIOError:
        print(f"RasterioIOError: Failed to open '{raster_path}'. Please ensure the file exists and is accessible.")
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except Exception as e:
        print(f"Error: {e}")