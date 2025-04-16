import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog

def perform_analysis(data):
    def select_date():
        # Create a simple dialog to get the date from the user
        root = tk.Tk()
        root.withdraw()  # Hide the main window
        selected_date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
        root.destroy()  # Destroy the hidden window after getting the input
        return selected_date

    selected_date = select_date()

    if selected_date:
        ds = data.get_xarray()
        ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

        plt.figure(figsize=(12, 8))
        plot = ds['rain'].sel(time=selected_date).plot.pcolormesh(x='lon', y='lat', robust=True)
        plt.title(f'Spatial Distribution of Rainfall on {selected_date}')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        cbar = plt.colorbar(plot, label='Rainfall (mm)')
        cbar.set_label('Rainfall (mm)')
        plt.show()