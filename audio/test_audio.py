from pygame import mixer
mixer.init()
mixer.music.load("audio/Pendejo.m4a")
mixer.music.play()
while mixer.music.get_busy():
   continue
