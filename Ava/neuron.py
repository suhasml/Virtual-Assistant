import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

Stemmer = PorterStemmer()


def tokenize(sentence): #tokenize the sentence
    return nltk.word_tokenize(sentence)


def stem(word):
    return Stemmer.stem(word)


def bag_of_words(tokenized_sent,words):
    sentences_word = [stem(word) for word in tokenized_sent]
    bag = np.zeros(len(words),dtype = np.float32)
    
    for idx,w in enumerate(words):
        if w in sentences_word:
            bag[idx]=1

    return bag
