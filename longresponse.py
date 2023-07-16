import random
import nltk

nltk.download('punkt')
from nltk import WordNetLemmatizer
import numpy as np
import dictionary,py as dictw
from nltk import PunktSentenceTokenizer


lematizer = WordNetLemmatizer()
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and type exactly what you wrote there!"



def unknown():
        response = ["Could you please re-phrase that? ",
                "...",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(4)]
    
  
        
        return response
#print(newword)   
def greetings():
        response = ["Hey how are you ",
                "Hello",
                "Holla",
                "Heyy"][
        random.randrange(4)]
        return response


def myresponses():
    greetingsresp = ["Hey",
                "Hello",
                "Hi",
                "Aloha",
                "Halloo"][
    random.randrange(5)]

    return greetingsresp
myword = 'Hey'
wordpresent = False
for x in range(5):
        if myword in myresponses():
                print(1)
                wordpresent = True
        else:
                print("nope")        

#


determine = []
def newword():
        newword = input("try teach me something:")
        meaning = input("what is it eg greeting,name,noun: ")
        determine = [newword,meaning]
        return newword,meaning

determine= (newword())
strdetermine = str(determine)  
print(determine)
print(strdetermine)



print(len(dictw.mynewwords))
#if strdetermine in dictw:
 #               print("Exists")
#else:
 #       dictw.mynewwords.append(determine)


        #outfile.


#dictionary = outfile
#print(dictionary)
#Opinion Shape Material Origin 