# Create Two-dimensional data with the help of data frames and perform different operations on it.

# Load the necessary library for working with data frames
library('dplyr')

# Create a two-dimensional data frame
data <- data.frame(
  A = c(1, 2, 3, 4, 5),
  B = c(6, 7, 8, 9, 10),
  C = c(11, 12, 13, 14, 15)
)

cat("Data Frame:\n")
print(data)

# Accessing columns
cat("Column A:\n")
print(data$A)
cat("Column B:\n")
print(data$B)
cat("Column C:\n")
print(data$C)

# Accessing rows
cat("Row 1:\n")
print(data[1,])


# Sum of columns
cat("Sum of Column A:", sum(data$A), "\n")
cat("Sum of Column B:", sum(data$B), "\n")
cat("Sum of Column C:", sum(data$C), "\n")

# Mean of rows
mean(as.numeric(data[1, ]))
mean(as.numeric(data[2, ]))

# Transpose the data frame
transposed_data <- t(data)
cat("Transposed Data Frame:\n")
print(transposed_data)
