import random
import json
import pickle
import numpy as np
from tensorflow.keras.models import Sequential

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
intents = json.loads(open(intents.json).read())

words =[]
classes = []
ignoreletters = ['?','!','.',',']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        wordlist = nltk.word_tokenize(pattern)
        words.extend(wordlist)
        #documents.append

print("hello world")        