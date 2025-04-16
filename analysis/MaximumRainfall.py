# max_rain_event_analysis.py

import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    max_rain_event = ds['rain'].max('time')

    fig, ax = plt.subplots()
    max_rain_event.plot(ax=ax)

    output_file = "max_rain_event_analysis.png"
    fig.savefig(output_file)

    show_plot(fig)

    return output_file

def show_plot(fig):
    plot_window = tk.Toplevel()
    plot_window.title("Maximum Rainfall Event Analysis Results")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

