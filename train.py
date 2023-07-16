import json
from nltkutils import tokenize , stem , bagofwords
import numpy as np
import pyaudio 
import pytorch as py 

with open('intents.json','r') as f:
    intents = json.load(f)
print(intents)

allwords = []
tags = []
xy = []


for intent in intents['intents']:
    
    tag = intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w = tokenize(pattern)
        allwords.extend(w)
        xy.append((w, tag) )


ignorewords = ['!','?','.',',',':']   
allwords = [stem(w) for w in allwords if w not in allwords]    
allwords = sorted(set(allwords))
tags = sorted(set(tags))
print(tags)

xtrain = []
ytrain = []
for (patternsentence, tag) in xy:
    bag = bagofwords(patternsentence, allwords)
    xtrain.append(bag)

    label =tags.index(tag)
    ytrain.append(label) #crossentropy loss
xtrain = np.array(xtrain)
ytrain = np.array(ytrain)

class Chatdataset(Dataset):
    def _init__ (self):
        self.nsamples = len(xtrain)
        self.xdata = xtrain
        self.ydata = ytrain
           
           #dAta set
    def __getitem__(self,index):

        return self.xdata[idx],self.ydata[idx]
    def __len__ (self):
        return self.nsamples
#hyper parameters
batch_size = 8
dataset = Chatdataset()
trainloader = Dataloader(dataset=dataset,batch_size=batch_size,shuffle=True,numworkers = 2)
    