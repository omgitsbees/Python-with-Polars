Polars Challenge 9-8-2024:
# Scatterplot Visualization of Automobile Data

This project demonstrates how to visualize automobile data using Polars for data manipulation and Seaborn for plotting. The dataset is analyzed to create a scatterplot that shows the relationship between `wheel_base` and `curb_weight`, colored by `body_style`.

## Prerequisites

Ensure you have the following Python packages installed:
- `polars`
- `matplotlib`
- `seaborn`

You can install them using pip:
```bash
pip install polars matplotlib seaborn

Dataset

The dataset used in this project is CHOsbautomobile_data.csv, which should be placed in the specified path: C:\\Users\\kyleh\\Downloads\\CHOsbautomobile_data.csv
Code Overview

    Load the Dataset: The dataset is loaded using Polars.
    Select Relevant Columns: The relevant columns (wheel_base, curb_weight, body_style) are selected.
    Convert to Pandas DataFrame: The Polars DataFrame is converted to a Pandas DataFrame for compatibility with Seaborn.
    Create Scatterplot: A scatterplot is generated with wheel_base on the x-axis, curb_weight on the y-axis, and different colors representing body_style.

How to Run

    Save the code in a Python file, e.g., visualization.py.
    Ensure the dataset path is correctly specified in the code.
    Run the script using:

    bash

python visualization.py

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Polars Challenge 9-7-2024:
# CSV File Selector with Tkinter

This project is a simple Tkinter application that allows users to select a CSV file and display rows where the 'make' column is "Audi". The application uses Polars for data manipulation.

## Prerequisites

Ensure you have the following Python packages installed:
- `tkinter` (usually included with Python)
- `polars`

You can install Polars using pip:
```bash
pip install polars

eatures

    Opens a file dialog to select a CSV file.
    Loads the CSV file and processes it using Polars.
    Displays rows where the 'make' column is "Audi" in a text widget.

How to Run

    Save the code in a Python file, e.g., csv_selector.py.

    Run the script using:

    bash

    python csv_selector.py

    Click the "Open CSV File" button to open a file dialog and select your CSV file.

    The rows where the 'make' column is "Audi" will be displayed in the text widget. If no such rows are found, or if no file is selected, appropriate messages will be shown.

Code Overview

    open_file(): Opens a file dialog to select a CSV file, reads the file using Polars, and processes it to find rows where 'make' is "Audi". Displays results in a Tkinter text widget.
    Tkinter GUI: The main window includes a button to open the file dialog and a text widget to display the results.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Polars Challenge 9-5-2024:
# Sedans Percentage Analysis

This project analyzes a CSV dataset to determine the percentage of sedan models for each manufacturer. The dataset is processed using Polars to calculate and display the percentage of sedan models compared to the total number of models per manufacturer.

## Prerequisites

Ensure you have the following Python package installed:
- `polars`

You can install Polars using pip:
```bash
pip install polars

Dataset

The dataset used in this project is CHOsbautomobile_data.csv, which should be located at: C:\Users\kyleh\Downloads\CHOsbautomobile_data.csv
Code Overview

    Load the Dataset: Reads the CSV file using Polars.
    Group by Manufacturer and Body Style: Counts the number of models for each combination of manufacturer and body style.
    Calculate Sedan Percentage:
        Pivot the grouped data to have manufacturers as rows and body styles as columns.
        Fill any missing body styles with 0.
        Calculate the percentage of sedans for each manufacturer by dividing the number of sedans by the total number of models.
    Display Results: Prints the DataFrame showing the percentage of sedan models by manufacturer.

How to Run

    Save the code in a Python file, e.g., sedan_percentage_analysis.py.

    Ensure the dataset path is correctly specified in the code.

    Run the script using:

    bash

    python sedan_percentage_analysis.py

    The script will output the DataFrame with the percentage of sedans for each manufacturer.

Example Output

The output will be a DataFrame with the percentage of sedan models for each manufacturer, similar to:

shape: (n, 2)
┌────────────┬────────────────────┐
│ make       │ sedan_percentage   │
│ ---        │ ---                │
│ str        │ f64                │
├────────────┼────────────────────┤
│ Toyota     │ 0.45               │
│ Honda      │ 0.60               │
│ Ford       │ 0.30               │
│ ...        │ ...                │
└────────────┴────────────────────┘

----------------------------------------------------------------------------------------------------------------------------------------------------------------------

Polars Challenge 9-4-2024:

# Car Make Analysis

This project analyzes a dataset of car makes to compute the average horsepower and price for each make, and calculates the price per horsepower. The data is processed using Polars for efficient analysis.

## Prerequisites

Ensure you have the following Python package installed:
- `polars`

You can install Polars using pip:
```bash
pip install polars

Dataset

Sample data includes car makes, horsepower, and prices. The data is defined within the script as follows:

python

data = {
    'Make': ['porsche', 'porsche', 'jaguar', 'jaguar', 'mercedes-benz', 'mercedes-benz', 
             'BMW', 'BMW', 'mazda', 'mazda', 'volkswagen', 'volkswagen', 
             'honda', 'honda', 'isuzu', 'isuzu', 'chevrolet', 'chevrolet'],
    'Horsepower': [220.0, 200.0, 210.0, 199.34, 160.0, 132.5, 145.0, 132.75, 90.0, 81.06, 
                   85.24, 76.92, 85.0, 75.45, 82.0, 72.0, 66.0, 59.34],
    'Price': [25990.0, 24250.8, 35500.0, 33700.0, 34500.0, 32794.0, 26900.0, 25337.5, 
              11200.0, 10105.75, 10500.0, 9655.0, 8350.0, 8019.38, 4500.0, 4416.5, 
              6050.0, 5964.0]
}

Code Overview

    Create DataFrame: Constructs a Polars DataFrame from the sample data.
    Group by Make: Groups the data by the car make and calculates the average horsepower and price.
    Calculate Price per Horsepower: Computes the price per horsepower for each make.
    Sort Results: Sorts the results by average horsepower in descending order.
    Display Results: Prints the resulting DataFrame showing the average horsepower, average price, and price per horsepower for each make.

How to Run

    Save the code in a Python file, e.g., car_make_analysis.py.

    Run the script using:

    bash

    python car_make_analysis.py

    The script will output a DataFrame with the average horsepower, average price, and price per horsepower for each car make, sorted by average horsepower.

Example Output

The output will be a DataFrame similar to the following:

rust

shape: (n, 4)
┌───────────────┬──────────┬───────────┬─────────────────┐
│ Make          │ avg_hp   │ avg_price │ price_per_hp    │
│ ---           │ ---      │ ---       │ ---             │
│ str           │ f64      │ f64       │ f64             │
├───────────────┼──────────┼───────────┼─────────────────┤
│ porsche       │ 210.00   │ 25120.40  │ 119.57          │
│ jaguar        │ 204.67   │ 34650.00  │ 169.32          │
│ mercedes-benz │ 146.25   │ 33647.00  │ 230.76          │
│ BMW           │ 138.38   │ 26118.75  │ 188.82          │
│ mazda         │ 85.03    │ 10607.88  │ 124.83          │
│ volkswagen    │ 81.08    │ 10477.50  │ 129.25          │
│ honda         │ 76.73    │ 7614.69   │ 99.09           │
│ isuzu         │ 72.00    │ 4458.25   │ 61.10           │
│ chevrolet     │ 64.17    │ 5952.25   │ 92.84           │
└───────────────┴──────────┴───────────┴─────────────────┘
