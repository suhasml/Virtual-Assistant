import pywhatkit
import Ava
import time

def play_music():
    try:
        Ava.speak("What song would you like to listen to?")
        song = Ava.TakeCommand().lower()
        if song != 'none':
            Ava.speak("Playing "+song)
            pywhatkit.playonyt(song)
    except Exception as e:
        Ava.speak("Sorry, could not find what you are looking for!")