# Practical 4 : Perform Reshaping of the hierarchical data and pivoting data frame data.
import pandas as pd

# hierarchical data frame
data = pd.DataFrame({'Year': [2019, 2019, 2020, 2020],
                     'Quarter': [1, 2, 1, 2],
                     'Sales': [100, 200, 150, 250],
                     'Expenses': [50, 75, 60, 90]})

print("Original Data Frame:")
print(data)

# Perform reshaping of hierarchical data
reshaped_data = data.set_index(['Year', 'Quarter'])
print("Reshaped Data:")
print(reshaped_data)

# Perform pivoting of data frame
pivoted_data = data.pivot(index='Year', columns='Quarter', values=['Sales', 'Expenses'])
print("Pivoted Data:")
print(pivoted_data)
