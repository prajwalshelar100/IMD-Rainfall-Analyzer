import tkinter as tk
from tkinter import simpledialog
import plotly.graph_objs as go
import imdlib as imd

def perform_analysis(data):
    def select_date():
        root = tk.Tk()
        root.withdraw()
        selected_date = simpledialog.askstring("Input", "Enter date (YYYY-MM-DD):")
        root.destroy()
        return selected_date

    selected_date = select_date()

    if selected_date:
        try:

            ds = data.get_xarray()
            ds = ds.where(ds['rain'] != -999.)  # Remove NaN values

            data_day = ds.sel(time=selected_date)

            fig = go.Figure(go.Scattermapbox(
                lat=data_day['lat'],
                lon=data_day['lon'],
                mode='markers',
                marker={'color': data_day['rain'], 'colorscale': 'Blues', 'size': 10},
                text=data_day['rain'].values.tolist(),
            ))

            fig.update_layout(
                mapbox_style="carto-positron",
                mapbox_zoom=4,
                mapbox_center={'lat': 20.5937, 'lon': 78.9629},  # Centered around India
                margin={'r': 0, 't': 0, 'l': 0, 'b': 0},
            )


            fig.show()

        except Exception as e:
            print(f"Error: {str(e)}")

    return None
