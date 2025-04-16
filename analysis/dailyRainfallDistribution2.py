# daily_rainfall_distribution.py

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values
    plt.figure(figsize=(12, 6))
    ds['rain'].mean(dim=['lat', 'lon']).plot()
    plt.title('Daily Rainfall Distribution')
    plt.xlabel('Time')
    plt.ylabel('Mean Daily Rainfall (mm)')
    plt.grid(True)

    output_file = "daily_rainfall_distribution_analysis.png"
    plt.savefig(output_file)
    show_plot(plt.gcf())

    return output_file

def show_plot(fig):
    plot_window = tk.Toplevel()
    plot_window.title("Daily Rainfall Distribution Analysis Results")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
