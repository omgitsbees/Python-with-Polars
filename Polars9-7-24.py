import tkinter as tk
from tkinter import filedialog
import polars as pl

def open_file():
    # Open a file dialog to select the CSV file
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        # Load the dataset
        df = pl.read_csv(file_path)
        
        # Get the 'make' column as a list
        make_list = df['make'].to_list()
        
        # Get indices where 'make' is "Audi"
        audi_indices = [i for i, make in enumerate(make_list) if make == "Audi"]
        
        # Select rows at these indices
        if audi_indices:
            audi_rows = df.take(audi_indices)
            # Display the result in the text widget
            result_text.delete("1.0", tk.END)  # Clear previous content
            result_text.insert(tk.END, audi_rows)
        else:
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, "No rows found for 'Audi'.")
    else:
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, "No file selected.")

# Create the main window
root = tk.Tk()
root.title("CSV File Selector")

# Create a button to open the file dialog
open_button = tk.Button(root, text="Open CSV File", command=open_file)
open_button.pack(pady=10)

# Create a text widget to display the results
result_text = tk.Text(root, wrap=tk.NONE, width=100, height=20)
result_text.pack()

# Run the application
root.mainloop()
