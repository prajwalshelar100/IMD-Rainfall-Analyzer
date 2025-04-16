import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def perform_analysis(data):
    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values
    fig, ax = plt.subplots()
    ds['rain'].mean('time').plot(ax=ax)

    output_file = "plot_analysis_results.png"
    fig.savefig(output_file)

    show_plot(fig)

    return output_file


def show_plot(fig):
    plot_window = tk.Toplevel()
    plot_window.title("Plot Analysis Results")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()
