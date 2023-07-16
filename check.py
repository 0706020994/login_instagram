import re
import longresponse as long

print('Bot: try typing something')
getresponse = input("You : ")

split_message = re.split(r'\s+|[,;?!.-]\s*', getresponse.lower())
print(split_message)
recognised_words =  ['hey','how','are','you']
print(len(split_message))
#response('Hello',['hey','how','are','you']) 
#response('my name is system32',['whats','your','name'])   
wordprob  = 0
for word in split_message:
    if word in recognised_words:
        wordprob +=1
        print(word)

listprob = 0   

def checkprob(wordprob):
    listprob = wordprob/len(split_message)
    percentage =int( listprob * 100)

    return percentage


 # print(response)
      
       

print(wordprob )
print(checkprob(wordprob))

outpercentage = checkprob(wordprob)


# to determine if the bot should say the word
if outpercentage > 50:
    print("this is a greeting")
    print(long.myresponses())
else:
    teachR= input("Bot:Please I don't understand Teach me :  y/n \n You:")
    if teachR == str('y') or teachR == str('yes'):
        print("he is willing")
        definput =input("Bot: use upto to two words to describe the above phrase \n You:")
        defword = re.split(r'\s+|[,;?!.-]\s*', definput.lower())
        print(defword)
        dictionary = open('dictionarydef','r') 
        for x in range(1):
             
            print(dictionary)        
            if definput  in dictionary:
                print("there is an existing " + definput )
                input()
            else:
                defword = [getresponse]
                print(defword)
    else:
        print(long.unknown())
