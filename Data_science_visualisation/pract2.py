# Practical 2:  Create Two-dimensional data with the help of data frames and perform different operations on it.

import pandas as pd

# Two-dimensional data frame
data = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                     'B': [6, 7, 8, 9, 10],
                     'C': [11, 12, 13, 14, 15]})

print("Data Frame:")
print(data)

# Accessing columns
print("Column A:")
print(data['A'])
print("Column B:")
print(data['B'])
print("Column C:")
print(data['C'])

# Accessing rows
print("Row 0:")
print(data.loc[0])
print("Row 1:")
print(data.loc[1])
print("Row 2:")
print(data.loc[2])

# Sum of columns
print("Sum of Column A:", data['A'].sum())
print("Sum of Column B:", data['B'].sum())
print("Sum of Column C:", data['C'].sum())

# Mean of rows
print("Mean of Row 0:", data.loc[0].mean())
print("Mean of Row 1:", data.loc[1].mean())
print("Mean of Row 2:", data.loc[2].mean())

# Transpose the data frame
transposed_data = data.transpose()
print("Transposed Data Frame:")
print(transposed_data)
