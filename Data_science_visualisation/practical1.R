# practical 1 : Create one-dimensional data using series and perform various operations on it 
library("methods")
data <- c(1,2,3,4,5,6)

cat("Data series",data, "\n")

# mathematical operations
cat("Sum: ", sum(data), "\n")
cat("Product : ", prod(data), "\n")
cat("Square Root : ", sqrt(data), "\n")
cat("Exponential : ", exp(data), "\n")
cat("Logarithm : ", log(data), "\n")

# Statistical operations
cat("Minimum : ", min(data), "\n")
cat("Maximum : ", max(data), "\n")
cat("Mean : ", mean(data), "\n")
cat("Median : ", median(data), "\n")
cat("Standard Deviation : ", sd(data), "\n")

# Array manipulation
cat("Sorted array : ", sort(data), "\n")
cat("Reversed array : ", rev(data), "\n")
cat("Unique value : ", unique(data), "\n")
cat("Reshaped data 2X3" , "\n")
matrix(data,nrow=2,ncol=3)
cat("series to matrix conversion : ",matrix(data,nrow=2,ncol=3) ,"\n")

cat("data series with element wise Addition : ", data + 2, "\n")
cat("data series with element wise multiplication : ", data * 2, "\n")



