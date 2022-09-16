import Ava
import wikipedia
import webbrowser as wb
from googlesearch import search
import re
import music
from website import open_website

if __name__=='__main__':

    Ava.greeting()
    a=1
    
    while a:
        query = Ava.TakeCommand().lower()

        if query != 'none':
            a = Ava.Main(query)

        else:
            Ava.speak("Sorry, I did not understand that. Please try again.")
            continue
        
