from pygame import mixer
import turtle


song= "/home/system32/AiJourney/mymusic/Mbosso - Maajab (Official Music Video) Sms SKIZA 8546310 to 811.mp3"
mixer.init()
mixer.music.load(song)
mixer.music.play()