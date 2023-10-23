# practical 1 : Create one-dimensional data using series and perform various operations on it 

import numpy as np

# Create a one-dimensional data series
data = np.array([1, 2, 3, 4, 5, 6])

print("Data Series:", data)

# mathematical operations
print("Sum:", np.sum(data))
print("Product:", np.prod(data))
print("Square root:", np.sqrt(data))
print("Exponential:", np.exp(data))
print("Logarithm:", np.log(data))

# statistical operations
print("Minimum:", np.min(data))
print("Maximum:", np.max(data))
print("Mean:", np.mean(data))
print("Median:", np.median(data))
print("Standard Deviation:", np.std(data))

# array manipulation operations
print("Sorted Data:", np.sort(data))
print("Reversed Data:", np.flip(data))
print("Unique Values:", np.unique(data))
print("Reshaped Data (2x3):", np.reshape(data, (2, 3)))
print("Data Series with Element-wise Addition:", data + 2)
print("Data Series with Element-wise Multiplication:", data * 3)
