# Write a program to Implement stemming and lemmatization.

import nltk

# nltk.download('punkt')
# nltk.download('wordnet')

words = ['eating', 'eats', 'eaten', 'eat']

stemmer = nltk.stem.PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in words]
print("Stemmed words:", stemmed_words)

lemmatizer = nltk.stem.WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in words]
print("Lemmatized words:", lemmatized_words)