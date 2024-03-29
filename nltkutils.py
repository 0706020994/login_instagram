import nltk
from nltk.stem.porter import PorterStemmer
import numpy as np 
import pytorch


stemmer = PorterStemmer()
def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return stemmer.stem(word.lower())

def bagofwords(tokenizedsentence,allwords):
    tokenizedsentence = [stem(w) for w in tokenizedsentence]
    bag = np.zeros(len(allwords), dtype=np.float32)
    for idx, w in enumerate(allwords):
        if w in tokenizedsentence:
            bag[idx] = 1.0
    return bag  
sentence = ["hello","how","are","you"]
words = ["hi","hello","I","you","bye","thank","cool"]   
bag = bagofwords(sentence, words)
print(bag)         

