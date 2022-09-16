import re
from unittest import result
import wikipedia
import Ava
import pywhatkit

def search(query):     
    #query = query.replace("what is ","")
    result = wikipedia.summary(query,sentences=2)
    Ava.speak(result)
    Ava.speak("That is it. Anything else that might interest you? ")

