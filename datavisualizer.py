import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Load the CSV data
data = pd.read_csv('./weather.csv')  # Replace with the correct file path

class DataVisualizerApp:
    def __init__(self, root, data):
        self.root = root
        self.root.title("Weather Data Visualizer")
        self.data = data

        # Dropdown for X and Y axis selections
        self.label_x = tk.Label(root, text="Select X-axis data:")
        self.label_x.pack()
        self.combo_x = ttk.Combobox(root, values=list(data.columns))
        self.combo_x.pack()

        self.label_y = tk.Label(root, text="Select Y-axis data:")
        self.label_y.pack()
        self.combo_y = ttk.Combobox(root, values=list(data.columns))
        self.combo_y.pack()

        # Plot button
        self.plot_button = tk.Button(root, text="Plot Line Chart", command=self.plot_data)
        self.plot_button.pack()

        # Placeholder for matplotlib canvas
        self.canvas = None

    def plot_data(self):
        # Get selected columns
        x_column = self.combo_x.get()
        y_column = self.combo_y.get()

        if not x_column or not y_column:
            messagebox.showerror("Selection Error", "Please select both X and Y columns to plot.")
            return

        try:
            # Get data for the selected columns
            x = self.data[x_column]
            y = self.data[y_column]

            # Create the line chart figure
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.plot(x, y, marker='o', linestyle='-', color='b')
            ax.set_xlabel(x_column)
            ax.set_ylabel(y_column)
            ax.set_title(f"Line Chart: {y_column} vs {x_column}")
            ax.grid(True)

            # Embed the figure in Tkinter
            if self.canvas:
                self.canvas.get_tk_widget().pack_forget()  # Clear previous chart
            self.canvas = FigureCanvasTkAgg(fig, master=self.root)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack()

        except Exception as e:
            messagebox.showerror("Plotting Error", f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizerApp(root, data)
    root.mainloop()
