import dictionary
import json
from nltkutils import tokenize , stem , bagofwords
import numpy as np
import pyaudio 



with open('dictionary.json','r') as j:
    myresponses = json.load(j)

print(myresponses)

for intent in myresponses['myresponses']:
    print(tag)