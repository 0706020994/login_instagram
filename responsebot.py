import nltk
from nltk.chat.util import Chat,reflections
import time
import pygame
from pygame import mixer
import os








time =time.asctime()
song_library = [song for song in os.listdir("/home/system32/AiJourney/mymusic/") if song.endswith(".mp3")]

def playsong():# Initialize pygame mixer
    pygame.mixer.init()

    # Create a list of all the songs in the library
    
    # Prompt the user to select a song
    print("Select a song to play:")
    for i, song in enumerate(song_library):
        print(f"{i+1}. {song}")

    # Get user selection
    song_index = int(input()) - 1

    # Load the selected song
    pygame.mixer.music.load(song_library[song_index])
    # Play the song
    pygame.mixer.music.play()
    return pygame.mixer.music.play() 
pairs= [
    [r"my name is(.*)",
    ["Hello%1,How are you today?"]
],
[
    r"hi|hey|hello",
    ["Hello","hey there"]
],
[
    r"What  your name?",
    ["You can call me a chatbot","I'm a chatbot,you can call me whatever you like"]
],
[
    r"How are you?",
    ["I'm doing good","I'm fine"]
],
[
    r"sorry (.*)",
    ["its alright","its OK,never mind"]
    
],
[
    r"quit",
    ["Bye bye take care. it was nice talking to you :)"]

],

[
    r"Whats the time?|what is the time?|current time?",
    ["Its exactly : ",time]
],
[
    r"Who are you?",
    ["I am system32, An AI chatbot created to learn and perform operaions at hand"]
],
[
    r"Play song?",
    ["sure thing, select from my playlist",playsong()]

]

]
chatbot = Chat(pairs,reflections)
chatbot.converse()
