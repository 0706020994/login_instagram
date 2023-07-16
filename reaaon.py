import random as rd 
greet =['hey','hello','hi']
newname = greet
#print(greet[])



print(greet[rd.randint(0, 1)])
intent = input("\n")
print(intent)
for x in range(3):
    if intent == greet[x]:
        print("This is a greeting")
        print(greet[rd.randint(0, 2)])
        
        
if intent != greet[0] or intent != greet[1]:
    resp=input("Is this a Greeting\n")
    if resp == str('yes'):
        strintent = str(intent)
        greet= greet + strintent
        print("greeting has been added")
         
    else:
         newname+=input("kindly explain what it is using one word\n")
         print(newname)
print(intent)              



     #if intent == greet[x] :
            #print("this is a greeting")


