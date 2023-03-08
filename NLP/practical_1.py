# Write a program to implement sentence segmentation and word tokenization.

import nltk
import spacy
nlp = spacy.load("en_core_web_sm")
  
# sentence segmentation  (part 1)
doc = nlp(u"I Love Coding. Geeks for Geeks helped me in this regard very much. I Love Geeks for Geeks.")
for sent in doc.sents:
  print(sent)


# word Tokenization  (part 2)
text = "A good traveler has no fixed plans and is not intent on arriving"

sentences = nltk.sent_tokenize(text)

for sentence in sentences:
    words = nltk.word_tokenize(sentence)
    print(words)
