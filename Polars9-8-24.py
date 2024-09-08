import polars as pl
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset using Polars
df = pl.read_csv('C:\\Users\kyleh\\Downloads\\CHOsbautomobile_data.csv')

# Select relevant columns
df_selected = df.select(['wheel_base', 'curb_weight', 'body_style'])

# Convert Polars DataFrame to Pandas for plotting
df_pandas = df_selected.to_pandas()

# Create a scatterplot with seaborn
plt.figure(figsize=(10, 6))
sns.scatterplot(x='wheel_base', y='curb_weight', hue='body_style', data=df_pandas, palette='Set2')

# Add labels and title
plt.xlabel('Wheel Base')
plt.ylabel('Curb Weight')
plt.title('Scatterplot of Wheel Base vs Curb Weight by Body Style')

# Show the plot
plt.show()
