import csv
from textblob import TextBlob

with open('./review.csv', 'r') as file:
    reader = csv.reader(file)

    for row in reader:
        text = row[0]
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        print(f"Sentiment score for '{text}': {sentiment}")
