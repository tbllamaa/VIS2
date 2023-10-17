import pandas as pd

# Read the CSV file
df = pd.read_csv('data.csv')

# Count the number of eruptions per year
df['num_eruptions'] = df.groupby('Year')['Year'].transform('count')

# Get the years with maximum and minimum number of eruptions
max_year = df.loc[df['num_eruptions'].idxmax()]['Year']
min_year = df.loc[df['num_eruptions'].idxmin()]['Year']

# Get the maximum and minimum number of eruptions
max_eruptions = df['num_eruptions'].max()
min_eruptions = df['num_eruptions'].min()
