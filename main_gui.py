import tkinter as tk
from tkinter import messagebox, filedialog, scrolledtext
import webbrowser
import imdlib as imd
import importlib
import customtkinter as ctk
import os

#Main GUI Setup
root = ctk.CTk()
root.title("IMD Rainfall Analyzer")
root.geometry("730x730")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

title_box = ctk.CTkFrame(root, corner_radius=0, bg_color="grey")
title_box.pack(pady=10, padx=20, fill="x")

title_label = ctk.CTkLabel(title_box, text="Rainfall Analytics and Analysis Application", font=("Helvetica", 16), text_color="white")
title_label.pack(pady=10)


def create_tooltip(widget, text):
    tooltip = ctk.CTkLabel(widget, text=text, bg_color="gray", text_color="white", fg_color="black")
    def on_enter(event):
        tooltip.place(x=event.x, y=event.y - 20)
    def on_leave(event):
        tooltip.place_forget()
    widget.bind("<Enter>", on_enter)
    widget.bind("<Leave>", on_leave)

# data Loading Frame
frame_data = ctk.CTkFrame(root, corner_radius=10)
frame_data.pack(pady=20, padx=20, fill="both", expand=True)

start_year_label = ctk.CTkLabel(frame_data, text="Start Year:")
start_year_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
create_tooltip(start_year_label, "Enter the starting year for data loading.")
start_year_var = ctk.StringVar()
start_year_entry = ctk.CTkEntry(frame_data, textvariable=start_year_var)
start_year_entry.grid(row=0, column=1, padx=10, pady=10)

end_year_label = ctk.CTkLabel(frame_data, text="End Year:")
end_year_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
create_tooltip(end_year_label, "Enter the ending year for data loading.")
end_year_var = ctk.StringVar()
end_year_entry = ctk.CTkEntry(frame_data, textvariable=end_year_var)
end_year_entry.grid(row=1, column=1, padx=10, pady=10)

data = None

def load_data():
    global data
    start_year = int(start_year_var.get())
    end_year = int(end_year_var.get())

    try:
        data = imd.get_data('rain', start_year, end_year, fn_format='yearwise')
        messagebox.showinfo("Success", "Data loaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

load_button = ctk.CTkButton(frame_data, text="Load Data", command=load_data)
load_button.grid(row=2, column=0, columnspan=2, pady=20)




def open_data():
    global data
    start_year = int(start_year_var.get())
    end_year = int(end_year_var.get())

    try:
        data = imd.open_data('rain', start_year, end_year, fn_format='yearwise')
        messagebox.showinfo("Success", "Data opened successfully!")
    except Exception as e:
        messagebox.showerror("Error", "Data not found. Please load the data first.")


open_button = ctk.CTkButton(frame_data, text="Open Data", command=open_data)
open_button.grid(row=3, column=0, columnspan=2, pady=20)




# Analysis Frame
frame_analysis = ctk.CTkFrame(root, corner_radius=10)
frame_analysis.pack(pady=20, padx=20, fill="both", expand=True)

analysis_type_label = ctk.CTkLabel(frame_analysis, text="Analysis Type:")
analysis_type_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
create_tooltip(analysis_type_label, "Select the type of analysis to perform.")
analysis_type_var = ctk.StringVar()

# Analysis Modules
analysis_modules = [filename.split('.')[0] for filename in os.listdir('analysis') if filename.endswith('.py') and filename != '__init__.py']
analysis_type_combobox = ctk.CTkComboBox(frame_analysis, values=analysis_modules, variable=analysis_type_var)
analysis_type_combobox.grid(row=0, column=1, padx=10, pady=10)

analysis_file = None



def run_analysis():
    global data, analysis_file
    if data is None:
        messagebox.showerror("Error", "No data available. Please load or open the data first.")
        return

    analysis_type = analysis_type_var.get()
    try:
        analysis_module = importlib.import_module('analysis.' + analysis_type)
        analysis_file = analysis_module.perform_analysis(data)
    except Exception as e:
        messagebox.showerror("Error", str(e))

perform_button = ctk.CTkButton(frame_analysis, text="Perform Analysis", command=run_analysis)
perform_button.grid(row=1, column=0, columnspan=2, pady=20)



def download_analysis():
    global analysis_file
    if analysis_file is None:
        messagebox.showerror("Error", "No analysis results available. Please perform an analysis first.")
        return

    save_path = filedialog.asksaveasfilename(defaultextension=".png", initialfile=os.path.basename(analysis_file))
    if save_path:
        try:
            with open(analysis_file, 'rb') as src, open(save_path, 'wb') as dst:
                dst.write(src.read())
            messagebox.showinfo("Success", f"Analysis results saved to {save_path}.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save the file: {str(e)}")

download_button = ctk.CTkButton(frame_analysis, text="Download Results", command=download_analysis)
download_button.grid(row=2, column=0, columnspan=2, pady=20)



# IMD website button
def open_imd_website():
    webbrowser.open("https://mausam.imd.gov.in/")

imd_button = ctk.CTkButton(root, text="IMD Website", command=open_imd_website, width=5)
imd_button.pack(side=tk.LEFT, anchor=tk.NW, padx=10, pady=10)

# README.md Button
def open_readme():
    readme_path = os.path.join(os.path.dirname(__file__), "README.md")
    if os.path.exists(readme_path):
        os.system(f"start {readme_path}")
    else:
        messagebox.showerror("Error", "README.md not found.")

readme_button = ctk.CTkButton(root, text="Readme", command=open_readme, width=5)
readme_button.pack(side=tk.TOP, anchor=tk.NW, padx=10, pady=10)

# Footer
footer_frame = ctk.CTkFrame(root, corner_radius=10)
footer_frame.pack(side=tk.BOTTOM, fill="x", padx=20, pady=10)

copyright_label = ctk.CTkLabel(footer_frame, text="© 2024 Prajwal Shelar. All rights reserved.", font=("Helvetica", 10))
copyright_label.pack(side=tk.LEFT, padx=10)



def open_link(url):
    webbrowser.open(url)

github_button = ctk.CTkButton(footer_frame, text="GitHub", command=lambda: open_link("https://github.com/prajwalshelar100"), width=10)
github_button.pack(side=tk.RIGHT, padx=5)

email_button = ctk.CTkButton(footer_frame, text="Email", command=lambda: open_link("mailto:prajwalshelar100@gmail.com"), width=10)
email_button.pack(side=tk.RIGHT, padx=5)

linkedin_button = ctk.CTkButton(footer_frame, text="LinkedIn", command=lambda: open_link("https://www.linkedin.com/in/prajwalshelar"), width=10)
linkedin_button.pack(side=tk.RIGHT, padx=5)


root.mainloop()
