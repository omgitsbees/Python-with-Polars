import polars as pl

# Load the dataset
df = pl.read_csv(r'C:\Users\kyleh\Downloads\CHOsbautomobile_data.csv')

# Group by 'make' and 'body_style' to count the number of models
model_counts = df.group_by(['make', 'body_style']).agg(
    pl.count('make').alias('model_count')
)

# To find manufacturers that specialize in sedans
# Calculate the total models per manufacturer and the sedan percentage
sedan_percentage = (
    model_counts
    .pivot(values="model_count", index="make", columns="body_style")
    .fill_null(0)  # Fill missing body styles with 0
    .with_columns(
        (pl.col('sedan') / pl.sum_horizontal([pl.exclude('make')])).alias('sedan_percentage')
    )
)

# Display the final dataframe with the percentage of sedans by brand
print(sedan_percentage)
