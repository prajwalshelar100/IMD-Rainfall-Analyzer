import tkinter as tk
from tkinter import simpledialog
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def select_date():

    root = tk.Tk()
    root.withdraw()  # Hide the main Tkinter window

    selected_date = simpledialog.askstring("Date Selection", "Enter date (YYYY-MM-DD):")
    return selected_date


def perform_analysis(data):
    selected_date = select_date()
    if not selected_date:
        return None

    ds = data.get_xarray()
    ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

    try:

        plt.figure(figsize=(12, 8))
        plot = ds['rain'].sel(time=selected_date).plot.pcolormesh(x='lon', y='lat', robust=True)
        plt.title(f'Spatial Distribution of Rainfall on {selected_date}')
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.colorbar(plot, label='Rainfall (mm)')
        plt.show()


        output_file = f"spatial_rainfall_{selected_date.replace('-', '')}.png"
        plt.savefig(output_file)

        return output_file

    except KeyError:
        tk.messagebox.showerror("Error", f"No data available for {selected_date}. Please select another date.")
        return None


def show_plot(fig):

    plot_window = tk.Toplevel()
    plot_window.title("Spatial Rainfall Distribution Analysis Results")
    canvas = FigureCanvasTkAgg(fig, master=plot_window)
    canvas.draw()
    canvas.get_tk_widget().pack()

