# Write a program to Implement a tri-gram model

import nltk
from nltk.util import ngrams

text = "The flame that burns Twice as bright burns half as long"

words = nltk.word_tokenize(text)

trigrams = ngrams(words, 3)

for trigram in trigrams:
    print(trigram)
