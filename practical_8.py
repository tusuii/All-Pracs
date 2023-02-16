# Write a program to Implement Text Summarization for the given sample text.

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from heapq import nlargest

text = """
Natural language processing (NLP) is a branch of artificial intelligence that focuses on the interaction between computers and human language. NLP has been around for several decades, but recent advances in machine learning and deep learning have dramatically improved its capabilities. NLP is used in a wide range of applications, from virtual assistants like Siri and Alexa to sentiment analysis, machine translation, and even content generation. NLP involves a range of techniques, including tokenization, part-of-speech tagging, named entity recognition, and sentiment analysis, among others. These techniques can be used to analyze and understand human language in a variety of contexts, from social media posts to scientific literature. Despite its many successes, NLP remains a challenging field, as natural language is complex and often ambiguous. As NLP continues to evolve, it has the potential to transform the way we interact with technology and with each other, opening up new possibilities for communication, collaboration, and creativity.
"""

num_sentences = 2
sentences = sent_tokenize(text)
words = word_tokenize(text)
stop_words = set(stopwords.words('english'))

word_freq = {}
for word in words:
    if word not in stop_words:
        if word not in word_freq:
            word_freq[word] = 1
        else:
            word_freq[word] += 1

max_freq = max(word_freq.values())

for word in word_freq.keys():
    word_freq[word] = (word_freq[word]/max_freq)

sent_scores = {}
for sentence in sentences:
    for word in word_tokenize(sentence.lower()):
        if word in word_freq.keys():
            if len(sentence.split(' ')) < 30:
                if sentence not in sent_scores.keys():
                    sent_scores[sentence] = word_freq[word]
                else:
                    sent_scores[sentence] += word_freq[word]

summary_sentences = nlargest(num_sentences, sent_scores, key=sent_scores.get)

summary = ' '.join(summary_sentences)
print(summary)
