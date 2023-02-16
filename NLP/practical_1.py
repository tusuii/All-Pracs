# Write a program to implement sentence segmentation and word tokenization.

import nltk

text = "A good traveler has no fixed plans and is not intent on arriving"

sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)

