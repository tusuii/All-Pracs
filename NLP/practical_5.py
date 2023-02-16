# Write a program to Implement syntactic parsing of a given text.

import nltk

# Download the required resources , only if necessary/on first try!
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')
# nltk.download('treebank')

text = "I ate hot ice-cream ,before match start"
words = nltk.word_tokenize(text)
tagged_words = nltk.pos_tag(words)

syntactic_tree = nltk.ne_chunk(tagged_words, binary=True)
print("Syntactic tree:", syntactic_tree)

