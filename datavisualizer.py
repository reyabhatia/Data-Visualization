import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

class DataVisualizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Data Visualizer")

        # Input fields
        self.label_x = tk.Label(root, text="Enter X values (comma separated):")
        self.label_x.pack()
        self.entry_x = tk.Entry(root)
        self.entry_x.pack()

        self.label_y = tk.Label(root, text="Enter Y values (comma separated):")
        self.label_y.pack()
        self.entry_y = tk.Entry(root)
        self.entry_y.pack()

        # Button to plot
        self.plot_button = tk.Button(root, text="Plot Data", command=self.plot_data)
        self.plot_button.pack()

    def plot_data(self):
        # Get values from entry fields
        x_values = self.entry_x.get()
        y_values = self.entry_y.get()

        try:
            # Convert input strings to lists of floats
            x = list(map(float, x_values.split(',')))
            y = list(map(float, y_values.split(',')))

            # Check if both lists have the same length
            if len(x) != len(y):
                raise ValueError("X and Y must have the same number of values.")

            # Create a scatter plot
            plt.scatter(x, y)
            plt.title("Scatter Plot")
            plt.xlabel("X values")
            plt.ylabel("Y values")
            plt.grid()
            plt.show()

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    app = DataVisualizerApp(root)
    root.mainloop()
