import random
from gtts import gTTS
import os
def speak(audio):
    
    r1 = random.randint(1, 10000000)
    r2 = random.randint(1, 10000000)
    randfile = ""+str(r2) + "randomtext" + str(r1) + ".mp3"
    tts = gTTS(text=audio, lang="en-IN", slow=False)
    tts.save(randfile)
    
    


speak("""""")