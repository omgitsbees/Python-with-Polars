import polars as pl

# Sample data
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

# Create Polars DataFrame
df = pl.DataFrame(data)

# Perform the operations
result = (
    df
    .group_by("Make")
    .agg([
        pl.col("Horsepower").mean().alias("avg_hp"),
        pl.col("Price").mean().alias("avg_price"),
    ])
    .with_columns([
        (pl.col("avg_price") / pl.col("avg_hp")).alias("price_per_hp")
    ])
    .sort(by="avg_hp", descending=True)
)

# Display the result
print(result)