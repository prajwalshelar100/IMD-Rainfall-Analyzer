import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    total_rainfall = ds['rain'].sum(dim=['lat', 'lon'])


    fig, ax = plt.subplots(figsize=(12, 6))
    total_rainfall.plot(ax=ax, marker='o')
    ax.set_title('Total Rainfall Over Time')
    ax.set_xlabel('Time')
    ax.set_ylabel('Total Rainfall (mm)')
    ax.grid(True)

    # Save the plot to a file
    output_file = "total_rainfall_over_time.png"
    fig.savefig(output_file)

    # Show the plot in a new window
    show_plot(plt.gcf())

    return output_file

def show_plot(fig):

    plot_window = tk.Toplevel()
    plot_window.title("Total Rainfall Over Time Analysis Results")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

