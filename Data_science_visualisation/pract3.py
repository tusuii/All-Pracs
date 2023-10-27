#Practical 3: Write a code to read data from the different file formats like JSON, HTML, XML, and CSV files and check for missing data and outlier values and handle them

import pandas as pd

json_data = pd.read_json('data.json') # Read JSON file

html_data = pd.read_html('data.html') # Read HTML file
html_table = html_data[0] # change parameters accordingly

xml_data = pd.read_xml('data.xml') # Read XML file

csv_data = pd.read_csv('data.csv') # Read CSV file

# Check for missing data
print("Missing Data in JSON file:")
print(json_data.isnull().sum())

print("Missing Data in HTML file:")
print(html_table.isnull().sum())

print("Missing Data in XML file:")
print(xml_data.isnull().sum())

print("Missing Data in CSV file:")
print(csv_data.isnull().sum())

# Handle missing data
json_data_filled = json_data.fillna(0)
html_table_filled = html_table.fillna(method='ffill')
xml_data_filled = xml_data.fillna(xml_data.mean())
csv_data_filled = csv_data.dropna()

# Check for outlier
print("Outlier Values in JSON file:")
print(json_data.describe())

print("Outlier Values in HTML file:")
print(html_table.describe())

print("Outlier Values in XML file:")
print(xml_data.describe())

print("Outlier Values in CSV file:")
print(csv_data.describe())
