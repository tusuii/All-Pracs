# Load the required libraries
library(rjson)
library(XML)

# Read data from JSON file
json_data <- fromJSON(file = "/home/subodh/Documents/subodh/Birla_college/sem3/Data_science_visualisation/Data_Visualization-main/Practical3/data.json")

# Read data from HTML file
html_data <- readHTMLTable("/home/subodh/Documents/subodh/Birla_college/sem3/Data_science_visualisation/Data_Visualization-main/Practical3/data.html")

# Read data from XML file
xml_data <- xmlParse("/home/subodh/Documents/subodh/Birla_college/sem3/Data_science_visualisation/Data_Visualization-main/Practical3/data.xml")
xml_data <- xmlToList(xml_data)

# Read data from CSV file
csv_data <- read.csv("/home/subodh/Documents/subodh/Birla_college/sem3/Data_science_visualisation/Data_Visualization-main/Practical3/data.csv")

# Check for missing data
missing_data <- sapply(json_data, function(x) sum(is.na(x)))
missing_data <- missing_data[missing_data > 0]

# Check for outlier values
outlier_data <- sapply(csv_data, function(x) sum(x < 0))
outlier_data <- outlier_data[outlier_data > 0]

# Handle missing data and outlier values
json_data[is.na(json_data)] <- 0
csv_data[csv_data < 0] <- 0

# Print the data
print(json_data)
print(html_data)
print(xml_data)
print(csv_data)

